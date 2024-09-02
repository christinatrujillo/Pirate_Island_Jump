import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI

class Game:
	def __init__(self):
		# game attributes
		self.max_level = 5
		self.max_health = 100
		self.curr_health = 100
		self.coins = 0

		# sound
		self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

		# overworld creation
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.overworld_bg_music.set_volume(0.04)

		# ui instance
		self.ui = UI(screen)

	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld, self.change_coins, self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops = -1)
		self.level_bg_music.set_volume(0.04)

	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		
		# Reset player's health to max health when finishing a level
		self.curr_health = self.max_health
		
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def change_coins(self, amount):
		self.coins += amount

	def change_health(self, amount):
		self.curr_health += amount

		# checks that current health doesn't exceed max health
		if self.curr_health > self.max_health:
			self.curr_health = self.max_health

	def check_game_over(self):
		if self.curr_health <= 0:
			self.curr_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.max_level,screen,self.create_level)
			self.status = 'overworld'
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops = -1)

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
			self.ui.show_health(self.curr_health, self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()
		
		
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('green')
    game.run()

    pygame.display.update()
    clock.tick(60)