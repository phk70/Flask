from flask import Flask, render_template, url_for, request


app = Flask(__name__)  # Создаем экземпляр класса Flask (приложение)

menu = [{'name': 'Установка', 'url': 'install-flask'},
        {'name': 'Первое приложение', 'url': 'first-app'},
        {'name': 'Обратная связь', 'url': 'contact'}]  # Меню с ссылками на другие страницы.


@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    print(url_for('index'))  # Печатаем URL адрес функции
    return render_template('index.html', title='Главная страница', menu=menu)  # Возвращает HTML-шаблон с именем 'index.html' и дополнительными параметрами title и menu


@app.route('/about')  # Декоратор, который связывает URL со функцией. По адресу '/about' будет вызываться функция about
def about():
    print(url_for('about'))  # Печатаем URL адрес функции
    return render_template('about.html', title='О нас', menu=menu)  # Возвращает HTML-шаблон с именем 'about.html' и дополнительными параметрами title и menu


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form)  # Печатаем данные формы
        print(request.form['username'])  # Печатаем значение поля username

    return render_template('contact.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение

# with app.test_request_context():  # Тестовое окружение приложения для тестирования URL 
#     print(url_for('index'))  # Печатаем URL адрес функции