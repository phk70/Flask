from flask import Flask, render_template


app = Flask(__name__)  # Создаем экземпляр класса Flask (приложение)

menu = ['Главная', 'О нас', 'Контакты']

@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return render_template('index.html', title='Главная страница', menu=menu)  # Возвращает HTML-шаблон с именем 'index.html' и дополнительными параметрами title и menu


@app.route('/about')  # Декоратор, который связывает URL со функцией. По адресу '/about' будет вызываться функция about
def about():
    return render_template('about.html', title='О нас', menu=menu)  # Возвращает HTML-шаблон с именем 'about.html' и дополнительными параметрами title и menu


if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение