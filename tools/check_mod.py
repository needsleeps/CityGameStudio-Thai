"""Replay the game's own mod validation rules (scripts/json/validator/translation-add) against a mod.json.
Usage: python tools/check_mod.py <english.json> <mod.json> [<earlier mod.json> ...]"""
import json, sys
TAGS = [("[url=", "[/url]"), ("[b]", "[/b]"), ("[img]", "[/img]"), ("[color=", "[/color]"), ("[i]", "[/i]"), ("[ul]", "[/ul]"), ("[code]", "[/code]")]
BUILTIN = {"cs", "de", "en", "es", "fr", "it", "ja", "ko", "nl", "pl", "pt", "pt_BR", "ru", "th", "tr", "uk", "zh"}
def main():
    en = json.load(open(sys.argv[1], encoding="utf-8"))
    loaded = {}  # locale -> messages already added by earlier mods
    errs = 0
    for path in sys.argv[3:] + [sys.argv[2]]:
        doc = json.load(open(path, encoding="utf-8"))
        for entry in (doc.get("translation") or {}).get("add", []):
            loc = entry["locale"]; have = loaded.setdefault(loc, {})
            for k, v in entry["messages"].items():
                e = en.get(k, "")
                if e and (loc in BUILTIN or k in have):
                    print("OVERRIDE", path, loc, k); errs += 1
                if len(k) > 128: print("note: key longer than 128 (schema limit)", path, k[:50])
                if e.count("%s") != v.count("%s"): print("%s MISMATCH", path, loc, k[:60]); errs += 1
                if e.count("%d") != v.count("%d"): print("%d MISMATCH", path, loc, k[:60]); errs += 1
                for o, c in TAGS:
                    if v.count(o) != v.count(c): print("TAG", o, path, loc, k[:60]); errs += 1
                have[k] = v
    print("validator replay:", "OK" if not errs else "%d problems" % errs)
    sys.exit(1 if errs else 0)
main()
