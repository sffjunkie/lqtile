import string
from typing import cast

from .typedef import Opacity, RGBColor, RGBHex


def rgbhex_to_rgbcolor(value: RGBHex, allow_short: bool = True) -> RGBColor | None:
    """Convert from a hex color string of the form `#abc` or `#abcdef` to an
    RGB tuple.

    :param value: The value to convert
    :type value: str
    :param allow_short: If True then the short of form of an hex value is
                        accepted e.g. #fff
    :type allow_short:  bool
    """
    if value[0] == "#":
        value = value[1:]

    for ch in value:
        if ch not in string.hexdigits:
            return None

    if len(value) == 6:
        # The following to_iterable function is based on the
        # :func:`grouper` function in the Python standard library docs
        # http://docs.python.org/library/itertools.html
        def to_iterable() -> RGBColor:
            # pylint: disable=missing-docstring
            args = [iter(value)] * 2

            elems: RGBColor = cast(
                RGBColor,
                tuple(
                    [int("%s%s" % t, 16) / 256 for t in zip(*args)],
                ),
            )
            return elems

    elif len(value) == 3 and allow_short:

        def to_iterable() -> RGBColor:
            # pylint: disable=missing-docstring
            return cast(
                RGBColor,
                tuple(
                    [int("%s%s" % (t, t), 16) / 256 for t in value[1:]],
                ),
            )

    else:
        return None

    try:
        return to_iterable()
    except ValueError:
        return None


def rgbcolor_to_rgbhex(value: RGBColor) -> RGBHex:
    """Convert from an (R, G, B) tuple to a hex color.

    :param value: The RGB value to convert

    R, G and B should be in the range 0.0 - 1.0
    """
    color = "".join(["%02x" % x1 for x1 in [int(x * 256) for x in value]])
    return "#%s" % color


def opacity_to_str(opacity: Opacity) -> str:
    return hex(int(opacity * 255.0))[2:]
