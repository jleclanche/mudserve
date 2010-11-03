class CombatantHandler(object):
	"""
	Proxies a combatant in order to provide a richer set of methods as well
	as providing a history of what has been done in order to correctly
	update the history and provide for instance combat log messages.
	"""
	
	def __init__(self, combatant):
		self.combatant = combatant
		self.log = {
			'damage': 0,
			'healing': 0,
			'auras': []
		}
		
	def damage(self, amount):
		"""
		Damages the combatant by a specific amount.
		"""
		
		# Can't have negative health
		self.combatant.health = max(self.combatant.health-amount, 0)
		self.log['damage'] += amount
	
	def heal(self, amount):
		"""
		Heals the combatant by a specific amount, provided they are not dead.
		"""
		
		# Make sure the combatant is alive; can't heal dead people
		# (although they are certainly visible)
		if self.is_alive():
			self.combatant.health += amount
			self.log['healing'] += amount
			
	def apply_aura(self, aura):
		"""
		Apply an aura on the combatant.
		TODO: Should it require the combatant being alive?
		"""
		
		#self.combatant.auras.append(aura)
		#self.log['auras'].append(aura)
		pass # NYI
	
	def is_alive(self):
		return self.combatant.health > 0
