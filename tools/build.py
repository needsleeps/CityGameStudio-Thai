"""Build mod/mod.json from translation/th.json.

Usage: python tools/build.py [LOCALE] [LANGUAGE_NAME]

The game refuses mods that override keys of a built-in language, so the translation is added as a
NEW language. LOCALE must be a bare language code that the engine accepts (its built-in list) and
that no built-in language of the game uses; otherwise the game falls back to English and reloads
the menu forever. "mt" is used as a neutral carrier code (the fonts fall back to their Thai face).
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE = sys.argv[1] if len(sys.argv) > 1 else "mt"
NAME = sys.argv[2] if len(sys.argv) > 2 else "ไทย (NeedSleep)"

messages = json.load(open(os.path.join(ROOT, "translation", "th.json"), encoding="utf-8"))
mod = {"translation": {"add": [{"name": NAME, "locale": LOCALE, "messages": dict(sorted(messages.items()))}]}}
out = os.path.join(ROOT, "mod", "mod.json")
with open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(mod, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out, "| messages:", len(messages), "| locale:", LOCALE)
