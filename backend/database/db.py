import psycopg2 # type: ignore
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

# Database connection parameters
hostname = os.getenv('POSTGRES_HOST')  # Replace with your PostgreSQL container IP address or hostname
username = os.getenv('POSTGRES_USER')   # Default superuser for PostgreSQL
password = os.getenv('POSTGRES_PASSWORD')     # Password you set for the PostgreSQL superuser
database = 'postgres'   # Default database name

class databaseHandler:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

        self.cursor = self.connection.cursor()

    def get_movies_by_language(self, language):
        self.cursor.execute("""
            SELECT 
                m.movie_id, 
                m.movie_title, 
                m.movie_language_id, 
                m.movie_releaseYear, 
                m.movie_description, 
                m.movie_thumbnailUrl,
                r.rating,
                r.vote_count
            FROM movies m
            LEFT JOIN ratings r ON m.movie_id = r.movie_id
            WHERE m.movie_language_id = (
                SELECT language_id FROM language WHERE language_name = %s
            );
        """, (language,))
        data = self.cursor.fetchall()
        print(data)
        return data  
    
    def get_movies_by_vector_embedding(self, vector):
        self.cursor.execute(f"""
            SELECT 
                m.movie_id, 
                m.movie_title, 
                m.movie_language_id, 
                m.movie_releaseYear, 
                m.movie_description, 
                m.movie_thumbnailUrl,
                r.rating,
                r.vote_count
            FROM movies m
            LEFT JOIN ratings r ON m.movie_id = r.movie_id
            ORDER BY m.movie_description_embedding <-> '{vector}'
            LIMIT 3;
        """)
        return self.cursor.fetchall()
    
    def get_movies_by_id(self, movie_id):
        self.cursor.execute("""
            SELECT 
                m.*, 
                r.rating, 
                r.vote_count 
            FROM movies m
            LEFT JOIN ratings r ON m.movie_id = r.movie_id
            WHERE m.movie_id = %s;
        """, (movie_id,))
        return self.cursor.fetchall()
    
    def get_movie_details_by_movie_id(self, movie_id):
        self.cursor.execute("""
            SELECT 
                m.movie_id, 
                m.movie_title, 
                m.movie_language_id, 
                m.movie_releaseYear, 
                m.movie_description, 
                m.movie_thumbnailUrl,
                r.rating,
                r.vote_count
            FROM movies m
            LEFT JOIN ratings r ON m.movie_id = r.movie_id
            WHERE m.movie_id = %s;
        """, (movie_id,))
        return self.cursor.fetchall()
    
    def get_urls(self):
        self.cursor.execute("SELECT movie_id, movie_thumbnailUrl FROM movies;")
        data = self.cursor.fetchall()
        return data
    
# Example usage:
# db = databaseHandler()
# data = db.get_urls()

# for tuple in data:
#     with open(f'static/{tuple[0]}.png', 'wb') as file:
#         try:
#             response = requests.get(tuple[1])
#             file.write(response.content)
#         except:
#             print(f"Error in fetching {tuple[1]}")
