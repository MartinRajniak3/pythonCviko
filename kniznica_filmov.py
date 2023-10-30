class Movie:
    def __init__(self, title, year, genre, duration, director):
        self._title = title
        self._year = year
        self._genre = genre
        self._duration = duration
        self._director = director

    def print(self):
        print("| {:20} | {:4} | {:6} | {:3}m | {:10} |".format(
            self._title,
            self._year,
            self._genre,
            self._duration,
            self._director
        ))

class Library:
    def __init__(self):
        self._movie_library = list()

    def seed(self):
        movie = Movie("Matrix", 1999, "scifi", 136, "Wachowski")
        self._movie_library.append(movie)
        movie = Movie("Jurrasic Park", 1993, "action", 127, "Spielberg")
        self._movie_library.append(movie)
        movie = Movie("Stargate", 1994, "scifi", 128, "Oneil")
        self._movie_library.append(movie)

    def print(self):
        print("| {:20} | {:4} | {:6} | {:3} | {:10} |".format(
            "Title",
            "Year",
            "Genre",
            "Duration",
            "Director"
        ))
        for i in self._movie_library:
            i.print()

    def addMovie(self):
        title = input("Insert movie title")

        while True:
            try:
                year = int(input("Enter the release year: "))
            except ValueError:
                print("please enter a valid year in range 1900-2023")
                continue
            if year >= 1900 and year <= 2023:
                print("the entered year has been accepted".format(year))
                break
            else:
                print("The release year of the movie must be in range 1900-2023")

        while True:
            try:
                genre = str(input("Enter the genre of the movie: "))
            except ValueError:
                print("Please enter a valid genre of the movie containing 2-20 characters")
                continue
            if genre.isnumeric() == False and len(genre) >= 2 and len(genre) <= 20:
                print("The entered genre of the movie has been accepted".format(genre))
                break
            else:
                print("The genre of the movie must contains 2-20 characters")

        while True:
            try:
                duration = int(input("Enter the duration of the movie in mninutes: "))
            except ValueError:
                print("Please enter a valid duration of the movie in minutes in range 10-600")
                continue
            if duration >= 10 and duration <= 600:
                print("The entered duration of the movie has been accepted".format(duration))
                break
            else:
                print("The duration of the movie is must be in range 10-600")

        while True:
            try:
                director = str(input("Enter the director's surname: "))
            except ValueError:
                print("Please enter a valid director's surname containing 2-20 characters")
                continue
            if director.isnumeric() == False and len(director) >= 2 and len(director) <= 20:
                print("The entered duration of the director's surname has been accepted".format(director))
                break
            else:
                print("The duration of the director's surname must be in range 2-20 characters")

        self._movie_library.append(Movie(title, year, genre, duration, director))

    def findMovie(self, title):
        for i in self._movie_library:
            if i._title == title:
                return i
            return None

    def deleteMovie(self):
        self.print()
        print()
        title = input("Enter the title of movie that you want to remove: ")
        movie = self.findMovie(title)
        if movie == None:
            print("Movie with title {} wasn't find".format(title))
            return

        self._movie_library.remove(movie)

    def menu(self):
        print("0 - add movie")
        print("1 - remove movie")
        print("2 - print library")
        print("3 - save library")
        print("q - exit")
        print()
        choice = input("Select an option (0-3, q): ")
        if choice == "0":
            self.addMovie()
        elif choice == "1":
            self.deleteMovie()
        elif choice == "2":
            self.print()
        elif choice == "3":
            self.saveMovieLibrary()
        else:
            exit()

    def banner(self):
        print("Movie Library, version 0.1a1")
        print()

    def saveMovieLibrary(self):
        subor = open('movie_library.txt', 'w')
        subor.write("| {:20} | {:4} | {:6} | {:3} | {:10} |".format(
            "Title",
            "Year",
            "Genre",
            "Duration",
            "Director"
        ))

        for i in self._movie_library:
            subor.write("\n| {:20} | {:4} | {:6} | {:3}m | {:10} |".format(
            i._title,
            str(i._year),
            i._genre,
            str(i._duration),
            i._director))

        subor.close()

if __name__ == "__main__":
    library = Library()
    library.seed()
    library.banner()
    while True:
      library.menu()