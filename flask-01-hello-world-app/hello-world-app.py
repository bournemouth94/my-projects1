from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "hello world from Sibel"

@app.route('/second')
def second():
    return "bize her yer Londra"

@app.route('/third/subthird')
def third():
    return "this is subpage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f"id number of this page is {id}"



    
if __name__ == '__main__':
    app.run(debug=True, port=2000)



