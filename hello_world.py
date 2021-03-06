import bottle

@bottle.route('/')
def home_page():
    mythings = ['red', 'blue', 'green', 'purple']
    return bottle.template('hello_world', username='Perry', things=mythings)
    # return 'hello_world\n'

@bottle.route('/testpage')
def test_page():
    return 'this is a test page'

@bottle.route('/favorite_color', method=["POST", "GET"])
def favorite_color():
    color = bottle.request.forms.get('color')
    if color is None or color == "":
        color = 'No Color Selected'

    bottle.response.set_cookie('color', color)
    bottle.redirect("/show_color")
    # return bottle.template('favorite_color.tpl', color=color)

@bottle.route('/show_color')
def show_color():
    color = bottle.request.get_cookie("color")

    return bottle.template('show_color', color=color)

bottle.debug(True)
bottle.run(host='localhost', port=8081)

