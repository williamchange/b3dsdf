# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "b3dsdf",
    "author": "cmzw",
    "description": "A toolkit of signed distance functions, operators and utility nodegroups",
    "blender": (2, 83, 0),
    "version": (0, 9, 1),
    "location": "Shader Editor > Add > SDF",
    "tracker_url": "https://github.com/williamchange/b3dsdf/issues/new",
    "doc_url": "https://github.com/williamchange/b3dsdf/wiki/Examples",
    "category": "Node",
}
import json
import bpy
import os
from bpy.types import Operator, Menu
from bpy.props import StringProperty


def add_sdf_button(self, context):
    if context.area.ui_type == "ShaderNodeTree":
        self.layout.menu("NODE_MT_sdf_menu", text="SDF", icon="CON_TRANSFORM")


sdf_group_cache = {}
shader_cat_list = []
draw_menu_functions = []

dir_path = os.path.dirname(__file__)

# adapted from https://github.com/blender/blender/blob/master/release/scripts/modules/nodeitems_utils.py
def shader_cat_generator():
    global shader_cat_list
    global draw_menu_functions

    shader_cat_list = []
    draw_menu_functions = []

    for item in sdf_group_cache.items():

        def custom_draw(self, context):
            layout = self.layout
            for group_name in sdf_group_cache[self.bl_label]:
                if group_name == "_":
                    layout.separator(factor=1.0)
                    continue
                if group_name.startswith("+"):
                    layout.label(text=group_name.split("+")[-1])
                    continue
                entry = group_name.split("@")

                # remove prefix in menu
                group_label = entry[0]
                for prefix in ["sd", "op", "3D", "LN"]:
                    group_label.replace(prefix, "")
                props = layout.operator(NODE_OT_group_add.bl_idname, text=group_label)

                props.group_name = entry[0]

                # Override tooltip
                if len(entry) > 1:
                    props.tooltip = entry[1]

        itemid = item[0].split("_")[0]

        menu_type = type(
            "NODE_MT_category_" + itemid,
            (bpy.types.Menu,),
            {
                "bl_idname": "NODE_MT_category_"
                + itemid.replace(" ", "_").replace("-", "_"),
                "bl_space_type": "NODE_EDITOR",
                "bl_label": item[0],
                "draw": custom_draw,
            },
        )
        if menu_type not in shader_cat_list:

            def generate_menu_draw(name, label):
                def draw_menu(self, context):
                    self.layout.menu(name, text=label.split("_")[0])
                    if "_" in label:
                        self.layout.separator(factor=1.0)

                return draw_menu

            bpy.utils.register_class(menu_type)
            draw_menu = generate_menu_draw(menu_type.bl_idname, menu_type.bl_label)
            bpy.types.NODE_MT_sdf_menu.append(draw_menu)

            draw_menu_functions.append(draw_menu)
            shader_cat_list.append(menu_type)


class NODE_MT_sdf_menu(Menu):
    bl_label = "SDF"
    bl_idname = "NODE_MT_sdf_menu"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "ShaderNodeTree"

    def draw(self, context):
        pass


class NODE_OT_group_add(Operator):
    """Add a node group"""

    bl_idname = "b3dsdf.group_add"
    bl_label = "Add node group"
    bl_description = "Append Node Group"
    bl_options = {"REGISTER", "UNDO"}

    group_name: StringProperty()
    tooltip: StringProperty()

    # adapted from https://github.com/blender/blender/blob/master/release/scripts/startup/bl_operators/node.py
    @staticmethod
    def store_mouse_cursor(context, event):
        space = context.space_data
        tree = space.edit_tree

        if context.region.type == "WINDOW":
            space.cursor_location_from_region(
                event.mouse_region_x, event.mouse_region_y
            )
        else:
            space.cursor_location = tree.view_center

    @classmethod
    def poll(cls, context):
        return context.space_data.node_tree

    @classmethod
    def description(self, context, props):
        return props.tooltip

    def execute(self, context):
        old_groups = set(bpy.data.node_groups)

        for file in os.listdir(dir_path):
            if file.endswith(".blend"):
                filepath = os.path.join(dir_path, file)
                break
        else:
            raise FileNotFoundError("No .blend File in directory " + dir_path)

        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            if self.group_name not in bpy.data.node_groups:
                data_to.node_groups.append(self.group_name)
        added_groups = list(set(bpy.data.node_groups) - old_groups)
        for group in added_groups:
            for node in group.nodes:
                if node.type == "GROUP":
                    new_name = node.node_tree.name.split(".")[0]
                    node.node_tree = bpy.data.node_groups[new_name]
        for group in added_groups:
            if "." in group.name and not ".5" in group.name:
                bpy.data.node_groups.remove(group)

        bpy.ops.node.add_node(type="ShaderNodeGroup")

        node = context.selected_nodes[0]
        node.node_tree = bpy.data.node_groups[self.group_name]

        node.location = context.space_data.cursor_location
        bpy.ops.transform.translate("INVOKE_DEFAULT")
        return {"FINISHED"}

    def invoke(self, context, event):
        self.store_mouse_cursor(context, event)
        return self.execute(context)


def register():
    global sdf_group_cache

    with open(os.path.join(os.path.dirname(__file__), "shader_nodes.json"), "r") as f:
        sdf_group_cache = json.loads(f.read())

    if not hasattr(bpy.types, "NODE_MT_sdf_menu"):
        bpy.utils.register_class(NODE_MT_sdf_menu)
        bpy.types.NODE_MT_add.append(add_sdf_button)
    bpy.utils.register_class(NODE_OT_group_add)

    shader_cat_generator()


def unregister():
    for func in draw_menu_functions:
        bpy.types.NODE_MT_sdf_menu.remove(func)

    if hasattr(bpy.types, "NODE_MT_sdf_menu"):
        bpy.types.NODE_MT_add.remove(add_sdf_button)
        bpy.utils.unregister_class(NODE_MT_sdf_menu)
    bpy.utils.unregister_class(NODE_OT_group_add)
