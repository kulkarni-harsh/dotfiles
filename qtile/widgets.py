import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen
from libqtile import qtile
from functions import PWA
import subprocess



class MyWidgets:
    def __init__(self):
        self.colors = [["#292d3e", "#292d3e"],  # panel background
                       # background for current screen tab
                       ["#434758", "#434758"],
                       ["#ffffff", "#ffffff"],  # font color for group names
                       # border line color for current tab
                       ["#bc13fe", "#bc13fe"],  # Group down color
                       # border line color for other tab and odd widgets
                       ["#8d62a9", "#8d62a9"],
                       ["#668bd7", "#668bd7"],  # color for the even widgets
                       ["#e1acff", "#e1acff"],  # window name

                       ["#000000", "#000000"],
                       ["#AD343E", "#AD343E"],
                       ["#f76e5c", "#f76e5c"],
                       ["#F39C12", "#F39C12"],
                       ["#F7DC6F", "#F7DC6F"],
                       ["#f1ffff", "#f1ffff"],
                       ["#4c566a", "#4c566a"], ]

        self.termite = "gnome-terminal"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        def open_htop():  # spawn gnome system monitor
            return qtile.cmd_spawn(['gnome-system-monitor'])

        def open_pavucontrol():  # spawn gnome system monitor
            return qtile.cmd_spawn(["pavucontrol"])
        
        def toggle_dnd():  # toggles dunst notification
            subprocess.call(["dunstctl", "set-paused", "toggle"])
            qtile.widgets_map["genpolltext"].cmd_eval("self.update(self.poll())")
            
        def get_dnd_status(): # returns current dunst status
            return '🔴'if subprocess.getoutput("dunstctl is-paused")=='true' else '🟢'
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
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.Image(
                filename="~/.config/qtile/icons/ubuntulogo.png",
                background=self.colors[0],
                

            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font="Ubuntu Bold",
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[-2],
                inactive=self.colors[-1],
                # rounded=True,
                rounded=False,
                # highlight_color=self.colors[9],
                # highlight_method="line",
                highlight_method='block',
                urgent_alert_method='block',
                # urgent_border=self.colors[9],
                this_current_screen_border=colors["nord_purple"],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0],
                disable_drag=True
            ),
    
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.WindowName(
                foreground=self.colors[6],
                background=self.colors[0],
                padding=0
            ),

            widget.Systray(
                background=self.colors[0],
                padding=5
            ),
           
            widget.Battery(
                charge_char="▲",
                discharge_char="▼",
                full_char="🔋",
                unknown_char="🔋",
                empty_char="⚠️",
                notify_below=0.2,
                low_percentage=0.2,
                format="🔋s{char} {percent:2.0%} ",
                update_interval=30,
                fontsize=18,
                background=self.colors[0],
                foreground=colors["nord_white_2"],
            ),
            widget.TextBox(
                text="",
                foreground=colors["nord_white_2"],
                background=self.colors[0],
                padding=0,
                fontsize=18
            ),
            widget.Memory(
                background=colors["nord_white_2"],
                foreground=colors["nord_dark_blue_3"],
                mouse_callbacks={'Button1': open_htop},
                padding=5,
                fontsize=18
            ),
            widget.TextBox(
                text="",
                background=colors["nord_white_2"],
                foreground=colors["nord_dark_blue_2"],
                padding=0,
                fontsize=37
            ),

            widget.TextBox(
                text="📢 ",
                foreground=self.colors[7],
                background=colors["nord_dark_blue_3"],
                padding=0,
                mouse_callbacks={"Button1": open_pavucontrol}
            ),
            widget.Volume(
                foreground=colors["nord_white_0"],
                background=colors["nord_dark_blue_3"],
                update_interval=0.3,
                fontsize=18,
            ),

            widget.TextBox(
                text="",
                background=colors["nord_dark_blue_3"],
                foreground=colors["nord_light_blue_0"],
                padding=0,
                fontsize=18
            ),

            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                foreground=colors["nord_green"],
                background=colors["nord_light_blue_0"],
                padding=0,
                scale=0.7
            ),
            
            widget.CurrentLayout(
                foreground=colors["nord_white_1"],
                background=colors["nord_light_blue_0"],
                padding=5,
                fontsize=18
            ),
            widget.TextBox(
                text="",
                foreground=colors["nord_white_2"],
                background=colors["nord_light_blue_0"],
                padding=0,
                fontsize=18
            ),
            widget.Clock(
                background=colors["nord_white_2"],
                foreground=colors["nord_dark_blue_3"],
                fontsize=18,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn(PWA.calendar())},
                format="%d-%m-%Y %a %I:%M %p"
            ),
            widget.TextBox(
                text="",
                foreground=self.colors[0],
                background=colors["nord_white_2"],
                padding=0,
                fontsize=18
            ),
            
            widget.GenPollText(
            	func=get_dnd_status,
            	padding=0,
                fontsize=16,
            	mouse_callbacks={'Button1': toggle_dnd},
            
            )
        ]
        return widgets_list

    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()
        return widgets_screen

    def init_widgets_screen2(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen2 = self.init_widgets_screen()
        return widgets_screen2

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=20)),
                Screen(top=bar.Bar(
                    widgets=self.init_widgets_screen2(), opacity=1.0, size=20))
                ]
