import json
import datetime

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return []

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes)+1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    print("Заметка добавлена.")

def edit_note():
    note_id = input("Введите ID заметки для редактирования: ")
    for note in notes:
        if str(note['id']) == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = timestamp
            print("Заметка отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = input("Введите ID заметки для удаления: ")
    for note in notes:
        if str(note['id']) == note_id:
            notes.remove(note)
            print("Заметка удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def print_notes():
    if not notes:
        print("Заметки отсутствуют.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело заметки: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print()

def main():
    while True:
        print("1. Вывести список заметок")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            print_notes()
        elif choice == '2':
            add_note()
            save_notes(notes)
        elif choice == '3':
            edit_note()
            save_notes(notes)
        elif choice == '4':
            delete_note()
            save_notes(notes)
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == '__main__':
    notes = load_notes()
    main()
