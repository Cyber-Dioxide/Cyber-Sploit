#!/bin/bash

process=$UID

# shellcheck disable=SC2154
if [ $process != 0 ]
then
    echo "[!] Run this tool as root"
fi