
<p align="center">
    <h1 align = "center">b3dsdf</h1>
</p>

<p align="center">
    Toolkit of 2D/3D signed distance functions and utility nodegroups for the material editor in Blender 2.83+
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/830253/169821105-1d13020e-6895-4402-aa0c-2c94db69867f.gif">
</p>

## License

The GPLv3 license ([LICENSE](LICENSE)) only applies to the python add-on source code.

Included asset file (`sdf_nodegroups.blend`) in this repository is under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) ([LICENSE_ASSET](LICENSE_ASSET.md)).

## Geometry Nodes (Volume Cube)

As of [D15198](https://developer.blender.org/D15198) it's also possible to use the SDF nodes/operators from this pack via their Geometry Nodes equivalents in Blender 3.3 or above ([more details](https://twitter.com/lateasusual_/status/1537792086719795201))

The shader nodes in this pack can't be used directly, but it's possible to convert them for use with an add-on, for example [Val Barashkov's](https://twitter.com/ValeraBarashkov) [Blender Booster](https://vsb.gumroad.com/l/blender_booster).

## Installation

Download the latest zip file from the [release page](https://github.com/williamchange/b3dsdf/releases) and install as normal. There's no need to unzip before installing. You might have to restart Blender for changes to take effect after installing / uninstalling.

Alternatively you have the option to install directly from source (code > download zip, or via repo cloning) which might include new features/nodes.

>[!NOTE]
>From Blender 4.2 LTS and onwards add-ons are now Extensions, however you can still use this by [installing as a legacy add-on](https://docs.blender.org/manual/en/4.2/editors/preferences/extensions.html#install-legacy-add-on). There are no plans to release this as an extension for the time being.

## Nodegroups

Nodes can be used by appending from the .blend file or use them with the addon which adds a menu in the shader editor. They can also be used with the asset browser by adding the .blend as an asset library and marking them as assets.

List of available nodegroups can be found in [shader_nodes.json](https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json). Examples (w/ images) can be found in the [wiki(incomplete)](https://github.com/williamchange/b3dsdf/wiki/Examples).

![sdf_nodegroups](https://github.com/user-attachments/assets/7330815c-7091-41c6-95e4-7ab18597a767)

## References

- [Erindale's Toolkit (original add menu logic)](https://erindale.gumroad.com/l/erintools)
- [D6464 Blender SDF patch](https://archive.blender.org/developer/D6464)
- [Additonal references / Shadertoy playlist](https://www.shadertoy.com/playlist/7cjGR1)
- [Inigo Quilez - 3D Distance Functions](https://iquilezles.org/articles/distfunctions/)
- [Inigo Quilez - 2D Distance Functions](https://iquilezles.org/articles/distfunctions2d/)
- [Inigo Quilez - 2D Distance Functions in L-infinity norm](https://iquilezles.org/articles/distfunctions2dlinf/)
- [Inigo Quilez - 2D Distance Functions and gradients](https://iquilezles.org/articles/distgradfunctions2d/)
- [hg_sdf glsl library](https://mercury.sexy/hg_sdf/)
