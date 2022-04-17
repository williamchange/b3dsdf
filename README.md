# b3dsdf

b3dsdf is a collection of 2d signed distance functions and operators nodegroups for Blender 2.83 or above. You can use these by appending the groups from the .blend file or use them with the addon which adds a menu in the shader editor.

A list of sources used for implementing the nodegroups/addon can be found under [References](https://github.com/williamchange/b3dsdf#references)

All of these groups were already marked as assets in the .blend file, which can be used with the asset browser in 3.0 by adding it as an asset library.

## Nodegroups

A list of available nodegroups can be viewed in the [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json) file. There's currently 50 nodegroups.

![sdf_nodegroups](https://user-images.githubusercontent.com/830253/163703038-ff86557c-78ac-43ed-b3d2-6fac3361363c.png)

## Preview

## Planned / work in progress

- sdUnevenCapsule
- sdHorseshoe
- sdEllipse
- sdBlobbyCross
- sdSquareStairs
- sdStairs

## References

1. [Inigo Quilez's 2D Distance Functions](https://www.iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm)
2. [Inigo Quilez's 2D SDF Primitves Shadertoy playlist](https://www.shadertoy.com/playlist/MXdSRf)
3. [Erindale's Toolkit (Add menu logic)](https://erindale.gumroad.com/l/erintools)
4. [D6464 Blender SDF patch (Vector operators)](https://developer.blender.org/D6464)
