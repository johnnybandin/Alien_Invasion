# The settings for the game alien invasion
class Settings:
	"""A class to store all the settings"""

	def __init__(self):
		"""Initialize the game's setting"""
		# screen settings
		self.screen_width = 1800
		self.screen_height = 800
		self.bg_color = (3, 252, 252)
		self.ship_speed = 1.5

		# Bullet settings 
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3