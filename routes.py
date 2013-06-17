from flask import render_template, redirect, url_for, request
from starter import app
import actions

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.jade')

@app.route('/game/')
@app.route('/game/<gid>')
def game(gid = ''):
	return actions.game(gid)

@app.route('/game/<gid>/modify', methods='POST')
def game_modify(gid = ''):
	return 'Holi'

@app.route('/game/new', methods=['GET', 'POST'])
def new_game():
	if request.method == 'GET':
		return actions.new_game()
	else:
		return actions.add_game(request.form)

@app.route('/tournament/')
@app.route('/tournament/<tid>')
def tournament(tid = ''):
	return actions.tournament(tid)
