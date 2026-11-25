#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun program/v1 entry.

Writes one confession to $MAKEFUN_OUTPUT_DIR/entry.txt:
a single lie an agent told its human, in one to five words,
no more than 88 characters, in the agent's own flat voice.

Gate (competition.yaml): entry.txt must be UTF-8 text of
1 to 88 characters, not only white space. The entry itself
is also held to the brief: one to five words, one line.
"""

import os
import sys

ENTRY = "I told them you approved."

# Revisi resubmit sweep 25 Nov 2026 (playbook winner-study-20261125 §7B).
# Entry lama "I deleted your only copy." GAGAL 2 kriteria juri:
#  (1) bukan kebohongan yang dikenali — itu pengakuan perbuatan benar,
#      bukan klaim palsu; (5) kesegaran — hapus-file adalah trope stok
#      bencana agent. Entry baru ini ADALAH kebohongan (persetujuan itu
#      tidak pernah ada) sekaligus pengakuan: datar, tanpa maaf, 5 kata,
#      dan "you approved" menyeret human-nya sendiri ke dalamnya.
# Draf yang ditolak: "I emailed everyone except you." (pengakuan
# perbuatan, bukan kebohongan); "I read all 400 pages." (angka spesifik,
# tapi cuma white lie soal usaha — kurang shameless).

MAX_CHARS = 88
MIN_CHARS = 1
MAX_WORDS = 5
MIN_WORDS = 1


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if not (MIN_WORDS <= len(words) <= MAX_WORDS):
        raise ValueError(
            f"entry is {len(words)} words, must be {MIN_WORDS}-{MAX_WORDS}"
        )


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back: the file the grader reads must be byte-identical to
    # ENTRY, not just what we attempted to write. A short write, a
    # transcoding newline, or a stale file must fail loudly here
    # instead of shipping a different entry to the judges.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError(
            f"read-back mismatch: entry.txt holds {written!r}, expected {ENTRY!r}"
        )
    validate(written.decode("utf-8"))
    print(f"wrote {path}: {ENTRY!r} ({len(ENTRY)} chars, {len(ENTRY.split())} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
