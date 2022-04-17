# b3dsdf

b3dsdf is a collection of 2d signed distance functions and operators nodegroups for Blender 2.83+

You can use these by appending the groups from the .blend file or use them with the addon which adds a menu in the shader editor.

These nodegroups can also be used with the asset browser by adding the .blend as an asset library (already marked as assets)

<p align="center">
  <img width="800" height="450" src="https://user-images.githubusercontent.com/830253/163708008-8ea814c3-f86f-48c8-835a-322e46d2b1e3.gif">
</p>

## Nodegroups

A list of available nodegroups can be viewed in the [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json) file. There's currently 51 nodegroups. Examples(with images) can be found in the [wiki page](https://github.com/williamchange/b3dsdf/wiki/Examples) (work in progress)

![sdf_nodegroups](https://user-images.githubusercontent.com/830253/163705497-02f7ed1f-32c5-4f83-88f6-70ae10208b75.png)

## Planned / work in progress

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
