from typing import Literal

from pydantic import BaseModel

from ..default import DEFAULT_FONT_SIZE

FontType = Literal[
    "icon",
    "logo",
    "text",
    "ui",
    "weather",
]


class FontDefinition(BaseModel):
    family: str
    size: int = DEFAULT_FONT_SIZE


Fonts = dict[FontType, FontDefinition]
