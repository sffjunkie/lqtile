from itertools import cycle
from typing import Iterator

from ...color.contrast import contrast_color
from ..default import DEFAULT_NAMED_COLORS
from .model import NamedColors


def _widget_fg_iter(named_colors: NamedColors) -> Iterator:
    def fg_cycle(iterable, fg_light: str, fg_dark: str) -> Iterator:
        saved = []
        for element in iterable:
            fg = contrast_color(element, fg_light, fg_dark)
            yield fg
            saved.append(fg)

        while saved:
            for element in saved:
                yield element

    return fg_cycle(
        named_colors.widget_bg or DEFAULT_NAMED_COLORS["widget_bg"],
        named_colors.widget_fg_light or DEFAULT_NAMED_COLORS["fg_light"],
        named_colors.widget_fg_dark or DEFAULT_NAMED_COLORS["fg_dark"],
    )


def _widget_bg_iter(named_colors: NamedColors) -> Iterator:
    return cycle(named_colors.widget_bg or DEFAULT_NAMED_COLORS["widget_bg"])


def widget_color_iter(named_colors: NamedColors) -> Iterator[tuple[str, str]]:
    bg_iter = _widget_bg_iter(named_colors)
    fg_iter = _widget_fg_iter(named_colors)

    while True:
        fg = next(fg_iter)
        bg = next(bg_iter)
        yield fg, bg
