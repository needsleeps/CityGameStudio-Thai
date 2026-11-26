"""Read the English (or any other) text of your own installed game for the keys in translation/th.json.

Usage: python tools/dump_game_strings.py "<path to City Game Studio folder>" [locale] > english.json
Example: python tools/dump_game_strings.py "C:\\Program Files (x86)\\Steam\\steamapps\\common\\City Game Studio" en

Nothing from the game is stored in this repository; this only reads your local copy so that
tools/check_mod.py can compare placeholders against the source text.
"""
import json, os, sys, struct, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pck, xl


def main():
    game = sys.argv[1]
    locale = sys.argv[2] if len(sys.argv) > 2 else "en"
    pck_path = os.path.join(game, "data.pck")
    _, files = pck.read_index(pck_path)
    wanted = "res://translation/translation.%s.xl" % locale
    hit = [f for f in files if f[0] == wanted]
    if not hit:
        sys.exit("locale not found in data.pck: " + locale)
    name, ofs, size = hit[0]
    with open(pck_path, "rb") as f:
        f.seek(ofs); blob = f.read(size)
    tmp = os.path.join(tempfile.gettempdir(), "cgs_translation_%s.xl" % locale)
    with open(tmp, "wb") as f:
        f.write(blob)
    table = xl.XL(tmp, xl.smaz_table())
    keys = json.load(open(os.path.join(os.path.dirname(HERE), "translation", "th.json"), encoding="utf-8"))
    out = {k: table.get(k) for k in keys}
    sys.stdout.reconfigure(encoding="utf-8")
    json.dump({k: v for k, v in out.items() if v is not None}, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
