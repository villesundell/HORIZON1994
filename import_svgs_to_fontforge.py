# Run this with: fontforge -script import_svgs_to_fontforge.py [small|large]
import fontforge
import sys
import os
import re

if sys.argv[1] == "small":
    SIZE = "Small"
    DIMENSIONS = "8x8"
    INPUT_DIR = "./glyphs_8_unicode_nopadding_svg"
elif sys.argv[1] == "large":
    SIZE = "Large"
    DIMENSIONS = "8x16"
    INPUT_DIR = "./glyphs_16_unicode_nopadding_svg"
else:
    exit("Error: Tell me the size")

# === SETTINGS ===
BASENAME = "horizon1994-" + SIZE.lower()
OUTPUT_SFD = BASENAME + ".sfd"
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

font.ascent = 800
font.descent = 200
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
    glyph.width = 500
    print(f"Imported {fname} → U+{codepoint:04X}")

# === Save the font ===
font.generate(OUTPUT_SFD)
print(f"✅ Saved SFD: {OUTPUT_SFD}")

if EXPORT_TTF:
    font.generate(BASENAME + ".ttf")
    print("✅ Saved TTF")

if EXPORT_WOFF:
    font.generate(BASENAME + ".woff")
    print("✅ Saved WOFF")

if EXPORT_WOFF2:
    font.generate(BASENAME + ".woff2")
    print("✅ Saved WOFF2")
