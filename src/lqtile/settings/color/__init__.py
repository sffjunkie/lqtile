from pathlib import Path

from ...color.deref import deref_color
from .model import Colors
from ..fs import read_yaml
from ..default import DEFAULT_NAMED_COLORS, DEFAULT_COLOR, DEFAULT_BASE16


def load_named_color_palette(
    color_data: dict,
) -> dict:
    if color_data["color"] is None or color_data["color"]["named"] is None:
        named_colors = DEFAULT_NAMED_COLORS
    else:
        named_colors = DEFAULT_NAMED_COLORS | color_data["color"]["named"]

    return named_colors


def load_color(settings_path: Path) -> Colors:
    default_colors = Colors.model_validate(DEFAULT_COLOR)
    color_data = read_yaml(settings_path)

    if not color_data:
        return default_colors

    base16_palette = theme_base16_color_palette(color_data)

    if user_theme["color"].get("base16", None) is None:
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

    return Colors.model_validate(color)
