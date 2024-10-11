# Fandom web scraping assignment:

For this assignment, we were required to scrape any fandom of our choosing!
For my project, I chose to scrape the DougDoug fandom page, located at https://dougdoug.fandom.com/wiki/The_Doughole. The wiki page I decided to scrape from here was https://dougdoug.fandom.com/wiki/Jokebot, since it's featured in one of DougDoug's newest second channel YouTube videos. (https://youtu.be/V_fcD2ewqk4?si=xrsGG4YmAPs8S30e)

If you don't know who DougDoug is, I recommend checking out his LinkedIn to learn more about him: https://www.linkedin.com/in/douglas-wreden-aa23827b/

The robots.txt file for the DougDoug fandom can be found here: https://dougdoug.fandom.com/robots.txt. The specific webpage we are scraping falls under the /wiki/Category: page, which is not disallowed.

With this project, I specifically wanted to see the average score of ratings that Jokebot gave jokes, and whether there was any correlation between joke length and Jokebot score. This is interesting for researchers because we can learn just how funny an AI believes DougDoug's chat is on average, and whether AI in general may be prone to giving higher ratings to jokes simply because of their length.

What you'll need to run the fandom_wiki_scraping.py file: 
* Python with pandas, beautifulsoup, requests, and csv installed
* Access to the internet to scrape the webpage
* A love of all things DougDoug related


If you are going to run the code and view the dataframe in a jupyter notebook, use the line of code:

pd.set_option('display.max_colwidth', None)

in order to see the full joke (if it gets cut off at the end as an ellipsis).

If you just want the dataframe in csv format, visit the Jokes.csv file in this folder.