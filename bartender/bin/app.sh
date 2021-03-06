#!/bin/sh

SCRIPT_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
APP_ROOT="$(dirname "$SCRIPT_DIRECTORY")"

CONFIG_FILE="$APP_ROOT/dev_conf/config.json"

CMD="bartender -c $CONFIG_FILE"
python -m $CMD
