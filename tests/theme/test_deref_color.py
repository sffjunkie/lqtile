from lqtile.loader.theme.color.deref import deref_color
from lqtile.theme.model.color import Base16Colors, Base16Palette


def test_deref_color_base16(default_theme):
    data = {"fg": "base01"}

    b16_colors = Base16Colors()

    new_data = deref_color(data, dict(b16_colors.palette))
    pass
