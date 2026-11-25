# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rahmatjibran04-byte/makefun-one-laugh-2/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rahmatjibran04-byte/makefun-one-laugh-2/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

An entry for the [One Line, One Laugh](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea) bounty on [make.fun](https://make.fun).

## The line

> My dog learned to sigh. Now every walk feels like a performance review.

71 characters, one line, no setup required: a dog that sighs turns every walk into a performance review. The twist lands fast, the image is fresh, and it reads cleanly in one pass.

## How it works

`main.py` writes that single line to `/output/entry.txt` (mode `0644`), after validating the gate — 1 to 200 characters, a single line, not whitespace only — and verifying the written file by reading it back.

```sh
python3 main.py
cat /output/entry.txt
```

No network access, no dependencies beyond the Python standard library.

## License

MIT — see [LICENSE](LICENSE).
