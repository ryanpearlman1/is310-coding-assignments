favorite_movies = [
    {
        "name": "Cold Pursuit",
        "release_year": 2019,
        "sequels": ["The Exchange: After The Firm"]
    },
    {
        "name": "Die Hard",
        "release_year": 1988,
        "sequels": ["Die Hard 2", "Die Hard with a Vengeance", "Live Free or Die Hard", "A Good Day to Die Hard"]
    }
]  

#Homework part 1
def release(movie):
    if (movie["release_year"] < 2000):
        print("This movie was released before 2000.")
    elif (movie["release_year"] > 2000):
        print("This movie was released after 2000.")
        return movie["name"]
    
#Homework part 2
recent_movies = []

#Homework part 3
for movie in favorite_movies:
    if ((release(movie)) is not None):
        recent_movies.append(movie["name"])

#Homework part 4
print(recent_movies)