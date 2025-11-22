import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
import shutil
from PIL import Image
import threading
from pathlib import Path

class EntryWithCopyPaste(ttk.Entry):
    """Поле ввода с поддержкой Ctrl+C/Ctrl+V"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Создаем контекстное меню
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Вырезать", command=self.cut_text)
        self.context_menu.add_command(label="Копировать", command=self.copy_text)
        self.context_menu.add_command(label="Вставить", command=self.paste_text)
        
        # Привязываем правую кнопку мыши
        self.bind("<Button-3>", self.show_context_menu)  # Button-3 - правая кнопка мыши
        
        # Привязываем горячие клавиши
        self.bind("<Control-KeyPress-c>", lambda e: self.copy_text())
        self.bind("<Control-KeyPress-v>", lambda e: self.paste_text())
        self.bind("<Control-KeyPress-x>", lambda e: self.cut_text())
    
    def show_context_menu(self, event):
        """Показывает контекстное меню"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def cut_text(self):
        """Вырезать текст"""
        try:
            self.event_generate("<<Cut>>")
        except tk.TclError:
            pass
    
    def copy_text(self):
        """Копировать текст"""
        try:
            self.event_generate("<<Copy>>")
        except tk.TclError:
            pass
    
    def paste_text(self):
        """Вставить текст"""
        try:
            self.event_generate("<<Paste>>")
        except tk.TclError:
            pass

class TextWithCopyPaste(scrolledtext.ScrolledText):
    """Текстовое поле с поддержкой Ctrl+C/Ctrl+V"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Создаем контекстное меню
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Вырезать", command=self.cut_text)
        self.context_menu.add_command(label="Копировать", command=self.copy_text)
        self.context_menu.add_command(label="Вставить", command=self.paste_text)
        
        # Привязываем правую кнопку мыши
        self.bind("<Button-3>", self.show_context_menu)  # Button-3 - правая кнопка мыши
        
        # Привязываем горячие клавиши
        self.bind("<Control-KeyPress-c>", lambda e: self.copy_text())
        self.bind("<Control-KeyPress-v>", lambda e: self.paste_text())
        self.bind("<Control-KeyPress-x>", lambda e: self.cut_text())
    
    def show_context_menu(self, event):
        """Показывает контекстное меню"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def cut_text(self):
        """Вырезать текст"""
        try:
            self.event_generate("<<Cut>>")
        except tk.TclError:
            pass
    
    def copy_text(self):
        """Копировать текст"""
        try:
            self.event_generate("<<Copy>>")
        except tk.TclError:
            pass
    
    def paste_text(self):
        """Вставить текст"""
        try:
            self.event_generate("<<Paste>>")
        except tk.TclError:
            pass

class NewsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Редактор новостей")
        self.root.geometry("1000x700")
        
        # Пути к файлам
        self.news_path = Path("static/dynamic/news")
        self.images_path = Path("static/img/news")
        self.news_json_path = self.news_path / "news.json"
        self.news_all_json_path = self.news_path / "news-all.json"
        
        # Создаем папки если их нет
        self.news_path.mkdir(parents=True, exist_ok=True)
        self.images_path.mkdir(parents=True, exist_ok=True)
        
        self.current_news_id = None
        self.uploaded_images = []
        
        self.setup_ui()
        self.load_news_list()
    
    def setup_ui(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Список новостей слева
        left_frame = ttk.LabelFrame(main_frame, text="Список новостей", padding="10")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        self.news_listbox = tk.Listbox(left_frame, width=30, height=20)
        self.news_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.news_listbox.bind('<<ListboxSelect>>', self.on_news_select)
        
        # Кнопки для списка новостей
        list_buttons_frame = ttk.Frame(left_frame)
        list_buttons_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(list_buttons_frame, text="Добавить новость", 
                  command=self.add_news).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(list_buttons_frame, text="Удалить новость", 
                  command=self.delete_news).pack(side=tk.LEFT)
        
        # Форма редактирования справа
        right_frame = ttk.LabelFrame(main_frame, text="Редактирование новости", padding="10")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Поля ввода
        ttk.Label(right_frame, text="ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.id_var = tk.StringVar()
        self.id_entry = EntryWithCopyPaste(right_frame, textvariable=self.id_var, width=10)
        self.id_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        ttk.Label(right_frame, text="Заголовок:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.title_var = tk.StringVar()
        self.title_entry = EntryWithCopyPaste(right_frame, textvariable=self.title_var, width=50)
        self.title_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(right_frame, text="Описание:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.desc_text = TextWithCopyPaste(right_frame, width=50, height=4)
        self.desc_text.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(right_frame, text="Текст новости:").grid(row=3, column=0, sticky=tk.NW, pady=5)
        self.content_text = TextWithCopyPaste(right_frame, width=50, height=10)
        self.content_text.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Загрузка изображений
        images_frame = ttk.LabelFrame(right_frame, text="Изображения", padding="10")
        images_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.images_listbox = tk.Listbox(images_frame, height=6)
        self.images_listbox.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(images_frame, text="Добавить изображения", 
                  command=self.add_images).grid(row=1, column=0, pady=5)
        ttk.Button(images_frame, text="Удалить изображение", 
                  command=self.remove_image).grid(row=1, column=1, pady=5)
        
        # Прогресс бар
        self.progress = ttk.Progressbar(images_frame, mode='determinate')
        self.progress.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Кнопки сохранения
        buttons_frame = ttk.Frame(right_frame)
        buttons_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        ttk.Button(buttons_frame, text="Сохранить новость", 
                  command=self.save_news).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Предпросмотр HTML", 
                  command=self.preview_html).pack(side=tk.LEFT)
        
        # Настройка весов для растягивания
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        left_frame.columnconfigure(0, weight=1)
        right_frame.columnconfigure(1, weight=1)
        right_frame.rowconfigure(3, weight=1)
        images_frame.columnconfigure(0, weight=1)
        images_frame.columnconfigure(1, weight=1)
        
        # Добавляем поддержку Ctrl+C/Ctrl+V для всех текстовых полей
        self.setup_keyboard_shortcuts()
    
    def setup_keyboard_shortcuts(self):
        """Настраивает горячие клавиши для всего приложения"""
        # Глобальные горячие клавиши
        self.root.bind("<Control-KeyPress-c>", lambda e: self.copy_text())
        self.root.bind("<Control-KeyPress-v>", lambda e: self.paste_text())
        self.root.bind("<Control-KeyPress-x>", lambda e: self.cut_text())
    
    def copy_text(self):
        """Копирует выделенный текст из активного виджета"""
        widget = self.root.focus_get()
        if hasattr(widget, 'copy_text'):
            widget.copy_text()
        elif isinstance(widget, (tk.Entry, ttk.Entry, tk.Text, tk.Listbox)):
            try:
                widget.event_generate("<<Copy>>")
            except tk.TclError:
                pass
    
    def paste_text(self):
        """Вставляет текст в активный виджет"""
        widget = self.root.focus_get()
        if hasattr(widget, 'paste_text'):
            widget.paste_text()
        elif isinstance(widget, (tk.Entry, ttk.Entry, tk.Text)):
            try:
                widget.event_generate("<<Paste>>")
            except tk.TclError:
                pass
    
    def cut_text(self):
        """Вырезает выделенный текст из активного виджета"""
        widget = self.root.focus_get()
        if hasattr(widget, 'cut_text'):
            widget.cut_text()
        elif isinstance(widget, (tk.Entry, ttk.Entry, tk.Text)):
            try:
                widget.event_generate("<<Cut>>")
            except tk.TclError:
                pass

    # Остальные методы остаются без изменений...
    def load_news_list(self):
        """Загружает список новостей из JSON файлов"""
        self.news_listbox.delete(0, tk.END)
        
        try:
            if self.news_json_path.exists():
                with open(self.news_json_path, 'r', encoding='utf-8') as f:
                    news_data = json.load(f)
                
                for news in news_data:
                    self.news_listbox.insert(tk.END, f"{news['id']}: {news['title']}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить список новостей: {e}")
    
    def on_news_select(self, event):
        """Обработчик выбора новости из списка"""
        selection = self.news_listbox.curselection()
        if not selection:
            return
        
        selected_text = self.news_listbox.get(selection[0])
        news_id = selected_text.split(":")[0]
        
        self.load_news(news_id)
    
    def load_news(self, news_id):
        """Загружает данные конкретной новости"""
        try:
            # Загружаем данные из JSON
            with open(self.news_json_path, 'r', encoding='utf-8') as f:
                news_data = json.load(f)
            
            news_item = next((item for item in news_data if str(item['id']) == news_id), None)
            if not news_item:
                return
            
            self.current_news_id = news_id
            self.id_var.set(news_id)
            self.title_var.set(news_item['title'])
            self.desc_text.delete(1.0, tk.END)
            self.desc_text.insert(1.0, news_item['description'])
            
            # Загружаем HTML контент
            html_file = self.news_path / f"{news_id}.html"
            if html_file.exists():
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Извлекаем текст из HTML
                content = self.extract_text_from_html(html_content)
                self.content_text.delete(1.0, tk.END)
                self.content_text.insert(1.0, content)
            
            # Загружаем список изображений
            self.load_images_list(news_id)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить новость: {e}")
    
    def extract_text_from_html(self, html_content):
        """Извлекает текст из HTML тегов p"""
        lines = html_content.split('\n')
        text_lines = []
        
        for line in lines:
            if line.strip().startswith('<p class="ab__p">'):
                # Извлекаем текст между тегами
                start = line.find('>') + 1
                end = line.find('</p>')
                if start > 0 and end > start:
                    text_lines.append(line[start:end])
        
        return '\n'.join(text_lines)
    
    def load_images_list(self, news_id):
        """Загружает список изображений для новости"""
        self.images_listbox.delete(0, tk.END)
        self.uploaded_images = []
        
        images_dir = self.images_path / news_id
        if images_dir.exists():
            # Сортируем изображения: сначала preview, потом по номеру
            images = []
            for img_file in images_dir.glob("*.webp"):
                if img_file.name == "preview.webp":
                    images.insert(0, img_file)  # preview всегда первый
                else:
                    images.append(img_file)
            
            # Сортируем остальные изображения по номеру
            def get_image_number(img_path):
                try:
                    return int(img_path.stem)
                except:
                    return 0
            
            images[1:] = sorted(images[1:], key=get_image_number)
            
            for img_file in images:
                self.images_listbox.insert(tk.END, img_file.name)
                self.uploaded_images.append(str(img_file))
    
    def add_news(self):
        """Добавляет новую новость"""
        # Находим максимальный ID
        max_id = 0
        try:
            if self.news_json_path.exists():
                with open(self.news_json_path, 'r', encoding='utf-8') as f:
                    news_data = json.load(f)
                max_id = max([news['id'] for news in news_data]) if news_data else 0
        except:
            pass
        
        new_id = max_id + 1
        self.current_news_id = str(new_id)
        self.id_var.set(str(new_id))
        self.title_var.set("")
        self.desc_text.delete(1.0, tk.END)
        self.content_text.delete(1.0, tk.END)
        self.images_listbox.delete(0, tk.END)
        self.uploaded_images = []
    
    def delete_news(self):
        """Удаляет выбранную новость"""
        selection = self.news_listbox.curselection()
        if not selection:
            messagebox.showwarning("Предупреждение", "Выберите новость для удаления")
            return
        
        if not messagebox.askyesno("Подтверждение", "Удалить выбранную новость?"):
            return
        
        selected_text = self.news_listbox.get(selection[0])
        news_id = selected_text.split(":")[0]
        
        try:
            # Удаляем из JSON
            self.remove_news_from_json(news_id)
            
            # Удаляем HTML файл
            html_file = self.news_path / f"{news_id}.html"
            if html_file.exists():
                html_file.unlink()
            
            # Удаляем папку с изображениями
            images_dir = self.images_path / news_id
            if images_dir.exists():
                shutil.rmtree(images_dir)
            
            self.load_news_list()
            messagebox.showinfo("Успех", "Новость удалена")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить новость: {e}")
    
    def remove_news_from_json(self, news_id):
        """Удаляет новость из JSON файлов"""
        for json_file in [self.news_json_path, self.news_all_json_path]:
            if json_file.exists():
                with open(json_file, 'r', encoding='utf-8') as f:
                    news_data = json.load(f)
                
                news_data = [news for news in news_data if str(news['id']) != news_id]
                
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(news_data, f, ensure_ascii=False, indent=2)
    
    def add_images(self):
        """Добавляет изображения с конвертацией в webp"""
        if not self.current_news_id:
            messagebox.showwarning("Предупреждение", "Сначала создайте или выберите новость")
            return
            
        files = filedialog.askopenfilenames(
            title="Выберите изображения",
            filetypes=[("Изображения", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")]
        )
        
        if not files:
            return
        
        # Запускаем конвертацию в отдельном потоке
        thread = threading.Thread(target=self.convert_images, args=(files,))
        thread.daemon = True
        thread.start()
    
    def convert_images(self, files):
        """Конвертирует изображения в webp с правильной нумерацией"""
        def update_progress():
            total = len(files)
            news_images_dir = self.images_path / self.current_news_id
            news_images_dir.mkdir(exist_ok=True)
            
            # Определяем следующий доступный номер
            existing_images = list(news_images_dir.glob("*.webp"))
            next_number = 1
            
            # Ищем максимальный номер среди существующих изображений (кроме preview)
            for img_path in existing_images:
                if img_path.name != "preview.webp":
                    try:
                        num = int(img_path.stem)
                        if num >= next_number:
                            next_number = num + 1
                    except ValueError:
                        pass
            
            for i, file_path in enumerate(files):
                try:
                    # Обновляем прогресс
                    self.progress['value'] = (i / total) * 100
                    self.root.update_idletasks()
                    
                    # Определяем имя файла
                    if i == 0 and not any(img.name == "preview.webp" for img in existing_images):
                        # Первое изображение становится preview, если его еще нет
                        output_name = "preview.webp"
                    else:
                        # Остальные получают последовательные номера
                        output_name = f"{next_number}.webp"
                        next_number += 1
                    
                    output_path = news_images_dir / output_name
                    
                    # Конвертируем в webp
                    with Image.open(file_path) as img:
                        img.convert("RGB").save(output_path, "WEBP", quality=85)
                    
                    # Добавляем в список
                    self.uploaded_images.append(str(output_path))
                    
                    # Обновляем список в UI
                    self.root.after(0, lambda name=output_name: self.images_listbox.insert(tk.END, name))
                    
                except Exception as e:
                    print(f"Ошибка конвертации {file_path}: {e}")
            
            # Завершаем прогресс бар
            self.progress['value'] = 100
            self.root.after(1000, lambda: self.progress.config(value=0))
        
        # Запускаем в основном потоке
        self.root.after(0, update_progress)
    
    def remove_image(self):
        """Удаляет выбранное изображение"""
        selection = self.images_listbox.curselection()
        if not selection:
            return
        
        image_name = self.images_listbox.get(selection[0])
        
        try:
            image_path = self.images_path / self.current_news_id / image_name
            if image_path.exists():
                image_path.unlink()
            
            self.images_listbox.delete(selection[0])
            
            # Перезагружаем список чтобы обновить нумерацию
            if self.current_news_id:
                self.load_images_list(self.current_news_id)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить изображение: {e}")
    
    def generate_html(self):
        """Генерирует HTML код новости"""
        content = self.content_text.get(1.0, tk.END).strip()
        paragraphs = [p.strip() for p in content.split('\n') if p.strip()]
        
        html_parts = []
        
        # Добавляем параграфы
        for p in paragraphs:
            html_parts.append(f'<p class="ab__p">{p}</p>')
        
        # Добавляем изображения
        if self.uploaded_images:
            html_parts.append('<br />')
            html_parts.append('<div>')
            
            # Группируем изображения по 2
            images = []
            for img_path in self.uploaded_images:
                img_name = os.path.basename(img_path)
                images.append(img_name)
            
            # Сортируем: preview первый, потом по номеру
            previews = [img for img in images if img == "preview.webp"]
            other_images = [img for img in images if img != "preview.webp"]
            
            # Сортируем остальные по номеру
            def get_image_number(img_name):
                try:
                    return int(img_name.split('.')[0])
                except:
                    return 0
            
            other_images.sort(key=get_image_number)
            all_images = previews + other_images
            
            for i in range(0, len(all_images), 2):
                html_parts.append('  <div class="img-container">')
                
                for j in range(2):
                    if i + j < len(all_images):
                        img_name = all_images[i + j]
                        src = f"/img/news/{self.current_news_id}/{img_name}"
                        html_parts.append(f'    <img class="img-single__minimg" src="{src}" />')
                
                html_parts.append('  </div>')
            
            html_parts.append('</div>')
        
        return '\n'.join(html_parts)
    
    def save_news(self):
        """Сохраняет новость"""
        try:
            news_id = self.id_var.get().strip()
            title = self.title_var.get().strip()
            description = self.desc_text.get(1.0, tk.END).strip()
            
            if not all([news_id, title, description]):
                messagebox.showwarning("Предупреждение", "Заполните все обязательные поля")
                return
            
            # Генерируем HTML
            html_content = self.generate_html()
            
            # Сохраняем HTML файл
            html_file = self.news_path / f"{news_id}.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Обновляем JSON файлы
            self.update_json_files(news_id, title, description)
            
            messagebox.showinfo("Успех", "Новость сохранена")
            self.load_news_list()
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить новость: {e}")
    
    def update_json_files(self, news_id, title, description):
        """Обновляет JSON файлы с данными новости"""
        news_item = {
            "teg": ["all"],
            "id": int(news_id),
            "title": title,
            "description": description
        }
        
        for json_file in [self.news_json_path, self.news_all_json_path]:
            news_data = []
            
            if json_file.exists():
                with open(json_file, 'r', encoding='utf-8') as f:
                    news_data = json.load(f)
            
            # Удаляем старую версию если есть
            news_data = [item for item in news_data if item['id'] != int(news_id)]
            
            # Добавляем новую
            news_data.append(news_item)
            
            # Сортируем по ID
            news_data.sort(key=lambda x: x['id'], reverse=True)
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(news_data, f, ensure_ascii=False, indent=2)
    
    def preview_html(self):
        """Показывает предпросмотр HTML"""
        html_content = self.generate_html()
        
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Предпросмотр HTML")
        preview_window.geometry("600x400")
        
        text_widget = TextWithCopyPaste(preview_window, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_widget.insert(1.0, html_content)
        text_widget.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = NewsEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
