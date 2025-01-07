<!-- Установка Flask -->

pip install Flask

<!-- Создаем рабочий файл site.py, импортируем Flask и пишем первое приложение. Просто переход на страницу -->

from flask import Flask

app = Flask(__name__)  # Создаем экземпляр класса Flask (приложение)

@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return 'Домашняя страница'  # Возвращает просто строку 'Домашняя страница'

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение

<!-- Если хотим добавить еще новую страницу, то добавляем еще один роутер -->

@app.route('/about')  # Декоратор, который связывает URL со функцией. По адресу '/about' будет вызываться функция about
def about():
    return '<h1>О нас</h1>'  # Возвращает просто заголовок 'О нас'

<!-- Если один и тот же обработчик (функция) должн срабатывать по нескольким адресам, то роутеры можно просто расположить друг над другом -->

@app.route('/index')  # Декоратор, который связывает URL со функцией. По адресу '/index' будет вызываться функция index  
@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return 'Домашняя страница'  # Возвращает просто строку 'Домашняя страница'

<!-- *************************************************************************************************************************************
2. Шаблонизаторы

Чтобы воспользоваться шаблонами необходимо дополнительно импортировать модуль из Flask -->

from flask import Flask, render_template

<!-- И тогда вызываем именно отдельно хранящийся шаблон.
Шаблоны берутся из подкаталога templates относитьльно нашей рабочей программы.
Создадим templstes/index.html в папке с site.py--> -->

@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return render_template('index.html')  # Возвращает HTML-шаблон с именем 'index.html'

<!-- Делаем тоже самое для второй страницы about  -->

@app.route('/about')  # Декоратор, который связывает URL со функцией. По адресу '/about' будет вызываться функция about
def about():
    return render_templates('about.html')  # Возвращает HTML-шаблон с именем 'about.html'

<!-- Параметры передаются в шаблоны с помощию {{ }}
Установим для title и заголовка h1 в обоих шаблонах -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> {{ title }} </title>
</head>
<body>
    <h1> {{ title }} </h1>
</body>
</html>

<!-- И при передаче шаблона установим значение параметра title -->

@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return render_template('index.html', title='Главная страница')  # Возвращает HTML-шаблон с именем 'index.html' и переменной title в параметрах


@app.route('/about')  # Декоратор, который связывает URL со функцией. По адресу '/about' будет вызываться функция about
def about():
    return render_template('about.html', title='О нас')  # Возвращает HTML-шаблон с именем 'about.html' и переменной title в параметрах

<!-- Передадим список в шаблон. Выражения в шаблонах помещаются в {% %}. В конце обязательно закрытие выражения {% end... %} -->

</head>
<body>
    <ul>
        {% for m in menu %}
        <li>{{m}}</li>
        {% endfor %}
    </ul>
    <h1> {{ title }} </h1>
</body>
</html>

<!-- В коде пропишем этот список menu и укажем его так же при передаче шаблона. Укажем новый параметр menu и передадим в него наш список -->

menu = ['Главная', 'О нас', 'Контакты']

@app.route('/')  # Декоратор, который связывает URL со функцией. По адресу '/' будет вызываться функция index
def index():
    return render_template('index.html', title='Главная страница', menu=menu)

<!-- Немного усложним. Добавим условие if. Если передаем параметр title в обработчик - получаем Первый сайт - {{ title }}.
Если title не передается, то просто пишется заранее подготовленный текст "Первый сайт" -->

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% if title %}
        <title>Первый сайт - {{ title }}</title>
    {% else %}
        <title>Первый сайт</title>
    {% endif %}
</head>

<!-- Примерно тоже самое сделаем для body -->

<body>
    <ul>
        {% for m in menu %}
        <li>{{m}}</li>
        {% endfor %}
    </ul>
    {% if title %}
        <h1>{{ title }}</h1>
    {% else %}
        <h1>Первый сайт - Главная страница</h1>
    {% endif %}    
</body>

<!-- Тоже самое делаем для about -->

<!-- Делаем БАЗОВЫЙ шаблон base.html. Он содержит основную информацию, для предотвращения повторений ее в коде других страниц 
Все разбивается на блоки, которые потом будут заполняться или останутся с тем что задано, если этот блок не указан в определенном шаблоне-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% block title %}
    {% if title %}
        <title>Первый сайт - {{ title }}</title>
    {% else %}
        <title>Первый сайт</title>
    {% endif %}
    {% endblock title %}
</head>
<body>
    {% block content %}
    {% block mainmenu %}
    <ul>        
        {% for m in menu %}
        <li>{{m}}</li>
        {% endfor %}
    </ul>
    {% endblock mainmenu %}
    {% if title %}
        <h1>{{ title }}</h1>
    {% else %}
        <h1>Первый сайт - Главная страница</h1>
    {% endif %}   
    {% endblock content %} 
</body>
</html>

<!-- Перепишем шаблон index. Благодаря super() отображает то что было в базовом шаблоне, а не просто заменяет содержимым блока content) -->

{% extends "base.html" %}

{% block content %}
{{ super() }}
<p>Cодержимое главной страницы</p>
{% endblock content %}

<!-- Перепишем шаблон about -->

{% extends "base.html" %}

{% block content %}
{{ super() }}
<p>Cодержимое страницы о нас</p>
{% endblock content %}











