from flask import Flask, render_template


app = Flask(__name__)  # Создаем экземпляр класса Flask (приложение)


@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return render_template('index.html')  # Возвращает HTML-шаблон с именем 'index.html'


@app.route('/about')  # Декоратор, который связывает URL со функцией. По адресу '/about' будет вызываться функция about
def about():
    return render_templates('about.html')  # Возвращает HTML-шаблон с именем 'about.html'


if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение