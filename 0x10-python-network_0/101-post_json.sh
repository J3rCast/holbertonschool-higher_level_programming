#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.

file="<$2"
curl -sX POST "$1" -H 'Content-Type: application/json' -d "$file"
