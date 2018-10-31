from flask import Flask, render_template, abort
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

class Article(object):

	def __init__(self, path):
		with open(path, 'r') as f:
			self.data = json.load(f)

	@property
	def title(self):
		return self.data['title']

	@property 
	def created_time(self):
		return self.data['created_time']

	@property 
	def content(self):
		return self.data['content']


def get_all_article(path):
	article_table = []
	for root, dirs, files in os.walk(path):
		for filename in files:
			path = root + filename
			article = Article(path)
			article_table.append(article)
	return article_table

@app.route('/')
def index():
	article_table = get_all_article('../files/')
	return render_template('index.html', article_table=article_table)

@app.route('/files/<filename>')
def file(filename):
	file_path = '../files/' + filename + '.json'
	if os.path.isfile(file_path):
		article = Article(file_path)
		return render_template('file.html', article=article)
	else:
		abort(404)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404