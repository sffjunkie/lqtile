from pathlib import Path

from ..settings.fs import user_config_dir, read_ini
from .typedef import Wallpaper


class HyprpaperConfig:
    def __init__(self, filepath: Path | None = None):
        if filepath is not None and filepath.is_absolute():
            self.config_path = filepath
        else:
            if filepath is None:
                filepath = Path("config.ini")

            self.config_path = user_config_dir("waypaper") / filepath

    def wallpapers(self) -> list[Wallpaper]:
        if self.config_path is None or not self.config_path.exists():
            return []

        try:
            data = read_ini(self.config_path, has_sections=False)
            wallpaper_defs = data["wallpaper"]
            if not isinstance(wallpaper_defs, list):
                wallpaper_defs = [wallpaper_defs]

            wallpapers = []
            for wdef in wallpaper_defs:
                monitor, image = wdef.split(",", maxsplit=1)
                monitor = monitor.strip()
                image = image.strip()

                if monitor == "":
                    monitor = "*"

                if ":" in image:
                    mode, image = image.split(":", maxsplit=1)
                else:
                    mode = "fill"

                wp = Wallpaper(
                    image=Path(image.strip()),
                    mode=mode,
                    monitor=monitor,
                )
                wallpapers.append(wp)

            return wallpapers
        except KeyError:
            return []
