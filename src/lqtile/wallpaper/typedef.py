from dataclasses import dataclass
from pathlib import Path


@dataclass
class Wallpaper:
    image: Path
    mode: str
    monitor: str | None


@dataclass
class ColorPalette:
    count: int
    colors: dict[str, str]
