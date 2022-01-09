#!/bin/bash
# A bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sIL "$1" -X OPTIONS | grep Allow | cut -d " " -f2-
