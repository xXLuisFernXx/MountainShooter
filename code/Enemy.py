#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_direction = -1  # -1 para subir, 1 para descer
        self.speed_y = ENTITY_SPEED[self.name]  # Velocidade inicial vertical

    def move(self):
            self.rect.centerx -= ENTITY_SPEED[self.name]
            # Movimento vertical com lógica especial para Enemy3
            if self.name == 'Enemy3':
                # Atualiza a posição vertical com a velocidade atual
                self.rect.centery += self.speed_y * self.vertical_direction

                # Verifica colisão com as bordas superior e inferior
                if self.rect.top <= 0:
                    # Ao atingir a borda superior, desce com o dobro da velocidade
                    self.vertical_direction = 1
                    self.speed_y = ENTITY_SPEED[self.name] * 2
                elif self.rect.bottom >= WIN_HEIGHT:
                    # Ao atingir a borda inferior, sobe com a velocidade normal
                    self.vertical_direction = -1
                    self.speed_y = ENTITY_SPEED[self.name]



    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
