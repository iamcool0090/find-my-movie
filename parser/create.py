import json
import time
import requests
from mistralai.client import MistralClient
import uuid

# Replace this with your actual Mistral API key
MISTRAL_API_KEY = "ADD-YOUR-MISTRAL-AI-API-KEY-HERE"
MISTRAL_API_URL = "https://api.mistralai.com/v1/embeddings"

client = MistralClient(api_key=MISTRAL_API_KEY)

# Function to get the embeddings from Mistral API
def get_embedding(text):
    embeddings_batch_response = client.embeddings(
    model="mistral-embed",
    input=[text])
    return embeddings_batch_response.data[0].embedding

# Sample JSON data

from bs4 import BeautifulSoup 

with open("parser/hindi.html", 'r') as file:
    soup = BeautifulSoup(file.read(), "html.parser")


data = soup.findAll('script',  {"id" : "__NEXT_DATA__"})[0].text


json_parsed = json.loads(data)
json_dict = dict(json_parsed)

movies = json_dict['props']['pageProps']['searchResults']['titleResults']['titleListItems']

# Prepare SQL insert statements
sql_statements = []


language_id = 1

print(len(movies))

counter = 0




with open("insert_movies.sql", "w") as file:

    for movie in movies:

        try:

            print(f"{counter}. {movie['titleText']}" ,end='\n')

            counter += 1
            # Get embedding for the plot
            movie_description = movie.get('plot', '')
            movie_embedding = get_embedding(movie_description)
            movie_embedding_str = ','.join(map(str, movie_embedding))

            image_save_url = str(uuid.uuid4()) + ".png"

            with open(f'static/{image_save_url}', 'wb') as image_file:
                image_data = requests.get(movie['primaryImage']['url'])
                image_file.write(image_data.content)
            
            # Insert into movies table
            sql_movie = f"""
            INSERT INTO movies (movie_title, movie_language_id, movie_releaseYear, movie_description, movie_thumbnailUrl, movie_description_embedding)
            VALUES (
                '{movie["titleText"].replace("'", "''")}', 
                3,
                {movie["releaseYear"]},
                '{movie_description.replace("'", "''")}',
                '{image_save_url}',
                ARRAY[{movie_embedding_str}]
            );
            """
            sql_statements.append(sql_movie)
            #            '{movie["primaryImage"]["url"]}',
            # Insert into ratings table
            if 'ratingSummary' in movie:
                rating = movie['ratingSummary']['aggregateRating']
                vote_count = movie['ratingSummary']['voteCount']
                sql_rating = f"""
                INSERT INTO ratings (movie_id, rating, vote_count)
                VALUES (
                    (SELECT movie_id FROM movies WHERE movie_title = '{movie["titleText"].replace("'", "''")}'),
                    {rating},
                    {vote_count}
                );
                """
                sql_statements.append(sql_rating)


            

            time.sleep(5)

    # Write SQL statements to a file

            for statement in sql_statements:
                file.write(statement + "\n")

            sql_statements = []
        except:
            print('Exception Occured!')
            print(movie['titleText'])
