#!/usr/bin/node

/**
 * 0. Star Wars Characters
 *
 * Prints all characters of a Star Wars movie.
 *
 */

const movieId = process.argv[2];
if (process.argv.length !== 3 || !Number(movieId)) {
  process.exit(1);
}

const request = require('request');
const filmUri = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(filmUri, (error, response, body) => {
  if (error) {
    console.log('Error: ', error);
  } else {
    const data = JSON.parse(body);
    for (const characterUri of data.characters) {
      request.get(characterUri, (error, response, body) => {
        if (error) {
          console.log('Error: ', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
