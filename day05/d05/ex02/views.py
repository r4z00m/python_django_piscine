import psycopg2
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


def db_init(request):
    try:
        db = settings.DATABASES['default']
        connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                                   host=db['HOST'], port=db['PORT'])
        with connect.cursor() as db_connect:
            db_connect.execute("CREATE TABLE IF NOT EXISTS ex02_movies (episode_nb INT PRIMARY KEY, "
                               "title VARCHAR(64) UNIQUE NOT NULL, director VARCHAR(32) NOT NULL, "
                               "producer VARCHAR(128) NOT NULL, release_date DATE NOT NULL);")
            connect.commit()
            connect.close()
            return HttpResponse("Ok")
    except Exception as e:
        return HttpResponse(e)


def populate(request):
    db = settings.DATABASES['default']
    connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                               host=db['HOST'], port=db['PORT'])
    movies = [
        {
            'episode_nb': 1,
            'title': 'The Phatom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
        }, {
            'episode_nb': 2,
            'title': 'Attack of th Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16',
        }, {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19',
        }, {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25',
        }, {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17',
        }, {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25',
        }, {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J.J. Abrams',
            'producer': 'Kathleen Kennedy, J.J. Abrams, Bryan Burk',
            'release_date': '2015-12-11',
        },
    ]
    count = 0
    try:
        with connect.cursor() as db_connect:
            for elem in movies:
                db_connect.execute(f"SELECT title FROM ex02_movies WHERE episode_nb={elem['episode_nb']};")
                if db_connect.fetchone():
                    continue
                db_connect.execute(f"INSERT INTO ex02_movies "
                                   f"(episode_nb, title, director, producer, release_date) "
                                   f"VALUES ({elem['episode_nb']}, '{elem['title']}', "
                                   f"'{elem['director']}', '{elem['producer']}', '{elem['release_date']}');")
                count += 1
            connect.commit()
            connect.close()
        if count == 0:
            return HttpResponse("Nothing to add")
        return HttpResponse("Ok " * count)
    except Exception as e:
        return HttpResponse(e)


def display(request):
    db = settings.DATABASES['default']
    connect = psycopg2.connect(dbname=db['NAME'], user=db['USER'], password=db['PASSWORD'],
                               host=db['HOST'], port=db['PORT'])
    try:
        with connect.cursor() as db_connect:
            db_connect.execute("SELECT * FROM ex02_movies;")
            data = db_connect.fetchall()
            connect.close()
            if len(data) == 0:
                return HttpResponse("No data available")
            return render(request, 'ex02/display.html', context={'data': data})
    except Exception as e:
        return HttpResponse("No data available")



