import movies
import fresh_tomatoes

#Initializing objects of class Movie
dunkirk = movies.Movie("Dunkirk",  
	"https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg", 
	"https://www.youtube.com/watch?v=_cmgiys2n1o")

inception = movies.Movie("Inception",  
	"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", 
	"https://www.youtube.com/watch?v=YoHD9XEInc0")

dark_knight = movies.Movie("Dark Knight",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY")

titanic = movies.Movie("Titanic",
	"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
	"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

man_of_steel = movies.Movie("Man of Steel",
	"https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
	"https://www.youtube.com/watch?v=T6DJcgm3wNY")

deadpool = movies.Movie("Deadpool",
	"https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
	"https://www.youtube.com/watch?v=I4tFNfROlqk")

movies = [dunkirk, inception, dark_knight, titanic, man_of_steel, deadpool]

fresh_tomatoes.open_movies_page(movies)