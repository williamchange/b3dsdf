# b3dsdf 🧰

b3dsdf (blender signed distance functions) is a toolkit of 2D/3D signed distance functions and operators nodegroups for the shader editor in Blender 2.83+.

These nodes can be used by appending from the .blend file or use them with the addon which adds a menu in the shader editor. They can also be used with the asset browser by adding the .blend as an asset library and marking them as assets.

<p align="center">
  <img src="https://user-images.githubusercontent.com/830253/169821105-1d13020e-6895-4402-aa0c-2c94db69867f.gif">
</p>

## Geometry Nodes (Volume Cube)

As of [D15198](https://developer.blender.org/D15198) it's also possible to use the SDF nodes/operators from this pack via their Geometry Nodes equivalents in Blender 3.3 or above ([more details](https://twitter.com/lateasusual_/status/1537792086719795201))

The shader nodes in this pack can't be used directly, but it's possible to convert them for use with an add-on, for example [Val Barashkov's](https://twitter.com/ValeraBarashkov) ['Blender Booster' add-on](https://vsb.gumroad.com/l/blender_booster).

## Installation

Download the latest zip file from the [release page](https://github.com/williamchange/b3dsdf/releases) and install as normal. There's no need to unzip before installing. You might have to restart Blender for changes to take effect after installing / uninstalling.

Alternatively you have the option to install directly from source (code > download zip, or via repo cloning) which might include new features/nodes.

**Note**: From Blender 4.2 LTS and onwards add-ons are now Extensions, however you can still use this by [installing as a legacy add-on](https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html#install-legacy-add-on). There are no plans to release this as an extension for the time being.

## Nodegroups

List of available nodegroups can be found in [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json). Examples (with images) can be found in the [wiki page](https://github.com/williamchange/b3dsdf/wiki/Examples).

![sdf_nodegroups](https://github.com/williamchange/b3dsdf/assets/830253/929a2ecc-7c13-4c47-8274-dd9964dff42d)

## References

- [Erindale's Toolkit (original add menu logic)](https://erindale.gumroad.com/l/erintools)
- [D6464 Blender SDF patch](https://developer.blender.org/D6464)
- [Additonal references / Shadertoy playlist](https://www.shadertoy.com/playlist/7cjGR1)
- [Inigo Quilez - 3D Distance Functions](https://iquilezles.org/articles/distfunctions/)
- [Inigo Quilez - 2D Distance Functions](https://iquilezles.org/articles/distfunctions2d/)
- [Inigo Quilez - 2D distance functions in L-infinity norm](https://iquilezles.org/articles/distfunctions2dlinf/)
- [hg_sdf glsl library](https://mercury.sexy/hg_sdf/)
