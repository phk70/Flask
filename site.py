from flask import Flask

app = Flask(__name__)  # Создаем экземпляр класса Flask (приложение)

@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return 'Домашняя страница'  # Возвращает просто строку 'Домашняя страница'

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение