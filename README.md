# Custom Kanji creator

This repo is a fork of [kage-python](https://github.com/HowardZorn/kage-engine), which is implemented in Python, basedon Kage Engine, is a glyph generation engine for Chinese Characters (漢字、汉字), which is mainly developed by [@kamichikoichi](https://github.com/kamichikoichi/kage-engine) (上地宏一) and [@kurgm](https://github.com/kurgm/kage-engine). 
## Example Usage

### Pre-requisites

Download `dump_newest_only.txt` or `dump_all_versions.txt` from [GlyphWiki](https://glyphwiki.org/wiki/GlyphWiki:%e9%ab%98%e5%ba%a6%e3%81%aa%e6%b4%bb%e7%94%a8%e6%96%b9%e6%b3%95) and store it in the root folder.

### Idea

```python3
def main():
    readData()

    sl1 = getStrokesList('杜')
    sl2 = getStrokesList('駂')

    strokes_list = sl1[:4] + sl2[4:]
    make_glyph(strokes_list)


main()
```

Assumption: the Kanji you want to create can be represented using portions of other existing Kanji.

Example custom Kanji:

![](example_output.png)

1. Find Kanji, where a portion of the Kanji closely matches what you want. In this case, we can take the left portion of 杜 and the right portion of 駂.
2. Use `getStrokesList()` to obtain the list of strokes for that Kanji. Then, you can take the appropriate subset of this list, to obtain the strokes that you require.
3. Combine them into a single `strokes_list` list and pass that into `make_glyph()`.
