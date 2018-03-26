#! /usr/bin/env python3
import json,os
from flask import Flask,render_template,abort
app=Flask(__name__)
@app.route('/')
def index():
	files_path='/home/feifei/Desktop/shiyanlou/files'
	title_list=[]
	for f in os.listdir(files_path):
		if ".json" in f:
			ff=os.path.join(files_path,f)
			with open(ff,"r") as file:
				main_contents=(json.loads(file.read()))
				title_list.append(main_contents.get('title'))
	#main_contents="www"
	return render_template('index.html',main_contents=title_list)

@app.route('/files/<filename>')
def file(filename):
	files_path='/home/feifei/Desktop/shiyanlou/files/'
	f_last=files_path+filename+'.json'
	try:
		with open(f_last,'r') as f:
			t=f.read()
			return render_template('file.html',filename=t)
	except:
		abort(404)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404