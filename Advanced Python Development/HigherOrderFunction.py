movies =[
    {"name":"The matrix", "director":"SSS"},
    {"name":"Vaishali","director":"eee"}
]

def fine_movie(expected, finder):
    for movie in movies:
        if finder(movie)== expected:
            return movie

find_by=input('What property are we searching by: ')
looking_for=input('Name: ')
movie= fine_movie(looking_for, lambda movie: movie[find_by])
print(movie)