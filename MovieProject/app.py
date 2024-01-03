movies=[]


def add_movie():
    print('Add a new movie: ')
    title = input("Enter the title of the movie: ")
    director = input("Enter the name of the director: ")
    rating = float(input("Enter the rating: "))
    year = int(input("Enter the release year: "))
    movies.append({
        "title": title,
        "director": director,
        "rating": rating,
        "year": year
    })
    print("Movie added successfully!")


def list_movies():
    if (len(movies) == 0):
        print('No Movies!!')
        return
    print("MOVIES: ")
    for counter, movie in enumerate(movies,start=1):
        print(f"Movie number: {counter}")
        print(f"Movie Name: {movie['title']} ")
        print(f"Movie Director Name: {movie['director']} ")
        print(f"Movie Rating: {movie['rating']} ")
        print(f"Movie Year: {movie['year']} ")
        print()


def search_movie():
    if(len(movies)==0):
        print("No movies")
        return
    name = input("Enter the name of the movie: ")
    for movie in movies:
        if movie["title"].lower() == name.lower():
            print(movie)
            break
    else:
        print("Movie not found!")


#User-Prompt
user_input= input("Press a to add movie, l to list movies, s to search for a movie and q to exit: ")

inputs={
    "a": add_movie,
    "l": list_movies,
    "s":search_movie
}
while(user_input!="q"):
    # if(user_input=="a"):
    #     add_movie()
    # elif(user_input=="l"):
    #     list_movies()
    # elif(user_input=="s"):
    #     search_movie()
    # else:
    #     print("Wrong input")
    if user_input in inputs:
        selected_fuction= inputs[user_input]
        selected_fuction()
    else:
        print("Wrong input! ")

    user_input= input("Press a to add movie, l to list movies, s to search for a movie and q to exit: ")


