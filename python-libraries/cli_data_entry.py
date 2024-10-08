from rich.console import Console
from rich.table import Table
import os

console = Console(record=True)

favorite_movies = [
    {
        "name": "Cold Pursuit",
        "release_year": 2019,
        "sequels": ["none"]
    },
    {
        "name": "Die Hard",
        "release_year": 1988,
        "sequels": ["Die Hard 2", "Die Hard with a Vengeance", "Live Free or Die Hard", "A Good Day to Die Hard"]
    }
]  

console.print("\n[bold cyan]Hello! Here are my favorite movies![/bold cyan]")
for movie in favorite_movies:
    for field, value in movie.items():
        console.print(f"[magenta]{field}[/magenta]: {value}")

console.print(f"\nWhat are [i]your[/i] [bold red]favorite movies[/]? Enter the name, release year, and sequels, then do it again for each movie! Or, type [bold green]f[/] when finished.")
def in_loop_func(favorite_movies):
    in_loop = True
    first_time = True
    while (in_loop == True):
        # Get the first input
        if (first_time == True):
            console.print("What is the [bold blue]name[/] of your first favorite movie?")
            first_time = False
        else:
            console.print("What is the [bold blue]name[/] of your next favorite movie? Or, type f if completed.")
    
        name = console.input("[bold blue]Name[/] of favorite movie: ")
        if name.lower() == 'f':
            return
        release_year = console.input("Enter [bold yellow]release year[/]: ")
        sequels = console.input("Enter the movie's [bold purple]sequels[/]! (comma separated). (If there isn't one, type [b]none[/b]) ").split(", ")
    
        # Create a new movie dictionary
        new_movie = {
            "name": name,
            "release_year": release_year,
            "sequels": sequels
        }

        favorite_movies.append(new_movie)

in_loop_func(favorite_movies)

def print_our_movies():
    console.print("\n[bold cyan]Hello! Here are [i]our[/i] favorite movies![/bold cyan]")
    for movie in favorite_movies:
        console.print("\n")
        for field, value in movie.items():
            console.print(f"[magenta]{field}[/magenta]: {value}")

def is_correct_func():
    restart = False
    in_loop_2 = True
    while (in_loop_2 == True):
        print_our_movies()
        is_correct = console.input(f"\nIs all of that correct? Type [bold purple]y[/] if yes, or [bold purple]n[/] if you would like to restart the data input process: ")
        if (is_correct.lower() == "y"):
            console.print("Awesome! Saving file to your computer...")
            console.save_html("Fav_Movies_html.html")
            path = os.path.abspath("Fav_Movies_html.html")
            console.print(f'File saved to: {path}')
            restart = True
            break
            
        else: 
            global favorite_movies
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

            console.print("Let's try again. Your previous entries have been cleared.")
            in_loop_2 = False
            in_loop_func(favorite_movies)  
            is_correct_func()
            if (restart):
                break  

is_correct_func()