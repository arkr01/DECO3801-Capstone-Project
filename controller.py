from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    name = "example"
    if 'x-kvd-payload' in request.headers:
        userjson = request.headers['x-kvd-payload']
        user = json.loads(userjson)
        name = user['user']
    name = "test"
    return render_template('example.html',title='welcome', name=name)


@app.route('/foobar')
def foobar():
    return "<span style='color:blue'>Hello again!</span>"

# Caleb DMZ =====

# Webpage for github webhook
@app.route('/githook')
def githook():
    secret = request.headers['X-Hub-Signature']
    parsed = json.loads(request.json)
    with open('/home/s4585694/hook','w') as handle:
        handle.write(json.dumps(parsed, indent=4, sort_keys=True))
    return render_template('errors/error_404.html')
    #return render_template('errors/error_404.html');

# Caleb DMZ =====

@app.route("/jason_test")
def jtest():
    return render_template("base.html", title="This is a test page")

@app.route("/matthew_test")
def cool_fun():
    return render_template("matthew_wuz_here.html", test=name=="s4582166", user=name)


@app.route("/kyle_test")
def sexy_asian():
    name = "Kyle Macaskill"
    return render_template("kyle_is_really_funny.html", name=name, title = "Kyle")

@app.route("/kyle_second")
def second_page():
    name = "Kyle Macaskill"
    return render_template("kyle_second_page.html", name = name, title = "Second")