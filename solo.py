import pygame
import random
import math
from sys import executable
#import os

def resource_path(relative_path):
    '''
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    '''
    return relative_path

def resource_path_out(relative_path):
    if __file__[-2:]=='py':
        return relative_path
    elif __file__[-3:] == 'exe':
        return executable+'\\'+relative_path

def change_asteroid_color(surface,colors):
    #[(35, 206, 35),(39, 170, 29),(27, 160, 27)]
    change_color(surface, (103, 58, 183), pygame.Color(*colors[0]))
    change_color(surface, (69, 39, 160), pygame.Color(*colors[1]))
    change_color(surface, (40, 53, 147), pygame.Color(*colors[2]))
    change_missed_colors(surface, [colors[0],
                                   colors[1],
                                   colors[2],
                                   (0, 0, 0),
                                   (255, 255, 255)], pygame.Color(*colors[1]))

def change_color(surface,color1, color2):
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r,g,b,_=surface.get_at((x, y))
            if (r,g,b)==color1:
                r, g, b,_= color2
                surface.set_at((x, y), pygame.Color(r, g, b,255))

def change_missed_colors(surface,dont_change, color2):
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r,g,b,_=surface.get_at((x, y))
            if (r,g,b) not in dont_change:
                if r==b and r==g:
                    change_color=(0,0,0,0)
                else:
                    change_color=color2
                r, g, b,_= change_color
                surface.set_at((x, y), pygame.Color(r, g, b,255))

width=800
height=800
fps=60

difficulty=1

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height),pygame.SCALED | pygame.RESIZABLE)
clock= pygame.time.Clock()


pygame.display.set_caption("asteroids")
pygame.display.set_icon(pygame.image.load(resource_path("assets_and_data\\icon.png")))

backround=pygame.image.load(resource_path('assets_and_data\\backround.jpg')).convert()
backround_rect=backround.get_rect()
menu_backround=pygame.transform.scale(pygame.image.load(resource_path('assets_and_data\\menu_backround.png')).convert(),(width,height))
menu_backround_rect=backround.get_rect()

lazer_beam=pygame.image.load(resource_path('assets_and_data\\lazer_beam.png')).convert()
lazer_beam.set_colorkey(white)

asteroid_img=pygame.image.load(resource_path('assets_and_data\\meteor.png')).convert()
astr1=pygame.transform.scale(asteroid_img, (100, 100))
astr1.set_colorkey(white)
astr2=pygame.transform.scale(asteroid_img, (66, 66))
astr2.set_colorkey(white)
astr3=pygame.transform.scale(asteroid_img, (32, 32))
astr3.set_colorkey(white)


asteroid_dict={
    1:[astr1,45],
    2:[astr2,29],
    3:[astr3,13]
}


follow_asteroid_img=pygame.image.load(resource_path('assets_and_data\\meteor.png')).convert()
change_asteroid_color(follow_asteroid_img,[(114, 117, 127),(78, 80, 80),(88, 91, 99)])
follow_astr1=pygame.transform.scale(follow_asteroid_img, (122, 122))
follow_astr1.set_colorkey(white)
follow_astr2=pygame.transform.scale(follow_asteroid_img, (49, 49))
follow_astr2.set_colorkey(white)


follow_asteroid_dict={
    1:[follow_astr1,54],
    2:[follow_astr2,21],
}

speed_asteroid_img=pygame.image.load(resource_path('assets_and_data\\meteor.png')).convert()
change_asteroid_color(speed_asteroid_img,[(35, 206, 35),(39, 170, 29),(27, 160, 27)])
speed_astr1=pygame.transform.scale(speed_asteroid_img, (100, 100))
speed_astr1.set_colorkey(white)
speed_astr2=pygame.transform.scale(speed_asteroid_img, (66, 66))
speed_astr2.set_colorkey(white)
speed_astr3=pygame.transform.scale(speed_asteroid_img, (32, 32))
speed_astr3.set_colorkey(white)


speed_asteroid_dict={
    1:[speed_astr1,45],
    2:[speed_astr2,29],
    3:[speed_astr3,13]
}

#health_meteor.png
ds=25

health_asteroid_img=pygame.image.load(resource_path('assets_and_data\\meteor.png')).convert()
change_asteroid_color(health_asteroid_img,[(201, 40, 30),(136, 28, 28),(156, 31, 31)])
health_astr1=pygame.transform.scale(health_asteroid_img, (100+ds, 100+ds))
health_astr1.set_colorkey(white)
health_astr2=pygame.transform.scale(health_asteroid_img, (66+ds, 66+ds))
health_astr2.set_colorkey(white)
health_astr3=pygame.transform.scale(health_asteroid_img, (32+ds, 32+ds))
health_astr3.set_colorkey(white)


health_asteroid_dict={
    1:[health_astr1,57],
    2:[health_astr2,42],
    3:[health_astr3,26]
}

ship=pygame.image.load(resource_path('assets_and_data\\spaceship64.png')).convert()

shield=pygame.image.load(resource_path('assets_and_data\\shield.png')).convert()
shield.set_colorkey(white)

bullet_power_up=pygame.image.load(resource_path('assets_and_data\\bullet_power_up.png')).convert()
bullet_power_up.set_colorkey(black)

bomb_shot_img=pygame.image.load(resource_path('assets_and_data\\bomb_power_up.png')).convert()
bomb_shot_img=pygame.transform.scale(bomb_shot_img,(20,20))
bomb_shot_img.set_colorkey(white)


fire_rate=pygame.image.load(resource_path('assets_and_data\\fire_rate.png')).convert()
fire_rate.set_colorkey(white)

pierce_shot_power_up=pygame.image.load(resource_path('assets_and_data\\spear.png')).convert()
pierce_shot_power_up.set_colorkey(white)

bomb_power_up=pygame.image.load(resource_path('assets_and_data\\bomb_power_up.png')).convert()
bomb_power_up.set_colorkey(white)

speed_power_up=pygame.image.load(resource_path('assets_and_data\\speed_img.png')).convert()
speed_power_up.set_colorkey(white)

nuke=pygame.image.load(resource_path('assets_and_data\\bomb.png')).convert()
nuke.set_colorkey(white)

restart_button1=pygame.image.load(resource_path('assets_and_data\\restart_button1.png')).convert()
restart_button1.set_colorkey(white)
restart_button2=pygame.image.load(resource_path('assets_and_data\\restart_button2.png')).convert()
restart_button2.set_colorkey(white)

main_menu_button1=pygame.image.load(resource_path('assets_and_data\\main_menu_button1.png')).convert()
main_menu_button1.set_colorkey(white)
main_menu_button2=pygame.image.load(resource_path('assets_and_data\\main_menu_button2.png')).convert()
main_menu_button2.set_colorkey(white)

mini_main_menu_button1=pygame.image.load(resource_path('assets_and_data\\mini_main_menu_button1.png')).convert()
mini_main_menu_button1.set_colorkey(white)
mini_main_menu_button2=pygame.image.load(resource_path('assets_and_data\\mini_main_menu_button2.png')).convert()
mini_main_menu_button2.set_colorkey(white)

settings_button1=pygame.image.load(resource_path('assets_and_data\\settings_button1.png')).convert()
settings_button1.set_colorkey(white)
settings_button2=pygame.image.load(resource_path('assets_and_data\\settings_button2.png')).convert()
settings_button2.set_colorkey(white)

play_button1=pygame.image.load(resource_path('assets_and_data\\play_button1.png')).convert()
play_button1.set_colorkey(white)
play_button2=pygame.image.load(resource_path('assets_and_data\\play_button2.png')).convert()
play_button2.set_colorkey(white)

change_key1=pygame.image.load(resource_path('assets_and_data\\change_key1.png')).convert()
change_key1.set_colorkey(white)
change_key2=pygame.image.load(resource_path('assets_and_data\\change_key2.png')).convert()
change_key2.set_colorkey(white)

press_key=pygame.image.load(resource_path('assets_and_data\\press_key.png')).convert()
press_key.set_colorkey(white)


boss_img=pygame.image.load(resource_path('assets_and_data\\enemy.png')).convert()
boss_img.set_colorkey(white)

fire_ball=pygame.image.load(resource_path('assets_and_data\\fireball.png')).convert()
fire_ball=pygame.transform.scale(fire_ball, (30, 52))
fire_ball.set_colorkey(white)


exp0=pygame.image.load(resource_path('assets_and_data\\regularExplosion00.png')).convert()
exp0.set_colorkey(black)
exp1=pygame.image.load(resource_path('assets_and_data\\regularExplosion01.png')).convert()
exp1.set_colorkey(black)
exp2=pygame.image.load(resource_path('assets_and_data\\regularExplosion02.png')).convert()
exp2.set_colorkey(black)
exp3=pygame.image.load(resource_path('assets_and_data\\regularExplosion03.png')).convert()
exp3.set_colorkey(black)
exp4=pygame.image.load(resource_path('assets_and_data\\regularExplosion04.png')).convert()
exp4.set_colorkey(black)
exp5=pygame.image.load(resource_path('assets_and_data\\regularExplosion05.png')).convert()
exp5.set_colorkey(black)
exp6=pygame.image.load(resource_path('assets_and_data\\regularExplosion06.png')).convert()
exp6.set_colorkey(black)
exp7=pygame.image.load(resource_path('assets_and_data\\regularExplosion07.png')).convert()
exp7.set_colorkey(black)
exp8=pygame.image.load(resource_path('assets_and_data\\regularExplosion08.png')).convert()
exp8.set_colorkey(black)

exp_list=[exp0,exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8]


bullet_sound=pygame.mixer.Sound(resource_path('assets_and_data\\Laser_Shoot.wav'))
bullet_sound.set_volume(.03)
exp_sound=pygame.mixer.Sound(resource_path('assets_and_data\\Explosion.wav'))
exp_sound.set_volume(.03)
expl2=pygame.mixer.Sound(resource_path('assets_and_data\\exps2.wav'))
expl2.set_volume(.25)
bombsoht_exp=pygame.mixer.Sound(resource_path('assets_and_data\\bombshot_exp.wav'))
bombsoht_exp.set_volume(.03)
bombshot_shot_sound=pygame.mixer.Sound(resource_path('assets_and_data\\bombshotsound.wav'))
bombshot_shot_sound.set_volume(.03)
player_hit=pygame.mixer.Sound(resource_path('assets_and_data\\Hit.wav'))
player_hit.set_volume(.04)
loss_sound=pygame.mixer.Sound(resource_path('assets_and_data\\lose.wav'))
loss_sound.set_volume(.04)
power_up_sound=pygame.mixer.Sound(resource_path('assets_and_data\\power_up_sound.wav'))
power_up_sound.set_volume(.03)
boss_bullet_sound=pygame.mixer.Sound(resource_path('assets_and_data\\boss_bullet_sound.wav'))
boss_bullet_sound.set_volume(.03)

font_name=pygame.font.match_font('arial')

#music
'''pygame.mixer.music.load('ObservingTheStar.ogg')
pygame.mixer.music.set_volume(.3)
pygame.mixer.music.play(-1)'''

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,size,center,angle):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=asteroid_dict[size][0]
        self.rect=self.image.get_rect()
        self.radius=asteroid_dict[size][1]
        self.rect.center=center
        self.floatx=self.rect.centerx
        self.floaty=self.rect.centery
        self.angle=angle
        self.speed=1.25
        self.speedx=math.cos(self.angle)
        self.speedy=math.sin(self.angle)
        self.hit_by=[]
        #pygame.draw.circle(self.image, red, (round(self.rect.width / 2), round(self.rect.height / 2)), self.radius)

    def update(self):
        self.floatx += self.speed * self.speedx
        self.floaty -= self.speed * self.speedy
        self.rect.center = (math.floor(self.floatx), math.floor(self.floaty))
        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = width
        if self.rect.bottom < 0:
            self.rect.top = height
        if self.rect.top > height:
            self.rect.bottom = 0
        self.floatx=self.rect.centerx+(self.floatx-math.floor(self.floatx))
        self.floaty=self.rect.centery+(self.floaty-math.floor(self.floaty))

        self.child_update()

    def child_update(self):
        pass

    def hit(self):
        level.astroids_destoyed+=1
        power_up=power_up_manager.chance()
        if power_up:
            power_up_group.add(power_up(self.rect.center))
        if self.size<3:
            astr1=Asteroid(self.size + 1, self.rect.center, (self.angle + math.pi / 10) % (2 * math.pi))
            astr2=Asteroid(self.size + 1, self.rect.center, (self.angle - math.pi / 10) % (2 * math.pi))
            astr1.hit_by = self.hit_by.copy()
            astr2.hit_by = self.hit_by.copy()
            asteroid_group.add(astr1)
            asteroid_group.add(astr2)
            self.kill()
        else:
            self.kill()

class FollowAsteroid(Asteroid):
    def __init__(self,size,center,angle):
        super().__init__(size,center,angle)
        self.speed=random.uniform(.5,.9) if size==1 else random.uniform(.7,1.1)

        self.size = size
        self.image = follow_asteroid_dict[size][0]
        self.rect = self.image.get_rect()
        self.radius = follow_asteroid_dict[size][1]
        self.rect.center = center
        self.floatx = self.rect.centerx
        self.floaty = self.rect.centery
        self.angle = angle
        self.speedx = math.cos(self.angle)
        self.speedy = math.sin(self.angle)
        self.hit_by = []


        #pygame.draw.circle(self.image, green, (round(self.rect.width / 2), round(self.rect.height / 2)), self.radius)

    def hit(self):
        level.astroids_destoyed += 1
        power_up = power_up_manager.chance()
        if power_up:
            power_up_group.add(power_up(self.rect.center))
        if self.size < 2:
            for i in range(5):
                astr1 = FollowAsteroid(self.size + 1, self.rect.center, random.uniform(0,2*math.pi))
                astr1.hit_by = self.hit_by.copy()
                asteroid_group.add(astr1)
                self.kill()
        else:
            self.kill()

    def child_update(self):
        clostest = get_closest_player(self.floatx, self.floaty, self.rect.centerx - self.rect.left,self.rect.centery - self.rect.top)
        x_shifted=clostest[0]-self.floatx
        y_shifted=clostest[1]-self.floaty
        angle=math.atan2(-y_shifted,x_shifted)
        self.speedx+=math.cos(angle)/50
        self.speedy+=math.sin(angle)/50
        magnitude=math.sqrt(self.speedx**2+self.speedy**2)
        self.speedx/=magnitude
        self.speedy/=magnitude

class SpeedAsteroid(Asteroid):
    def __init__(self,size,center,angle):
        super().__init__(size,center,angle)
        self.speed=2.45
        self.image=speed_asteroid_dict[size][0]

    def hit(self):
        level.astroids_destoyed += 1
        power_up = power_up_manager.chance()
        if power_up:
            power_up_group.add(power_up(self.rect.center))
        if self.size < 3:
            astr1 = SpeedAsteroid(self.size + 1, self.rect.center, (self.angle + math.pi / 10) % (2 * math.pi))
            astr2 = SpeedAsteroid(self.size + 1, self.rect.center, (self.angle - math.pi / 10) % (2 * math.pi))
            astr1.hit_by = self.hit_by.copy()
            astr2.hit_by = self.hit_by.copy()
            asteroid_group.add(astr1)
            asteroid_group.add(astr2)
            self.kill()
        else:
            self.kill()

class HealthAsteroid(Asteroid):
    def __init__(self,size,center,angle):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image=health_asteroid_dict[size][0]
        self.rect = self.image.get_rect()
        self.radius = health_asteroid_dict[size][1]
        self.rect.center = center
        self.floatx = self.rect.centerx
        self.floaty = self.rect.centery
        self.angle = angle
        self.speed=1
        self.speedx = math.cos(self.angle)
        self.speedy = math.sin(self.angle)
        self.hit_by = []

        self.health=3
        self.alive=True

        if self.size==1:
            length=150
        elif self.size==2:
            length = 110
        elif self.size==3:
            length = 70
        self.health_bar = LoadingBar(0, 0, length, 4, self.health)
        health_bar_group.append(self.health_bar)
        #pygame.draw.circle(self.image, green, (round(self.rect.width / 2), round(self.rect.height / 2)), self.radius)

    def hit(self):
        if self.health<=0 and self.alive:
            self.alive=False
            try:
                health_bar_group.remove(self.health_bar)
            except ValueError:
                print('health bar error')
            level.astroids_destoyed += 1
            power_up = power_up_manager.chance()
            if power_up:
                power_up_group.add(power_up(self.rect.center))
            if self.size < 3:
                astr1 = HealthAsteroid(self.size + 1, self.rect.center, (self.angle + math.pi / 10) % (2 * math.pi))
                astr2 = HealthAsteroid(self.size + 1, self.rect.center, (self.angle - math.pi / 10) % (2 * math.pi))
                astr1.hit_by = self.hit_by.copy()
                astr2.hit_by = self.hit_by.copy()
                asteroid_group.add(astr1)
                asteroid_group.add(astr2)
                self.kill()
            else:
                self.kill()

    def child_update(self):
        if self.size==1:
            dy=80
        elif self.size==2:
            dy = 60
        elif self.size==3:
            dy = 40

        if self.size==1:
            dx = -2
        elif self.size==2:
            dx = 20
        elif self.size==3:
            dx = 40
        self.health_bar.update(self.floatx - 75+dx, self.floaty + dy, self.health)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.left_key = left_key
        self.right_key = right_key
        self.up_key = up_key
        self.down_key = down_key
        self.shoot_key = shoot_key

        self.image=pygame.transform.scale(ship,(32,32))
        self.image.set_colorkey(white)
        self.image_copy=self.image.copy()
        self.rect=self.image.get_rect()

        self.living=True

        self.rot_speed = math.pi / 60
        self.radius=15
        self.speedx = 0
        self.speedy = 0
        self.speed=2
        self.slide=1.01
        self.angle=math.pi/2
        self.floaty= height / 2
        self.floatx= width / 2
        self.rect.center = (round(self.floatx), round(self.floaty))
        self.last_shot=now

        self.shields=0
        self.multiple_shot=1
        self.shoot_angle=0
        self.bomb_shot=False
        self.pierce_shot=False
        self.normal_speed=2
        self.increased_speed=2.8
        self.nomal_rot_speed = math.pi / 60
        self.increased_rot_speed = math.pi / 50
        self.rot_speed = math.pi / 60
        self.fire_rate_buff = False
        self.normal_fire_rate = 50
        self.increased_fire_rate = 35
        self.normal_bomb_fire_rate = 80
        self.increased_bomb_fire_rate = 50


        self.rot_speed=self.nomal_rot_speed
        self.speed = self.normal_speed

        self.shoot_dalay = self.normal_fire_rate
        #pygame.draw.circle(self.image, red, (round(self.rect.width/2),round(self.rect.height/2)), self.radius)

    def update(self):
        self.speedx=self.speedx/self.slide
        self.speedy=self.speedy/self.slide
        #keys
        keystate=pygame.key.get_pressed()
        mousestate = pygame.mouse.get_pressed()
        if keystate[self.left_key] or (mousestate[self.left_key-1] if self.left_key in [1,2,3] else False):
            self.angle+=self.rot_speed
            self.angle = (self.angle) % (2 * math.pi)
            self.image=pygame.transform.rotate(self.image_copy,self.angle*180/math.pi-90)
            self.rect=self.image.get_rect()
            self.rect.center=(round(self.floatx), round(self.floaty))
        if keystate[self.right_key] or (mousestate[self.right_key-1] if self.right_key in [1,2,3] else False):
            self.angle+=-self.rot_speed
            self.angle=(self.angle)%(2*math.pi)
            self.image=pygame.transform.rotate(self.image_copy,self.angle*180/math.pi-90)
            self.rect=self.image.get_rect()
            self.rect.center=(round(self.floatx), round(self.floaty))
        if keystate[self.up_key] or (mousestate[self.up_key-1] if self.up_key in [1,2,3] else False):
            self.speedy=-self.speed*math.sin(self.angle)
            self.speedx=self.speed*math.cos(self.angle)
        if keystate[self.down_key] or (mousestate[self.down_key-1] if self.down_key in [1,2,3] else False):
            self.speedy=self.speed*math.sin(self.angle)
            self.speedx=-self.speed*math.cos(self.angle)
        if keystate[self.shoot_key] or (mousestate[self.shoot_key-1] if self.shoot_key in [1,2,3] else False):
            self.shoot()
        #move sprite
        self.floatx+=self.speedx
        self.floaty+=self.speedy
        self.rect.centerx=round(self.floatx)
        self.rect.centery=round(self.floaty)


        #rap around to the other side of screen
        if self.rect.left>width:
            self.rect.right=0
            self.floatx=self.rect.centerx
        if self.rect.right<0:
            self.rect.left=width
            self.floatx=self.rect.centerx
        if self.rect.bottom<0:
            self.rect.top=height
            self.floaty=self.rect.centery
        if self.rect.top>height:
            self.rect.bottom=0
            self.floaty=self.rect.centery

    def shoot(self):
        if now-self.last_shot>self.shoot_dalay:
            if not self.bomb_shot:
                bullet_sound.play()
                group=bullets_group
                projectile=PlayerBullet
            else:
                bombshot_shot_sound.play()
                group = bombs_group
                projectile = Bomb
            self.last_shot=now
            if self.multiple_shot%2==1:
                projectile1 = projectile(self.rect.centerx, self.rect.centery, self.angle)
                group.add(projectile1)
                for i in range(1,int((self.multiple_shot-1)/2+1)):
                    shot = projectile(self.rect.centerx, self.rect.centery, (self.angle+i*self.shoot_angle) % (2 * math.pi))
                    group.add(shot)
                for i in range(1,int((self.multiple_shot-1)/2+1)):
                    shot = projectile(self.rect.centerx, self.rect.centery, (self.angle-i*self.shoot_angle) % (2 * math.pi))
                    group.add(shot)
            else:
                for i in range(int((self.multiple_shot)/2)):
                    shot = projectile(self.rect.centerx, self.rect.centery, (self.angle+i*self.shoot_angle+self.shoot_angle/2) % (2 * math.pi))
                    group.add(shot)
                for i in range(int((self.multiple_shot)/2)):
                    shot = projectile(self.rect.centerx, self.rect.centery, (self.angle-i*self.shoot_angle-self.shoot_angle/2) % (2 * math.pi))
                    group.add(shot)

    def hit(self):
        power_up_manager.player_hit()
        if self.shields<0:
            self.die()
        else:
            player_hit.play()

    def change_num_shots(self,n):
        self.multiple_shot=n
        if n==1:
            player.shoot_angle=0
        elif n == 2:
            player.shoot_angle = math.pi / 12
        elif n == 3:
            player.shoot_angle = math.pi / 8
        elif n==4:
            player.shoot_angle = math.pi / 6.5
        elif n==5:
            player.shoot_angle = math.pi / 5.5
        else:
            self.shoot_angle=(math.pi*(1-1/n))/(n-1)

    def die(self):
        self.living = False
        self.kill()
        loss_sound.play()

        data=read_game_date()

        if data['highest_level']<level.get_level:
            write_game_date('highest_level',level.get_level)
        write_game_date('asteroid_destroyed',data['asteroid_destroyed']+level.astroids_destoyed)
        write_game_date('bosses_killed', data['bosses_killed'] + level.bosses_killed)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,x,y,angle,speed,life_span):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image=pygame.transform.rotate(self.image,angle*180/(math.pi)-90)
        self.angle=angle
        self.image_copy=self.image.copy()
        self.rect=self.image.get_rect()
        self.floatx=x
        self.floaty=y
        self.rect.centery=self.floaty
        self.rect.centerx=self.floatx
        self.speed=speed
        self.life_span=life_span
        self.time_spawned=now
        self.things_hit=0

    def update(self):
        self.floaty+= self.speed * math.sin(-self.angle)
        self.floatx+= self.speed * math.cos(-self.angle)
        self.rect.centery=round(self.floaty)
        self.rect.centerx=round(self.floatx)
        if self.rect.left>width:
            self.rect.right=0
            self.floatx=self.rect.centerx
        if self.rect.right<0:
            self.rect.left=width
            self.floatx=self.rect.centerx
        if self.rect.bottom<0:
            self.rect.top=height
            self.floaty=self.rect.centery
        if self.rect.top>height:
            self.rect.bottom=0
            self.floaty=self.rect.centery
        if now-self.time_spawned>self.life_span:
            self.die()

    def die(self):
        self.kill()

class PlayerBullet(Bullet):
    def __init__(self,x,y,angle):
        super().__init__(lazer_beam, x, y, angle, 9, 80)

    def die(self):
        self.kill()

class Bomb(Bullet):
    def __init__(self,x,y,angle):
        super().__init__(bomb_shot_img,x,y,angle,5.5,50)
        self.radius=70
    def die(self):
        global last_exp
        if last_exp!=now:
            bombsoht_exp.play()
            last_exp = now
        exp_group.add(Explosion(self.rect.center))
        hits1 = pygame.sprite.spritecollide(self, asteroid_group, False, pygame.sprite.collide_circle)
        if len(boss_group.sprites()) != 0:
            if boss_group.sprites()[0].fighting:
                hits2 = pygame.sprite.spritecollide(self, boss_group, False, pygame.sprite.collide_circle)
                for boss in hits2:
                    boss.health-=1
        for asteroid in hits1:
            if isinstance(asteroid, HealthAsteroid):
                asteroid.health-=1
            asteroid.hit()
        self.kill()

class FireBall(Bullet):
    def __init__(self,x,y,angle):
        super().__init__(fire_ball, x, y, angle, 4.25, 350)
        self.radius=18
        #pygame.draw.circle(self.image, red, (round(self.rect.width/2),round(self.rect.height/2)), self.radius)
    def die(self):
        self.kill()

class Level():
    def __init__(self,level):
        self.get_level=level
        self.between_rounds=False
        self.between_rounds_start=0
        self.between_rounds_time=240
        self.grace_period = False
        self.grace_start = 0
        self.grace_period_time = 190

        self.timer_stay_time=35
        self.timer_staying=False
        self.timer_stay_start=0

        self.astroids_destoyed=0
        self.bosses_killed=0

    def next_level(self):
        self.get_level+=1
        if self.get_level%10!=0:
            if self.get_level>=10 and random.choice([i for i in range(7)])==0:
                power_up_manager.nuke_avaiable=True
                power_up_manager.nuke_chance= (self.get_level - 3) * 7

            for _ in range(self.get_level):
                if self.get_level>=7:
                    asteroid=random.choices([Asteroid,SpeedAsteroid,HealthAsteroid,FollowAsteroid], weights=((100-5*(self.get_level-6)) if (100-5*(self.get_level-6)) >=0 else 0,2.5*(self.get_level-6)/2+15,2.5*(self.get_level-6)/2+15,2.5*(self.get_level-6)/2+15))[0]
                    asteroid_group.add(asteroid(1,(random.randrange(width),random.randrange(height)),random.uniform(0,2*math.pi)))
                else:
                    asteroid_group.add(Asteroid(1,(random.randrange(width),random.randrange(height)),random.uniform(0,2*math.pi)))
                    #asteroid_group.add(HealthAsteroid(1,(random.randrange(width),random.randrange(height)),random.uniform(0,2*math.pi)))
                    #asteroid_group.add(HealthAsteroid(2,(random.randrange(width),random.randrange(height)),random.uniform(0,2*math.pi)))
                    #asteroid_group.add(HealthAsteroid(3,(random.randrange(width),random.randrange(height)),random.uniform(0,2*math.pi)))
                    #asteroid_group.add(Asteroid(1,(random.randrange(width),random.randrange(height)),random.uniform(0,2*math.pi)))
                '''asteroid_group.add(
                    Asteroid(1, (random.randrange(width), random.randrange(height)), random.uniform(0, 2 * math.pi)))
                asteroid_group.add(
                    SpeedAsteroid(1, (random.randrange(width), random.randrange(height)), random.uniform(0, 2 * math.pi)))'''
        else:
            boss_group.add(Boss())

    def update(self):
        if len(asteroid_group)<=0 and not self.between_rounds and len(boss_group)==0:
            self.between_rounds=True
            self.between_rounds_start=now
        if self.between_rounds and (now - self.between_rounds_start >= self.between_rounds_time):
            self.grace_period=True
            self.grace_start=now
            self.next_level()
            self.between_rounds=False
        if self.grace_period and now-self.grace_start>=self.grace_period_time:
            self.grace_period=False
            self.timer_staying=True
            self.timer_stay_start=now
        if self.timer_staying and now - self.timer_stay_start >= self.timer_stay_time:
            self.timer_staying=False

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        #radius is 60
        self.center=center
        self.frame=0
        self.image=exp_list[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame_start=now
        self.frame_time=4
    def update(self):
        if now - self.frame_start>=self.frame_time:
            self.frame_start = now
            self.frame+=1
            if self.frame<=8:
                self.image = exp_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center=self.center
            else:
                self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,img,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img,(30,30))
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.radius=14
        if self.rect.right>width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>height:
            self.rect.bottom=height

    def update(self, *args):
        pass

    def collected(self):
        pass

class PowerUpManager():
    def __init__(self):
        self.num_of_multiple_shot=1
        self.shield_avaiable=3
        self.fire_rate_avaiable=1
        self.bomb_shot_avaiable=1
        self.pierce_shot_avaiable=1
        self.speed_avaiable=1
        self.nuke_avaiable=False
        self.nuke_chance=10

        self.display_que=[]

    def chance(self):
        if self.nuke_avaiable:
            self.nuke_chance-=1
        if random.choice([i for i in range(40)])==0 and self.shield_avaiable>0:
            self.shield_avaiable-=1
            return Sheild
        if random.choice([i for i in range(150)])==0 and level.get_level>=5 and self.fire_rate_avaiable>0:
            self.fire_rate_avaiable=0
            return FireRate
        if random.choice([i for i in range(150)])==0 and level.get_level>=5 and self.pierce_shot_avaiable>0:
            self.pierce_shot_avaiable=0
            return PierceShot
        if random.choice([i for i in range(int(155*self.num_of_multiple_shot-60))])==0 and level.get_level>=5:
            self.num_of_multiple_shot+=1
            return MultipleShot
        if random.choice([i for i in range(200)])==0 and level.get_level>=10 and self.speed_avaiable>=1:
            self.speed_avaiable=0
            return Speed
        #if random.choice([i for i in range(1)])==0 and level.get_level>=1 and self.bomb_shot_avaiable>0:
        #    self.bomb_shot_avaiable = 0
        #    return BombShot
        try:
            if random.choice([i for i in range(self.nuke_chance)])==0 and self.nuke_avaiable:
                self.nuke_chance=40
                self.nuke_avaiable=False
                return Nuke
        except IndexError:
            print('Nuke_error')
        return None

    def player_hit(self):
        player.shields -= 1
        self.shield_avaiable += 1

        player.fire_rate_buff=False
        if firerate_display in self.display_que: self.display_que.remove(firerate_display)
        if not player.bomb_shot:
            self.pierce_shot_avaiable=1
            player.pierce_shot = False
            if pierce_shot_display in self.display_que: self.display_que.remove(pierce_shot_display)
        player.shoot_dalay=player.normal_fire_rate
        self.fire_rate_avaiable=1

        if player.multiple_shot != 2 and player.multiple_shot != 1:
            self.num_of_multiple_shot -= 2
            player.multiple_shot -= 2
            player.change_num_shots(player.multiple_shot)
            if multishot_display in self.display_que and player.multiple_shot==1: self.display_que.remove(multishot_display)
        elif player.multiple_shot != 1:
            self.num_of_multiple_shot -= 1
            player.multiple_shot -= 1
            player.change_num_shots(player.multiple_shot)
            if multishot_display in self.display_que and player.multiple_shot == 1: self.display_que.remove(multishot_display)

        player.speed=player.normal_speed
        player.rot_speed=player.nomal_rot_speed
        self.speed_avaiable=1
        if speed_display in self.display_que: self.display_que.remove(speed_display)

        if self.bomb_shot_avaiable == 0 and player.bomb_shot:
            self.bomb_shot_avaiable = 1
        player.bomb_shot = False
        if bombshot_display in self.display_que: self.display_que.remove(bombshot_display)
        to_add=self.display_que.copy()
        self.display_que=[]
        for i in to_add:
            self.change_display(i)

    def change_display(self,power_up_display):
        if multishot_display not in self.display_que or multishot_display!= power_up_display:
            self.display_que.append(power_up_display)
            seen_multi_shot=False
            for i,power_up in enumerate(self.display_que):
                if power_up == multishot_display:
                    seen_multi_shot=True
                power_up.change_potision((495+41*i+(0 if not seen_multi_shot else 12),35))

    def display_que_draw(self,screen):
        for i,power_up in enumerate(power_up_manager.display_que):
            power_up.draw()
            if power_up==multishot_display:
                draw_text(screen, f'{player.multiple_shot-1}x', 15, 493+41*i-18, 29,top_left=True)

class Sheild(PowerUp):
    def __init__(self,center):
        super().__init__(shield,center)

    def collected(self):
        player.shields+=1

class FireRate(PowerUp):
    def __init__(self,center):
        super().__init__(fire_rate,center)

    def collected(self):
        player.fire_rate_buff=True
        player.shoot_dalay=player.increased_fire_rate
        power_up_manager.change_display(firerate_display)

class MultipleShot(PowerUp):
    def __init__(self,center):
        super().__init__(bullet_power_up,center)

    def collected(self):
        player.change_num_shots(player.multiple_shot+1)
        power_up_manager.change_display(multishot_display)

class BombShot(PowerUp):
    def __init__(self,center):
        super().__init__(bomb_power_up,center)

    def collected(self):
        player.bomb_shot=True
        player.shoot_dalay=player.normal_bomb_fire_rate if not player.fire_rate_buff else player.increased_fire_rate
        power_up_manager.change_display(bombshot_display)

class PierceShot(PowerUp):
    def __init__(self,center):
        super().__init__(pierce_shot_power_up, center)

    def collected(self):
        player.pierce_shot=True
        power_up_manager.change_display(pierce_shot_display)

class Nuke(PowerUp):
    def __init__(self,center):
        super().__init__(nuke,center)

    def collected(self):
        global health_bar_group
        health_bar_group=[]
        expl2.play()
        for asteroid in asteroid_group:
            exp_group.add(Explosion(asteroid.rect.center))
            asteroid.kill()

class Speed(PowerUp):
    def __init__(self,center):
        super().__init__(speed_power_up,center)

    def collected(self):
        player.speed=player.increased_speed
        player.rot_speed=player.increased_rot_speed
        power_up_manager.change_display(speed_display)

class PowerUpDisplay(pygame.sprite.Sprite):
    def __init__(self,img,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img,(35,35))
        self.rect=self.image.get_rect()
        self.rect.center=center

    def draw(self):
        screen.blit(self.image,self.rect)

    def change_potision(self,center):
        self.rect.center = center

class Button:
    def __init__(self,sprites,top_left,bottom_right,function):
        self.bottom_right=bottom_right
        self.top_left=top_left
        self.function=function
        self.sprites=sprites
        self.sprite=self.sprites[0]
        self.mouse_down_on_button=False

    def on_button(self,x_y):
        if self.top_left[0]<=x_y[0] and self.top_left[1]<=x_y[1] and self.bottom_right[0]>=x_y[0]>=x_y[0] and self.bottom_right[1]>=x_y[1]:
            return True
        else:
            return False

    def upadate(self):
        if self.on_button(pygame.mouse.get_pos()):
            self.sprite=self.sprites[1]
            if pygame.mouse.get_pressed()[0]==1:
                self.mouse_down_on_button=True
            if self.mouse_down_on_button and pygame.mouse.get_pressed()[0]==0:
                self.mouse_down_on_button = False
                if isinstance(self.function,list):
                    function = self.function[0]
                    args=self.function[1:]
                    args=[arg if arg != 'self' else self for arg in args]
                    function(*args)
                else:
                    self.function()
        else:
            self.mouse_down_on_button = False
            self.sprite=self.sprites[0]

    def draw(self,screen):
        screen.blit(self.sprite,self.top_left)

class LoadingBar:
    def __init__(self,x,y,width,height,tot_health):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.tot_health=tot_health
        self.current_health=tot_health

    def update(self,x,y,health):
        self.x=x
        self.y=y
        self.current_health=int(health)

    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),(int(self.x),int(self.y),int(self.width),int(self.height)))
        if self.current_health>0:
            pygame.draw.rect(screen,(0,255,0),(int(self.x),int(self.y),int(math.floor((self.current_health/self.tot_health)*self.width)),int(self.height)))

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(boss_img, (115, 100))
        self.image.set_colorkey(white)
        self.image_copy=self.image.copy()
        self.rect=self.image.get_rect()

        self.living=True

        self.health=50
        self.health_bar=LoadingBar(0,0,150,9,self.health)

        self.rot_speed = math.pi / 45
        self.radius=51
        self.rect.center=(-70,150)
        self.speedx = 0
        self.speedy = 0
        self.speed=1
        self.slide=1.01
        self.last_shot=now
        self.shoot_dalay=140
        self.angle=0
        self.floaty= self.rect.centery
        self.floatx= self.rect.centerx
        self.last_shot=now
        self.fighting=False
        self.hit_by=[]

        #pygame.draw.circle(self.image, red, (round(self.rect.width/2),round(self.rect.height/2)), self.radius)

    def update(self):
        if self.fighting:
            self.fight_sage()
        else:
            self.start_stage()

    def start_stage(self):
        self.floatx+=self.speed
        self.rect.centerx=round(self.floatx)
        if self.floatx>=height/2:
            self.last_shot=now
            self.fighting=True
            self.speed=.5

    def fight_sage(self):
        turn=True
        thresh_hold=2
        if abs(self.rect.left - width)<thresh_hold:
            turn=False
        if abs(self.rect.right)<thresh_hold:
            turn=False
        if abs(self.rect.bottom)<thresh_hold:
            turn=False
        if abs(self.rect.top - height)<thresh_hold:
            turn=False

        if turn:
            clostest = get_closest_player(self.floatx,self.floaty,self.rect.centerx-self.rect.left,self.rect.centery-self.rect.top)

            angle_to_player=get_angle(self.floatx,self.floaty,clostest[0],clostest[1])%(math.pi*2)
            cw=(angle_to_player-self.angle)%(2*math.pi)
            ccw=(self.angle-angle_to_player)%(2*math.pi)
            min_angle=min([cw,ccw])
            if abs(angle_to_player-self.angle) <=self.rot_speed or (2*math.pi-abs(angle_to_player-self.angle))<=self.rot_speed:
                self.angle=angle_to_player
            elif min_angle==cw:
                self.angle+=self.rot_speed
            elif min_angle==ccw:
                self.angle-=self.rot_speed


        if now-self.last_shot>=self.shoot_dalay:
            self.shoot()
            self.last_shot=now
            self.shoot_dalay=random.randrange(65,145)

        self.image = pygame.transform.rotate(self.image_copy, self.angle * 180 / math.pi)
        self.rect = self.image.get_rect()

        self.speedx= self.speed*math.cos(angle_to_player if turn else self.angle)
        self.speedy = -self.speed*math.sin(angle_to_player if turn else self.angle)


        self.speedx = self.speedx / self.slide
        self.speedy = self.speedy / self.slide

        self.floatx += self.speedx
        self.floaty += self.speedy
        self.rect.centerx = round(self.floatx)
        self.rect.centery = round(self.floaty)

        # rap around to the other side of screen
        if self.rect.left > width:
            self.rect.right = 0
            self.floatx = self.rect.centerx
        if self.rect.right < 0:
            self.rect.left = width
            self.floatx = self.rect.centerx
        if self.rect.bottom < 0:
            self.rect.top = height
            self.floaty = self.rect.centery
        if self.rect.top > height:
            self.rect.bottom = 0
            self.floaty = self.rect.centery

        self.health_bar.update(self.floatx-77,self.floaty+60,self.health)
        if self.health<=0:
            bombsoht_exp.play()
            exp_group.add(Explosion(self.rect.center))
            if power_up_manager.shield_avaiable>=3:
                power_up_manager.shield_avaiable-=1
                power_up_group.add(Sheild((self.rect.centerx,self.rect.centery+32)))
            if power_up_manager.shield_avaiable>=2:
                power_up_manager.shield_avaiable-=1
                power_up_group.add(Sheild((self.rect.centerx-32, self.rect.centery)))
            if power_up_manager.shield_avaiable>=1:
                power_up_manager.shield_avaiable-=1
                power_up_group.add(Sheild((self.rect.centerx +32, self.rect.centery)))
            if power_up_manager.bomb_shot_avaiable == 1:
                power_up_group.add(BombShot(self.rect.center))
                power_up_manager.bomb_shot_avaiable=0
            level.bosses_killed+=1
            self.kill()

    def shoot(self):
        boss_bullet_sound.play()
        bullet=FireBall(self.floatx,self.floaty,self.angle)
        boss_bullet_group.add(bullet)

    def hit(self):
        pass

def collision():
    bullet_hit = pygame.sprite.groupcollide(asteroid_group, bullets_group, False, not player.pierce_shot)
    if not player.pierce_shot:
        if bullet_hit:
            exp_sound.play()
            for asteroid in bullet_hit:
                if isinstance(asteroid,HealthAsteroid):
                    asteroid.health-=1
                asteroid.hit()
    else:
        if bullet_hit:
            for asteroid in bullet_hit:
                bullets=bullet_hit[asteroid]
                for bullet in bullets:
                    if bullet not in asteroid.hit_by:
                        exp_sound.play()
                        asteroid.hit_by.append(bullet)
                        if isinstance(asteroid, HealthAsteroid):
                            asteroid.health -= 1
                        asteroid.hit()
                        bullet.things_hit += 1
                    if bullet.things_hit>=2:
                        bullet.die()

    for boss in boss_group:
        bullet_hit = pygame.sprite.spritecollide(boss, bullets_group, not player.pierce_shot, pygame.sprite.collide_circle)
        if boss.fighting:
            if not player.pierce_shot:
                if bullet_hit:
                    for _ in bullet_hit:
                        boss.health -= 1
            else:
                if bullet_hit:
                    for hit in bullet_hit:
                        if hit not in boss.hit_by:
                            boss.hit_by.append(hit)
                            for _ in bullet_hit:
                                boss.health -= 1
                            hit.things_hit += 1
                        if hit.things_hit >= 2:
                            bullet.die()

    bombs_hit = pygame.sprite.groupcollide(bombs_group, asteroid_group, False, False)
    if bombs_hit:
        for bomb in bombs_hit:
            bomb.die()

    bombs_hit = pygame.sprite.groupcollide(bombs_group, boss_group, False, False)
    if bombs_hit:
        for bomb in bombs_hit:
            bomb.die()

    if player.living and not level.grace_period:
        player_astroid_col = pygame.sprite.spritecollide(player, asteroid_group, True, pygame.sprite.collide_circle)
        for asteroid in player_astroid_col:
            if isinstance(asteroid, HealthAsteroid):
                try:
                    health_bar_group.remove(asteroid.health_bar)
                except ValueError:
                    print('health bar error')
        if player_astroid_col:
            player.hit()
        if pygame.sprite.spritecollide(player, boss_group, False, pygame.sprite.collide_circle):
            player.die()
        player_boss_bullet_col = pygame.sprite.spritecollide(player, boss_bullet_group, True, pygame.sprite.collide_circle)
        if player_boss_bullet_col:
            player.hit()

    power_up_col = pygame.sprite.spritecollide(player, power_up_group, True, pygame.sprite.collide_circle)
    for power_up in power_up_col:
        power_up_sound.play()
        power_up.collected()

def restart():
    global now,pause,last_exp,health_bar_group,bullets_group,player_group,asteroid_group,exp_group,power_up_group,bombs_group,boss_bullet_group,boss_group,player,power_up_manager,level
    update_game_date()

    pause=False

    now = 0
    bullets_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    exp_group = pygame.sprite.Group()
    power_up_group = pygame.sprite.Group()
    bombs_group = pygame.sprite.Group()
    boss_bullet_group = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    health_bar_group = []

    player = Player()
    player_group.add(player)
    power_up_manager = PowerUpManager()


    '''power_up_group.add(Sheild((100, 300)), Sheild((200, 300)), Sheild((300, 300)),
                       MultipleShot((100,400)),MultipleShot((200,400)),MultipleShot((300,400)),
                       Speed((100,500)),FireRate((200,500)),BombShot((300,500)),Nuke((200,600)),PierceShot((200,700)))'''

    level = Level(0)
    last_exp = now

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def get_angle(x1,y1,x2,y2):
    return math.atan2(-(y2-y1),x2-x1)

def get_closest_player(x,y,wid,hei):
    wid = 0 if x>0 or x<width else wid
    hei = 0 if x > 0 or x < height else hei
    d=[distance(x,y,player.floatx,player.floaty),distance(x,y,player.floatx+(width+wid),player.floaty+(height+hei)),distance(x,y,player.floatx+(width+wid),player.floaty),distance(x,y,player.floatx+(width+wid),player.floaty-(height+hei)),distance(x,y,player.floatx,player.floaty-(height+hei)),distance(x,y,player.floatx-(width+wid),player.floaty-(height+hei)),distance(x,y,player.floatx-(width+wid),player.floaty),distance(x,y,player.floatx-(width+wid),player.floaty+(height+hei)),distance(x,y,player.floatx,player.floaty+(height+hei))]
    xy=[(player.floatx,player.floaty),(player.floatx+width,player.floaty+height),(player.floatx+width,player.floaty),(player.floatx+width,player.floaty-height),(player.floatx,player.floaty-height),(player.floatx-width,player.floaty-height),(player.floatx-width,player.floaty),(player.floatx-width,player.floaty+height),(player.floatx,player.floaty+height)]
    return xy[d.index(min(d))]

def all_distances(center,distance):
    hits=[]
    cx=center[0]
    cy=center[1]
    for astroid in asteroid_group:
        ax=astroid.rect.center[0]
        ay = astroid.rect.center[1]
        if math.sqrt((cx-ax)**2+(cy-ay)**2)<=distance:
            hits.append(astroid)
    return hits

def draw_text(surf, text, size, x, y,top_left=False,color=white):
    font = pygame.font.Font(font_name, size)
    text_surface=font.render(text, True, color)
    text_rect=text_surface.get_rect()
    if not top_left:
        text_rect.midtop=(x,y)
    else:
        text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)

def change_key(key,button):
    global changing_key
    changing_key=key
    button.sprite=press_key

def update_game_date():
    global highest_level,asteroid_destroyed,bosses_killed,left_key,up_key,right_key,down_key,shoot_key,pause_key
    data=read_game_date()
    highest_level = data['highest_level']
    asteroid_destroyed = data['asteroid_destroyed']
    bosses_killed = data['bosses_killed']
    left_key = data['left_key']
    up_key = data['up_key']
    right_key = data['right_key']
    down_key = data['down_key']
    shoot_key = data['shoot_key']
    pause_key = data['pause_key']

def read_game_date():
    data={}
    with open(resource_path_out('assets_and_data\\game_data.txt'), 'r') as file:
        lines = file.readlines()
        lines = [(line.rstrip() + '\n') for line in lines]
        for indx, line in enumerate(lines):
            colon_index = line.find(':')
            word = line[:colon_index]
            if word == 'highest_level':
                data['highest_level']=int(line[colon_index + 1:])
            if word == 'asteroid_destroyed':
                data['asteroid_destroyed']=int(line[colon_index + 1:])
            if word == 'bosses_killed':
                data['bosses_killed']=int(line[colon_index + 1:])
            if word == 'up_key':
                data['up_key'] = int(line[colon_index + 1:])
            if word == 'left_key':
                data['left_key'] = int(line[colon_index + 1:])
            if word == 'right_key':
                data['right_key'] = int(line[colon_index + 1:])
            if word == 'down_key':
                data['down_key'] = int(line[colon_index + 1:])
            if word == 'shoot_key':
                data['shoot_key'] = int(line[colon_index + 1:])
            if word == 'pause_key':
                data['pause_key'] = int(line[colon_index + 1:])

        file.close()
    return data

def write_game_date(value,change):
    things_changed=0
    with open(resource_path_out('assets_and_data\\game_data.txt'), 'r') as file:
        lines = file.readlines()
        lines = [(line.rstrip() + '\n') for line in lines]
        for indx, line in enumerate(lines):
            colon_index = line.find(':')
            word = line[:colon_index]
            if word == value:
                things_changed+=1
                lines[indx]=value+':'+str(change)+'\n'
    if things_changed==0:
        string=f'"{value}" not in game data'
        raise Exception(string)

    with open(resource_path_out('assets_and_data\\game_data.txt'), 'w') as file:
        file.writelines(lines)
        file.close()

def change_asteroid_color(surface,colors):
    #[(35, 206, 35),(39, 170, 29),(27, 160, 27)]
    change_color(surface, (103, 58, 183), pygame.Color(*colors[0]))
    change_color(surface, (69, 39, 160), pygame.Color(*colors[1]))
    change_color(surface, (40, 53, 147), pygame.Color(*colors[2]))
    change_missed_colors(surface, [(35, 206, 35),
                                   (39, 170, 29),
                                   (27, 160, 27),
                                   (0, 0, 0),
                                   (255, 255, 255)], pygame.Color(*colors[1]))

def change_color(surface,color1, color2):
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r,g,b,_=surface.get_at((x, y))
            if (r,g,b)==color1:
                r, g, b,_= color2
                surface.set_at((x, y), pygame.Color(r, g, b,255))

def change_missed_colors(surface,dont_change, color2):
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r,g,b,_=surface.get_at((x, y))
            if (r,g,b) not in dont_change:
                if r==b and r==g:
                    change_color=(0,0,0,0)
                else:
                    change_color=color2
                r, g, b,_= change_color
                surface.set_at((x, y), pygame.Color(r, g, b,255))

def menu_to_game():
    global game_running,menu_running
    restart()
    menu_running=False
    game_running=True

def game_to_menu():
    global game_running,menu_running
    update_game_date()
    menu_running=True
    game_running=False

def settings_to_menu():
    global in_settings
    update_game_date()
    in_settings=False

def menu_to_settings():
    global in_settings
    update_game_date()
    in_settings = True

def game():
    global now,running,pause
    clock.tick(fps)
    # prosses input and if the the window should close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #(pygame.key.key_code(pygame.key.name(event.key)))
            if event.key == pygame.K_SPACE:
                pass
            if event.key == pause_key:
                if player.living:
                    pause=not pause
            if event.key == pygame.K_r:
                print('')
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pause_key:
                if player.living:
                    pause = not pause

    # update
    if not pause:
        collision()
        asteroid_group.update()
        player_group.update()
        bullets_group.update()
        level.update()
        exp_group.update()
        bombs_group.update()
        boss_group.update()
        boss_bullet_group.update()
        bar.update(bar.x, bar.y,level.grace_period_time if level.between_rounds else (level.grace_period_time - (now - level.grace_start) if level.grace_period else 0))
        now += 1
        if not player.living:
            restart_button.upadate()
            main_menu_button.upadate()



    # draw
    screen.blit(backround, backround_rect)
    bullets_group.draw(screen)
    bombs_group.draw(screen)
    player_group.draw(screen)
    asteroid_group.draw(screen)
    power_up_group.draw(screen)
    boss_bullet_group.draw(screen)
    for i in health_bar_group:
        i.draw(screen)
    boss_group.draw(screen)
    exp_group.draw(screen)
    for bos in boss_group:
        if bos.fighting:
            bos.health_bar.draw(screen)
    if level.between_rounds or level.grace_period or level.timer_staying:
        draw_text(screen, f'Beginning of Round Invincibility', 19, width - 425, 90)
        bar.draw(screen)
    if not player.living:
        restart_button.draw(screen)
        main_menu_button.draw(screen)
    if pause:
        draw_text(screen, f'Paused', 100, round(width / 2), round(height / 2 - 250))
        main_menu_button2.upadate()
        main_menu_button2.draw(screen)

    draw_text(screen, f'Asteroids Destroyed', 24, width - 425, 10)
    draw_text(screen, f'{level.astroids_destoyed}', 24, width - 425, 50)
    draw_text(screen, f'Level:{level.get_level}', 25, width - 55, 20)
    if player.living == False:
        draw_text(screen, f'GAME OVER', 100, round(width / 2), round(height / 2 - 250))
    if player.shields >= 1:
        shield_display1.draw()
    if player.shields >= 2:
        shield_display2.draw()
    if player.shields >= 3:
        shield_display3.draw()
    power_up_manager.display_que_draw(screen)

    pygame.display.flip()
    #print(clock.get_fps())

def menu():
    global running, changing_key,now,mouse_change,can_click_button,can_click_button_time
    clock.tick(fps)
    # prosses input and if the the window should close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if changing_key:
                data=read_game_date()
                keys=['up_key','left_key','right_key','down_key','shoot_key',"pause_key"]
                keys.remove(changing_key)
                if event.key not in [data[key] for key in keys]:
                    #print(changing_key,event.key)
                    write_game_date(changing_key,event.key)
                    changing_key=None
                    update_game_date()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if changing_key:
                data=read_game_date()
                keys=['up_key','left_key','right_key','down_key','shoot_key',"pause_key"]
                keys.remove(changing_key)
                if event.button not in [data[key] for key in keys]:
                    #print(changing_key,event.button)
                    write_game_date(changing_key,event.button)
                    changing_key=None
                    update_game_date()
                    mouse_change = True
                    can_click_button = False
                    #print(mouse_change, can_click_button)
        if event.type == pygame.MOUSEBUTTONUP:
            if mouse_change == True:
                can_click_button = True
                can_click_button_time = now
                mouse_change = False
    if in_settings:
        screen.blit(menu_backround, menu_backround_rect)

        def add_arrow(key):
            if key in ['up','left','right','down']:
                return 'arrow '+key
            elif key=='':
                return 'left click'
            elif key=='':
                return 'right click'
            elif  key=='':
                return 'middle click'
            else:
                return key

        if not changing_key and can_click_button and (abs(can_click_button_time-now)>=1):
            #print(abs(can_click_button_time-now),can_click_button_time)
            mini_main_menu_button.upadate()

            change_up_key_button.upadate()
            change_left_key_button.upadate()
            change_right_key_button.upadate()
            change_down_key_button.upadate()
            change_shoot_key_button.upadate()
            change_pause_key_button.upadate()

        mini_main_menu_button.draw(screen)

        change_up_key_button.draw(screen)
        change_left_key_button.draw(screen)
        change_right_key_button.draw(screen)
        change_down_key_button.draw(screen)
        change_shoot_key_button.draw(screen)
        change_pause_key_button.draw(screen)

        draw_text(screen, f"KEY BINDS", 50, 10, 10, top_left=True, color=black)
        draw_text(screen, f"Up: {add_arrow(pygame.key.name(up_key))}", 30, 150, 70, top_left=True, color=black)
        draw_text(screen, f"Left: {add_arrow(pygame.key.name(left_key))}", 30, 150, 110, top_left=True, color=black)
        draw_text(screen, f"Right: {add_arrow(pygame.key.name(right_key))}", 30, 150, 150, top_left=True, color=black)
        draw_text(screen, f"Down: {add_arrow(pygame.key.name(down_key))}", 30, 150, 190, top_left=True, color=black)
        draw_text(screen, f"Shoot: {add_arrow(pygame.key.name(shoot_key))}", 30, 150, 230, top_left=True, color=black)
        draw_text(screen, f"Pause: {add_arrow(pygame.key.name(pause_key))}", 30, 150, 270, top_left=True, color=black)
        pygame.display.flip()
    else:
        # update
        play_button.upadate()
        settings_button.upadate()
        # draw
        screen.blit(menu_backround, menu_backround_rect)
        play_button.draw(screen)
        settings_button.draw(screen)
        draw_text(screen,f"Highest level: {highest_level}", 30, 10, 10, top_left=True, color=black)
        draw_text(screen, f"Asteroids destroyed: {asteroid_destroyed}", 30, 10, 50, top_left=True, color=black)
        draw_text(screen, f"Bosses killed: {bosses_killed}", 30, 10, 90, top_left=True, color=black)
        pygame.display.flip()
    now += 1
        # print(clock.get_fps())

update_game_date()

restart()

bar=LoadingBar((width - 489),120,130,20,level.grace_period_time)

restart_button=Button([restart_button1, restart_button2], (112 + 85, 400 - 120), (512 + 85, 525 - 120), restart)
main_menu_button=Button([main_menu_button1, main_menu_button2], (112 + 85, 400 + 40), (512 + 85, 525 + 40), game_to_menu)
main_menu_button2=Button([main_menu_button1, main_menu_button2], (112 + 85, 400 - 120), (512 + 85, 525 - 120), game_to_menu)
play_button=Button([play_button1, play_button2], (112+350, 440-350), (112+350+240, 440+75-350), menu_to_game)
mini_main_menu_button=Button([mini_main_menu_button1, mini_main_menu_button2], (112+350, 440-350), (112+350+240, 440+75-350), settings_to_menu)
settings_button=Button([settings_button1, settings_button2], (112+350, 440-350+100), (112+350+240, 440+75-350+100), menu_to_settings)
change_up_key_button=Button([change_key1, change_key2], (10, 75+0*40), (100+129, 75+32+0*40), [change_key,'up_key','self'])
change_left_key_button=Button([change_key1, change_key2], (10, 75+1*40), (100+129, 75+32+1*40), [change_key,'left_key','self'])
change_right_key_button=Button([change_key1, change_key2], (10, 75+2*40), (100+129, 75+32+2*40), [change_key,'right_key','self'])
change_down_key_button=Button([change_key1, change_key2], (10, 75+3*40), (100+129, 75+32+3*40), [change_key,'down_key','self'])
change_shoot_key_button=Button([change_key1, change_key2], (10, 75+4*40), (100+129, 75+32+4*40), [change_key,'shoot_key','self'])
change_pause_key_button=Button([change_key1, change_key2], (10, 75+5*40), (100+129, 75+32+5*40), [change_key,'pause_key','self'])

shield_display1=PowerUpDisplay(shield, (25+40, 35))
shield_display2=PowerUpDisplay(shield, (95+40, 35))
shield_display3=PowerUpDisplay(shield, (165+40, 35))

pierce_shot_display=PowerUpDisplay(pierce_shot_power_up, (105, 35))
multishot_display=PowerUpDisplay(bullet_power_up, (105, 35))
firerate_display=PowerUpDisplay(fire_rate, (105, 35))
bombshot_display=PowerUpDisplay(bomb_power_up, (105, 35))
speed_display=PowerUpDisplay(speed_power_up, (105, 35))

#power_up_group.add(Nuke((300,300)))

running=True
game_running=False
menu_running=True
in_settings=False
changing_key=None
pause=False
mouse_change=False
can_click_button=True
can_click_button_time=0


while running:
    if game_running:
        game()
    elif menu_running:
        menu()