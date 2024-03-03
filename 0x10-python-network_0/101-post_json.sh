#!/bin/bash
# Sends a JSON POST request to the URL passed as the first argument and displays the response body
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
