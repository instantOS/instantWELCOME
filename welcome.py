#!/usr/bin/env python3
import webbrowser
import gi
import os
import pathlib
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def window_destroy_cb(self, *args):
        Gtk.main_quit()

    def on_githubbutton_clicked(self, button):
        webbrowser.open_new_tab('https://github.com/instantos')

    def on_youtubebutton_clicked(self, button):
        webbrowser.open_new_tab('https://www.youtube.com/playlist?list=PLczWCikHiuy_2fBZ_ttJuybBXVERrJDAu')

    def starttoggle_toggled_cb(self, button):
        if button.get_active():
            if not os.path.exists(os.environ['HOME'] + '/.cache/instantautostart'):
                pathlib.Path(os.environ['HOME'] + '/.cache/instantautostart').touch
            print("startup active")
        else:
            if os.path.exists(os.environ['HOME'] + '/.cache/instantautostart'):
                os.remove(os.environ['HOME'] + '/.cache/instantautostart')
            print("startup inactive")

builder = Gtk.Builder()
builder.add_from_file("welcome.glade")
builder.connect_signals(Handler())

window = builder.get_object('window')
window.show_all()

Gtk.main()