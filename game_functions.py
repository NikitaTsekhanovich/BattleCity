import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, player_tank, bullets):
    if event.key == pygame.K_d or \
            event.key == pygame.K_RIGHT:
        player_tank.moving_right = True
    elif event.key == pygame.K_a or \
            event.key == pygame.K_LEFT:
        player_tank.moving_left = True
    elif event.key == pygame.K_s or \
            event.key == pygame.K_DOWN:
        player_tank.moving_down = True
    elif event.key == pygame.K_w or \
            event.key == pygame.K_UP:
        player_tank.moving_up = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, player_tank)
            bullets.add(new_bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, player_tank):
    if event.key == pygame.K_d or \
            event.key == pygame.K_RIGHT:
        player_tank.moving_right = False
    elif event.key == pygame.K_a or \
            event.key == pygame.K_LEFT:
        player_tank.moving_left = False
    elif event.key == pygame.K_s or \
            event.key == pygame.K_DOWN:
        player_tank.moving_down = False
    elif event.key == pygame.K_w or \
            event.key == pygame.K_UP:
        player_tank.moving_up = False


def check_events(ai_settings, screen, player_tank, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player_tank, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player_tank)


def update_screen(ai_settings, screen, player_tank, bullets):
    screen.fill(ai_settings.back_ground_color)
    player_tank.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()
