from pymongo.collection import Collection

class FormValidationRepository:
	def __init__(self, c: Collection):
		self.cl = c

	def get_forms(self) -> list:
		return list(self.cl.find())
