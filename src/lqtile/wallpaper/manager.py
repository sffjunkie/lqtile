from pathlib import Path
from .waypaper import WaypaperConfig
from .hyprpaper import HyprpaperConfig
from .palette import ColorPalette, wallpaper_palette_imagemagik


class WallpaperManager:
    def __init__(self, setter: str = "waypaper"):
        if setter == "waypaper":
            self._wallpaper_cfg = WaypaperConfig()
        else:
            self._wallpaper_cfg = HyprpaperConfig()

        self._wallpaper_list = self._wallpaper_cfg.wallpapers()

    def wallpaper(self, output_name: str = "*") -> Path | None:
        all_path = None
        for wallpaper in self._wallpaper_list:
            if output_name == wallpaper.monitor:
                return wallpaper.image
            elif wallpaper.monitor == "All" and all_path is not None:
                all_path = wallpaper.image

        return all_path

    def fill_mode(self, output_name: str = "*") -> str:
        for wallpaper in self._wallpaper_list:
            if output_name == wallpaper.monitor:
                return wallpaper.mode
        return "fill"

    def palette(self, wallpaper: Path, count: int = 16) -> ColorPalette | None:
        cp = wallpaper_palette_imagemagik(wallpaper, count)
        return cp
