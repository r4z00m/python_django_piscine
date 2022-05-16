#!/bin/sh

curl -Is $1 | grep -i Location: | cut -d " " -f 2