from libqtile import layout  # type: ignore
from libqtile.config import Screen  # type: ignore

from lqtile import bars
from lqtile import floating
from lqtile import scratchpad
from lqtile.wallpaper.manager import WallpaperManager
from lqtile.debug import show_runtime_info
from lqtile.builder.group import build_groups
from lqtile.builder.keys import build_keys
from lqtile.builder.buttons import build_buttons
from lqtile.secret.loader import load_secrets
from lqtile.settings.loader import load_settings

show_runtime_info()

secrets = load_secrets()
settings = load_settings()

wallpaper_manager = WallpaperManager()

bar_defs = bars.build_bars(settings=settings, theme=theme)
screens = [
    Screen(
        top=bar_defs["top"],
        bottom=bar_defs["bottom"],
        left=bar_defs["left"],
        right=bar_defs["right"],
        wallpaper=str(wallpaper_manager.wallpaper()),
        wallpaper_mode="fill",
    ),
]

groups = build_groups(settings) + scratchpad.build_scratchpads(settings)

keys = build_keys(settings) + scratchpad.build_keys(settings)
mouse = build_buttons(settings)

floating_layout = floating.build_layout(theme=settings.floating_layout)

if theme.window_tiled is not None:
    layout_params = dict(theme.window_tiled)
else:
    layout_params = {}

layouts = [
    layout.MonadTall(**layout_params),
    layout.Max(**layout_params),
]

auto_fullscreen = True
bring_front_click = "floating_only"
cursor_warp = False
extension_defaults = theme.extension
focus_on_window_activation = "smart"
follow_mouse_focus = False
widget_defaults = theme.widget
wmname = "QTile"


# to get ids use `qtile cmd-obj -o core -f get_inputs`
wl_input_rules = load_inputs()

wl_xcursor_size = 32
