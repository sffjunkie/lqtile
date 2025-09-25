from .typedef import RGBColor, RGBHex
from .convert import rgbhex_to_rgbcolor


def rgb_intensity(rgb: RGBColor):
    """Convert an RGB color to its intensity"""

    intensity = rgb[0] * 0.299 + rgb[1] * 0.587 + rgb[2] * 0.114
    return intensity


def contrast_color(
    color: RGBHex,
    light: RGBHex = "#FFFFFF",
    dark: RGBHex = "#000000",
) -> str:
    """Return either the light ior dark color
    whichever provides the most contrast"""

    rgb = rgbhex_to_rgbcolor(color)
    if rgb is None:
        return light

    if rgb == (0.0, 0.0, 0.0) or rgb_intensity(rgb) < (160.0 / 256.0):
        return light

    return dark
