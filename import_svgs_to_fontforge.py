# Run this with: fontforge -script import_svgs_to_fontforge.py ./my_png_folder
import fontforge
import sys
import os
import re

# === SETTINGS ===
INPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "./"
OUTPUT_SFD = "horizon-1994-small.sfd"
EXPORT_TTF = False
EXPORT_WOFF = False
EXPORT_WOFF2 = False

# === Initialize font ===
font = fontforge.font()
font.encoding = "UnicodeFull"
font.fontname = "BIOSSmall"
font.fullname = "Horizon '94 Small"
font.familyname = "Horizon '94"
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
    print(f"Imported {fname} → U+{codepoint:04X}")

# === Save the font ===
font.generate(OUTPUT_SFD)
print(f"✅ Saved SFD: {OUTPUT_SFD}")

if EXPORT_TTF:
    font.generate("bios-font.ttf")
    print("✅ Saved TTF: bios-font.ttf")

if EXPORT_WOFF:
    font.generate("bios-font.woff")
    print("✅ Saved WOFF: bios-font.woff")

if EXPORT_WOFF2:
    font.generate("bios-font.woff2")
    print("✅ Saved WOFF2: bios-font.woff2")
