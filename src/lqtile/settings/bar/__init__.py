from pathlib import Path

from .model import Bars
from ..default import DEFAULT_BAR
from ..fs import read_yaml


def load_bar(settings_path: Path) -> dict:
    default_bar = Bars.model_validate(DEFAULT_BAR)

    bar_settings = read_yaml(settings_path)
    settings = Bars.model_validate(bar_settings)

    merged = default_bar.model_dump() | settings.model_dump()
    return merged
