from __future__ import annotations

import json
import random
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from importlib.resources import files

from .Cow import Cow

COW_NAMES = json.loads(
    files(__package__).joinpath("cow_names.json").read_text(encoding="utf-8")
)
KB_BATCH_SIZE = 64

def rand_cow_name():
    return random.choice(COW_NAMES)

def make_cow_text(normal_only: bool = False) -> tuple[str, bool]:
    """Build one random cow and return its rendered text and normality."""
    cow = Cow(
        rand_cow_name(),
        is_normal_cow=True if normal_only else None,
    )
    return cow.moo_text(), cow.is_normal_cow

def run_kilobytes(kilobytes: int, write_output: bool, normal_only: bool = False) -> tuple[Counter[str], int]:
    """Generate cows in a thread pool until at least `kilobytes` KB are produced."""
    target = kilobytes * 1024
    produced = 0
    counter: Counter[str] = Counter()

    with ThreadPoolExecutor() as pool:
        while produced < target:
            for text, is_normal in pool.map(
                lambda _: make_cow_text(normal_only),
                range(KB_BATCH_SIZE),
            ):
                if write_output:
                    sys.stdout.write(text + "\n")
                produced += len(text.encode("utf-8")) + 1
                counter.update(["Normal Cows" if is_normal else "Anomalous Cows"])
                if produced >= target:
                    break

    return counter, produced
