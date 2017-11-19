# Movies Database

Aim is to create backend functions for REST application. Application is a service for movies database. It is build around 2 types of objects
* movie object - representing a movie
* person - representing people involved in movie creation/production
Objects are serialized to JSON always

Requirmentes:
* Django 1.11
* Django-REST-Framework

Technologies used:
* Python 3.6
* Django

## API documentation

Movies API

|Verb    | Url                    | Action                                   |
|--------|------------------------|------------------------------------------|
|GET     | /api-movies/movies     | Get list of all movie objects            |
|POST    | /api-movies/movies     | Add a movie object to db                 |
|--------|------------------------|------------------------------------------|
|GET     | /api-movies/movie/{id} | Get details of a movie with {id}         |
|DELETE  | /api-movies/movie/{id} | Delete movie with {id}                   |
|PATCH   | /api-movies/movie/{id} | Update provided fields of movie with {id}|


Persons API

|Verb    | Url                      | Action                                    |
|--------|--------------------------|-------------------------------------------|
|GET     | /api-persons/persons     | Get list of all person objects            |
|POST    | /api-persons/persons     | Add a person  object to db                |
|--------|--------------------------|-------------------------------------------|
|GET     | /api-persons/person/{id} | Get details of a person with {id}         |
|DELETE  | /api-persons/person/{id} | Delete person object with {id}            |
|PATCH   | /api-persons/person/{id} | Update provided fields of person with {id}|


## Samples

### Movies API

JSON Representation of movie object in list GET: /api-movies/movies
```
    {
        "title": "Inception",
        "year": 2010,
        "director": [
            "Christopher Nolan"
        ],
        "details_url": "/api-movies/movie/1/"
    }
```

JSON representation of movie object details in GET: /api-movies/movie/{id}
```
{
    "title": "Inception",
    "year": 2010,
    "director": [
        "Christopher Nolan"
    ],
    "description": "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
    "cast_movie": [
        {
            "person": {
                "fullname": "Leonardo DiCaprio ",
                "details_url": "/api-persons/person/7/"
            },
            "character": "Cobb"
        },
        {
            "person": {
                "fullname": "Tom Hardy",
                "details_url": "/api-persons/person/5/"
            },
            "character": "Eames"
        }
    ],
    "genre": [
        {
            "name": "action",
            "movies_list_url": "/api-movies/movies/genre/1/"
        },
        {
            "name": "si-fi",
            "movies_list_url": "/api-movies/movies/genre/2/"
        },
        {
            "name": "adventure",
            "movies_list_url": "/api-movies/movies/genre/3/"
        }
    ],
    "crew_movie": [
        {
            "person": {
                "fullname": "Christopher Nolan",
                "details_url": "/api-persons/person/3/"
            },
            "credit": "director"
        }
    ]
}
```

### Person API


JSON representation
```

{
    "count": 19,
    "next": "http://localhost:8000/api-persons/persons/?page=2",
    "previous": null,
    "results": [
        {
            "fullname": "Christian Bale",
            "details_url": "/api-persons/person/2/"
        },
        {
            "fullname": "Nicolas Cage",
            "details_url": "/api-persons/person/17/"
        },
        {
            "fullname": "Russell Crowe",
            "details_url": "/api-persons/person/18/"
        },
        {
            "fullname": "Leonardo DiCaprio ",
            "details_url": "/api-persons/person/7/"
        },
        {
            "fullname": "David Fincher",
            "details_url": "/api-persons/person/9/"
        },
    ]
}
```

JSON representation of person object in GET
```
{
    "first_name": "Leonardo",
    "second_name": "DiCaprio ",
    "year_of_birth": 1974
}
```