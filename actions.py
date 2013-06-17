#encoding: utf-8
from flask import render_template
from tournament_organizer.base_definitions import Game, Tournament
from tournament_organizer.table_tournament import TableTournament

def game(gid):
	if gid == '':
		return render_template('game_index.jade', games = Game.objects)
	else: 
		selected_game = Game.objects(id=gid).first()
		if len(selected_game) == 0:
			return redirect(url_for('game'))
		return render_template('game_admin.jade', game = selected_game)

def tournament(tid):
	if tid == '':
		return render_template('tournament_index.jade',
		 ts = Tournament.objects)
	else: 
		return render_template('tournament_admin.jade',
		 t = Tournament.objects(id=tid).first())

def new_game():
	return render_template('game_admin.jade', game = None)
	
def add_game(gamedata):
	return 'bueno, chau'
	
