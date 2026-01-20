import json
import os
import re
from transliterate import translit

# --- НАСТРОЙКИ ---
JSON_FILENAME = 'educational_data.json'  # Имя вашего файла JSON
ROOT_DIR = 'data'  # Имя корневой папки с файлами
# -----------------

def make_safe_filename(filename):
    """
    Превращает 'Учебный план 2024.pdf' в 'uchebnyy_plan_2024.pdf'
    """
    # 1. Отделяем имя от расширения
    name, ext = os.path.splitext(filename)
    
    # 2. Транслитерация (русские буквы -> латиница)
    try:
        # reversed=True переводит с русского на латиницу
        name = translit(name, 'ru', reversed=True)
    except:
        pass # Если там уже английский или цифры, оставляем как есть

    # 3. Приводим к нижнему регистру
    name = name.lower()

    # 4. Заменяем пробелы и спецсимволы на нижнее подчеркивание
    # Оставляем только буквы, цифры и _
    name = re.sub(r'[^a-z0-9]', '_', name)
    
    # 5. Убираем дублирующиеся подчеркивания (напр. plan__2024 -> plan_2024)
    name = re.sub(r'_+', '_', name)
    
    # 6. Убираем подчеркивание в начале и конце
    name = name.strip('_')

    return f"{name}{ext}"

def process_files():
    # Проверка существования JSON
    if not os.path.exists(JSON_FILENAME):
        print(f"Ошибка: Файл {JSON_FILENAME} не найден!")
        return

    # Чтение JSON
    with open(JSON_FILENAME, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed_files_count = 0
    errors_count = 0

    print("--- Начинаю обработку файлов ---")

    # Проходимся по списку объектов в JSON
    for item in data:
        # Проходимся по всем ключам (plan21, z, eduprocess и т.д.)
        for key, value in item.items():
            
            # Нас интересуют только строки, которые заканчиваются на .pdf
            # И начинаются с /data/ (чтобы не трогать обычный текст)
            if isinstance(value, str) and value.lower().endswith('.pdf') and value.startswith('/data/'):
                
                original_json_path = value
                
                # Убираем первый слэш, чтобы путь стал относительным для скрипта
                # Пример: /data/folder/file.pdf -> data/folder/file.pdf
                relative_path = original_json_path.lstrip('/')
                
                # Полный путь к файлу на диске
                full_path = os.path.abspath(relative_path)
                directory = os.path.dirname(full_path)
                filename = os.path.basename(full_path)

                # Проверяем, существует ли файл физически
                if not os.path.exists(full_path):
                    print(f"[!] Файл не найден (пропуск): {relative_path}")
                    errors_count += 1
                    continue

                # Генерируем новое имя
                new_filename = make_safe_filename(filename)

                # Если имя изменилось - переименовываем
                if filename != new_filename:
                    new_full_path = os.path.join(directory, new_filename)
                    
                    try:
                        # 1. Переименовываем файл на диске
                        os.rename(full_path, new_full_path)
                        
                        # 2. Обновляем путь в JSON (возвращаем слэш в начале)
                        # os.path.join использует обратный слэш на Windows, нам нужны прямые для web
                        new_json_path = '/' + os.path.relpath(new_full_path, start=os.getcwd()).replace('\\', '/')
                        
                        item[key] = new_json_path
                        
                        print(f"[OK] {filename} -> {new_filename}")
                        changed_files_count += 1
                        
                    except OSError as e:
                        print(f"[Ошибка] Не удалось переименовать {filename}: {e}")
                        errors_count += 1

    # Сохраняем обновленный JSON
    new_json_name = 'updated_' + JSON_FILENAME
    with open(new_json_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("-" * 30)
    print(f"Готово! Переименовано файлов: {changed_files_count}")
    print(f"Ошибок (файлы не найдены): {errors_count}")
    print(f"Новый JSON сохранен как: {new_json_name}")

if __name__ == "__main__":
    process_files()
