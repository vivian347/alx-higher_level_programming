#!/usr/bin/node
const request = require('request');
let url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2]
request.get(url, (err, response, body) => {
	console.log(err || JSON.parse(body).title);
});
