import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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
    return f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, {duration_str}, жанры: {genres_str}'

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
    return {movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg}

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

def main():
    print("Hello from catalog_analysis.py!")
    
    # --- Тестирование функций Этапа 1 ---
    print("\n--- Проверка Этапа 1 ---")
    print(f"Средняя оценка: {average_rating(movies)}")
    print(f"Статистика возраста: {catalog_age_stats(movies)}")
    print(f"155 минут в часах: {duration_in_hours(155)}")

    # --- Тестирование функций Этапа 2 ---
    print("\n--- Проверка Этапа 2 ---")
    print(f"Оценка 9.2: {rating_tier(9.2)}")
    print(f"Оценка 7.5: {rating_tier(7.5)}")
    print(f"Оценка 6.0: {rating_tier(6.0)}")
    print(f"Оценка 4.5: {rating_tier(4.5)}")
    print(f"Год 2024: {decade_label(2024)}")
    print(f"Год 2018: {decade_label(2018)}")
    print(f"Год 2011: {decade_label(2011)}")

    # --- Тестирование функций Этапа 3 ---
    print("\n--- Проверка Этапа 3 ---")
    print("\n1. Фильмы не в жанре 'comedy' (for + continue):")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(f" - {movie['title']}")
    
    print("\n2. Первый фильм с рейтингом > 9.0 (while + break):")
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            title = movies[index]["title"]
            rating = movies[index]["rating"]
            print(f" - Найден: {title} (рейтинг {rating})")
            break
        index += 1
    else:
        print(" - Шедевров не найдено")

    print("\n3. Количество фильмов длиннее 120 минут:")
    print(f" - {count_long_movies(movies, 120)} шт.")

    # --- Тестирование функций Этапа 4 ---
    print("\n--- Проверка Этапа 4 ---")
    print(f"normalize_title('silent hours') -> {normalize_title('silent hours')}")
    print(f"make_slug('Silent Hours')       -> {make_slug('Silent Hours')}")
    print(f"format_report_line(movies[7])   -> {format_report_line(movies[7])}")

    # --- Тестирование функций Этапа 5 ---
    print("\n--- Проверка Этапа 5 ---")
    print("Список названий по убыванию рейтинга:")
    print(titles_sorted_by_rating(movies))
    print("\nТоп-3 фильма по рейтингу:")
    print(top_n_by_rating(movies, 3))

    # --- Тестирование функций Этапа 6 ---
    print("\n--- Проверка Этапа 6 ---")
    print("Количество фильмов по жанрам:")
    print(count_by_genre(movies))
    print("\nФильмография актеров:")
    filmography = actor_filmography(movies)
    for actor, films in filmography.items():
        print(f" - {actor}: {films}")
    print(f"\nФильмы с рейтингом выше среднего ({average_rating(movies)}):")
    print(high_rated_movies(movies))

    # --- Тестирование функций Этапа 7 ---
    print("\n--- Проверка Этапа 7 ---")
    
    print("Все уникальные жанры:")
    print(all_genres(movies))
    
    print("\nОбщие актеры в movies[0] и movies[3]:")
    print(common_actors(movies[0], movies[3]))
    
    print("\nЖанры только в movies[5:6], но не в movies[:5]:")
    print(genres_only_in_one(movies[5:6], movies[:5]))

    print("\n--- Проверка Этапа 8 ---")
    
    print("Фильмы с рейтингом >= 8.0:")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
        
    print("\nСуммарная длительность фильмов с рейтингом > 7:")
    # Генераторное выражение (без квадратных скобок) передается в sum()
    total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
    print(f" - {total_duration} минут")

if __name__ == "__main__":
    main()