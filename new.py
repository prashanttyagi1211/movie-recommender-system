import pickle
import streamlit as st
import requests

def fetch_poster(movie_title):
    api_key = '95543b8b'  # Your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['Response'] == 'True':
            return data.get('Poster', 'https://via.placeholder.com/500x750?text=No+Image')
        else:
            print(f"Movie not found: {movie_title}")
            return 'https://via.placeholder.com/500x750?text=No+Image'
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return 'https://via.placeholder.com/500x750?text=No+Image'

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster using the movie title
        movie_title = movies.iloc[i[0]].title
        recommended_movie_posters.append(fetch_poster(movie_title))
        recommended_movie_names.append(movie_title)

    return recommended_movie_names, recommended_movie_posters


# Streamlit UI
st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
