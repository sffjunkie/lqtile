from pathlib import Path

from lqtile.settings.model import Settings
from lqtile.settings.loader import load_settings


def test_setting_loader_load_nonexistent():
    p = Path("/tmp/settings.notthere")
    settings = load_settings(p)
    assert settings.device.net == "eth0"


def test_setting_loader_load(settings: Settings):
    assert settings.device.net == "wlp3s0"
