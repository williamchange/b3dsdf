# b3dsdf

b3dsdf is a collection of 2d signed distance functions and operators nodegroups for Blender 2.83+

You can use these by appending from the .blend or use them with the addon which adds a menu in the shader editor.

These nodegroups can also be used with the asset browser by adding the .blend as an asset library (already marked as assets)

<p align="center">
  <img src="https://user-images.githubusercontent.com/830253/163708008-8ea814c3-f86f-48c8-835a-322e46d2b1e3.gif">
</p>

## Nodegroups

A list of available nodegroups can be viewed in the [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json) file. There's currently 55 nodegroups. Examples(with images) can be found in the [wiki page](https://github.com/williamchange/b3dsdf/wiki/Examples) (work in progress)

![sdf_nodegroups](https://user-images.githubusercontent.com/830253/163722690-31c6135c-ecfd-4a8c-aa8d-3eba58c30772.png)

## Work in progress

- sdEllipse
- sdBlobbyCross

## References

1. [Inigo Quilez's 2D Distance Functions](https://www.iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm)
2. [Inigo Quilez's 2D SDF Primitves Shadertoy playlist](https://www.shadertoy.com/playlist/MXdSRf)
3. [Erindale's Toolkit (Add menu logic)](https://erindale.gumroad.com/l/erintools)
4. [D6464 Blender SDF patch (Vector operators)](https://developer.blender.org/D6464)
