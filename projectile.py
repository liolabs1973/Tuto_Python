import pygame

#definir la classe qui gerera les projectiles du joueur

class Projectile(pygame.sprite.Sprite):
    # definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load('Assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y +  80
        self.origine_image = self.image
        self.angle = 0  


    def rotate(self):
        # tourner le projectile
        self.angle += 2 
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
         self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            
            #infliger des dégats
            monster.damage(self.player.attack)

        # vérifier si notre projectile est sorti de l'écran
        if self.rect.x > 1080:
            # le supprimer de la liste des projectiles
            self.remove()