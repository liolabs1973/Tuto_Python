import pygame
from game import Game

pygame.init()

#generer la fenetre de notre jeu
pygame.display.set_caption("Commet Fall Game By Liolabs1973")
screen = pygame.display.set_mode((1080,720))

# charger notre arriere plan
background = pygame.image.load('Assets/bg.jpg')

# frequence d'affichage à 120
fps = 120
clock = pygame.time.Clock()

# charger notre jeu
game = Game()

running = True

#boucle infinie
while running:
    
    # appliquer l'arriere plan
    screen.blit(background, (0,-200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect) 

    # actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    # recuperer les monstres du jeu

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)    

    # applique l'ensemble des images de projectiles
    game.player.all_projectiles.draw(screen) 

    # applique l'ensemble des images de monstres
    game.all_monsters.draw(screen)

    # verifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left() 
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right() 

    # mettre à jour l'écran
    pygame.display.flip()
    
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #détecter si un joueur lache un touche du clavier
        elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                # detecter si la touche espace est enclenchée
                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

    clock.tick(fps)