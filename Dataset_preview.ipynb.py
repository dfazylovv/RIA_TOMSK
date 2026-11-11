import pandas as pd
from IPython.display import display

# Настройки отображения
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_colwidth', 300)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

# Загрузка датасета
df = pd.read_csv(
    "news_2026_full.csv",
    sep=";",
    encoding="utf-8-sig"
)

# 1. Общая информация
print("=" * 80)
print("ОБЩАЯ ИНФОРМАЦИЯ О ДАТАСЕТЕ")
print("=" * 80)

print(f"Количество новостей: {df.shape[0]}")
print(f"Количество столбцов: {df.shape[1]}")
print(f"Объём памяти: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# 2. Просмотр всех столбцов
print("\nСТРУКТУРА ДАТАСЕТА:")
print(df.info())

# 3. Первые 10 новостей со всеми столбцами
print("\nПЕРВЫЕ 10 НОВОСТЕЙ:")
display(df.head(10))

# 4. Случайные 10 новостей
print("\nСЛУЧАЙНЫЕ 10 НОВОСТЕЙ:")
display(df.sample(10, random_state=42))

# 5. Последние 10 новостей
print("\nПОСЛЕДНИЕ 10 НОВОСТЕЙ:")
display(df.tail(10))

# 6. Информация о пропущенных значениях
print("\nПРОПУЩЕННЫЕ ЗНАЧЕНИЯ:")
missing = pd.DataFrame({
    "Количество пропусков": df.isnull().sum(),
    "Процент пропусков": (df.isnull().mean() * 100).round(2)
})
display(missing)

# 7. Проверка дубликатов
print("\nПРОВЕРКА ДУБЛИКАТОВ:")
print(f"Полные дубликаты: {df.duplicated().sum()}")
print(f"Дубликаты URL: {df['URL'].duplicated().sum()}")

# 8. Статистика текстов
print("\nСТАТИСТИКА НОВОСТЕЙ:")
display(
    df[[
        "Количество символов",
        "Количество слов",
        "Количество абзацев",
        "Количество предложений"
    ]].describe().round(2)
)

# 9. Распределение по дням недели
print("\nРАСПРЕДЕЛЕНИЕ НОВОСТЕЙ ПО ДНЯМ НЕДЕЛИ:")
display(df["День недели"].value_counts().to_frame("Количество новостей"))

# 10. Количество новостей по месяцам
print("\nРАСПРЕДЕЛЕНИЕ ПО МЕСЯЦАМ:")
display(df["Месяц"].value_counts().sort_index().to_frame("Количество новостей"))
