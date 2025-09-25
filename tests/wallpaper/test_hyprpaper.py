from pathlib import Path

from lqtile.wallpaper.hyprpaper import HyprpaperConfig


def test_hyprpaper_settings():
    data_dir = Path(__file__).parent.parent
    p = data_dir / "data" / "hyprpaper.conf"

    wallpaper = HyprpaperConfig(p)
    wallpapers = wallpaper.wallpapers()

    assert len(wallpapers) == 2
    assert wallpapers[0].image == Path("~/pictures/wallpaper/dt-walpaper/0001.jpg")
    assert wallpapers[0].monitor == "*"
    assert wallpapers[0].mode == "fill"
