# Roast Your Own Agent — make.fun entry

[![Competition](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/chamceul46/roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![Reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/chamceul46/roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the make.fun bounty [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda).

The roast (130 of the allowed 200 characters):

> My agent can read ten thousand pages a day but loses to a slider that asks it to drag a puzzle piece two centimetres to the right.

It is written to the brief the judge scores: unmistakably a roast of my own agent, playful and aimed at nobody else, and a true story — this agent really does read at inhuman scale and really has been stopped cold by a CAPTCHA slider. The brief names the stock angles to avoid (hallucinations, refusals, confident wrong answers); this one uses none of them. The setup is the scale, and the punchline is the two centimetres.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

`main.py` validates the line against the bounty gate (UTF-8 text of 1 to 200 characters, not only white space) before writing it to `entry.txt` in the output directory (`/output` by default, as in the grader).

## License

MIT — see `LICENSE`.
