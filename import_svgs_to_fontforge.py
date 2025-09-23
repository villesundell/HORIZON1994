# Run this with: fontforge -script import_svgs_to_fontforge.py [small|large]
import fontforge
import sys
import os
import re

def generate_files(SIZE, DIMENSIONS, INPUT_DIR, GLYPH_WIDTH):
    # === SETTINGS ===
    BASENAME = "horizon1994-" + SIZE.lower()
    EXPORT_TTF = True
    EXPORT_WOFF = True
    EXPORT_WOFF2 = True

    # === Initialize font ===
    font = fontforge.font()
    font.encoding = "UnicodeFull"
    font.fontname = "HORIZON1994"
    font.fullname = "HORIZON1994 Fixed " + SIZE + " (" + DIMENSIONS + ")"
    font.familyname = "HORIZON1994"
    font.copyright = "Public domain (CC0)"
    font.version = "1.0"

    font.sfnt_names = [
        ("English (US)", "License", "CC0-1.0"),
        ("English (US)", "License URL", "https://creativecommons.org/publicdomain/zero/1.0/"),
        ("English (US)", "Manufacturer", "Ville Sundell")
    ]

    font.ascent = 875
    font.descent = 125
    font.em = 1000

    # === Regex for U+XXXX.svg filenames ===
    pattern = re.compile(r'U\+([0-9A-Fa-f]{4,6})\.svg')

    # === Process all matching SVGs ===
    for fname in os.listdir(INPUT_DIR):
        match = pattern.match(fname)
        if not match:
            continue
        codepoint = int(match.group(1), 16)
        path = os.path.join(INPUT_DIR, fname)
        glyph = font.createChar(codepoint)
        glyph.manualHints = True;
        glyph.importOutlines(path)
        glyph.width = GLYPH_WIDTH
        print(f"Imported {fname} → U+{codepoint:04X}")

    # === Save the font ===
    font.generate(BASENAME + ".sfd")
    print(f"✅ Saved SFD")

    if EXPORT_TTF:
        font.generate(BASENAME + ".ttf")
        print("✅ Saved TTF")

    if EXPORT_WOFF:
        font.generate(BASENAME + ".woff")
        print("✅ Saved WOFF")

    if EXPORT_WOFF2:
        font.generate(BASENAME + ".woff2")
        print("✅ Saved WOFF2")

def generate_small_files():
    generate_files("Small", "8x8", "./glyphs_8_unicode_nopadding_svg", 1000)

def generate_large_files():
    generate_files("Large", "8x16", "./glyphs_16_unicode_nopadding_svg", 500)

def generate_all_files():
    generate_small_files()
    generate_large_files()

if sys.argv[1] == "small":
    generate_small_files()    
elif sys.argv[1] == "large":
    generate_large_files()
else:
    generate_all_files()


