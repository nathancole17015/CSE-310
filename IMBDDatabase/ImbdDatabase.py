import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Incorrect998!",
    database = "imbd_movies"
)

print()
print("List of actors")
myActor = mydb.cursor()

myActor.execute("SELECT * FROM actor")

myActorResult = myActor.fetchall()

for x in myActorResult:
    print(x)
myActor.close()    



print()
print("List of Movies")   

myMovies = mydb.cursor()

myMovies.execute("SELECT * FROM movie;")

myMovieResult = myMovies.fetchall()

for x in myMovieResult:
    print(x)

myMovies.close()

print()

myWriters = mydb.cursor()

myWriters.execute("SELECT * FROM writers;")

myWritersResult = myWriters.fetchall()

print("List of writers")
for x in myWritersResult:
    print(x)

myWriters.close()


myGenre = mydb.cursor()

myGenre.execute('''SELECT Genre_name, count(m.movie_id) as count from genre g 
                inner join genre_of_movie gm on g.Genre_id = 
                gm.Genre_id inner join movie m on m.Movie_id = gm.Movie_id group by g.genre_id order by count desc;''')

myGenreResult = myGenre.fetchall()
print()
print("Number of movies in each Genre")
for x in myGenreResult:
    print(x)

myGenre.close()

print()
print("Actors in Movies")

myActorInMovie = mydb.cursor()

myActorInMovie.execute('''SELECT Concat(First_name,' ',Last_name) as "Actor Name", title from actor a 
                inner join actors_in_movie am on a.Actor_id = am.Actor_id 
                inner join movie m on m.Movie_id = am.Movie_id 
                order by title, concat(First_name, ' ' , Last_name );''')

myActorInMovieResult = myActorInMovie.fetchall()



for x in myActorInMovieResult:
    print(x)

myGenre.close()




mydb.close()