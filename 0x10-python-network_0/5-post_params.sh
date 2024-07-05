#!/bin/bash
# This script sends a POST request to the URL passed as an argument with specific parameters and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
