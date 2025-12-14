# HORIZON1994 Font

Authentic IBM VGA BIOS-compatible font from 1994, originally designed for Cirrus Logic's CL-GD543x series. Designed to look as seen on a CRT monitor of [IBM Aptiva 2144-92W](http://ps-2.kev009.com/pcpartnerinfo/ctstips/9e36.htm) from 1995 (with aspect ratio correction and enchanged glyphs). Traced from the [STB Horizon Plus'](https://dosdays.co.uk/topics/Manufacturers/stb/horizon+.php) BIOS. The BIOS firmware is still available on-line ([`HORIZON-PCI-1.31.rom`](https://drive.usercontent.google.com/download?id=1WG81D1si9OFmcvAahldc1smjFVArijJx)), and has SHA3 checksum of `471cda4e422b826adaadbfeccd7081d91cd6c44b4c1cb68bb11eb53d`. The same font can be found from `VGAPCI30.BIN` which is part of the source distribution [`CL543X110B_Firmware.ZIP`](https://dosdays.co.uk/media/cirrus_logic/CL543X110B_Firmware.ZIP) (SHA3: `f71dca4e8f5df4fa9b9739ddd253a278a63abf39485e5abb9d1000cc`).

This work is in the public domain ([CC0](https://creativecommons.org/publicdomain/zero/1.0/)), as [are the original bitmap fonts](https://www.crowdspring.com/blog/font-law-licensing/).

Thanks to [Valentin François](https://github.com/ValentinFrancois) for the [pixels2svg](https://github.com/ValentinFrancois/pixels2svg) Python library, which was used to generate the SVGs!

With small modifications, you can adapt the [generate_font_files.py](./generate_font_files.py) script for any "SVG to font files" project (especially for monospaced fonts).

## Generate font files
To generate the font files from the SVG sources, you need [FontForge](https://fontforge.org/en-US/). Once installed, you can simple run:
```bash
fontforge -script generate_font_files.py
```
to generate all the font files. Optionally you can supply "large" or "small" to generate just one subset.

**⚠️ NOTE:** Despite numerous efforts to [find out](https://graphicdesign.stackexchange.com/questions/169571/should-i-use-descent-in-monospace-fonts), I was unable to conclude whether I should use `descent` to set the `baseline` in the case of fixed fonts like this one. I decided to pursue the model I find more idiomatic: defining baseline along the base of capital letters (commit cdebc7d).