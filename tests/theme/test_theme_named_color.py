from lqtile.theme.model import Theme
from lqtile.theme.model.color import NamedColors


def test_theme_named_color_startswith_hash(default_theme: Theme):
    assert default_theme.color.named.panel_bg.startswith("#")
