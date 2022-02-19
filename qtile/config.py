
####### IMPORTS #########
import os
import subprocess


# from typing import List  # noqa: F401

from libqtile import hook, layout
from libqtile.config import Group, Match

# Local Files
from keys.keybindings import Mouse,Keybindings

from widgets import MyWidgets
from layouts import Layouts
from groups import CreateGroups
from icons import group_icons

 
###### MAIN ######
if __name__ in ["config", "__main__"]:
    # Initializes objects

    # Initializes keybindings
    obj_keys          = Keybindings()

    # Mouse
    obj_mouse         = Mouse()
    obj_widgets       = MyWidgets()
    obj_layouts       = Layouts()
    obj_groups        = CreateGroups()
    
    # Initializes qtile variables
    keys              = obj_keys.init_keys()
    mouse             = obj_mouse.init_mouse()
    layouts           = obj_layouts.init_layouts()
    groups            = obj_groups.init_groups()

    # Append group keys for groups
    keys              += obj_keys.init_keys_groups(group_icons)

    ### DISPLAYS WIDGETS IN THE SCREEN ####

    screens           = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list()
    widgets_screen1   = obj_widgets.init_widgets_screen()


colors = {
    "nord_dark_blue_0": "#2E3440",
    "nord_dark_blue_1": "#3B4252",
    "nord_dark_blue_2": "#434C5E",
    "nord_dark_blue_3": "#4C566A",
    "nord_white_0": "#D8DEE9",
    "nord_white_1": "#E5E9F0",
    "nord_white_2": "#ECEFF4",
    "nord_light_blue_0": "#5E81AC",
    "nord_light_blue_1": "#81A1C1",
    "nord_light_blue_2": "#88C0D0",
    "nord_light_blue_3": "#8FBCBB",
    "nord_red": "#BF616A",
    "nord_orange": "#D08770",
    "nord_yellow": "#EBCB8B",
    "nord_green": "#A3BE8C",
    "nord_purple": "#B48EAD",
}

dgroups_key_binder = None

dgroups_app_rules = []  # type: list

follow_mouse_focus = False

bring_front_click = True

cursor_warp = False

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Mono",
    fontsize=14,
    padding=3,
)

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='dialog'),  # Dialogs stuff
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='Android Emulator - Pixel_3a_XL_API_30:5554')
    
])
auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
respect_minimize_requests = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True
