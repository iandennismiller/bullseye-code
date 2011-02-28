import os
from bottle import route, run, static_file, post

path = "/tmp"

@route('/')
@route('/index.html')
def index():
    return static_file("index.html", root=os.path.join(path, "usr", "public"))

@route('/favicon.ico')
def index():
    return static_file("favicon.ico", root=os.path.join(path, "usr", "public"))

@route('/static/:filename#.+#')
def server_static(filename):
    return static_file(filename, root=os.path.join(path, "usr", "public"))

@route('/images/:filename#.+#')
def server_static(filename):
    return static_file(filename, root=os.path.join(path, "usr", "images"))

#@post('/')

def go(host, port, new_path):
    global path
    path = new_path
    run(host=host, port=port, reloader=True)
