from flask import Flask, flash, render_template, url_for, request


app = Flask(__name__)  # Создаем экземпляр класса Flask (приложение)
app.config['SECRET_KEY'] = '123456789'  # Установка секретного ключа

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


@app.route('/contact', methods=['POST', 'GET'])  # По адресу '/contact' будет вызываться функция contact. В данном случае методы 'POST' и 'GET' разрешены
def contact(): 
    if request.method == 'POST':  # Проверяем что передается метод post
        if len(request.form['username']) > 2:  # Проверяем длину поля username
            flash('Сообщение отправлено', category='success')  # Выводим сообщение если ок
        else:
            flash('Ошибка отправки', category='error')  # Выводим сообщение если ошибка 

    return render_template('contact.html', title='Обратная связь', menu=menu)  # Возвращает HTML-шаблон с именем 'contact.html' и дополнительными параметрами title и menu


@app.errorhandler(404)  # Декоратор, который связывает URL со функцией. По адресу '/404' будет вызываться функция page_not_found
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu), 404    



if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение

# with app.test_request_context():  # Тестовое окружение приложения для тестирования URL 
#     print(url_for('index'))  # Печатаем URL адрес функции