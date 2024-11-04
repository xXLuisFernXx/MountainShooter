#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_direction = -1
        self.speed_y = ENTITY_SPEED[self.name]

    def move(self):
            self.rect.centerx -= ENTITY_SPEED[self.name]
            # Vertical movement with special logic for Enemy3
            if self.name == 'Enemy3':
                # Updates the vertical position with the current speed
                self.rect.centery += self.speed_y * self.vertical_direction

                # Check for collision with top and bottom edges
                if self.rect.top <= 0:
                    # When it reaches the top edge, it descends twice as fast
                    self.vertical_direction = 1
                    self.speed_y = ENTITY_SPEED[self.name] * 2
                elif self.rect.bottom >= WIN_HEIGHT:
                    # Upon reaching the lower edge, it rises with normal speed
                    self.vertical_direction = -1
                    self.speed_y = ENTITY_SPEED[self.name]



    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
