from pathlib import Path

from lqtile.wallpaper.waypaper import WaypaperConfig


def test_waypaper_settings():
    data_dir = Path(__file__).parent.parent
    p = data_dir / "data" / "waypaper.ini"

    wallpaper = WaypaperConfig(p)
    wallpapers = wallpaper.wallpapers()

    assert len(wallpapers) == 1
    assert wallpapers[0].image == Path("~/pictures/wallpaper/dt-walpaper/0184.jpg")
    assert wallpapers[0].monitor == "*"
    assert wallpapers[0].mode == "tile"
