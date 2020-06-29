from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import requests

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")

@app.route("/about.html")
def form():
	return render_template("about.html")

#@app.route("/courses.html")
#def courses():
	#return render_template("courses.html")

@app.route("/course-details-python1.html")
def course_details_python1():
	return render_template("course-details-python1.html")

@app.route("/course-details-python2.html")
def course_details_python2():
	return render_template("course-details-python2.html")

@app.route("/course-details-python3.html")
def course_details_python3():
	return render_template("course-details-python3.html")

@app.route("/course-details-biomed.html")
def course_details_biomed():
	return render_template("course-details-biomed.html")

@app.route("/course-details-java1.html")
def course_details_java1():
	return render_template("course-details-java1.html")

@app.route("/course-details-c1.html")
def course_details_c1():
	return render_template("course-details-c1.html")

@app.route("/course-details-scratch.html")
def course_details_scratch():
	return render_template("course-details-scratch.html")

@app.route("/course-details-web1.html")
def course_details_web1():
	return render_template("course-details-web1.html")

@app.route("/contacts.html")
def register():
	return render_template("contacts.html")

@app.route("/elements.html")
def elements():
	return render_template("elements.html")

#@app.route("/blog-home.html")
#def blog_home():
	#return render_template("blog-home.html")

#@app.route("/blog-single.html")
#def blog_single():
	#return render_template("blog-single.html")

if __name__ == '__main__':
	app.run(debug=True)
