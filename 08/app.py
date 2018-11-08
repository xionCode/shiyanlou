from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

client = MongoClient('127.0.0.1', 27017)
mongodb = client.shiyanlou

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Category: %r>' % self.name

class File(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))
	content = db.Column(db.Text)

	def __init__(self, title, created_time, category, content):
		self.title = title
		self.created_time = created_time
		self.category = category
		self.content = content

	def __repr__(self):
		return '<File: %r> ' %self.title

	def add_tag(self, tag_name):

		# if tag_name in tags:
		mongodb.tags.insert_one({'tag': tag_name})

	@property 
	def tags(self):
		tag_list = []
		for i in mongodb.tags.find():
			tag_list.append(i['tag'])
		return tag_list


@app.route('/')
def index():
	dct = {}
	files = db.session.query(File).all()
	for f in files:
		category = db.session.query(Category).filter(Category.id==f.category_id).first()
		dct[f.title] = category.name
	return render_template('index.html', category_dct=dct)

@app.route('/files/<filename>')
def file(filename):
	category = db.session.query(Category).filter(Category.name==filename).first()
	if(category):
		file1 = db.session.query(File).filter(File.category_id==category.id).first()
		return render_template('file.html', file1=file1)
	else:
		abort(404)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404