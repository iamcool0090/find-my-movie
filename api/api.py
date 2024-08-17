from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


from pydantic import BaseModel


from typing import List



from database.db import databaseHandler
from api.embedding import generate_embeddings
from dotenv import load_dotenv
import os




load_dotenv()
app = FastAPI()
dbhandler = databaseHandler()
embedding_generator = generate_embeddings(os.getenv("MISTRAL_API_KEY"))


app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {"message": "Welcome to the Movie Recommendation API"}


@app.get("/api/movies/{language}")
def get_movies_by_language(language: str):
    try:
        movies = dbhandler.get_movies_by_language(language)
    except:
        return JSONResponse(content={"error": "Error in fetching movies"})
    
    return JSONResponse(content=movies)

@app.post("/api/movies/natural-language")
async def get_movies_by_natural_language(Request: Request):
    request_content = await Request.json()
    try:
        vector = embedding_generator.get_embeddings(request_content['text'])
    except:
        return JSONResponse(content={"error": "Error in generating embeddings"})
    try:
        movies = dbhandler.get_movies_by_vector_embedding(vector=vector)
    except:
        print(vector)
        return JSONResponse(content={"error": "Error in fetching movies"})
    
    return JSONResponse(content=movies)

@app.get("/api/movies/id/{movie_id}")
def get_movie_details(movie_id: int):
    movie_details = dbhandler.get_movie_details_by_movie_id(movie_id)
    return JSONResponse(content=movie_details)


