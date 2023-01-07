#!/bin/bash
#sends a POST request anddisplays bodyof response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
