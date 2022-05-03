# b3dsdf 🧰

b3dsdf (blender signed distance functions) is a collection of 2D signed distance functions and operators nodegroups for the shader editor in Blender 2.83+.

These nodes can be used by appending from the .blend file or use them with the addon which adds a menu in the shader editor.

They can also be used with the asset browser by adding the .blend as an asset library and marking them as assets.

<p align="center">
  <img src="https://user-images.githubusercontent.com/830253/165154162-406dca54-cd5c-43df-9bee-9344113d2f13.gif">
</p>

## Installation

Download the latest zip file from the [release page](https://github.com/williamchange/b3dsdf/releases) and install as normal. There's no need to unzip before installing. You might have to restart Blender for changes to take effect after installing / uninstalling.

## Nodegroups

The full list of nodegroups can be viewed in [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json). Examples (with images) can be found in the [wiki page](https://github.com/williamchange/b3dsdf/wiki/Examples) (work in progress).

![sdf_nodegroups](https://user-images.githubusercontent.com/830253/166426434-3e27da3c-f34e-4350-b4da-8d12cafd4a5c.png)

## References

- [Inigo Quilez's 2D Distance Functions](https://www.iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm)
- [Inigo Quilez's 2D SDF Primitves Shadertoy playlist](https://www.shadertoy.com/playlist/MXdSRf)
- [Erindale's Toolkit (Add menu logic)](https://erindale.gumroad.com/l/erintools)
- [D6464 Blender SDF patch](https://developer.blender.org/D6464)
- [hg_sdf glsl library](https://mercury.sexy/hg_sdf/)
