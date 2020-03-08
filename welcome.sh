#!/bin/bash

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

xdotool key super+shift+space
sleep 0.2
xdotool key super+alt+w
