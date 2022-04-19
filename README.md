# b3dsdf

b3dsdf (blender signed distance functions) is a collection of 2d signed distance functions and operators nodegroups for the shader editor in Blender 2.83+.

These nodes can be used by appending from the .blend file or use them with the addon which adds a menu in the shader editor.

These nodegroups can also be used with the asset browser by adding the .blend as an asset library and marking them as assets.

<p align="center">
  <img src="https://user-images.githubusercontent.com/830253/163708008-8ea814c3-f86f-48c8-835a-322e46d2b1e3.gif">
</p>

## Installation

The easiest way to install the add is to download the latest release zip file from the [release page](https://github.com/williamchange/b3dsdf/releases) and install as normal. There's no need to unzip before installing.

You might have to restart Blender for changes to take effect after installing / uninstalling.


## Installation (From source)

If you wish to install from the source directly (i.e. via downloading the zip file), note that the added suffix(`-master`) have to be removed from the zipped folder for the add-on toe enable properly.

<p align="center">
  <img src="https://user-images.githubusercontent.com/830253/164016537-8d820e1e-a311-4f37-953e-10a1eaa3e49d.gif">
</p>

## Nodegroups

A list of available nodegroups can be viewed in [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json). Examples (with images) can be found in the [wiki page](https://github.com/williamchange/b3dsdf/wiki/Examples) (work in progress).

![sdf_nodegroups](https://user-images.githubusercontent.com/830253/163992200-6b7d416f-146f-4b2d-9e9c-293005366354.png)

## References

1. [Inigo Quilez's 2D Distance Functions](https://www.iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm)
2. [Inigo Quilez's 2D SDF Primitves Shadertoy playlist](https://www.shadertoy.com/playlist/MXdSRf)
3. [Erindale's Toolkit (Add menu logic)](https://erindale.gumroad.com/l/erintools)
4. [D6464 Blender SDF patch](https://developer.blender.org/D6464)
5. [hg_sdf glsl library](https://mercury.sexy/hg_sdf/)
