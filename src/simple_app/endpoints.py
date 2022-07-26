from flask import request,render_template
import pymongo

def api_routes(endpoints):
    @endpoints.route('/registration', methods=['GET'])
    def login():
        return render_template("index.html")

    @endpoints.route('/data', methods=["GET", "POST"])
    def data():
        uri = "mongodb+srv://admin:admin@cluster0.ey1zthd.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        database = client['Register_USER']
        collection = database['users']
        data = {}
        if request.method == "POST":
            data['email'] = request.form['email']
            data['name'] = request.form['name']
            data['pass'] = request.form['pass']
            collection.insert_one(data)
        return render_template("success.html")

    return endpoints