#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of AwesomeWM
# TODO: run_once


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

run picom --experimental-backend &  
run nitrogen --restore & 
run copyq &
run flameshot &
/usr/lib/kdeconnectd &
/usr/bin/kdeconnect-indicator &
run redshift-gtk -l 20:70 -t 2000:-8000



#run megasync
#run xfce4-clipman
#run gammy
