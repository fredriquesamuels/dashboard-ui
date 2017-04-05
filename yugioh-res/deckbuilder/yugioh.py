import os
import sys
sys.path += ["libs"]


import itertools
import math

# print len(list(itertools.permutations(range(40), 5)))
print math.factorial(40)/(math.factorial(35)*math.factorial(5))


ACTION_ACTIVATED="ACTION_ACTIVATED"
ACTION_RESOLVED="ACTION_RESOLVED"

EFFECT="EFFECT"
NORMAL_SUMMON="NORMAL_SUMMON"


class ActionTransport:
	def __init__(self, action, type):
		self.action = action
		self.type = type
	def onResolving(self):
		return self.type==ACTION_RESOLVED
	def onActivated(self):
		return self.type==ACTION_ACTIVATED


class ACTION_TRIGGERS:
	@staticmethod
	def monsterNormalSummoned(action, duelQuery):
		b1 = action.onResolving()
		b2 = action.action.type==NORMAL_SUMMON
		return b1 and b2

class DuelEntity:
	def __init__(self):
		self.duelId = 0
	def getTriggerActions(self, action, duel):return []

class DuelAction:
	def __init__(self, **kargs):
		self.parent = self.getArg(kargs,'parent')
		self.type = self.getArg(kargs,'type')
		self.entity = self.getArg(kargs,'entity')
		self.args = kargs
		self.activateCallback = self.getArg(kargs,'activateCallback')
		self.resolveCallback = self.getArg(kargs,'resolveCallback')
		self.negated = False
	def getArg(self, m, k):
		if(k in m):return m[k]
	def __str__(self):
		return "<%s>"  % (self.type)
	def activate(self, duel):
		duel.logger.activating(self)
		if(self.activateCallback):
			self.activateCallback(self, duel)
			return True
		return False
	def resolve(self, duel):
		duel.logger.resolving(self)
		if(self.resolveCallback):
			self.resolveCallback(self, duel)
			return True
		return False

class DuelQuery:
	@staticmethod
	def monsterNormalSummoned(action, duelQuery):
		b1 = action.onResolving()
		b2 = action.action.type==NORMAL_SUMMON
		return b1 and b2

class DuelModify:

	def __init__(self, duel):
		self.duel = duel
	def negate(action):
		action.negated=True


	class NormalSummon (DuelAction):
		def __init__(self, entity):
			DuelAction.__init__(self,
				type=NORMAL_SUMMON,
				entity=entity,
				resolveFunc=self.summon)
		def summon(self, d):pass
	def normalSummon(self, entity):
		self.duel.execute(DuelModify.NormalSummon(entity))

class AbstractLogger:
	def activating(self, action):
		print 'Activating', action
	def resolving(self, action):
		print 'Resolving', action

class Player:
	def select(duel, options, params):
		print 'Player Selecting from ', options, params
		return options[0]

class YugiohDuel:
	def __init__(self, player1, player2, entities, logger=AbstractLogger()):
		self.players = [player1, player2]
		self.entities = entities
		self.logger = logger
	def modify(self):return DuelModify(self)
	def query(self):return DuelQuery()
	def execute(self, action):
		if(action.activate(self)):
			self.checkForActionResponses(ActionTransport(action, ACTION_ACTIVATED))
		if(not action.negated):
			action.resolve(self)
			self.checkForActionResponses(ActionTransport(action, ACTION_RESOLVED))

	def triggerEffects(self, action):
		triggerActions = []
		for e in self.entities:
			triggerActions += e.getTriggerActions(action, self.query())
		for e in triggerActions:
			execute(e)
	def chainEffects(self, action):pass
	def resolveEffects(self):pass
	def checkForActionResponses(self, action):
		pass
		# self.triggerEffects(action)
		# self.chainEffects(action)
		# self.resolveEffects()

if __name__ == '__main__':

	class TestCard (DuelEntity):
		pass

	class EntityTriggersOnNormalSummonSuccess(DuelEntity):
		class OnSummonEffect(DuelAction):
			def __init__(self, entity):
				DuelAction.__init__(self,
					type="OnSummonEffect",
					entity=entity,
					resolveFunc=self.do)
			def do():print self

		def getTriggerActions(self, action, duel):
			if DuelQuery.monsterNormalSummoned(action, duel):
				return []

	monster1 = TestCard()
	trap1 = EntityTriggersOnNormalSummonSuccess()

	duel = YugiohDuel(Player(), Player(), [monster1, trap1])
	duel.modify().normalSummon(monster1)
