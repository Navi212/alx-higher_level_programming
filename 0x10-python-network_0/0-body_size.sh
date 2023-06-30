#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL
#and displays the size (bytes) of the body of the response

curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
