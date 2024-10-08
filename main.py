from kage import Kage
from kage.font.sans import Sans
import csv
from cairosvg import svg2png

# Set the flag `ignore_component_version` if you want to use the glyph data in `dump_newest_only.txt`.
# This is because `dump_newest_only.txt` only contains the latest version of components.
# However, glyphs in `dump_newest_only.txt` may reference older versions of multiple components.
k = Kage(ignore_component_version=True)
# You can use `Serif()` as well!
k.font = Sans()


# get unicode 0x6708 then strip 0x
def getUnicode(kanji):
    return hex(ord(kanji))[2:]


# get strokes list
def getStrokesList(kanji):
    strokes_list = k.get_strokes_list_given_glyph(kanji)
    for stroke in strokes_list:
        print("\t", stroke, "\n", end="")


# generate a glyph
def gen(kanji):
    idx = getUnicode(kanji)
    key = 'u' + idx
    canvas = k.make_glyph(name=key)

    # Save as PNG
    xml_string = canvas.tostring()
    svg2png(bytestring=xml_string, write_to=f'output/{idx}.png')

    # Save as SVG
    # canvas.saveas(os.path.join('./output', f'{key}.svg'))


def readData():
    # read the glyph data
    with open('dump_newest_only.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = csv.reader(lines, delimiter='|')
    for i, line in enumerate(lines):
        if i <= 1 or len(line) < 3:
            continue
        line = [i.strip() for i in line]

        k.components.push(line[0], line[2])


def main():
    readData()
    gen('林')


main()

