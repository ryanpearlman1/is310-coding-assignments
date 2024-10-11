from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

response = requests.get("https://dougdoug.fandom.com/wiki/Jokebot")
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", class_="fandom-table")

jokes = []
ratings = []

for row in table.find_all('tr')[13:]: #Skipping unrated jokes
    cells = row.find_all('td')

    joke = cells[0].get_text(strip=True)
    score = cells[1].get_text(strip=True)

    first_half = score.split("/")[0]

    rating_string = "" #Taking only the number and not the word associated with the rating
    for part in first_half:
        if (part.isdigit()):
            rating_string += part 

    ratings.append(int(rating_string))
    jokes.append(joke)

#Creating, sorting, and printing a dataframe with our jokes and ratings
df = pd.DataFrame({"Joke": jokes, "Score out of ten": ratings})
df = df.sort_values(by="Score out of ten", ascending=False).reset_index(drop=True)
print(df)

#Totaling scores
total_score = df["Score out of ten"].sum()
average_score = total_score / len(df)
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")

#Finding potential correlation to learn how AI rates jokes
df["Joke_Length"] = df["Joke"].apply(len)
correlation = df["Joke_Length"].corr(df["Score out of ten"])
print("Joke length is correlated with Jokebot's rating at a score of:", correlation)

#Saving dataframe to a file
with open('Jokes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Joke', 'Score out of ten'])
    for index, row in df.iterrows():
        writer.writerow([row['Joke'], row['Score out of ten']])