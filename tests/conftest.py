from pathlib import Path
from pytest import fixture

from lqtile.settings.input.model import InputConfiguration
from lqtile.settings.input.loader import load_inputs
from lqtile.settings.model import Settings
from lqtile.settings.loader import load_settings
from lqtile.themes.model import Theme
from lqtile.settings.layout import load_theme


@fixture
def settings() -> Settings:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "settings.yaml"
    return load_settings(p)


@fixture
def default_theme() -> Theme:
    return load_theme()


@fixture
def theme() -> Theme:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "theme.yaml"
    return load_theme(p)


@fixture
def inputs() -> InputConfiguration:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "input.yaml"
    return load_inputs(p)
