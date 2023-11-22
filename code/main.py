import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# Setup Geral
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# Sons 
		pygame.mixer.init()
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		fade_alpha = 0
		fade_speed = 3
		font = pygame.font.Font(None, 36)

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()

			if self.level.player.is_dead():
				fade_alpha += fade_speed
				if fade_alpha > 255:
					fade_alpha = 255

				message_text = "Game Over! Press any key to restart."
				message_surface = font.render(message_text, True, (255, 255, 255))
				self.screen.fill((0, 0, 0))  # Fill with black
				message_surface.set_alpha(fade_alpha)

				self.screen.blit(
					message_surface,
					(WIDTH // 2 - message_surface.get_width() // 2, HEIGHT // 2 - message_surface.get_height() // 2)
				)

				keys = pygame.key.get_pressed()
				if any(keys):
					# If any key is pressed, reset the fading parameters and restart the game
					self.level = Level()
					fade_alpha = 0

if __name__ == '__main__':
	game = Game()
	game.run()