from mongoengine import *

class Game(Document):
	name = StringField(required = True)	
	players_min = IntField(required = True)
	players_max = IntField(required = True)

	def is_multiplayer(self):
		return True if self.players_max > 1 or self.players_min > 1 else False

class Tournament(Document):
	name = StringField(required = True)
	game = ReferenceField(Game)

	date_from = DateTimeField()
	date_to = DateTimeField()

	inscription_start = DateTimeField()
	inscription_end = DateTimeField()
	contestants_max = IntField()

	meta = {'allow_inheritance': True}


class Contestant(Document):
	name = StringField(required = True)
	game = ReferenceField(Game)
	tournament = ReferenceField(Tournament)

	meta = {'allow_inheritance': True}

class Team(Contestant):
	members = ListField(StringField)
	captain_email = EmailField()

class Player(Contestant):
	real_name = StringField(required = True)
	email = EmailField(required = True)

class Match(EmbeddedDocument):
	home = ReferenceField(Contestant)
	away = ReferenceField(Contestant)

	tournament = ReferenceField(Tournament)

	home_result = IntField()
	away_result = IntField()

	match_date = DateTimeField()

	meta = {'allow_inheritance': True}

	def get_winner(self):
		if self.home_result > self.away_result:
			return self.home
		elif self.away_result > self.home_result:
			return self.away
		else: 
			return None
