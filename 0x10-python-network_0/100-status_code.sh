#!/bin/bash
# sends a request to a URL passed as an argument,
# and displays only the status code of the response.

curl -sI 0.0.0.0:5000 | grep HTTP | cut -d " " -f 2
