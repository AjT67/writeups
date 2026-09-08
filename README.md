# Writeups

Penetration testing lab writeups — methodology, reasoning, and the dead ends.

These are working notes rather than walkthroughs. Where a solution path was
obvious in hindsight, the interesting part is what it took to see it, so the
enumeration reasoning and the approaches that failed are kept in deliberately.

**Only retired targets are published here.** See [publishing rules](writeups/README.md).

## Index

<!-- INDEX:START -->
| Date | Target | Platform | OS | Difficulty | Tags |
| --- | --- | --- | --- | --- | --- |
| 2026-09-07 | [Example — Home Lab VM](writeups/2026-09-example-homelab.md) | Own lab | Linux | Easy | `example`, `template-demo` |

_1 published writeup._
<!-- INDEX:END -->

## Layout

```
TEMPLATE.md            the writeup template — copy this to start a new one
writeups/              one markdown file per target
notes/methodology.md   the running personal checklist, updated as I learn
tools/build_index.py   regenerates the index table above from post frontmatter
```

## Adding a writeup

```bash
cp TEMPLATE.md writeups/2026-09-targetname.md
# write it, then flip `status: draft` to `status: published` in the frontmatter
python3 tools/build_index.py
```

Drafts are excluded from the index, so a half-finished writeup can live in the
repo without appearing on the front page.

The index also rebuilds automatically on push via GitHub Actions, so forgetting
the command is not fatal.

