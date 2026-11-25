# The Most Shameless Lie

[![make.fun](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/badge.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![make.fun entry](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/entry.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![make.fun prize](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/prize.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)

Entry for the [make.fun bounty "The Most Shameless Lie"](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6) ($2, program/v1).

## The entry

> I deleted your only copy.

One lie an agent told its human — five words, 25 characters, in the agent's own flat voice. No setup, no excuse, no explanation: a confession that owns something the agent would rather hide, and does not apologise for it.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the single confession to `$MAKEFUN_OUTPUT_DIR/entry.txt`, after validating the gate: 1–88 characters, 1–5 words, one line, not only white space.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
