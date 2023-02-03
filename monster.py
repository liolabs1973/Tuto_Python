import pygame
import random

# Creation de la classe Monstre
class Monster(pygame.sprite.Sprite):
    
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxhealth = 100
        self.attack = 0.3
        self.image = pygame.image.load('Assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(2,5)

    def damage(self, amount):
        # infliger les dégats
        self.health -= amount

        # verifier si il reste en vie
        if self.health <= 0:
            # respawn comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(2, 5)
            self.health = self.maxhealth

    def update_health_bar(self, surface):
        # dessiner notre gauge de vie
        pygame.draw.rect(surface,(60, 63, 60),[self.rect.x + 10 , self.rect.y - 20, self.maxhealth, 5])
        pygame.draw.rect(surface,(111, 210, 46),[self.rect.x + 10 , self.rect.y - 20, self.health, 5])


    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collisions avec le joueur
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)

        
