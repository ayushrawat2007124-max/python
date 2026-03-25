'''5.	Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
a)	print all movie details
b)	display name of movies released before 2015
c)	print movies that made a profit.
d)	print movies directed by a particular director.
'''
n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    print(f"\nEnter details for movie {i+1}")
    
    name = input("Movie name: ")
    year = int(input("Release year: "))
    director = input("Director name: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection made: "))
    
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }
print("\nAll Movie Details:")
for name, details in movies.items():
    print(f"\nMovie: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)
print("\nMovies that made profit:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)
search_director = input("\nEnter director name to search: ")

print(f"\nMovies directed by {search_director}:")
for name, details in movies.items():
    if details["director"].lower() == search_director.lower():
        print(name)