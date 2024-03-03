#!/bin/bash
# takes a URL input, sends a request to that URL, and displays the size of the response body
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
