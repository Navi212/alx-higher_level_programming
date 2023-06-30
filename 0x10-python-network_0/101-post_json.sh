#!/bin/bash
#A script that sends a JSON POST request to a URL passed as arg and displays the body response.
curl -s -X POST "$1" -H "Content-Type: application/json" -d "@$2"
