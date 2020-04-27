#!/usr/bin/env python3
import webbrowser
import gi
gi.require_version('Gtk', '3.0')
import subprocess
import pathlib
from gi.repository import Gtk

# won't show icons otherwise
settings = Gtk.Settings.get_default()
settings.props.gtk_button_images = True

class Handler:
    def window_destroy_cb(self, *args):
        Gtk.main_quit()

    def githubbutton_clicked_cb(self, button):
        subprocess.run(['xdotool', 'key', 'super+2'])
        webbrowser.open_new_tab('https://github.com/instantos')

    def supportbutton_clicked_cb(self, button):
        subprocess.run(['xdotool', 'key', 'super+2'])
        webbrowser.open_new_tab('https://instantos.github.io/instantos.github.io/support')

    def youtubebutton_clicked_cb(self, button):
        subprocess.run(['xdotool', 'key', 'super+2'])
        webbrowser.open_new_tab(
            'https://www.youtube.com/playlist?list=PLczWCikHiuy_2fBZ_ttJuybBXVERrJDAu')

    def settingsbutton_clicked_cb(self, button):
        subprocess.run(['xdotool', 'key', 'super+3'])
        subprocess.Popen('instantsettings')
    def installbutton_clicked_cb(self, button):
        subprocess.run(['xdotool', 'key', 'super+3'])
        subprocess.Popen('pamac-manager')

    def starttoggle_toggled_cb(self, button):
        if button.get_active():
            subprocess.run(['iconf', 'welcome', '1'])
            print("startup active")
        else:
            subprocess.run(['iconf', 'welcome', '0'])
            print("startup inactive")
    def quitbutton_clicked_cb(self, button):
        Gtk.main_quit()

builder = Gtk.Builder()

if pathlib.Path('./welcome.glade').exists():
    builder.add_from_file("./welcome.glade")
else:
    builder.add_from_file("/usr/share/instantwelcome/welcome.glade")


builder.connect_signals(Handler())

window = builder.get_object('window')
window.show_all()

Gtk.main()
