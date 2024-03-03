#!/bin/bash
# Takes a URL as an argument, sends a GET request to the URL with a specific header, and displays the body of the response
curl -sX GET $1 -H "X-School-User-Id: 98" -L

