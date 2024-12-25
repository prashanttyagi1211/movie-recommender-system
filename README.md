# Movie Recommender System

A web-based Movie Recommender System built using Python, Streamlit, and the OMDb API. This application suggests movies similar to the one selected by the user and displays their posters.

## Features
- Suggests 5 similar movies based on the selected movie.
- Displays movie posters fetched from the OMDb API.
- Easy-to-use dropdown interface for selecting movies.

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Data**: Pickle files containing precomputed movie similarities.
- **API**: [OMDb API](https://www.omdbapi.com/)

## Prerequisites
- Python 3.7 or later
- An API key from [OMDb API](https://www.omdbapi.com/)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/movie-recommender-system.git
   cd movie-recommender-system
2. pip install -r requirements.txt
3. Add your OMDb API key: Replace the placeholder your_api_key in the code with your actual OMDb API key.

4. Ensure you have the required data files:

4.1 movie_list.pkl
4.2 similarity.pkl Place these files in the project directory.
