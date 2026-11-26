"""Build mod/mod.json from translation/th.json.

Usage: python tools/build.py [LOCALE] [LANGUAGE_NAME]

The game refuses mods that override keys of a built-in language, so the translation is added as a
NEW language. LOCALE must therefore be a locale code the game does not ship; "tt" is used as a
neutral carrier code (the game's fonts fall back to their Thai face for Thai characters).
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE = sys.argv[1] if len(sys.argv) > 1 else "tt"
NAME = sys.argv[2] if len(sys.argv) > 2 else "ไทย (NeedSleep)"

messages = json.load(open(os.path.join(ROOT, "translation", "th.json"), encoding="utf-8"))
mod = {"translation": {"add": [{"name": NAME, "locale": LOCALE, "messages": dict(sorted(messages.items()))}]}}
out = os.path.join(ROOT, "mod", "mod.json")
with open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(mod, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out, "| messages:", len(messages), "| locale:", LOCALE)
