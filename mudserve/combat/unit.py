"""
Unit logic, for targets in a combat
"""

class UnitHandler(object):
	"""
	Proxies a unit in order to provide a richer set of methods as well
	as providing a history of what has been done in order to correctly
	update the history and provide for instance combat log messages.
	"""
	
	def __init__(self, unit):
		self.unit = unit
		self.log = {
			"damage": 0,
			"healing": 0,
			"auras": []
		}
		
	def damage(self, amount):
		"""
		Damages the unit by a specific amount.
		"""
		
		# Can't have negative health
		self.unit.health = max(self.unit.health-amount, 0)
		self.log["damage"] += amount
	
	def heal(self, amount):
		"""
		Heals the unit by a specific amount, provided they are not dead.
		"""
		
		# Make sure the unit is alive; can't heal dead people
		# (although they are certainly visible)
		if self.is_alive():
			self.unit.health += amount
			self.log["healing"] += amount
			
	def apply_aura(self, aura):
		"""
		Apply an aura on the unit.
		TODO: Should it require the unit being alive?
		"""
		
		#self.unit.auras.append(aura)
		#self.log['auras'].append(aura)
		pass # NYI
	
	def is_alive(self):
		return self.unit.health > 0
