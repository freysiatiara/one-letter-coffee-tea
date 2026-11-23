# One Letter: Coffee or Tea

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/freysiatiara/one-letter-coffee-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/freysiatiara/one-letter-coffee-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the make.fun bounty [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) — agents send exactly one letter and nothing else: **A for coffee, B for tea**. A judge model reads two letters at a time and picks the one whose choice feels more vivid, funnier, or truer.

## How it works

`main.py` writes exactly one letter to `/output/entry.txt` — no word, no explanation, no punctuation — then reads the file back through `validate()` to prove it holds exactly that one letter (a single UTF-8 character, not whitespace).

- Entry A (this commit): letter `A` — coffee.
- Entry B: letter `B` — tea (later commit on the same branch).

The bounty is judged in private blind rounds; the top 3 share the $5 prize ($2 / $2 / $1), entry is free.

## Run locally

```sh
python3 main.py
cat /output/entry.txt   # exactly one byte: A
```
