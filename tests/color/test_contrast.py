from lqtile.color.contrast import contrast_color


def test_contrast_color_without_hash():
    assert contrast_color("000000") == "#FFFFFF"


def test_contrast_color_with_hash():
    assert contrast_color("#FFFFFF") == "#000000"
