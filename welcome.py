#!/usr/bin/env python3
import webbrowser
import gi
gi.require_version('Gtk', '3.0')
import subprocess
import pathlib
from gi.repository import Gtk


class Handler:
    def window_destroy_cb(self, *args):
        Gtk.main_quit()

    def on_githubbutton_clicked(self, button):
        subprocess.run(['xdotool', 'key', 'super+2'])
        webbrowser.open_new_tab('https://github.com/instantos')

    def on_youtubebutton_clicked(self, button):
        subprocess.run(['xdotool', 'key', 'super+2'])
        webbrowser.open_new_tab(
            'https://www.youtube.com/playlist?list=PLczWCikHiuy_2fBZ_ttJuybBXVERrJDAu')

    def starttoggle_toggled_cb(self, button):
        if button.get_active():
            subprocess.run(['iconf', 'welcome', '1'])
            print("startup active")
        else:
            subprocess.run(['iconf', 'welcome', '0'])
            print("startup inactive")
    def quit_clicked_cb(self, button):
        Gtk.main_quit()

builder = Gtk.Builder()

if pathlib.Path('./welcome.glade'):
    builder.add_from_file("./welcome.glade")
else:
    builder.add_from_file("/usr/share/instantwelcome/welcome.glade")


builder.connect_signals(Handler())

window = builder.get_object('window')
window.show_all()

Gtk.main()
