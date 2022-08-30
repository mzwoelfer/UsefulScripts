#!/bin/bash
short_cut_list="['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/pause-song/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/next-song/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/previous-song/' ]"

gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "$short_cut_list"
