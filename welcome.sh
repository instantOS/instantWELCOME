#!/bin/bash

########################################################
## Welcome app for instantOS, starts after first boot ##
########################################################

# wrapper to center it on the screen

echo "welcome to instantOS"
if [ -e welcome.py ]; then
    python3 welcome.py &
else
    python3 /usr/share/instantwelcome/welcome.py &
fi

while :; do
    sleep 0.2
    if WINDOWTITLE="$(xdotool getactivewindow getwindowname)"; then
        if grep -iq 'welcome' <<<"$WINDOWTITLE.."; then
            break
        fi
    fi
done

xdotool key super+alt+w
