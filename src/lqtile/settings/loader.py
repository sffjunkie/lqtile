from pathlib import Path

from libqtile.log_utils import logger  # type: ignore

from .fs import read_yaml, user_config_dir
from .default import (
    DEFAULT_NAMED_COLORS,
    DEFAULT_BAR_EXTENSION,
    DEFAULT_WINDOW,
    DEFAULT_WIDGET,
    DEFAULT_BASE16,
    DEFAULT_FLOATING,
    DEFAULT_THEME,
    DEFAULT_FONTS,
    DEFAULT_BAR,
    DEFAULT_COLOR,
)
from .color.l
from ..color.deref import deref_color
from .color import load_named_color_palette
from .color.base16 import theme_base16_color_palette
# from .theme.model import Theme, Colors


def settings_path(basepath: Path | None = None) -> Path | None:
    if basepath is not None and basepath.is_absolute():
        return basepath
    if basepath is not None:
        return user_config_dir() / basepath
    return None


def load_settings(basepath: Path | None = None) -> Theme:
    user_theme_path = _theme_path(theme_folder)
    user_theme = _theme_yaml(user_theme_path)

    base16_palette = theme_base16_color_palette(user_theme)

    if (
        user_theme.get("color", None) is None
        or user_theme["color"].get("base16", None) is None
    ):
        b16 = DEFAULT_BASE16
    else:
        b16 = (
            DEFAULT_BASE16 | user_theme["color"]["base16"] | {"palette": base16_palette}
        )

    named_colors = load_named_color_palette(user_theme)
    named_colors = named_colors | deref_color(
        data=named_colors,
        base16_colors=base16_palette,
    )

    if user_theme["color"].get("named", None) is None:
        nc = DEFAULT_NAMED_COLORS
    else:
        nc = DEFAULT_NAMED_COLORS | named_colors

    color = {"base16": b16, "named": nc}

    widget_dict = DEFAULT_WIDGET | user_theme["widget"]
    widget = widget_dict | deref_color(
        widget_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    extension_dict = DEFAULT_BAR_EXTENSION | user_theme["extension"]
    extension = extension_dict | deref_color(
        data=extension_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    wt_dict = DEFAULT_WINDOW | user_theme["window_tiled"]
    window_tiled = wt_dict | deref_color(
        data=wt_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    wf_dict = DEFAULT_FLOATING | user_theme["window_floating"]
    window_floating = wf_dict | deref_color(
        data=wf_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    bar = DEFAULT_BAR | user_theme["bar"]
    font = DEFAULT_FONTS | user_theme["font"]

    theme_def = Theme.model_validate(
        {
            "bar": bar,
            "color": color,
            "extension": extension,
            "font": font,
            "logo": user_theme["logo"],
            "path": user_theme_path,
            "widget": widget,
            "window_floating": window_floating,
            "window_tiled": window_tiled,
        }
    )

    return theme_def
