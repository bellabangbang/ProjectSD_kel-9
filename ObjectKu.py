import pygame
class object:
    def __init__(self, coordinate : list, img : list, width: int, height: int) -> None:
        self.img = img
        self.x =  coordinate[0]
        self.y = coordinate[1]
        self.width = width
        self.height = height
        self.frame = 0 # default
        self.arahKanan = True
        self.speedX = 0
        self.speedY = 0

    def update(self, coorEnd : list, fps):
        self.x += 3*self.speedX 
        self.y += 3*self.speedY

        self.frame += 1

        if self.frame >= len(self.img):
            self.frame = 0
    
    def draw(self, screen):
        screen.blit(self.img[self.frame], (self.x, self.y))
    
    def cekArah(self, coordDituju: list):
        # cek depan atau ke belakang
        if self.x > coordDituju[0] and self.arahKanan:
            self.flip_arahX()
            self.arahKanan = False
        elif self.x < coordDituju[0] and not(self.arahKanan):
            self.flip_arahX()
            self.arahKanan = True
            
    # flip gambar
    def flip_arahX(self): # pencerminan terhadap garis y
        for i in range(len(self.img)):
            self.img[i] = pygame.transform.flip(self.img[i], True, False)
    

    def move(self,screen, background, vertex2):
        running = True
        clock =  pygame.time.Clock()
        gerak = True
        animation_cooldown = 100
        last_update = pygame.time.get_ticks()

        while gerak:
            # update background
            screen.fill((0,0,0))
            screen.blit(background, (0,0))

            # gambar sprite
            self.draw(screen)

            # update run
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                # update
                self.update([vertex2.hitbox[0] + vertex2.hitbox[2]/2, vertex2.hitbox[1] + (vertex2.hitbox[3]/2)], 60)
                last_update = current_time 

                # cek apakah sudah sampai
                if vertex2.collition(self):
                    print('masuk', vertex2.nama)
                    gerak = False
                    self.frame = 0

                    # cek hartaKarun
                    if vertex2.hartaKarun:
                        vertex2.hartaKarun() # pindah ke screen ke harta karun terus endingScreen

            pygame.display.update()
            clock.tick(60)
                    

