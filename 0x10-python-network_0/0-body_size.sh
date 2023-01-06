# takes in URL, sends arequest to that URL, and displays size of the body of the response inbytes

curl -sI "$1" |  grep Content-Length | cut -d ":" -f 2 | cut -d " " -f 2
