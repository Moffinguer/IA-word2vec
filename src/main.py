import requests
import json

# función para obtener el campo 'overview', 'genres' y 'original_title' de una película
def get_movie_data(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    payload = {'api_key': '8c84889123c57f94a58c3d60912b646b', 'language': 'es-ES'}
    response = requests.get(url, params=payload)
    data = json.loads(response.text)
    overview = data.get('overview', '')
    genres = [genre['name'] for genre in data.get('genres', [])]
    title = data.get('original_title','')
    if overview == '':
        return get_movie_data(movie_id + 550)
    genre = genres[0]
    print(f"Title: {title} | Genre: {genre} | ID: {movie_id}")
    return overview, genre, title;

# bucle para realizar las consultas y guardar los datos en archivos separados
for i in range(100, 550):
    overview, genre, title = get_movie_data(i)
    if overview:
        with open('overview.txt', 'a', encoding='utf-8') as f1:
            f1.write(overview + '\n\n')
        with open('genres.txt', 'a', encoding='utf-8') as f2:
            f2.write(genre + '\n\n')
        with open('titles.txt', 'a', encoding='utf-8') as f3:
        	 f3.write(title + "\n\n")