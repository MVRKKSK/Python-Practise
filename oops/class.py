
class Movie:
    def __init__(self , name , director , actor , music , storyline , trailer , poster):
        self.name = name
        self.director = director
        self.actor = actor 
        self.music = music 
        self.storyline = storyline
        self.trailer = trailer 
        self.poster = poster

    def show():
        print(f"Name : {self.name} Director: {self.director} Actor: {self.actor} Music : {self.music} StoryLine: {self.storyline} Trailer:{self.storyline} Poster: {self.poster} ")


name = input("enter your movie name : ")
director = input("enter your movie director : ")
actor = input("enter your movie actor : ")
music = input("enter your movie music : ")
storyline = input("enter your movie storyline : ")
trailer = input("enter your movie trailer : ")
poster = input("enter your movie poster : ")

movie1 = Movie(name , director , actor , music , storyline , trailer , poster)

movie1.show()



