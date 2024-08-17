# find-my-movie

## Description
This project is based on Vector Databases(Postgres + pgvector) built using FastAPI. It provides endpoints to fetch movie details based on natural language queries. The API also supports CORS and serves static files.Data was scraped from IMDB

![image](https://github.com/user-attachments/assets/390676c1-292b-45d9-800d-4fd24b43630d)
![image](https://github.com/user-attachments/assets/fe994fb4-63a0-47ea-b9ca-f93e0fc4b06e)

## Data Scraping

### How We Scraped the Data
We scraped movie data from IMDb to populate our recommendation system. This was done using the `BeautifulSoup` library in Python to parse the HTML content of IMDb pages.

1. **Identify the Target Pages**: We identified the IMDb pages that contained the movie data we needed, such as movie titles, descriptions, genres, and release dates.

2. **HTTP Requests**: We sent HTTP requests to these pages using the `requests` library to retrieve the HTML content.

3. **Parse the HTML**: The HTML content was parsed using `BeautifulSoup`, allowing us to extract specific elements such as movie titles, descriptions, genres, etc.


### Prerequisites
- PostgreSQL with `pgvector` extension

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/iamcool0090/find-my-movie.git
    ```
2. Navigate to the project directory:
    ```sh
    cd find-my-movie
    ```
3. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Create a `.env` file in the backend directory 
    ```env
        MISTRAL_API_KEY="MISTRAL_API_KEY"
        POSTGRES_PASSWORD="mysecretpassword"
        POSTGRES_USER="postgres"
        POSTGRES_DB="postgres"
        POSTGRES_HOST="localhost"
        POSTGRES_PORT="5432"
    ```

## Usage
1. Start the FastAPI server:
    ```sh
    backend/run.sh
    ```
2. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.

## API Endpoints

### Home
- **GET /** 
    - Returns a welcome message.
    - **Response:**
        ```json
        {
            "message": "Welcome to the Movie Recommendation API"
        }
        ```

### Get Movies by Language
- **GET /api/movies/{language}**
    - Fetches movies based on the specified language.
    - **Parameters:**
        - `language` (str): The language of the movies to fetch.
    - **Response:**
        ```json
        [
            {
                "movie_id": 1,
                "title": "Movie Title",
                "language": "en"
            },
        ]
        ```

### Get Movies by Natural Language
- **POST /api/movies/natural-language**
    - Fetches movies based on a natural language query.
    - **Request Body:**
        ```json
        {
            "text": "Find a movie involving dyslexia"
        }
        ```


### Get Movie Details by ID
- **GET /api/movies/id/{movie_id}**
    - Fetches details of a movie based on its ID.
    - **Parameters:**
        - [`movie_id`](command:_github.copilot.openSymbolFromReferences?%5B%22movie_id%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Frazor%2Fproject%2Ffind-my-movie-improved%2Fbackend%2Fbackend%2Fapi%2Fapi.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Frazor%2Fproject%2Ffind-my-movie-improved%2Fbackend%2Fbackend%2Fapi%2Fapi.py%22%2C%22path%22%3A%22%2Fhome%2Frazor%2Fproject%2Ffind-my-movie-improved%2Fbackend%2Fbackend%2Fapi%2Fapi.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A69%2C%22character%22%3A22%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Frazor%2Fproject%2Ffind-my-movie-improved%2Fbackend%2Fbackend%2Fapi%2Fapi.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Frazor%2Fproject%2Ffind-my-movie-improved%2Fbackend%2Fbackend%2Fapi%2Fapi.py%22%2C%22path%22%3A%22%2Fhome%2Frazor%2Fproject%2Ffind-my-movie-improved%2Fbackend%2Fbackend%2Fapi%2Fapi.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A69%2C%22character%22%3A22%7D%7D%5D%5D "Go to definition") (int): The ID of the movie to fetch details for.
    - **Response:**
        ```json
        {
            "movie_id": 1,
            "title": "Movie Title",
            "description": "Movie Description",
            "language": "en"
        }
        ```




## Project Name Change

Originally, this project was named **find-that-movie.com**. However, after some consideration and feedback, we decided to rename it to **find-my-movie**. The new name better reflects the personalized experience we aim to provide, helping users find the perfect movie just for them.



## Contributing
1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
