<p align="center">
    <h1 align = "center">b3dsdf</h1>
</p>
<p align="center">
    Toolkit of SDFs/vector utility nodes for Blender 2.83+
</p>
<p align="center">
    <a href="https://github.com/williamchange/b3dsdf/releases/download/v0.12/b3dsdf-demo-b45.blend"><img width="960" alt="b3dsdf-sample" src="https://github.com/user-attachments/assets/544603d8-109b-4f1e-bd55-7bffb870f391" /></a>
</p>

## Nodegroups

Nodegroups can be used by appending from the .blend file or use them with the addon which adds a menu in the material editor.

<p align="center">
    <img width="1200" alt="sample" src="https://github.com/user-attachments/assets/e9f7e6ec-06c4-40e4-a93c-82945d3aaf63" />
</p>

<a href="https://github.com/williamchange/b3dsdf/blob/master/shader_nodes.json">![sdf_nodegroups](https://github.com/user-attachments/assets/7330815c-7091-41c6-95e4-7ab18597a767)</a>

## Install

Download the latest zip file from the [release page](https://github.com/williamchange/b3dsdf/releases) and install as normal. There's no need to unzip before installing. You might have to restart Blender for changes to take effect after installing.

Sample illustration built using some of these nodegroups can be downloaded <a href="https://github.com/williamchange/b3dsdf/releases/download/v0.12/b3dsdf-demo-b45.blend">here</a>.

## License

GPLv3 license ([LICENSE](LICENSE)) only applies to the python add-on source code. The Included asset file (`sdf_nodegroups.blend`) in this repository is under [CC0](https://creativecommons.org/publicdomain/zero/1.0/)([LICENSE_ASSET](LICENSE_ASSET.md)).

## References

- [Erindale's Toolkit (original add menu logic)](https://erindale.gumroad.com/l/erintools)
- [D6464 Blender SDF patch](https://archive.blender.org/developer/D6464)
- [Additonal references / Shadertoy playlist](https://www.shadertoy.com/playlist/7cjGR1)
- [Inigo Quilez - 3D Distance Functions](https://iquilezles.org/articles/distfunctions/)
- [Inigo Quilez - 2D Distance Functions](https://iquilezles.org/articles/distfunctions2d/)
- [Inigo Quilez - 2D Distance Functions in L-infinity norm](https://iquilezles.org/articles/distfunctions2dlinf/)
- [Inigo Quilez - 2D Distance Functions and gradients](https://iquilezles.org/articles/distgradfunctions2d/)
- [hg_sdf glsl library](https://mercury.sexy/hg_sdf/)
