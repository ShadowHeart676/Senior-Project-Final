import pygame
from CreateMidiFiles import *
from os import listdir
from os.path import isfile, join
from CreateMidiFiles import CreateNotes
from CreateFullSongs import CreateMusic
import os
import sys
import time

if getattr(sys, 'frozen', False):
   os.chdir(sys._MEIPASS)

os.path.join("CodeCreatedSounds")
os.path.join("CreatedMusic")
os.path.join("Images")


pygame.init()
pygame.mixer.init()
x = 1200
y = 750

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,128)
yellow = (255,242,0)


screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Digital Keyboard')
screen.fill(black)
pygame.display.flip()

background = pygame.image.load("Images/Keyboard Appearance Attempt.png")
background1_5 = pygame.image.load("Images/Keyboard Appearance Attempt 2.png") 
background2 = pygame.image.load("Images/RecordedPage.png")
startscreen = pygame.image.load("Images/Start Screen.png")
pmm = pygame.mixer.music

recordingfiles = [f for f in listdir("CreatedMusic") if isfile(join("CreatedMusic", f))]
song = []
noteDuration = []
recordingNum = len(recordingfiles)-1

MainScreen1 = False
MainScreen2 = False
Recordings = False
Starting = True
clicked = False
running = True
CreateNotes()

while running:
    if(Starting == True and MainScreen1 == False and MainScreen2 == False and Recordings == False):
        screen.blit(startscreen,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouseX,mouseY = pos
                if(mouseX > 443 and mouseX < 725 and mouseY > 660 and mouseY < 730):
                    Starting = False
                    MainScreen1 = True
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    if(MainScreen1 == True and Recordings == False and MainScreen2 == False):
        screen.blit(background, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowC.mid")
                    pmm.play()
                if event.key == pygame.K_2:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowC#.mid")
                    pmm.play()
                if event.key == pygame.K_3:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowD.mid")
                    pmm.play()
                if event.key == pygame.K_4:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowD#.mid")
                    pmm.play()
                if event.key == pygame.K_5:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowE.mid")
                    pmm.play()
                if event.key == pygame.K_6:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowF.mid")
                    pmm.play()
                if event.key == pygame.K_7:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowF#.mid")
                    pmm.play()
                if event.key == pygame.K_8:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowG.mid")
                    pmm.play()
                if event.key == pygame.K_9:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowG#.mid")
                    pmm.play()
                if event.key == pygame.K_0:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowA.mid")
                    pmm.play()
                if event.key == pygame.K_q:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowA#.mid")
                    pmm.play()
                if event.key == pygame.K_w:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowB.mid")
                    pmm.play()
                if event.key == pygame.K_e:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/C.mid")
                    pmm.play()
                if event.key == pygame.K_r:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/C#.mid")
                    pmm.play()
                if event.key == pygame.K_t:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/D.mid")
                    pmm.play()
                if event.key == pygame.K_y:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/D#.mid")
                    pmm.play()
                if event.key == pygame.K_u:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/E.mid")
                    pmm.play()
                if event.key == pygame.K_i:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/F.mid")
                    pmm.play()
                if event.key == pygame.K_o:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/F#.mid")
                    pmm.play()
                if event.key == pygame.K_p:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/G.mid")
                    pmm.play()
                if event.key == pygame.K_a:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/G#.mid")
                    pmm.play()
                if event.key == pygame.K_s:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/A.mid")
                    pmm.play()
                if event.key == pygame.K_d:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/A#.mid")
                    pmm.play()
                if event.key == pygame.K_f:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/B.mid")
                    pmm.play()
                if event.key == pygame.K_g:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighC.mid")
                    pmm.play()
                if event.key == pygame.K_h:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighC#.mid")
                    pmm.play()
                if event.key == pygame.K_j:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighD.mid")
                    pmm.play()
                if event.key == pygame.K_k:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighD#.mid")
                    pmm.play()
                if event.key == pygame.K_l:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighE.mid")
                    pmm.play()
                if event.key == pygame.K_z:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighF.mid")
                    pmm.play()
                if event.key == pygame.K_x:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighF#.mid")
                    pmm.play()
                if event.key == pygame.K_c:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighG.mid")
                    pmm.play()
                if event.key == pygame.K_v:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighG#.mid")
                    pmm.play()
                if event.key == pygame.K_b:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighA.mid")
                    pmm.play()
                if event.key == pygame.K_n:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighA#.mid")
                    pmm.play()
                if event.key == pygame.K_m:
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighB.mid")
                    pmm.play()
            if event.type == pygame.KEYUP:
                pmm.stop()
                pmm.unload()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouseX,mouseY = pos
                if(((mouseX > 68) & (mouseX < 98) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68) & (mouseX < 112) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowC.mid")
                    pmm.play()
                if(((mouseX > 99) & (mouseX < 130) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/LowC#.mid")
                    pmm.play()
                if(((mouseX > 130) & (mouseX < 150) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120) & (mouseX < 160) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowD.mid")
                    pmm.play()
                if(((mouseX > 150) & (mouseX < 180) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/LowD#.mid")
                    pmm.play()
                if(((mouseX > 180) & (mouseX < 210) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170) & (mouseX < 210) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowE.mid")
                    pmm.play()
                if(((mouseX > 220) & (mouseX < 245) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220) & (mouseX < 260) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowF.mid")
                    pmm.play()
                if(((mouseX > 245) & (mouseX < 280) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/LowF#.mid")
                    pmm.play()
                if(((mouseX > 280) & (mouseX < 300) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270) & (mouseX < 310) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowG.mid")
                    pmm.play()
                if(((mouseX > 300) & (mouseX < 328) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/LowG#.mid")
                    pmm.play()
                if(((mouseX > 328) & (mouseX < 348) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320) & (mouseX < 360) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowA.mid")
                    pmm.play()
                if(((mouseX > 348) & (mouseX < 380) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/LowA#.mid")
                    pmm.play()
                if(((mouseX > 380) & (mouseX < 410) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368) & (mouseX < 410) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/LowB.mid")
                    pmm.play()
                
                if(((mouseX > 68+347) & (mouseX < 98+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68+347) & (mouseX < 112+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/C.mid")
                    pmm.play()
                if(((mouseX > 99+347) & (mouseX < 130+347) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/C#.mid")
                    pmm.play()
                if(((mouseX > 130+347) & (mouseX < 150+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120+347) & (mouseX < 160+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/D.mid")
                    pmm.play()
                if(((mouseX > 150+347) & (mouseX < 180+347) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/D#.mid")
                    pmm.play()
                if(((mouseX > 180+347) & (mouseX < 210+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170+347) & (mouseX < 210+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/E.mid")
                    pmm.play()
                if(((mouseX > 220+347) & (mouseX < 245+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220+347) & (mouseX < 260+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/F.mid")
                    pmm.play()
                if(((mouseX > 245+347) & (mouseX < 280+347) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/F#.mid")
                    pmm.play()
                if(((mouseX > 280+347) & (mouseX < 300+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270+347) & (mouseX < 310+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/G.mid")
                    pmm.play()
                if(((mouseX > 300+347) & (mouseX < 328+347) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/G#.mid")
                    pmm.play()
                if(((mouseX > 328+347) & (mouseX < 348+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320+347) & (mouseX < 360+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/A.mid")
                    pmm.play()
                if(((mouseX > 348+347) & (mouseX < 380+347) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/A#.mid")
                    pmm.play()
                if(((mouseX > 380+347) & (mouseX < 410+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368+347) & (mouseX < 410+347) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/B.mid")
                    pmm.play()

                if(((mouseX > 68+692) & (mouseX < 98+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68+692) & (mouseX < 112+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighC.mid")
                    pmm.play()
                if(((mouseX > 99+692) & (mouseX < 130+692) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/HighC#.mid")
                    pmm.play()
                if(((mouseX > 130+692) & (mouseX < 150+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120+692) & (mouseX < 160+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighD.mid")
                    pmm.play()
                if(((mouseX > 150+692) & (mouseX < 180+692) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/HighD#.mid")
                    pmm.play()
                if(((mouseX > 180+692) & (mouseX < 210+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170+692) & (mouseX < 210+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighE.mid")
                    pmm.play()
                if(((mouseX > 220+692) & (mouseX < 245+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220+692) & (mouseX < 260+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighF.mid")
                    pmm.play()
                if(((mouseX > 245+692) & (mouseX < 280+692) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/HighF#.mid")
                    pmm.play()
                if(((mouseX > 280+692) & (mouseX < 300+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270+692) & (mouseX < 310+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighG.mid")
                    pmm.play()
                if(((mouseX > 300+692) & (mouseX < 328+692) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/HighG#.mid")
                    pmm.play()
                if(((mouseX > 328+692) & (mouseX < 348+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320+692) & (mouseX < 360+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighA.mid")
                    pmm.play()
                if(((mouseX > 348+692) & (mouseX < 380+692) & (mouseY > 170) & (mouseY < 440))):
                    pmm.load("CodeCreatedSounds/HighA#.mid")
                    pmm.play()
                if(((mouseX > 380+692) & (mouseX < 410+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368+692) & (mouseX < 410+692) & (mouseY > 440) & (mouseY < 670))):
                    pmm.load("CodeCreatedSounds/HighB.mid")
                    pmm.play()
                if((mouseX > 176) & (mouseX < 370) & (mouseY > 15) & (mouseY < 95)):
                    MainScreen1 = False
                    MainScreen2 = False
                    Recordings = True
                if((mouseX > 702) & (mouseX < 897) & (mouseY > 20) & (mouseY < 95)):
                    MainScreen1 = False
                    MainScreen2 = True
            if event.type == pygame.MOUSEBUTTONUP:
                pmm.stop()
                pmm.unload()
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    elif(MainScreen1 == False and Recordings == False and MainScreen2 == True):
        screen.blit(background1_5, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_time = time.time()
                    song.append(48)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowC.mid")
                    pmm.play()
                if event.key == pygame.K_2:
                    start_time = time.time()
                    song.append(49)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowC#.mid")
                    pmm.play()
                if event.key == pygame.K_3:
                    start_time = time.time()
                    song.append(50)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowD.mid")
                    pmm.play()
                if event.key == pygame.K_4:
                    start_time = time.time()
                    song.append(51)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowD#.mid")
                    pmm.play()
                if event.key == pygame.K_5:
                    start_time = time.time()
                    song.append(52)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowE.mid")
                    pmm.play()
                if event.key == pygame.K_6:
                    start_time = time.time()
                    song.append(53)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowF.mid")
                    pmm.play()
                if event.key == pygame.K_7:
                    start_time = time.time()
                    song.append(54)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowF#.mid")
                    pmm.play()
                if event.key == pygame.K_8:
                    start_time = time.time()
                    song.append(55)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowG.mid")
                    pmm.play()
                if event.key == pygame.K_9:
                    start_time = time.time()
                    song.append(56)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowG#.mid")
                    pmm.play()
                if event.key == pygame.K_0:
                    start_time = time.time()
                    song.append(57)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowA.mid")
                    pmm.play()
                if event.key == pygame.K_q:
                    start_time = time.time()
                    song.append(58)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowA#.mid")
                    pmm.play()
                if event.key == pygame.K_w:
                    start_time = time.time()
                    song.append(59)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/LowB.mid")
                    pmm.play()
                if event.key == pygame.K_e:
                    start_time = time.time()
                    song.append(60)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/C.mid")
                    pmm.play()
                if event.key == pygame.K_r:
                    start_time = time.time()
                    song.append(61)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/C#.mid")
                    pmm.play()
                if event.key == pygame.K_t:
                    start_time = time.time()
                    song.append(62)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/D.mid")
                    pmm.play()
                if event.key == pygame.K_y:
                    start_time = time.time()
                    song.append(63)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/D#.mid")
                    pmm.play()
                if event.key == pygame.K_u:
                    start_time = time.time()
                    song.append(64)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/E.mid")
                    pmm.play()
                if event.key == pygame.K_i:
                    start_time = time.time()
                    song.append(65)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/F.mid")
                    pmm.play()
                if event.key == pygame.K_o:
                    start_time = time.time()
                    song.append(66)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/F#.mid")
                    pmm.play()
                if event.key == pygame.K_p:
                    start_time = time.time()
                    song.append(67)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/G.mid")
                    pmm.play()
                if event.key == pygame.K_a:
                    start_time = time.time()
                    song.append(68)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/G#.mid")
                    pmm.play()
                if event.key == pygame.K_s:
                    start_time = time.time()
                    song.append(69)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/A.mid")
                    pmm.play()
                if event.key == pygame.K_d:
                    start_time = time.time()
                    song.append(70)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/A#.mid")
                    pmm.play()
                if event.key == pygame.K_f:
                    start_time = time.time()
                    song.append(71)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/B.mid")
                    pmm.play()
                if event.key == pygame.K_g:
                    start_time = time.time()
                    song.append(72)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighC.mid")
                    pmm.play()
                if event.key == pygame.K_h:
                    start_time = time.time()
                    song.append(73)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighC#.mid")
                    pmm.play()
                if event.key == pygame.K_j:
                    start_time = time.time()
                    song.append(74)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighD.mid")
                    pmm.play()
                if event.key == pygame.K_k:
                    start_time = time.time()
                    song.append(75)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighD#.mid")
                    pmm.play()
                if event.key == pygame.K_l:
                    start_time = time.time()
                    song.append(76)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighE.mid")
                    pmm.play()
                if event.key == pygame.K_z:
                    start_time = time.time()
                    song.append(77)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighF.mid")
                    pmm.play()
                if event.key == pygame.K_x:
                    start_time = time.time()
                    song.append(78)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighF#.mid")
                    pmm.play()
                if event.key == pygame.K_c:
                    start_time = time.time()
                    song.append(79)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighG.mid")
                    pmm.play()
                if event.key == pygame.K_v:
                    start_time = time.time()
                    song.append(80)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighG#.mid")
                    pmm.play()
                if event.key == pygame.K_b:
                    start_time = time.time()
                    song.append(81)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighA.mid")
                    pmm.play()
                if event.key == pygame.K_n:
                    start_time = time.time()
                    song.append(82)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighA#.mid")
                    pmm.play()
                if event.key == pygame.K_m:
                    start_time = time.time()
                    song.append(83)
                    pmm.unload()
                    pmm.load("CodeCreatedSounds/HighB.mid")
                    pmm.play()
            if event.type == pygame.KEYUP:
                pmm.stop()
                pmm.unload()
                stop_time = time.time()
                noteDuration.append(float(stop_time - start_time))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouseX,mouseY = pos
                if(((mouseX > 68) & (mouseX < 98) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68) & (mouseX < 112) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(48)
                    pmm.load("CodeCreatedSounds/LowC.mid")
                    pmm.play()
                if(((mouseX > 99) & (mouseX < 130) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(49)
                    pmm.load("CodeCreatedSounds/LowC#.mid")
                    pmm.play()
                if(((mouseX > 130) & (mouseX < 150) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120) & (mouseX < 160) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(50)
                    pmm.load("CodeCreatedSounds/LowD.mid")
                    pmm.play()
                if(((mouseX > 150) & (mouseX < 180) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(51)
                    pmm.load("CodeCreatedSounds/LowD#.mid")
                    pmm.play()
                if(((mouseX > 180) & (mouseX < 210) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170) & (mouseX < 210) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(52)
                    pmm.load("CodeCreatedSounds/LowE.mid")
                    pmm.play()
                if(((mouseX > 220) & (mouseX < 245) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220) & (mouseX < 260) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(53)
                    pmm.load("CodeCreatedSounds/LowF.mid")
                    pmm.play()
                if(((mouseX > 245) & (mouseX < 280) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(54)
                    pmm.load("CodeCreatedSounds/LowF#.mid")
                    pmm.play()
                if(((mouseX > 280) & (mouseX < 300) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270) & (mouseX < 310) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(55)
                    pmm.load("CodeCreatedSounds/LowG.mid")
                    pmm.play()
                if(((mouseX > 300) & (mouseX < 328) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(56)
                    pmm.load("CodeCreatedSounds/LowG#.mid")
                    pmm.play()
                if(((mouseX > 328) & (mouseX < 348) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320) & (mouseX < 360) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(57)
                    pmm.load("CodeCreatedSounds/LowA.mid")
                    pmm.play()
                if(((mouseX > 348) & (mouseX < 380) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(58)
                    pmm.load("CodeCreatedSounds/LowA#.mid")
                    pmm.play()
                if(((mouseX > 380) & (mouseX < 410) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368) & (mouseX < 410) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(59)
                    pmm.load("CodeCreatedSounds/LowB.mid")
                    pmm.play()
                if(((mouseX > 68+347) & (mouseX < 98+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68+347) & (mouseX < 112+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(60)
                    pmm.load("CodeCreatedSounds/C.mid")
                    pmm.play()
                if(((mouseX > 99+347) & (mouseX < 130+347) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(61)
                    pmm.load("CodeCreatedSounds/C#.mid")
                    pmm.play()
                if(((mouseX > 130+347) & (mouseX < 150+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120+347) & (mouseX < 160+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(62)
                    pmm.load("CodeCreatedSounds/D.mid")
                    pmm.play()
                if(((mouseX > 150+347) & (mouseX < 180+347) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(63)
                    pmm.load("CodeCreatedSounds/D#.mid")
                    pmm.play()
                if(((mouseX > 180+347) & (mouseX < 210+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170+347) & (mouseX < 210+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(64)
                    pmm.load("CodeCreatedSounds/E.mid")
                    pmm.play()
                if(((mouseX > 220+347) & (mouseX < 245+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220+347) & (mouseX < 260+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(65)
                    pmm.load("CodeCreatedSounds/F.mid")
                    pmm.play()
                if(((mouseX > 245+347) & (mouseX < 280+347) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(66)
                    pmm.load("CodeCreatedSounds/F#.mid")
                    pmm.play()
                if(((mouseX > 280+347) & (mouseX < 300+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270+347) & (mouseX < 310+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(67)
                    pmm.load("CodeCreatedSounds/G.mid")
                    pmm.play()
                if(((mouseX > 300+347) & (mouseX < 328+347) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(68)
                    pmm.load("CodeCreatedSounds/G#.mid")
                    pmm.play()
                if(((mouseX > 328+347) & (mouseX < 348+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320+347) & (mouseX < 360+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(69)
                    pmm.load("CodeCreatedSounds/A.mid")
                    pmm.play()
                if(((mouseX > 348+347) & (mouseX < 380+347) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(70)
                    pmm.load("CodeCreatedSounds/A#.mid")
                    pmm.play()
                if(((mouseX > 380+347) & (mouseX < 410+347) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368+347) & (mouseX < 410+347) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(71)
                    pmm.load("CodeCreatedSounds/B.mid")
                    pmm.play()

                if(((mouseX > 68+692) & (mouseX < 98+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 68+692) & (mouseX < 112+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(72)
                    pmm.load("CodeCreatedSounds/HighC.mid")
                    pmm.play()
                if(((mouseX > 99+692) & (mouseX < 130+692) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(73)
                    pmm.load("CodeCreatedSounds/HighC#.mid")
                    pmm.play()
                if(((mouseX > 130+692) & (mouseX < 150+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 120+692) & (mouseX < 160+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(74)
                    pmm.load("CodeCreatedSounds/HighD.mid")
                    pmm.play()
                if(((mouseX > 150+692) & (mouseX < 180+692) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(75)
                    pmm.load("CodeCreatedSounds/HighD#.mid")
                    pmm.play()
                if(((mouseX > 180+692) & (mouseX < 210+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 170+692) & (mouseX < 210+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(76)
                    pmm.load("CodeCreatedSounds/HighE.mid")
                    pmm.play()
                if(((mouseX > 220+692) & (mouseX < 245+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 220+692) & (mouseX < 260+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(77)
                    pmm.load("CodeCreatedSounds/HighF.mid")
                    pmm.play()
                if(((mouseX > 245+692) & (mouseX < 280+692) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(78)
                    pmm.load("CodeCreatedSounds/HighF#.mid")
                    pmm.play()
                if(((mouseX > 280+692) & (mouseX < 300+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 270+692) & (mouseX < 310+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(79)
                    pmm.load("CodeCreatedSounds/HighG.mid")
                    pmm.play()
                if(((mouseX > 300+692) & (mouseX < 328+692) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(80)
                    pmm.load("CodeCreatedSounds/HighG#.mid")
                    pmm.play()
                if(((mouseX > 328+692) & (mouseX < 348+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 320+692) & (mouseX < 360+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(81)
                    pmm.load("CodeCreatedSounds/HighA.mid")
                    pmm.play()
                if(((mouseX > 348+692) & (mouseX < 380+692) & (mouseY > 170) & (mouseY < 440))):
                    clicked = True
                    start_time = time.time()
                    song.append(82)
                    pmm.load("CodeCreatedSounds/HighA#.mid")
                    pmm.play()
                if(((mouseX > 380+692) & (mouseX < 410+692) & (mouseY > 170) & (mouseY < 440)) | ((mouseX > 368+692) & (mouseX < 410+692) & (mouseY > 440) & (mouseY < 670))):
                    clicked = True
                    start_time = time.time()
                    song.append(83)
                    pmm.load("CodeCreatedSounds/HighB.mid")
                    pmm.play()
                if((mouseX > 176) & (mouseX < 370) & (mouseY > 15) & (mouseY < 95)):
                    CreateMusic(song, noteDuration, recordingNum)
                    song = []
                    noteDuration = []
                    recordingNum+=1
                    MainScreen1 = False
                    MainScreen2 = False
                    Recordings = True
                if((mouseX > 702) & (mouseX < 897) & (mouseY > 20) & (mouseY < 95)):
                    CreateMusic(song, noteDuration, recordingNum)
                    song = []
                    noteDuration = []
                    recordingNum+=1
                    MainScreen1 = True
                    MainScreen2 = False
            if (event.type == pygame.MOUSEBUTTONUP) and (clicked == True):
                clicked = False
                pmm.stop()
                pmm.unload()
                stop_time = time.time()
                noteDuration.append(stop_time - start_time)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    elif(MainScreen1 == False and Recordings == True and MainScreen2 == False):
        screen.blit(background2,[0,0])
        musicFiles = [f for f in listdir("CreatedMusic") if isfile(join("CreatedMusic", f))]
        musicText = ["Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty","Empty"]
        temp = 0
        while(temp < len(musicFiles)):
            musicText[temp] = musicFiles[temp]
            temp += 1
        font = pygame.font.SysFont('freesansbold.ttf', 18)
        texty = 98
        for file in musicText:
            text = font.render(file, True, black, yellow)
            textRect = text.get_rect()
            textRect.center = (561,texty)
            screen.blit(text, textRect)
            texty += 58
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouseX,mouseY = pos
                track1 = False
                if((mouseX > 23) & (mouseX < 95) & (mouseY > 8) & (mouseY < 45)):
                    MainScreen1 = True
                    Recordings = False
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75) & (mouseY < 120)):
                    if(musicText[0] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[0])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*1)) & (mouseY < 120+(58*1))):
                    if(musicText[1] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[1])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*2)) & (mouseY < 120+(58*2))):
                    if(musicText[2] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[2])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*3)) & (mouseY < 120+(58*3))):
                    if(musicText[3] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[3])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*4)) & (mouseY < 120+(58*4))):
                    if(musicText[4] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[4])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*5)) & (mouseY < 120+(58*5))):
                    if(musicText[5] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[5])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*6)) & (mouseY < 120+(58*6))):
                    if(musicText[6] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[6])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*7)) & (mouseY < 120+(58*7))):
                    if(musicText[7] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[7])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*8)) & (mouseY < 120+(58*8))):
                    if(musicText[8] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[8])
                        pmm.play()
                if((mouseX > 10) & (mouseX < 1188) & (mouseY > 75+(58*9)) & (mouseY < 120+(58*9))):
                    if(musicText[9] != "Empty"):
                        pmm.load("CreatedMusic/" + musicText[9])
                        pmm.play()
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()
 