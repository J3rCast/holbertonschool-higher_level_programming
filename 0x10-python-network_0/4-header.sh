#!/bin/bash
# takes in a URL as an argument, sends a GET
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
