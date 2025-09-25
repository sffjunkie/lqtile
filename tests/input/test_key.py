from libqtile.config import Key  # type: ignore

from lqtile.settings.model import Settings
from lqtile.builder.keys import build_keys


def test_key_all(settings: Settings):
    keys = build_keys(settings)
    assert len(keys) > 0
    assert isinstance(keys[0], Key)
    assert keys[0].key == "F12"
