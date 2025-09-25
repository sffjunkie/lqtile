import string


def is_rgbhex(value: str) -> bool:
    if value[0] == "#":
        value = value[1:]
    return (len(value) == 6 or len(value) == 3) and all(
        [ch in string.hexdigits for ch in value]
    )


def is_base16(value: str) -> bool:
    return (
        len(value) == 6
        and value[:4] == "base"
        and value[4] in string.hexdigits.upper()
        and value[5] in string.hexdigits.upper()
    )
