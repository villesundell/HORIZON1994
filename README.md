# HORIZON1994 Font

Authentic IBM VGA BIOS-compatible font from 1994, originally designed for Cirrus Logic's CL-GD543x series. Traced from the [STB Horizon Plus'](https://dosdays.co.uk/topics/Manufacturers/stb/horizon+.php) BIOS. The BIOS firmware is still available on-line ([`HORIZON-PCI-1.31.rom`](https://drive.usercontent.google.com/download?id=1WG81D1si9OFmcvAahldc1smjFVArijJx)), and has SHA3 checksum of `471cda4e422b826adaadbfeccd7081d91cd6c44b4c1cb68bb11eb53d`. This work is in the public domain ([CC0](https://creativecommons.org/publicdomain/zero/1.0/)), as [are the original bitmap fonts](https://www.crowdspring.com/blog/font-law-licensing/).

Thanks to [Valentin François](https://github.com/ValentinFrancois) for the [pixels2svg](https://github.com/ValentinFrancois/pixels2svg) Python library, which was used to generate the SVGs!

With small modifications, you can adapt the [generate_font_files.py](./generate_font_files.py) script for any "SVG to font files" project (especially for monospaced fonts).

**⚠️ NOTE:** Despite numerous efforts to [find out](https://graphicdesign.stackexchange.com/questions/169571/should-i-use-descent-in-monospace-fonts), I was unable to conclude whether I should use `descent` to set the `baseline` in the case of fixed fonts like this one. I decided to pursue the model I find more idiomatic: defining baseline along the base of capital letters (commit cdebc7d).