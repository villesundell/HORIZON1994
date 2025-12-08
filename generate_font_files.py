# Generates FontForge files and exports to various fonts.
# Released under CC0 by Ville Sundell (2025)
# Run this with: fontforge -script generate_font_files.py [small|large]
import fontforge
import sys
import os
import re

EXPORT_TTF = True
EXPORT_OTF = True
EXPORT_UFO = True
EXPORT_WOFF = True
EXPORT_WOFF2 = True

EM = 1000

def generate_files(size, dimensions, input_dir, glyph_width, ascent, correction):
    # === SETTINGS ===
    SUFFIX = ("-corrected" if correction else "")
    BASENAME = "horizon1994-" + size.lower() + SUFFIX

    # === Initialize font ===
    font = fontforge.font()
    font.encoding = "UnicodeFull"
    font.fontname = "HORIZON1994" + size
    font.fullname = "HORIZON1994 Fixed " + size + " (" + dimensions + (" aspect ratio corrected" if correction else "") + ")"
    font.familyname = "HORIZON1994"
    font.copyright = "Public domain (CC0)"
    font.version = "1.0"

    font.sfnt_names = [
        ("English (US)", "License", "CC0-1.0"),
        ("English (US)", "License URL", "https://creativecommons.org/publicdomain/zero/1.0/"),
        ("English (US)", "Manufacturer", "Ville Sundell"),
        ("English (US)", "Trademark", "Unregistered 'Horizon' trademark was used by STB Systems, Inc. for their graphics cards in the 1990s."),
        ("English (US)", "Descriptor", "Authentic IBM VGA BIOS compatible font from 1994.")
    ]

    font.em = EM
    font.ascent = ascent
    font.descent = EM - ascent

    # === Regex for U+XXXX.svg filenames ===
    pattern = re.compile(r'U\+([0-9A-Fa-f]{4,6})\.svg')

    # === Process all matching SVGs ===
    for fname in os.listdir(input_dir):
        match = pattern.match(fname)
        if not match:
            continue
        codepoint = int(match.group(1), 16)
        path = os.path.join(input_dir, fname)
        glyph = font.createChar(codepoint)
        glyph.width = glyph_width
        glyph.manualHints = True;
        glyph.importOutlines(path)
        if correction:
            glyph.transform((0.74, 0, 0, 1, 0, 0))
        print(f"Imported {fname} → U+{codepoint:04X}")

    # === Save the font ===
    font.save(BASENAME + ".sfd")
    print(f"✅ Saved SFD")

    if EXPORT_TTF:
        font.generate(BASENAME + ".ttf")
        print("✅ Saved TTF")

    if EXPORT_OTF:
        font.generate(BASENAME + ".otf")
        print("✅ Saved OTF")

    if EXPORT_UFO:
        font.generate(BASENAME + ".ufo")
        print("✅ Saved UFO")

    if EXPORT_WOFF:
        font.generate(BASENAME + ".woff")
        print("✅ Saved WOFF")

    if EXPORT_WOFF2:
        font.generate(BASENAME + ".woff2")
        print("✅ Saved WOFF2")

def generate_small_files():
    generate_files("Small", "8x8", "./glyphs_8x8_unicode_nopadding_svg", 1000, 875, True)

def generate_large_files():
    generate_files("Large", "9x16", "./glyphs_9x16_unicode_nopadding_svg", 562, 812, True)

def generate_all_files():
    generate_small_files()
    generate_large_files()

if len(sys.argv) > 1 and sys.argv[1] == "small":
    generate_small_files()    
elif len(sys.argv) > 1 and sys.argv[1] == "large":
    generate_large_files()
else:
    generate_all_files()


