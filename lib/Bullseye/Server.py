from __future__ import with_statement
import os, json, shutil, glob
from bottle import route, run, static_file, post, get, request

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

@post('/rpc/store_data')
def store_data():
    data = request.forms.get('data')
    id = request.forms.get('id')
    with open(os.path.join(path, "usr", "csv", "bullseye.csv"), "a") as f:
        f.write(id + "\t" + data + "\n")
    src = os.path.join(path, "usr", "images", "%s.png" % id)
    dst = os.path.join(path, "usr", "processed")
    shutil.move(src, dst)

@get('/rpc/next_image')
def next_image():
    files = glob.glob(os.path.join(path, "usr", "images", "*.png"))
    if files:
        filename = os.path.basename(files[0])
        return json.dumps({
            "filename": "/images/" + filename,
            "id": os.path.splitext(filename)[0]
        })
    else:
        return "{}"

def go(host, port, new_path):
    global path
    path = new_path
    run(host=host, port=port, reloader=True)
