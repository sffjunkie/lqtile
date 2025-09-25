from lqtile.color.convert import rgbhex_to_rgbcolor, rgbcolor_to_rgbhex


def test_is_valid_rgbhex_with_hash():
    assert rgbhex_to_rgbcolor("#808080") == (0.5, 0.5, 0.5)


def test_is_valid_rgbhex_without_hash():
    assert rgbhex_to_rgbcolor("c0c0c0") == (0.75, 0.75, 0.75)


def test_rgbcolor_to_hex():
    assert rgbcolor_to_rgbhex((0.25, 0.25, 0.25)) == "#404040"
