import webbrowser

class Movie():
	'''Class Movie is defined which produces instances of movie
	 by taking movie_title, poster_image, trailer_youtube as inputs'''
	def __init__(self, movie_title, poster_image, trailer_youtube):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#Method to open movie url in a web browser
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)