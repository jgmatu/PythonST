#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import flask
import json

POST = [ {"userId" : 1 ,
          "id" : 1 ,
          "title" : "sunt aut facere repellat provident occaecati excepturi optio reprehenderit" ,
          "body" :  "quia et suscipit\n \
           suscipit recusandae consequuntur expedita et cum \n  \
           reprehenderit molestiae ut ut quas totam\n \
           nostrum rerum est autem sunt rem eveniet architecto"
         }
         ,
         {
            "userId" : 1,
            "id" : 2,
            "title" : "qui est esse" ,
            "body" :    "est rerum tempore vitae\n \
             sequi sint nihil reprehenderit dolor beatae ea dolores neque\n \
             fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\n \
             qui aperiam non debitis possimus qui neque nisi nulla"
         }
         ,
         {
            "userId": 1,
            "id": 3,
            "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
            "body" : "et iusto sed quo iure\n \
             voluptatem occaecati omnis eligendi aut ad\n \
             voluptatem doloribus vel accusantium quis pariatur\n \
             molestiae porro eius odio et labore et velit aut"
         }
         ,
         {
            "userId": 1,
            "id": 4,
            "title": "eum et est occaecati",
            "body": "ullam et saepe reiciendis voluptatem adipisci\n \
             sit amet autem assumenda provident rerum culpa\n \
             quis hic commodi nesciunt rem tenetur doloremque ipsam iure\n \
             quis sunt voluptatem rerum illo velit"
         },
         {
            "userId": 1,
            "id": 5,
            "title": "nesciunt quas odio",
            "body": "repudiandae veniam quaerat sunt sed\n \
             alias aut fugiat sit autem sed est\n \
             voluptatem omnis possimus esse voluptatibus quis\n \
             est aut tenetur dolor neque"
         }
         ,
         {
            "userId": 1,
            "id": 6,
            "title": "dolorem eum magni eos aperiam quia",
            "body": "ut aspernatur corporis harum nihil quis provident sequi\n \
             mollitia nobis aliquid molestiae\n \
             perspiciatis et ea nemo ab reprehenderit accusantium quas\n \
             voluptate dolores velit et doloremque molestiae"
         }
         ,
         {
            "userId": 1,
            "id": 7,
            "title": "magnam facilis autem",
            "body": "dolore placeat quibusdam ea quo vitae\n \
             magni quis enim qui quis quo nemo aut saepe\n \
             quidem repellat excepturi ut quia\n \
             sunt ut sequi eos ea sed quas"
         }
         ,
         {
            "userId": 1,
            "id": 8,
            "title": "dolorem dolore est ipsam",
            "body": "dignissimos aperiam dolorem qui eum\n \
             facilis quibusdam animi sint suscipit qui sint possimus cum\n \
             quaerat magni maiores excepturi\n \
             ipsam ut commodi dolor voluptatum modi aut vitae"
         }
         ,
         {
            "userId": 1,
            "id": 9,
            "title": "nesciunt iure omnis dolorem tempora et accusantium",
            "body": "consectetur animi nesciunt iure dolore\n  \
             enim quia ad\n  \
             veniam autem ut quam aut nobis\n \
             et est aut quod aut provident voluptas autem voluptas"
         }
         ,
         {
            "userId": 1,
            "id": 10,
            "title": "optio molestias id quia eum",
            "body": "quo et expedita modi cum officia vel magni\n \
             doloribus qui repudiandae\n \
             vero nisi sit\n \
             quos veniam quod sed accusamus veritatis error"
         }
         ,
         {
            "userId": 2,
            "id": 11,
            "title": "et ea vero quia laudantium autem",
            "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\n \
             accusamus in eum beatae sit\n \
             vel qui neque voluptates ut commodi qui incidunt\n \
             ut animi commodi"
         }
         ,
         {
            "userId": 2,
            "id": 12,
            "title": "in quibusdam tempore odit est dolorem",
            "body": "itaque id aut magnam\n \
             praesentium quia et ea odit et ea voluptas et\n \
             sapiente quia nihil amet occaecati quia id voluptatem\n \
             incidunt ea est distinctio odio"
         }
         ,
         {
            "userId": 2,
            "id": 13,
            "title": "dolorum ut in voluptas mollitia et saepe quo animi",
            "body": "aut dicta possimus sint mollitia voluptas commodi quo doloremque\n \
             iste corrupti reiciendis voluptatem eius rerum\n \
             sit cumque quod eligendi laborum minima\n \
             perferendis recusandae assumenda consectetur porro architecto ipsum ipsam"
         }
    ]


USERS = [
        {
             "id": 1,
             "name": "Leanne Graham",
             "username": "Bret",
             "email": "Sincere@april.biz",
             "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                 }
             },
             "phone": "1-770-736-8031 x56442",
             "website": "hildegard.org",
             "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "address": {
                "street": "Victor Plains",
                "suite": "Suite 879",
                "city": "Wisokyburgh",
                "zipcode": "90566-7771",
                "geo": {
                    "lat": "-43.9509",
                    "lng": "-34.4618"
                }
            },
            "phone": "010-692-6593 x09125",
            "website": "anastasia.net",
            "company": {
                "name": "Deckow-Crist",
                "catchPhrase": "Proactive didactic contingency",
                "bs": "synergize scalable supply-chains"
            }
        },

        {
            "id": 3,
            "name": "Clementine Bauch",
            "username": "Samantha",
            "email": "Nathan@yesenia.net",
            "address": {
                "street": "Douglas Extension",
                "suite": "Suite 847",
                "city": "McKenziehaven",
                "zipcode": "59590-4157",
                "geo": {
                    "lat": "-68.6102",
                    "lng": "-47.0653"
                }
            },
            "phone": "1-463-123-4447",
            "website": "ramiro.info",
            "company": {
                "name": "Romaguera-Jacobson",
                "catchPhrase": "Face to face bifurcated interface",
                "bs": "e-enable strategic applications"
            }
        },

        {
            "id": 4,
            "name": "Patricia Lebsack",
            "username": "Karianne",
            "email": "Julianne.OConner@kory.org",
            "address": {
                "street": "Hoeger Mall",
                "suite": "Apt. 692",
                "city": "South Elvis",
                "zipcode": "53919-4257",
                "geo": {
                    "lat": "29.4572",
                    "lng": "-164.2990"
                }
            }
        }
    ]


app = flask.Flask(__name__)

@app.route('/')
def index () :
    return "Hello World"


@app.route('/posts/1')
def post1 () :
    return json.dumps(POST[0])


@app.route('/posts/2')
def post2 () :
    return json.dumps(POST[1])


@app.route('/posts/3')
def post3 () :
    return json.dumps(POST[2])


@app.route('/posts')
def post () :
    return json.dumps(POST)


@app.route('/users')
def users () :
    return json.dumps(USERS)


if __name__ == "__main__" :
    app.run(debug=True)
