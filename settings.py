class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 740
        self.bg_color = (30,30,30)
       

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (150,150,150)
        self.bullets_allowed = 5

        # Alien Settings
        self.fleet_drop_speed = 10

        # Ship Settings
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # How quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.5

        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)