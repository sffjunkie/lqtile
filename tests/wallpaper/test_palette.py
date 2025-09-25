from pathlib import Path
from lqtile.wallpaper.palette import wallpaper_palette_imagemagik


def test_wallpaper_palette():
    wallpaper = Path(__file__).parent.parent / "data" / "98856.jpg"

    color_palette = wallpaper_palette_imagemagik(wallpaper)
    assert color_palette is not None
    assert len(color_palette.colors.keys()) == 16
    assert color_palette.colors["color02"] == "#171A29"
