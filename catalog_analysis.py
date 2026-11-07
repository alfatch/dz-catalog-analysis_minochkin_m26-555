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
    """Возвращает категорию фильма по его оценке."""
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

if __name__ == "__main__":
    main()