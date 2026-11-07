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
    """ средняя оценка"""
    if not movies:
        return 0.0
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """самый старый возраст, самый новый возраст, средний возраст"""
    if not movies:
        return (0, 0, 0)
    
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    
    return (oldest, newest, average_age)

def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

def rating_tier(rating):
    """Возвращает категорию фильма по оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        # Используем тернарный оператор, как того требует задание
        return "хорошо" if rating < 9 else "шедевр" 
    elif rating >= 5:
        return "средне"
    else:
        # И здесь тоже используем тернарный оператор для надежности
        return "слабо" if rating < 5 else "средне"

def decade_label(year):
    """Возвращает метку десятилетия для фильма через оператор match."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут через цикл for."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    """Приводит строку к Title Case вручную, без использования str.title()."""
    words = title.split()
    normalized_words = []
    for word in words:
        if word: # Защита от пустых строк на случай двойных пробелов
            normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)

def make_slug(title):
    """Превращает название в слаг (например, 'Silent Hours' -> 'silent-hours')."""
    return normalize_title(title).lower().replace(" ", "-")

def format_report_line(movie):
    """Возвращает отформатированную строку с описанием фильма."""
    genres_str = ", ".join(sorted(list(movie["genres"])))
    duration_str = duration_in_hours(movie["duration_min"])
    
    return f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, {duration_str}, жанры: {genres_str}'

def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    # Извлекаем только названия
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

def main():
    print("Hello from catalog_analysis.py!")
    
    #Тестирование функций Этапа 1
    print("\n--- Проверка Этапа 1 ---")
    print(f"Средняя оценка: {average_rating(movies)}")
    print(f"Статистика возраста: {catalog_age_stats(movies)}")
    print(f"155 минут в часах: {duration_in_hours(155)}")

    #Тестирование функций Этапа 2
    print("\n--- Проверка Этапа 2 ---")
    print(f"Оценка 9.2: {rating_tier(9.2)}")
    print(f"Оценка 7.5: {rating_tier(7.5)}")
    print(f"Оценка 6.0: {rating_tier(6.0)}")
    print(f"Оценка 4.5: {rating_tier(4.5)}")
    print(f"Год 2024: {decade_label(2024)}")
    print(f"Год 2018: {decade_label(2018)}")
    print(f"Год 2011: {decade_label(2011)}")

    #Тестирование функций Этапа 3
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
            print(f" - Найден: {movies[index]['title']} (рейтинг {movies[index]['rating']})")
            break
        index += 1
    else:
        print(" - Шедевров не найдено")

    print("\n3. Количество фильмов длиннее 120 минут:")
    print(f" - {count_long_movies(movies, 120)} шт.")

    #Тестирование функций Этапа 4
    print("\n--- Проверка Этапа 4 ---")
    print(f"normalize_title('silent hours') -> {normalize_title('silent hours')}")
    print(f"make_slug('Silent Hours')       -> {make_slug('Silent Hours')}")
    print(f"format_report_line(movies[7])   -> {format_report_line(movies[7])}")

    #Тестирование функций Этапа 5
    print("\n--- Проверка Этапа 5 ---")
    
    print("Список названий по убыванию рейтинга:")
    print(titles_sorted_by_rating(movies))
    
    print("\nТоп-3 фильма по рейтингу:")
    print(top_n_by_rating(movies, 3))

if __name__ == "__main__":
    main()