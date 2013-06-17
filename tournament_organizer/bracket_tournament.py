from base_definitions import * 

class Bracket(EmbeddedDocument):
	number = IntField()
	matches = ListField(EmbeddedDocumentField(Match))

class BracketTournament(Tournament):
	score_to_qualify = IntField()
	current_bracket = IntField()
	matcheslist = ListField(EmbeddedDocumentField(Bracket))
