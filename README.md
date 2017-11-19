# Movies Database

Aim is to create backend functions for REST application. Application is a service for movies database.

Project uses:
* Django 1.11
* Django-REST-Framework

## API documentation
|Verb    | Url                    | Action                                   |
|--------|------------------------|------------------------------------------|
|GET     | /api-movies/movies     | Get list of all movies                   |
|POST    | /api-movies/movies     | Add a movie                              |
|GET     | /api-movies/movie/{id} | Get details of a movie with {id}         |
|DELETE  | /api-movies/movie/{id} | Delete movie with {id}                   |
|PATCH   | /api-movies/movie/{id} | Update provided fields of movie with {id}|
|--------|------------------------|------------------------------------------|
