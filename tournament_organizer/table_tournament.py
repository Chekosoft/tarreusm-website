from base_definitions import *

class ContestantPosition(EmbeddedDocument):
	contestant = ListField(ReferenceField(Contestant))
	total_points = IntField()

class TableTournament(Tournament):
	score_for_winner = IntField()
	score_for_loser = IntField()
	score_for_tie = IntField()

	position_table = ListField(EmbeddedDocumentField(ContestantPosition))
	matches_list = ListField(EmbeddedDocumentField(Match))
