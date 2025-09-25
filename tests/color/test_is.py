from lqtile.color.match import is_rgbhex, is_base16


def test_is_rgbhex_with_hash():
    assert is_rgbhex("#000000")


def test_is_rgbhex_without_hash():
    assert is_rgbhex("000000")


def test_is_not_rgbhex():
    assert not is_rgbhex("#g00000")


def test_is_base16():
    assert is_base16("base0F")


def test_is_not_base16():
    assert not is_base16("base0f")


def test_is_short_rgbhex():
    assert is_rgbhex("#aaa")


def test_is_not_short_rgbhex():
    assert not is_rgbhex("#gaa")
