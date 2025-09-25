from lqtile.theme.model import Theme


def test_default_theme(default_theme: Theme):
    assert default_theme.color.base16.palette.base00 == "#32302F"
