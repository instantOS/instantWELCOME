#!/bin/bash

echo "welcome to instantOS"
if [ -e welcome.py ]; then
    python3 welcome.py &
else
    python3 /usr/share/instantwelcome/welcome.py
fi

while :; do
    sleep 0.2
    WINDOWTITLE=$(xdotool getactivewindow getwindowname)
    if grep -iq 'welcome' <<<"$WINDOWTITLE"; then
        break
    fi
done

xdotool getactivewindow getwindowname
xdotool key super+shift+space
sleep 0.2
xdotool key super+alt+w
