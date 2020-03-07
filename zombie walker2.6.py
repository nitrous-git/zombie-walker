import pygame
import math, sys
import random

######################################################################################################
# This is a Zombie Walker Demo v1.4 inspired by the mouse shooting script. Using vector and list.
#
#  update 2.x : - Shooting collision with Zombie /x
#               - HP player/ Zombie System /x
#               - Random HP pickups     
#               - Game Over/ Restart scene /Higscore Ranking 
#               - Keydown shooting event, Next level Scenes .... /x
######################################################################################################

pygame.init()

####   R G B
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (192,192,192)
WHITE = (255,255,255)
#X#X
MAGENTA = (186,85,211)
AQUA = (0,255,255)
ORANGE = (255,165,0)

width = 800
heigth = 600
SCREEN = pygame.display.set_mode((width,heigth))
FONT = pygame.font.SysFont('Helvetica', 20, bold=True)
FONT_2 = pygame.font.SysFont('Helvetica', 50, bold=True)

#------PLAYER------#
player_hp = 20
player_size = 30
player_pos = [400,300]
ZOMBIE_COUNT = 0

#------ZOMBIE------#
zombie_vec = [random.randint(50,750),random.randint(50,550),0,0,0,0,0]
zombie_size = [25,50]
zombie_list = []
zombie_color = GRAY
n_zombie = 2

#------ZOMBIE LEVEL 2------#
randPos_list = [[0,0],[width,0],[0,heigth],[width,heigth]]
randColor = [GRAY, MAGENTA, AQUA, ORANGE]
zombie2_vec = [random.choice(randPos_list)[0],random.choice(randPos_list)[1],0,0,0,0,0]
print(zombie2_vec)
zombie2_size = [25,50]
zombie2_list = []
zombie2_color = random.choice(randColor)
print(zombie2_color)
n_zombie2 = 20

#-----SHOOT-----#
shoot = False
bullet_angle = 90
bullet_vel = 8
bullet_size = [10,10]
bullet_pos = [player_pos[0]+player_size,player_pos[1],0]
bullet_list = []

#-----HP PICKUPS----#
pickup_pos = [random.randint(20,width-20),random.randint(20,heigth-100)]
pickup_color = GREEN
n_pickup = 3

#-----SCENES-----#
scene = 1       # 0: Restart/ Exit 1: Easy MODE 2: Hard MODE
RESTART_BUTTON = pygame.Rect((width/2)-200,(heigth/2)+50,50,50)
EXIT_BUTTON = pygame.Rect((width/2)+200,(heigth/2)+50,50,50)
MAIN_MENU = False


###########################
# MAIN LOOP
###########################

done = False
while not done:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot = True
            print('shoot_TRUE')
        if event.type == pygame.MOUSEBUTTONUP:
            shoot = False
            print('shoot_TRUE')
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        player_pos[0] -= 10
    if pressed[pygame.K_d]:
        player_pos[0] += 10
    if pressed[pygame.K_w]:
        player_pos[1] -= 10
    if pressed[pygame.K_s]:
        player_pos[1] += 10

    #------ZOMBIE lvl 1------#
    random_prob = random.random()
    if len(zombie_list) < n_zombie and random_prob < 0.1:

        zombie_hp = 5
        zombie_color = GRAY
        zlabel_color = WHITE

        zombie_x = random.randint(0,800)
        zombie_y = random.randint(0,60)

        distance_x = player_pos[0] - zombie_x
        distance_y = player_pos[1] - zombie_y

        zombie_angle = math.atan2(distance_y, distance_x)*-55
        zombie_vel = math.sqrt((player_pos[0]-zombie_x)**2 + (player_pos[1]-zombie_y)**2) 
        #zombie_vel = 8

        zombie_list.append([zombie_x, zombie_y, zombie_angle, zombie_vel, zombie_hp, zombie_color, zlabel_color])

    for zombie_vec in zombie_list:

        distance_x = player_pos[0] - zombie_vec[0]
        distance_y = player_pos[1] - zombie_vec[1]
        new_zombie_angle = math.atan2(distance_y, distance_x)*-55
        zombie_vec[2] = new_zombie_angle

        comp_x = zombie_vec[3]*math.cos(zombie_vec[2]*math.pi/180)
        comp_y = zombie_vec[3]*math.sin(zombie_vec[2]*math.pi/180)

        zombie_vec[0] += comp_x*0.003
        zombie_vec[1] -= comp_y*0.003

    #------ZOMBIE lvl 2------#
    if len(zombie2_list) < n_zombie2 and random_prob < 0.1:

        zombie2_hp = 5
        zombie2_color = random.choice(randColor)
        zlabel_color2 = WHITE

        zombie2_x = random.choice(randPos_list)[0]
        zombie2_y = random.choice(randPos_list)[1]

        distance_x_4 = player_pos[0] - zombie_x
        distance_y_4 = player_pos[1] - zombie_y

        zombie2_angle = math.atan2(distance_y_4, distance_x_4)*-55
        zombie2_vel = math.sqrt((player_pos[0]-zombie2_x)**2 + (player_pos[1]-zombie2_y)**2) 
        #zombie_vel = 8

        zombie2_list.append([zombie2_x, zombie2_y, zombie2_angle, zombie2_vel, zombie2_hp, zombie2_color, zlabel_color2])

    for zombie2_vec in zombie2_list:

        distance_x_4 = player_pos[0] - zombie2_vec[0]
        distance_y_4 = player_pos[1] - zombie2_vec[1]
        new_zombie2_angle = math.atan2(distance_y_4, distance_x_4)*-55
        zombie2_vec[2] = new_zombie2_angle

        comp2_x = zombie2_vec[3]*math.cos(zombie2_vec[2]*math.pi/180)
        comp2_y = zombie2_vec[3]*math.sin(zombie2_vec[2]*math.pi/180)

        zombie2_vec[0] += comp2_x*0.003
        zombie2_vec[1] -= comp2_y*0.003


    
    #-----SHOOT-----#
    mouse_pos = pygame.mouse.get_pos()

    if shoot == True:

        bullet_x = player_pos[0]+player_size/2
        bullet_y = player_pos[1]+player_size/2

        #-----ANGLE-----#
        distance_x = mouse_pos[0] - bullet_x  # destination - starting 
        distance_y = mouse_pos[1] - bullet_y  # destination - starting
        bullet_angle = math.atan2(distance_y, distance_x)*-55 # angle to append 

        bullet_list.append([bullet_x,bullet_y,bullet_angle])

    for bullet_pos in bullet_list:

        comp_x = bullet_vel*math.cos(bullet_pos[2]*math.pi/180)
        comp_y = bullet_vel*math.sin(bullet_pos[2]*math.pi/180)

        bullet_pos[0] += comp_x
        bullet_pos[1] -= comp_y

    #print(bullet_angle)

    #------COLLISIONS lvl 1------#
    for zombie_vec in zombie_list:

        distance_x_2 = bullet_pos[0]-zombie_vec[0]
        distance_y_2 = bullet_pos[1]-zombie_vec[1]
        magnitude = math.sqrt((distance_x_2**2)+(distance_y_2**2))

        if magnitude < 25 :
            zombie_vec[4] -= 1
            #print('collided','HP:',zombie_vec[4])
            if zombie_vec[4] <= 0 :
                zombie_list.remove(zombie_vec)
                ZOMBIE_COUNT += 1
                zombie_vec[6] = BLACK
                zombie_vec[5] = BLACK

    for zombie_vec in zombie_list:

        distance_x_3 = player_pos[0]-zombie_vec[0]
        distance_y_3 = player_pos[1]-zombie_vec[1]
        magnitude_2 = math.sqrt((distance_y_3**2)+(distance_x_3**2))

        if magnitude_2 < 25 :
            player_hp -= 1
            if player_hp <= 0 :
                player_hp = 0
                scene = 0
                MAIN_MENU = True
                print('GAME OVER ... ')


    #print(player_hp)

    #------COLLISIONS lvl 2------#
    for zombie2_vec in zombie2_list:

        distance_x_5 = bullet_pos[0]-zombie2_vec[0]
        distance_y_5 = bullet_pos[1]-zombie2_vec[1]
        magnitude_2 = math.sqrt((distance_x_5**2)+(distance_y_5**2))

        if magnitude_2 < 25 :
            zombie2_vec[4] -= 1
            #print('collided','HP:',zombie_vec[4])
            if zombie2_vec[4] <= 0 :
                zombie2_list.remove(zombie2_vec)
                ZOMBIE_COUNT += 1
                zombie2_vec[6] = BLACK
                zombie2_vec[5] = BLACK

    for zombie2_vec in zombie2_list:

        distance_x_6 = player_pos[0]-zombie2_vec[0]
        distance_y_6 = player_pos[1]-zombie2_vec[1]
        magnitude_3 = math.sqrt((distance_y_6**2)+(distance_x_6**2))

        if magnitude_3 < 25 :
            player_hp -= 1
            if player_hp <= 0 :
                player_hp = 0
                scene = 0
                MAIN_MENU = True
                print('GAME OVER ... ')

    #-----MENU-----#    
    if RESTART_BUTTON.collidepoint(mouse_pos) and MAIN_MENU == True:
    
        player_pos[0] = width/2
        player_pos[1] = heigth/2+100
        player_hp = 20
        ZOMBIE_COUNT = 0
        for zombie_vec in zombie_list:
            zombie_list.remove(zombie_vec)

        for zombie2_vec in zombie2_list:
            zombie2_list.remove(zombie2_vec)

        pygame.time.wait(1000)
        if len(zombie_list) <= 0 and len(zombie2_list) <= 0 :
            scene = 2        # 2   ---> to next level
            #print(scene)

    if EXIT_BUTTON.collidepoint(mouse_pos) and MAIN_MENU == True:
        done = True
        sys.exit()      
    

    ###################################################
    # DRAW FUNCTION
    ###################################################

    SCREEN.fill(BLACK)

    if scene == 1:

        MAIN_MENU = False

        for zombie2_vec in zombie2_list:
            zombie2_list.remove(zombie2_vec)
            #print(len(zombie_list))

        player_rect = pygame.Rect(player_pos[0],player_pos[1],player_size,player_size)
        pygame.draw.rect(SCREEN, RED, player_rect)

        for zombie_vec in zombie_list:
            zombie_rect = pygame.Rect(zombie_vec[0],zombie_vec[1],zombie_size[0],zombie_size[1])
            pygame.draw.rect(SCREEN, zombie_vec[5], zombie_rect, 1)
        
        for bullet_pos in bullet_list:
            bullet_rect = pygame.Rect(bullet_pos[0],bullet_pos[1],bullet_size[0],bullet_size[1])
            pygame.draw.rect(SCREEN, BLUE, bullet_rect, 1)
        
        pickup_rect = pygame.Rect(pickup_pos[0],pickup_pos[1],20,20)
        if ZOMBIE_COUNT > 4 and n_pickup > 0:
            pygame.draw.rect(SCREEN, pickup_color, pickup_rect)

        if player_rect.colliderect(pickup_rect):
            player_hp += 10
            n_pickup -= 1
            pickup_pos[0] = random.randint(10,width-10)
            pickup_pos[1] = random.randint(10,heigth-100)
        
        ######### SCORES LABEL
        player_hp_str = 'HP : ' + str(player_hp)
        player_hp_render = FONT.render(player_hp_str, False, WHITE)
        SCREEN.blit(player_hp_render, (50,heigth-50))

        player_score = ZOMBIE_COUNT*99
        player_score_str = 'SCORE : ' + str(player_score)
        player_score_render = FONT.render(player_score_str, False, WHITE)
        SCREEN.blit(player_score_render, (50,heigth-75))

        for zombie_vec in zombie_list:
            zombie_hp_str = str(zombie_vec[4])
            zombie_hp_render = FONT.render(zombie_hp_str, False, zombie_vec[6])
            SCREEN.blit(zombie_hp_render, (zombie_vec[0],zombie_vec[1]))
        
        if ZOMBIE_COUNT < 5 and n_pickup > 0:
            pickup_str1 = 'HP PACKAGE INCOMING'
            pickup_str1_render = FONT.render(pickup_str1, False, WHITE)
            SCREEN.blit(pickup_str1_render, (500,heigth-50))

        if ZOMBIE_COUNT > 4:
            pickup_str2 = 'HP PACKAGE LEFT : ' + str(n_pickup)
            pickup_str2_render = FONT.render(pickup_str2, False, WHITE)
            if n_pickup <= 0:
                n_pickup = 0
            SCREEN.blit(pickup_str2_render, (500,heigth-50))

    if scene == 0 and MAIN_MENU == True:

        pygame.draw.rect(SCREEN, GRAY, RESTART_BUTTON)
        pygame.draw.rect(SCREEN, GRAY, EXIT_BUTTON)

        gameOver_str = 'GAME OVER ...'
        gameOver_render = FONT_2.render(gameOver_str, False, WHITE)
        SCREEN.blit(gameOver_render, ((width/2)-150,(heigth/2)-100))

        restart_str = 'RESTART'
        restart_render = FONT.render(restart_str, False, WHITE)
        SCREEN.blit(restart_render, ((width/2)-220,(heigth/2)+110))
        
        exit_str = 'EXIT'
        exit_render = FONT.render(exit_str, False, WHITE)
        SCREEN.blit(exit_render, ((width/2)+205,(heigth/2)+110))

        ##### HIGHSCORE LABEL
        highscore_str = 'HIGHSCORE : ' + str(ZOMBIE_COUNT*99)
        highscore_render = FONT.render(highscore_str, False, WHITE)
        SCREEN.blit(highscore_render, ((width/2)-65,(heigth/2)-200))


    if scene == 2:

        MAIN_MENU = False

        for zombie_vec in zombie_list:
            zombie_list.remove(zombie_vec)
            #print(len(zombie_list))

        player_rect = pygame.Rect(player_pos[0],player_pos[1],player_size,player_size)
        pygame.draw.rect(SCREEN, RED, player_rect)


        for zombie2_vec in zombie2_list:
            zombie2_rect = pygame.Rect(zombie2_vec[0],zombie2_vec[1],zombie2_size[0],zombie2_size[1])
            pygame.draw.rect(SCREEN, zombie2_vec[5], zombie2_rect, 1)

        for bullet_pos in bullet_list:
            bullet_rect = pygame.Rect(bullet_pos[0],bullet_pos[1],bullet_size[0],bullet_size[1])
            pygame.draw.rect(SCREEN, BLUE, bullet_rect, 1)
        
        pickup_rect = pygame.Rect(pickup_pos[0],pickup_pos[1],20,20)
        if ZOMBIE_COUNT > 4 and n_pickup > 0:
            pygame.draw.rect(SCREEN, pickup_color, pickup_rect)

        if player_rect.colliderect(pickup_rect):
            player_hp += 10
            n_pickup -= 1
            pickup_pos[0] = random.randint(10,width-10)
            pickup_pos[1] = random.randint(10,heigth-100)


        ######### SCORES LABEL
        player_hp_str = 'HP : ' + str(player_hp)
        player_hp_render = FONT.render(player_hp_str, False, WHITE)
        SCREEN.blit(player_hp_render, (50,heigth-50))

        player_score = ZOMBIE_COUNT*99
        player_score_str = 'SCORE : ' + str(player_score)
        player_score_render = FONT.render(player_score_str, False, WHITE)
        SCREEN.blit(player_score_render, (50,heigth-75))

        for zombie2_vec in zombie2_list:
            zombie2_hp_str = str(zombie2_vec[4])
            zombie2_hp_render = FONT.render(zombie2_hp_str, False, zombie_vec[6])
            SCREEN.blit(zombie2_hp_render, (zombie2_vec[0],zombie2_vec[1]))

        if ZOMBIE_COUNT < 5 and n_pickup > 0:
            pickup_str1 = 'HP PACKAGE INCOMING'
            pickup_str1_render = FONT.render(pickup_str1, False, WHITE)
            SCREEN.blit(pickup_str1_render, (500,heigth-50))

        if ZOMBIE_COUNT > 4:
            pickup_str2 = 'HP PACKAGE LEFT : ' + str(n_pickup)
            pickup_str2_render = FONT.render(pickup_str2, False, WHITE)
            if n_pickup <= 0:
                n_pickup = 0
            SCREEN.blit(pickup_str2_render, (500,heigth-50))
        

    pygame.display.update()

###################################################
# END
###################################################
pygame.quit()
