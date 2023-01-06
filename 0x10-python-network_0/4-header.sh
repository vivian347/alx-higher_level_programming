#!/usr/bin/bash
#send GET request and displays bodyofresponse

curl -sX "GET" "$1" -H "X-School-User-Id:98"
