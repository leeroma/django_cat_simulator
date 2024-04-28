from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from random import randint


class Cat(models.Model):
    name = models.CharField(max_length=100, default='Alex')
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    happiness = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    fullness = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    state = models.TextField(default='happy')

    def set_state(self, state):
        self.state = state

    def feed(self):
        if self.state != 'sleep':
            self.fullness += 15
            self.happiness += 5
            self.set_state('happy')
            if self.fullness == 100:
                self.happiness -= 30
            self.check_state()

    def sleep(self):
        self.set_state('sleep')

    def play(self):
        if self.state == 'sleep':
            self.set_state('angry')
            self.happiness -= 5

        else:
            if not self.failure():
                self.happiness += 15
                self.fullness -= 10
                self.check_state()
            else:
                self.happiness = 0
                self.set_state('sad')

    def check_state(self):
        if self.happiness <= 30:
            self.set_state('sad')
        else:
            self.set_state('happy')

    def check_stats(self):
        if self.happiness < 0:
            self.happiness = 0

        if self.fullness < 0:
            self.fullness = 0

        if self.happiness > 100:
            self.happiness = 100

        if self.fullness > 100:
            self.fullness = 100

    @staticmethod
    def failure():
        number = randint(1, 3)
        return number == 1
