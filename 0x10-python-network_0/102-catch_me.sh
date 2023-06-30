#!/bin/bash
#A Bash script that makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!"
curl -sL -X PUT -d "You%20got%20me!" 0.0.0.0:5000/catch_me
