#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.

curl -sX PUT 0.0.0.0:5000/catch_me -L -F 'user_id=98' -H "Origin: HolbertonSchool"
