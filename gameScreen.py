import pygame
import sys, random, time
import Graphku, ObjectKu
from pygame.locals import *
from Button import Button,Sound
from pygame import mixer # buat music

# >>> ASSET
# screen
width = 600
height = 360 
screen = pygame.display.set_mode((width,height))

# Background
background = pygame.image.load("asset\\in_game_background2.png")
background = pygame.transform.scale(background, (width,height))

# Background Story
story_bg = pygame.image.load("asset\\peta_kakek_milo.png")
story_bg = pygame.transform.scale(story_bg, (width,height))

# path music
path_game_bgm = "asset\\game.mp3"
path_story_bgm = "asset\\kakek.mp3"      

# >> Asset Graph
popImg = pygame.image.load("asset\Pop Up image\\auditW.png")
AuditoriumW = Graphku.vertex("Auditorium W",-15,63,60,30, popImg)

popImg = pygame.image.load("asset\Pop Up image\perpus.png")
Perpustakaan = Graphku.vertex("Perpustakaan",-10,163,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\eh.png")
RadiusPrawiro = Graphku.vertex("Entrance Hall",35,95,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\kantinP.png")
KantinP = Graphku.vertex("Kantin P",130,103,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\kolamHijau.png")
KolamHijau = Graphku.vertex("Kolam Hijau",205,45,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\labStudio.png")
LabStudio = Graphku.vertex("Lab Studio",165,163,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\labSI.png")
LabSi = Graphku.vertex("Lab SI",250,210,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\labPuskom.png")
LabPuskom = Graphku.vertex("Lab Puskom",285,125,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\loveGarden.png")
LoveGarden = Graphku.vertex("Love Garden",360,55,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\\rooftop.png")
RooftopGarden = Graphku.vertex("Rooftop Garden",385,180,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\kolamQ.png")
KolamQ = Graphku.vertex("Kolam Q",445,110,60,30,popImg)

popImg = pygame.image.load("asset\Pop Up image\\light.png")
Light = Graphku.vertex("Light",500,70,60,30, popImg)

popImg = pygame.image.load("asset\Pop Up image\\amphiQ.png")
AuditoriumQ = Graphku.vertex("Amphitheater Q",500,210,60,30,popImg)

RouteUKP = Graphku.Graph()
RouteUKP.add_vertex(AuditoriumW)
RouteUKP.add_vertex(Perpustakaan)
RouteUKP.add_vertex(RadiusPrawiro)
RouteUKP.add_vertex(KantinP)
RouteUKP.add_vertex(KolamHijau)
RouteUKP.add_vertex(LabStudio)
RouteUKP.add_vertex(LabSi)
RouteUKP.add_vertex(LabPuskom)
RouteUKP.add_vertex(LoveGarden)
RouteUKP.add_vertex(RooftopGarden)
RouteUKP.add_vertex(KolamQ)
RouteUKP.add_vertex(Light)
RouteUKP.add_vertex(AuditoriumQ)

RouteUKP.add_edge(AuditoriumW,RadiusPrawiro)
RouteUKP.add_edge(Perpustakaan,RadiusPrawiro)
RouteUKP.add_edge(KantinP,RadiusPrawiro)
RouteUKP.add_edge(KantinP,KolamHijau)
RouteUKP.add_edge(KantinP,LabStudio)
RouteUKP.add_edge(LabStudio,LabPuskom)
RouteUKP.add_edge(LabStudio,LabSi)
RouteUKP.add_edge(LabSi,LabPuskom)
RouteUKP.add_edge(LabPuskom,KolamHijau)
RouteUKP.add_edge(KolamHijau,LoveGarden)
RouteUKP.add_edge(LoveGarden,RooftopGarden)
RouteUKP.add_edge(LoveGarden,KolamQ)
RouteUKP.add_edge(RooftopGarden,KolamQ)
RouteUKP.add_edge(RooftopGarden,AuditoriumQ)
RouteUKP.add_edge(AuditoriumQ,KolamQ)
RouteUKP.add_edge(KolamQ,Light)

# list vertex
arrVertex = RouteUKP.get_Arr()


# option button bg
op_img = pygame.image.load('asset/assets/optionbg.png')
op_img = pygame.transform.scale(op_img,(width,height))
# pause bg
pause_img = pygame.image.load('asset/assets/pausebg.jpg')
pause_img = pygame.transform.scale(pause_img, (width, height))
mouse_pos = pygame.mouse.get_pos()

mixer.init()
click_effect = mixer.Sound('asset\mixkit-arcade-game-jump-coin-216.wav')

pygame.init()
pygame.display.set_caption("Finding PCU's Treasure")
width = 600
height = 360
SCREEN = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('asset/postermm.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

op_img = pygame.image.load('asset/assets/optionbg.png')
op_img = pygame.transform.scale(op_img,(width,height))

bg_story_awal = pygame.image.load('asset\\foto_kakek.png')
bg_story_kedua = pygame.image.load('asset\\peta_kakek_milo.png')
bg_loading = pygame.image.load('asset\\loading.png')
bg_harta = pygame.image.load('asset\\harta_bg.png')
harta = pygame.image.load('asset\\harta.png')

# clock 
clock = pygame.time.Clock()

# >> Asset Dog
player_foot = [20, 20]
player_listAnimate = []
player_img_step = 9

for x in range(player_img_step):
    img = pygame.image.load("asset\\KarakterAfterCrop\\"+ str(x+1) + ".png").convert_alpha()
    img = pygame.transform.scale(img, (30,30) )
    player_listAnimate.append(img)


# >>> METHOD
# fungsi bantuan / tambahan
def get_x_y_mouse(pos):
    x,y = pos
    return x , y

def get_font(size):
    return pygame.font.Font("asset/font/mm.ttf", size)

def print_path(path : list[Graphku.vertex]):
    for i in range(len(path)):
        print(path[i].nama , end='-->')

def PopUp(nama,Start):
    pygame.display.set_caption("Finding PCU's Treasure")
    for vertex in RouteUKP.vertices.keys():
        if nama == vertex.nama:
            pop = vertex.popUpImg
    while True:
        # loop tiap event
        curr = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(background,(0,0))
        screen.blit(pop,(0,0))
        if curr-Start > 2:
            break
        pygame.display.update()

# >> SCREEN
def hartaKarun(soundOn):
    pygame.display.set_caption("Finding PCU's Treasure")
    x_sprite = 0

    # pygame run terus di while ini
    while True:
        # loop tiap event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                EndingScreen(soundOn)

        # draw all our elements
        # update everything
        screen.fill((255,255,255))
        screen.blit(bg_harta,(0,0))
        screen.blit(harta,(width/2-43,height/2-50),(x_sprite * 89,0,89,128))

        ready_text = get_font(30).render("You found the treasure", True, "#FFF000")
        ready_rect = ready_text.get_rect(center=(300, 50))
        ready_text1 = get_font(31).render("You found the treasure", True, "#000000")
        ready_rect1 = ready_text1.get_rect(center=(300, 50))

        ready_text2 = get_font(30).render("Congratulations!", True, "#FFF000")
        ready_rect2 = ready_text.get_rect(center=(365, 80))
        ready_text3 = get_font(31).render("Congratulations!", True, "#000000")
        ready_rect3 = ready_text1.get_rect(center=(367, 80))

        screen.blit(ready_text1, ready_rect1)
        screen.blit(ready_text, ready_rect)
        screen.blit(ready_text3, ready_rect3)
        screen.blit(ready_text2, ready_rect2)

        # looping lagi ke awal
        if x_sprite*89 >= 3026:
            x_sprite = 0

        # atur 60fps
        # while true loop gaakan run lebih cepat dari 60fps
        clock.tick(10) 
        x_sprite += 1

        pygame.display.update()


# buat fungsi screen game
def gameScreen(soundOn):
    # random harta karun
    randomAngka = random.randint(0,11)

    # reset visited 
    RouteUKP.reset_visited()
    
    # reset arahAnjing

    # set 
    print(arrVertex[randomAngka])
    RouteUKP.listVertex[arrVertex[randomAngka]].hartaKarun = True

    # posisi awal dog
    dog = ObjectKu.object([RouteUKP.listVertex['Kolam Hijau'].hitbox[0] + RouteUKP.listVertex['Kolam Hijau'].hitbox[2]/2, RouteUKP.listVertex['Kolam Hijau'].hitbox[1] + RouteUKP.listVertex['Kolam Hijau'].hitbox[3]/2], player_listAnimate, 27,27)
    counter= 1

    Start = time.time()
    # pop up kolam hijau
    PopUp('Kolam Hijau', Start)
    RouteUKP.listVertex['Kolam Hijau'].visited = True

    pygame.init() # inisialisasi modul pygame
    pygame.display.set_caption('Game Screen')

    if soundOn == True:
        # jalankan music
        mixer.music.load(path_game_bgm)
        mixer.music.set_volume(0.3)
        mixer.music.play(-1) # repeat

    last_update = pygame.time.get_ticks()
    last_update_vertex = pygame.time.get_ticks()
    animation_cooldown = 100
    frame = 0
    update_speed = True

    # cek gerak
    gerak = False
    coorEnd = [0,0]

    # jalan kan screen
    running = True
    clock = pygame.time.Clock()
    posisi_x = 50
    posisi_y = 175

    path_dfs = RouteUKP.dfs_path('Kolam Hijau')
    print_path(path_dfs)

    while running:
        # update background
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        pause_button = Button(pygame.image.load("asset/assets/pause.png"), 
                        (540, 20), "PAUSE", get_font(20), "brown", "white")
        pause_button.changeColor(pygame.mouse.get_pos())
        pause_button.update(screen)

        # gambar sprite
        dog.draw(screen)
        # event yang terjadi
        for event in pygame.event.get():
            # buat cek mouse klik
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.checkMousePos(pygame.mouse.get_pos()):
                    click_effect.play()
                    PauseScreen()

            # buat tutup screen
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # # jika gerak karena belum sampai coorEnd
        # looping dfs
        # counter path
        vertexDituju = path_dfs[counter]
        detikNow = pygame.time.get_ticks()
        gerak = True
        
        # cara fix speed ketika masih move
        if update_speed:
            print(vertexDituju.nama)
            # update speed nya
            dog.speedX = ((vertexDituju.hitbox[0] + vertexDituju.hitbox[2]/2) - (dog.x+dog.width/2)) /60 # (coorEnd(titik tengah box) - coorAwal(titik tengah dog))/fps
            dog.speedY = ((vertexDituju.hitbox[1] + vertexDituju.hitbox[3]/2) - (dog.y+dog.height/2)) /60

            # cek flip
            dog.cekArah((vertexDituju.hitbox[0] + (vertexDituju.hitbox[2]/2) , vertexDituju.hitbox[1] + (vertexDituju.hitbox[3]/2) ))
            print('arah kanan :', dog.arahKanan)
            # tutup
            update_speed = False

        # jika gerak karena belum sampai coorEnd 
        if gerak:
            # update run
            curerent_time = pygame.time.get_ticks()
            if curerent_time - last_update >= animation_cooldown:
                frame +=1

                # update
                dog.update([vertexDituju.hitbox[0] + vertexDituju.hitbox[2]/2,vertexDituju.hitbox[1] + vertexDituju.hitbox[3]], 60)

                last_update = curerent_time 

                # cek apakah sudah sampai
                if vertexDituju.collition_titik([(dog.x + dog.width/2), (dog.y + dog.height/2)]):
                    for vertex in RouteUKP.vertices.keys():
                        if vertex.nama == path_dfs[counter].nama:
                            if vertex.visited == False:
                                Start = time.time()
                                PopUp(path_dfs[counter].nama,Start)
                                vertex.visited = True
                    
                    gerak = False

                    # update frame diam
                    dog.frame = 0
                    # last update pindah vertex
                    last_update_vertex = pygame.time.get_ticks() 
                    # update tujuan vertex
                    counter += 1 
                    # update speed
                    update_speed = True

                    if counter == len(path_dfs)-1:
                        print('selesai')
                        # looping infinite
                        last_update_vertex = -2000

                    if vertexDituju.hartaKarun:
                        hartaKarun(soundOn)

                    # update background
                    screen.fill((0,0,0))
                    screen.blit(background, (0,0))
                    dog.draw(screen)
                    pygame.display.update()

                    # sleep 2 detik
                    print(time.sleep(2))

        # mengubah mouse jadi tangan
        if pause_button.checkMousePos(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        pygame.display.update()
        clock.tick(60)

def PauseScreen():
    pygame.display.set_caption("Pause")

    cek_pause = True
    while cek_pause:
        pause_pos = pygame.mouse.get_pos()
    
        screen.blit(pause_img, (0, 0))

        resume_button = Button(pygame.image.load("asset/assets/3.png"), 
                        (300, 140), "RESUME", get_font(40), "#7c0a02", "white")
    
        exit_button = Button(pygame.image.load("asset/assets/4.png"), 
                    (300, 210), "EXIT", get_font(40), "#7c0a02", "white")

        arrButton = [resume_button, exit_button]
        for b in arrButton:
            b.changeColor(pause_pos)
            b.update(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_effect.play()
                if resume_button.checkMousePos(pause_pos):
                    cek_pause = False
                if exit_button.checkMousePos(pause_pos):
                    pygame.quit() 
                    sys.exit()
        
        # mengubah mouse jadi tangan
        if resume_button.checkMousePos(pause_pos) or exit_button.checkMousePos(pause_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
                
        pygame.display.update()


def EndingScreen(soundOn):
    pygame.display.set_caption("End")

    while True:
        end_pos = pygame.mouse.get_pos()
        screen.blit(pause_img, (0, 0))

        end_text = get_font(30).render("Thank you for playing!", True, "#7c0a02")
        end_text2 = get_font(31).render("Thank you for playing!", True, "white")
        end_text3 = get_font(31).render("Thank you for playing!", True, "#7c0a02")

        end_rect = end_text.get_rect(center=(300, 100))
        end_rect2 = end_text.get_rect(center=(296, 101))
        end_rect3 = end_text.get_rect(center=(296, 97))

        screen.blit(end_text3, end_rect3)
        screen.blit(end_text2, end_rect2)
        screen.blit(end_text, end_rect)

        replay_button = Button(pygame.image.load("asset/assets/1.png"), 
                        (300, 180), "REPLAY", get_font(34), "#7c0a02", "white")

        mm_button = Button(pygame.image.load("asset/assets/2.png"), 
                    (300, 250), "MAIN MENU", get_font(30), "#7c0a02", "white")

        arrButton = [replay_button, mm_button]
        for b in arrButton:
            b.changeColor(end_pos)
            b.update(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_effect.play()
                if replay_button.checkMousePos(end_pos):
                    fotoKakek(soundOn)
                if mm_button.checkMousePos(end_pos):
                    MainMenuScreen(soundOn)
        
        # mengubah mouse jadi tangan
        if replay_button.checkMousePos(end_pos) or mm_button.checkMousePos(end_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
                
        pygame.display.update()

def get_font(size):
    return pygame.font.Font("asset/font/mm.ttf", size)

def MainMenuScreen(soundOn):
    pygame.display.set_caption("Main Menu")
    
    # buat set sound
    if soundOn == True:
        mixer.init()
        mixer.music.load('asset/assets/mainmenu.wav')
        mixer.music.set_volume(0.3) # setting volume dikecilin jadi 30% 
        mixer.music.play(-1)

    while True:
        SCREEN.blit(bg_img,(0,0))
        menu_pos = pygame.mouse.get_pos()

        play_button = Button(pygame.image.load("asset/assets/3.png"), 
                    (460, 180), "START", get_font(40), "white", "black")
        options_button = Button(pygame.image.load("asset/assets/1.png"), 
                    (460, 250), "OPTIONS", get_font(35), "white", "black")
        exit_button = Button(pygame.image.load("asset/assets/4.png"), 
                    (460, 320), "EXIT", get_font(40), "white", "black")

        arrButton = [play_button, options_button, exit_button]
        for b in arrButton:
            b.changeColor(menu_pos)
            b.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_effect.play()
                if play_button.checkMousePos(menu_pos):
                    StartScreen(soundOn)
                if options_button.checkMousePos(menu_pos):
                    OptionsScreen()
                if exit_button.checkMousePos(menu_pos):
                    pygame.quit() 
                    sys.exit()
        
        # mengubah mouse jadi tangan
        if play_button.checkMousePos(menu_pos) or options_button.checkMousePos(menu_pos) or exit_button.checkMousePos(menu_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                
        pygame.display.update()



def fotoKakek(soundOn):
    pygame.display.set_caption("StoryLine")

    if soundOn == True:
        mixer.init()
        mixer.music.load('asset/kakek.mp3')
        mixer.music.play()

    font = pygame.font.SysFont('bahnschrift',18)
    messageFirst = 'Kakek Milo meninggalkan sebuah surat wasiat yang bertuliskan..'
    messages = ['"Hai cucuku Milo, ada pesan yang belum kakek sampaikan"             ',
                '"Terdapat sebuah harta karun yang kakek simpan di UKP"             ',
                '"Carilah harta karun tersebut dengan bantuan peta ini"            ',
                '"Harta karun tersebut berada di salah satu spot pada peta"  ']

    # awalnya mau dibuat tulisannya itu nda ada/empty
    snip = font.render('', True, 'black')
    counterFirst = 0
    counter = 0

    # 60(kan tadi fps 60) karakter per 3 detik
    speed = 4
    speed2 = 6
    active_message = 0
    # ambil 1 message dari list messages
    message = messages[active_message]
    done = False

    clock = pygame.time.Clock()
    waktu_awal = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # pas di klik kan curr_time jadi static_time
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    fadeOut(7)
                    pygame.time.delay(620)
                    LoadingScreen(soundOn)

        SCREEN.fill((0,0,0)) 
        SCREEN.blit(bg_story_awal, (0,0))

        if counterFirst < speed * len(messageFirst):
            counterFirst+= 1
        snip = font.render(messageFirst [0:counterFirst//speed], True, 'black')
        SCREEN.blit(snip, (37, 313))

        waktu_diFoto = pygame.time.get_ticks() - waktu_awal 

        if waktu_diFoto > 7500:
            SCREEN.fill((0,0,0))
            SCREEN.blit(bg_story_kedua, (0,0))

            # semua message undah ditampilin, tapi belum sampai di last message dari list
            if done and active_message < len(messages) - 1:
                active_message += 1
                # di reset donenya, soalnya kan emang blum selesai semua listnya
                done = False
                # reset messagenya
                message = messages[active_message]
                # untuk restartnya
                counter = 0

            # kalau belum nampilin semua karakter di layar
            if  counter < speed2 * len(message):
                counter+= 1
            elif counter >= speed2 * len(message):
                done = True
            # ambil sebagian message, dari awal(0) sampai ke counter floor(untuk membulatkan ke bawah) devided by speed
            snip = font.render(message[0:counter//speed2], True, 'black')
            # pakai 1/speed, supaya bisa lebih faster
            SCREEN.blit(snip, (61, 25))

            if waktu_diFoto > 38000:
                fadeOut(8)
                pygame.time.delay(700)
                LoadingScreen(soundOn)

        pygame.display.update()
        clock.tick(60)

def fadeOut(waktu):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)

        SCREEN.fill((210,210,210))
        SCREEN.blit(fade, (0,0))
        pygame.display.update()
        # akan pause sebanyak brp milisecond
        pygame.time.delay(waktu)

def StartScreen(soundOn):
    fotoKakek(soundOn)

def OptionsScreen():
    pygame.display.set_caption("Options")
    soundOn = 1 # buat kasih value di if else
    while True:
        opt_pos = pygame.mouse.get_pos()
        SCREEN.blit(op_img,(0,0))

        sound_on = pygame.image.load('asset/assets/soundon.png')
        sound_off = pygame.image.load('asset/assets/soundoff.png')

        sound_on_b = Sound(sound_on, 350, 148)
        sound_off_b = Sound(sound_off, 390, 148)

        sound_text = get_font(40).render("SOUND", True, "#7c0a02")
        sound_rect = sound_text.get_rect(center = (260, 150))

        SCREEN.blit(sound_text, sound_rect)
        sound_on_b.update(SCREEN)
        sound_off_b.update(SCREEN)

        mm_button = Button(pygame.image.load("asset/assets/mmbg.png"), (285, 260), 
                    "MAIN MENU", get_font(40), "#7c0a02", "white")
        mm_button.changeColor(opt_pos)
        mm_button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mm_button.checkMousePos(opt_pos):
                    click_effect.play()
                    if soundOn == 1 :
                        MainMenuScreen(True)
                    else:
                        MainMenuScreen(soundOn)
                if sound_on_b.checkMousePos(opt_pos):
                    click_effect.play()
                    mixer.music.play(-1)
                    soundOn = True
                if sound_off_b.checkMousePos(opt_pos):
                    click_effect.play()
                    mixer.music.stop()
                    soundOn = False

        # mengubah mouse jadi tangan
        if mm_button.checkMousePos(opt_pos) or sound_on_b.checkMousePos(opt_pos) or sound_off_b.checkMousePos(opt_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 

        pygame.display.update()


def LoadingScreen(soundOn):
    # buat loading bar dari cerita storyline ke ingame
    pygame.display.set_caption("Loading...")

    if soundOn == True:
        mixer.init()
        mixer.music.load('asset/assets/mainmenu.wav')
        mixer.music.set_volume(0.3)
        mixer.music.play()

    speed = 65
    fps = 60
    inner_rect = [150,70,0,250]
    warna = ((255,255,0))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if inner_rect[2] < 350:
            inner_rect[2] += speed/fps

        elif inner_rect[2] >= 350:
            gameScreen(soundOn)

        SCREEN.fill((255,255,255))
        pygame.draw.rect(SCREEN,warna,(inner_rect[0], inner_rect[1], int(inner_rect[2]), inner_rect[3]))
        SCREEN.blit(bg_loading, (0,0))

        ready_text = get_font(30).render("Get everything ready...", True, "#FFF000")
        ready_rect = ready_text.get_rect(center=(300, 50))
        ready_text1 = get_font(31).render("Get everything ready...", True, "#000000")
        ready_rect1 = ready_text1.get_rect(center=(300, 50))

        SCREEN.blit(ready_text1, ready_rect1)
        SCREEN.blit(ready_text, ready_rect)

        clock.tick(fps)
        pygame.display.update()



if __name__ == "__main__":
    MainMenuScreen(True)










