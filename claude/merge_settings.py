# Fusionne les réglages du kit dans ~/.claude/settings.json sans écraser l'existant.
import json, os, sys
p = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")
cur = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
new = json.load(open(sys.argv[1], encoding="utf-8"))
for k, v in new.items():
    cur[k] = {**cur.get(k, {}), **v} if isinstance(v, dict) else v
json.dump(cur, open(p, "w", encoding="utf-8"), indent=2)
