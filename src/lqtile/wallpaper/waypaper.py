import configparser
from pathlib import Path

from ..settings.fs import user_config_dir
from .typedef import Wallpaper


"""
wallpaper = image.png
monitors = All

wallpaper = image1.png,image2.png
monitors = All, HDMI-A-1
"""


class WaypaperConfig:
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

        parser = configparser.ConfigParser()
        with self.config_path.open() as fp:
            parser.read_file(fp)

        wallpaper = parser["Settings"].get("wallpaper", None)
        monitor = parser["Settings"].get("monitors", "*")
        mode = parser["Settings"].get("fill", "fill")

        if wallpaper is None:
            return []

        if "," in wallpaper:
            _image_strs = wallpaper.split(",")
        else:
            _image_strs = [wallpaper]

        images = [Path(p) for p in _image_strs]

        if "," in monitor:
            monitors = monitor.split(",")
        else:
            monitors = [monitor]

        assert len(images) == len(monitors)

        wallpapers = []
        for idx, image in enumerate(images):
            monitor = monitors[idx]
            if monitor == "All":
                monitor = "*"
            wallpapers.append(
                Wallpaper(
                    image=image,
                    monitor=monitor,
                    mode=mode,
                )
            )

        return wallpapers
