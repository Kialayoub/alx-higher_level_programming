#!/bin/bash
# This script takes a URL as input, sends a request to the URL, and displays the size of the response body.
curl -sX GET $1 -L
