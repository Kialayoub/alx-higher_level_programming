#!/bin/bash
# Takes a URL input, sends a POST request to the URL, and displays the response body
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L

