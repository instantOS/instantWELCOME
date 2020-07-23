#!/bin/bash

# welcome app for instantOS

welcomemenu() {
    echo '>>b Welcome to instantOS
:r Get started
:b Settings
:y Install
:b GitHub
:b Support
:g Enable welcome app on startup
:r Close' | instantmenu -l 20 -c -h -1 -wm -w -1 -q 'welcome app'

}

openbrowser() {
    openapp "firefox --new-window $1"
}

openapp() {
    pgrep instantsettings && pkill instantsettings
    instantwelcome &
    sleep 0.7
    xdotool key super+2
    sleep 0.4
    $1
    exit
}

while :; do
    CHOICE="$(welcomemenu)"

    if [ -z "$CHOICE" ]; then
        exit
    fi

    case "$CHOICE" in
    *Settings)
        instantsettings &
        ;;
    *started)
        openbrowser 'https://www.youtube.com/playlist?list=PLczWCikHiuy_2fBZ_ttJuybBXVERrJDAu'
        ;;
    *GitHub)
        openbrowser "https://github.com/instantOS"
        ;;
    *Support)
        openbrowser "https://instantos.github.io/instantos.github.io/support"
        ;;
    *Install)
        if [ -e /usr/share/liveutils ]; then
            instantosinstaller &
            exit
        else
            openapp pamac-manager
        fi
        ;;
    *startup)
        if echo 'enable welcome app on bootup?
(can be relaunched later with instantwelcome)' | imenu -C; then
            iconf welcome 1
        else
            iconf welcome 0
        fi
        ;;
    *Close)
        exit
        ;;
    esac
done
