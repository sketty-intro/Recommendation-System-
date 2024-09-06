# Simple Content-Based Movie Recommendation System

# Sample dataset of movies (movie titles and their genres)
movies = [
    {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
    {"title": "The Godfather", "genres": ["Crime", "Drama"]},
    {"title": "Toy Story", "genres": ["Animation", "Family"]},
    {"title": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"]},
    {"title": "Titanic", "genres": ["Romance", "Drama"]},
    {"title": "The Avengers", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "Finding Nemo", "genres": ["Animation", "Family"]},
    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"title": "Forrest Gump", "genres": ["Drama", "Romance"]},
]

# Function to recommend movies based on user's genre preferences
def recommend_movies(preferred_genres):
    recommended = []
    
    for movie in movies:
        # Check if any of the user's preferred genres match the movie's genres
        if any(genre in preferred_genres for genre in movie["genres"]):
            recommended.append(movie["title"])
    
    return recommended

# Simulating user preferences
user_preferences = input("Enter your preferred genres (comma-separated): ").split(', ')
user_preferences = [genre.capitalize() for genre in user_preferences]  # Capitalize for matching

# Recommend movies based on preferences
recommended_movies = recommend_movies(user_preferences)

# Display recommendations
if recommended_movies:
    print("\nWe recommend the following movies based on your preferences:")
    for movie in recommended_movies:
        print(f"- {movie}")
else:
    print("\nSorry, we couldn't find any movies matching your preferences.")
