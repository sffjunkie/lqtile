from pydantic import BaseModel

from ..default import DEFAULT_WINDOW
from ..default import (
    DEFAULT_TEXT_FONT,
    DEFAULT_FONT_SIZE,
    DEFAULT_BASE16_PALETTE,
    DEFAULT_NAMED_COLORS,
    DEFAULT_MARGIN,
    DEFAULT_PADDING,
)


class Widget(BaseModel):
    font: str = DEFAULT_TEXT_FONT
    fontsize: int = DEFAULT_FONT_SIZE
    foreground: str = DEFAULT_BASE16_PALETTE["base00"]
    background: str = DEFAULT_NAMED_COLORS["widget_bg"]
    margin: int = DEFAULT_MARGIN
    padding: int = DEFAULT_PADDING


class WindowTiled(BaseModel):
    margin: int = DEFAULT_WINDOW["margin"]
    border_width: int = DEFAULT_WINDOW["border_width"]
    border_focus: str = DEFAULT_WINDOW["border_focus"]
    border_normal: str = DEFAULT_WINDOW["border_normal"]


class WindowFloating(BaseModel):
    border_width: int = DEFAULT_WINDOW["border_width"]
    border_focus: str = DEFAULT_WINDOW["border_focus"]
    border_normal: str = DEFAULT_WINDOW["border_normal"]
