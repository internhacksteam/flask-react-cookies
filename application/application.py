from flask import (Flask, render_template, make_response, request)

application = Flask(__name__)

application.add_url_rule('/','index',(lambda: render_template("index.html",flask_token="Hellow World")))

def my_index():
	return render_template("index.html", flask_token="Hello World")

#response to attach cookies to (essentially returning a string)
#you can buiild your response ahead of time and modify before returning it 
@application.route("/cookies")
def cookies():
	resp = make_response("Cookies")
	#Setting a cookie that has key flavor and the value of chocolate chip
	resp.set_cookie("flavor","chocolate chip")
	return resp

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run()
