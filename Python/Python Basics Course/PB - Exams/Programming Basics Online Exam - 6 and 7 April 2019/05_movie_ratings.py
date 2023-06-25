import sys
number_of_movies = int(input())
highest_rating_movie = ''
highest_rating = -sys.maxsize
lowest_rating_movie = ''
lowest_rating = sys.maxsize
total_ratings_counter = 0.0
all_movies_avg_rating = 0.0

for nums in range(number_of_movies):
    current_movie_name = input()
    current_movie_rating = float(input())
    total_ratings_counter += current_movie_rating

    if current_movie_rating >= highest_rating:
        highest_rating = current_movie_rating
        highest_rating_movie = current_movie_name
    if current_movie_rating <= lowest_rating:
        lowest_rating = current_movie_rating
        lowest_rating_movie = current_movie_name

    all_movies_avg_rating = total_ratings_counter / number_of_movies

print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {all_movies_avg_rating:.1f}")
