# # Using flask to make an api 
# # import necessary libraries and functions 
# from flask import Flask, jsonify, request 

# # creating a Flask app 
# app = Flask(__name__) 

# # on the terminal type: curl http://127.0.0.1:5000/ 
# # returns hello world when we use GET. 
# # returns the data that we send when we use POST. 
# @app.route('/', methods = ['GET', 'POST']) 
# def home(): 
# 	if(request.method == 'GET'): 

# 		data = "hello world"
# 		return jsonify({'data': data}) 


# # A simple function to calculate the square of a number 
# # the number to be squared is sent in the URL when we use GET 
# # on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# # this returns 100 (square of 10) 
# @app.route('/home/<int:num>', methods = ['GET']) 
# def disp(num): 

# 	return jsonify({'data': num**2}) 


# # driver function 
# if __name__ == '__main__': 

# 	app.run(debug = True) 

# app.py

from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)