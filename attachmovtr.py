import webbrowser

class happy():
    def __init__(self,to_know,to_read,
                 to_see,to_watch):
        self.title=to_know
        self.storyline=to_read
        self.poster_image_url=to_see
        self.trailer_youtube_url=to_watch
    def show_movie_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
        
