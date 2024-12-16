import pandas as pd

def filter_netflix_data(file_path):
    # Завантаження даних
    df = pd.read_csv(file_path)
    
    # Крок 1: Фільтруємо дані за рейтингом > 7.5
    high_rating_df = df[df['rating'] > 7.5]
    print("\nФільми/шоу з рейтингом > 7.5:")
    print(high_rating_df[['title', 'rating', 'type', 'language']].head())

    # Крок 2: Обмежуємо лише перші 5 стовпців
    reduced_columns_df = high_rating_df.iloc[:, :5]
    print("\nПерші 5 стовпців:")
    print(reduced_columns_df.head())
    
    # Крок 3: Генераторна функція для умов: English, type=movie/tvSeries, endYear > 2015
    def generator_function(df):
        for _, row in df.iterrows():
            if (row['language'] == 'English' and 
                row['type'] in ['movie', 'tvSeries'] and 
                pd.notna(row['endYear']) and row['endYear'] > 2015):
                yield row
    
    print("\nРядки, що відповідають умовам генератора:")
    gen = generator_function(df)
    for _ in range(5):  # Виведемо перші 5 результатів
        print(next(gen, "Немає більше даних"))
    
    # Додаткове завдання
    print("\nЗавдання 2: Ітератор для основного акторського складу (довжина > 50 символів):")
    class CastIterator:
        def __init__(self, data):
            self.data = data
            self.index = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            while self.index < len(self.data):
                row = self.data.iloc[self.index]
                self.index += 1
                if pd.notna(row['cast']) and len(row['cast']) > 50:
                    return row['cast']
            raise StopIteration
    
    cast_iterator = CastIterator(df)
    for i, cast in enumerate(cast_iterator):
        if i >= 10:  # Виведемо перші 10 записів
            break
        print(cast)
    
    # Функція для підрахунків
    print("\nЗавдання 3: Функція для підрахунків")
    def calculate_metrics(data):
        # a) Кількість шоу/фільмів для дорослих (isAdult == 1)
        adult_count = len(data[data['isAdult'] == 1])
        print(f"Кількість шоу/фільмів для дорослих: {adult_count}")
        
        # b) Середній рейтинг шоу та фільмів з більше ніж 1000 голосів
        filtered = data[data['numVotes'] > 1000]
        average_rating = filtered['rating'].mean()
        print(f"Середній рейтинг шоу та фільмів з більше 1000 голосів: {average_rating:.2f}")
    
    calculate_metrics(df)
    
    # Генератор та спискове включення для шоу з більше ніж 10 епізодами та високим рейтингом
    print("\nЗавдання 4: Генератор та спискове включення")
    def high_episode_generator(data):
        for _, row in data.iterrows():
            if pd.notna(row['episodes']) and row['episodes'] > 10 and row['rating'] > data['rating'].mean():
                yield row['title']
    
    high_episode_titles = [title for title in high_episode_generator(df)]
    print("Шоу з більше ніж 10 епізодами та рейтингом вище середнього:")
    print(high_episode_titles[:10])  # Виведемо перші 10 записів

# Шлях до файлу
file_path = 'C:/Studying/pythan/Materials/netflix_list.csv'
filter_netflix_data(file_path)
