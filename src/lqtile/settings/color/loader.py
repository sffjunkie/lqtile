from pathlib import Path

from ..fs import read_yaml


def load_color(basepath: Path) -> dict:
    p = basepath / "color.yaml"
    data = read_yaml(p)
    return data
