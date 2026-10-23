from livereload import Server


def rebuild():
    print(r"Сервер http://127.0.0.1:35729/ обновлен!")


server = Server()
server.watch('index.html', rebuild)
server.serve(root='.')