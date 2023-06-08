# testing script
# author: Ondrej Mikula
# 2023



host=http://localhost:8080


echo list all movies. Currently empty.
curl -X GET $host/movies

echo ""
echo insert 2 movies.
curl -X POST $host/movies --json '{ "title": "The Matryx", "release_year" : 1999, "description" : "The Matrix is a computer-generated dream world..." }'
echo the description is not required
curl -X POST $host/movies --json '{ "title": "The Matrix Reloaded", "release_year" : 2003 }'

echo ""
echo update the 1st movie.
curl -X PUT $host/movies/1 --json '{ "title": "The Matrix" }'


echo ""
echo any number of parameters may be updated in one request.
curl -X PUT $host/movies/2 --json '{ "title": "The Matrix 2.0",  "description" : "Second Matrix film" }'


echo ""
echo list all movies.
curl -X GET $host/movies

echo ""
echo movie detail.
curl -X GET $host/movies/1



echo ""
echo get detail of nonexistent item.
curl -X GET $host/movies/1234

echo ""
echo try to update nonexistent item.
curl -X PUT $host/movies/4321 --json '{ "title": "The Matrix", "release_year" : 1999 }'

echo ""
echo insert another movie.
curl -X POST $host/movies --json '{ "title": "Dr. Strangelove", "release_year" : 1964 }'

echo ""
echo new movie without required parameters is not accepted.
curl -X POST $host/movies --json '{ "release_year" : 1964 }'
curl -X POST $host/movies --json '{ "title": "2001: A Space Odyssey" }'
curl -X POST $host/movies --json '{ }'
curl -X POST $host/movies --json '{ "description": "A film with no name" }'
echo additional parameters are ignored
curl -X POST $host/movies --json '{ "release_year" : 1965, "title": "Empire", "badparam": "badparam" }'

echo ""
echo update accepts only parameters \"title\", \"description\", \"release_year\", the rest is ignored.
curl -X PUT $host/movies/1 --json '{ "badparam": "The Matrix" }'
echo update with no parameters is invalid.
curl -X PUT $host/movies/1 --json '{ }'


echo ""
echo insert does check for data types.
curl -X POST $host/movies --json '{ "title": "Vertigo", "release_year" : "A.D. 2023" }'
echo data types are converted, if possible.
curl -X POST $host/movies --json '{ "title": 1984, "release_year" : "1948", "description": 1984 }'
echo update also does check for data types.
curl -X PUT $host/movies/7 --json '{ "release_year" : "1984" }'
curl -X PUT $host/movies/42 --json '{ "release_year" : "A.D. 2023" }'

echo ""
echo it is not possible to change the id - it is ignored.
curl -X PUT $host/movies/1 --json '{ "id": "789" }'

echo ""
echo try to update nonexistent item.
curl -X PUT $host/movies/4321 --json '{ "title": "The Matrix", "release_year" : 2000 }'

echo ""
echo list all movies.
curl -X GET $host/movies
