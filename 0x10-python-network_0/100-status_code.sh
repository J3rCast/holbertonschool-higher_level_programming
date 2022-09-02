#!/bin/bash
# sends a request to a URL passed as an argument,
curl -sI 0.0.0.0:5000 | grep HTTP | cut -d " " -f 2
