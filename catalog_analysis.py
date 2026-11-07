import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    if not movies:
        return 0.0
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return (0, 0, 0)
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average_age)

def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо" if rating < 9 else "шедевр" 
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating < 5 else "средне"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    words = title.split()
    normalized_words = []
    for word in words:
        if word:
            normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)

def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")

def format_report_line(movie):
    genres_str = ", ".join(sorted(list(movie["genres"])))
    duration_str = duration_in_hours(movie["duration_min"])
    title_str = normalize_title(movie["title"])
    return (f'"{title_str}" ({movie["year"]}) — {movie["rating"]}/10, '
            f'{duration_str}, жанры: {genres_str}')

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography

def high_rated_movies(movies):
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg
    }

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])
    genres_b = set()
    for movie in movies_b:
        genres_b.update(movie["genres"])
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    
    # 1. Общая статистика
    avg_rating = average_rating(movies)
    avg_age = catalog_age_stats(movies)[2] 
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")
    
    # 2. Топ-3 фильма
    print("\nТоп-3 фильма:")
    top_movies = top_n_by_rating(movies, 3)
    for title, _ in top_movies:
        movie = next(m for m in movies if m["title"] == title)
        print(f"  {format_report_line(movie)}")
        
    # 3. Фильмов по жанрам
    print("\nФильмов по жанрам:")
    genres_count = count_by_genre(movies)
    sorted_genres = sorted(genres_count.items(), key=lambda item: (-item[1], item[0]))
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
        
    # 4. Все жанры каталога
    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")


def main():
    # Очищаем консоль перед выводом отчета для красоты (опционально)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    build_report(movies)


if __name__ == "__main__":
    main()