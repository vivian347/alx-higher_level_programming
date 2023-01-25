#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
	if (!err) {
		const actors = JSON.parse(body).results;
		console.log(actors.reduce((count, movie) => {
			return movie.characters.find((character) => character.endsWith('/18/'))
			? count + 1
			: count;
		}, 0));
	}
});
