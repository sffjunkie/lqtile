from lqtile.theme.model import Theme
from qtile.config.loader.theme.color.iter import (
    _widget_bg_iter,
    _widget_fg_iter,
    widget_color_iter,
)


def test_default_bg_iter(default_theme: Theme):
    iter = _widget_bg_iter(default_theme.color.named)
    assert next(iter) == "#D08770"
    assert next(iter) == "#D08770"
    assert next(iter) == "#D08770"


def test_bg_iter(theme: Theme):
    iter = _widget_bg_iter(theme.color.named)
    assert next(iter) == "#8FBCBB"
    assert next(iter) == "#ECEFF4"
    assert next(iter) == "#8FBCBB"


def test_default_fg_iter(default_theme: Theme):
    iter = _widget_fg_iter(default_theme.color.named)
    assert next(iter) == "#D8DEE9"


def test_fg_iter(theme: Theme):
    iter = _widget_fg_iter(theme.color.named)
    assert next(iter) == "#2E3440"


def test_widget_color_iter(theme: Theme):
    iter = widget_color_iter(theme.color.named)
    assert next(iter) == ("#2E3440", "#8FBCBB")
    assert next(iter) == ("#2E3440", "#ECEFF4")
    assert next(iter) == ("#2E3440", "#8FBCBB")
