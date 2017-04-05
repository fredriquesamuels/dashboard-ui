CARD_NAME = ""
CARD_STARS = '[[Level]]/[[Rank]]'
CARD_ATK = '[[ATK]]'
CARD_DEF = '[[DEF]]'
CARD_TYPE = '[[Type]]'
CARD_PEN_EFF = '[[Pendulum Effect]]'
CARD_JAP_NAME = 'Japanese name'
CARD_PASSCODE = '[[Passcode]]'
CARD_PRI_TYPE = 'Primary type'
CARD_SEC_TYPE = 'Secondary type'
CARD_ATTR = '[[Attribute]]'
CARD_LORE = '[[Lore]]'
CARD_PEN_SCALE = 'Pendulum Scale'
CARD_IMAGE = 'Card image'
CARD_RIT_SP_REQ = 'Ritual Spell Card required'
CARD_MAT_REQ = 'Materials'
CARD_RIT_MON_REQ = 'Ritual Monster required'
CARD_FUS_MAT_REQ = 'Fusion Material'
CARD_PROPERTY = 'Property'

class NameTransformer:
	def get(self, f):
		return f[CARD_NAME][0]

class StarsTransformer:
	def get(self, f):
		return f[CARD_STARS][0]

class AtkTransformer:
	def get(self, f):
		return f[CARD_ATK][0]
