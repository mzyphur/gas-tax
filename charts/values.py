"""Load the public values manifest (data/values.yml).

Chart scripts import via `from values import load_values` when run from
the charts directory.
"""

from __future__ import annotations
from functools import lru_cache
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
_VALUES_FILE = _REPO_ROOT / "data" / "values.yml"


@lru_cache(maxsize=1)
def load_values() -> dict:
    """Parse and return the values manifest as a dict.

    Cached so repeated calls within one process don't re-parse the YAML.
    """
    if not _VALUES_FILE.exists():
        raise FileNotFoundError(
            f"Canonical values manifest not found at {_VALUES_FILE}. "
            "This file is the single source of truth for every number "
            "that appears in more than one place across the report."
        )
    return yaml.safe_load(_VALUES_FILE.read_text(encoding="utf-8"))


# Convenience alias for direct attribute-style access if preferred.
VALUES = load_values()
