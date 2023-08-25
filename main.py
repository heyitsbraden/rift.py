from random import randrange, random
import pygame #to play sound use | pygame.mixer.init() | pygame.mixer.music.load("file.mp3") | pygame.mixer.music.play()
import os
import time
import colorama
from colorama import Fore, Back, Style
import math
colorama.init(autoreset=True)
t = 0.8
coins = 0 #the amount of coins the user has
xp = 0 #xp value (player)
xp2 = 5 #xp per xp gain
xpTlvl = 100 #xp to level up
lvl = 0 #player levels
score = 0 #player score
ph = 20 # Player Health
pa = 4 # Player Attack
bh = 100 # Boss Health
ba = 4 # Boss Attack
heal = 5 # Healing Value
petselect = 0
flag = 0 #Anti-Tamper flag
i = 1 #responsible for looping the game

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

print("Welcome to RiFT!")
print("If you do not want to save/load your game, press n")
sInput = input("")
if sInput == "y":
  print(colorama.Style.BRIGHT + "Loading your game...")
  time.sleep(t)
  try:
    f = open("savefile", "r")
    xp = f.read()
    xp = int(xp)
    if xp > 500:
      print(colorama.Fore.RED + colorama.Style.BRIGHT + "Suspicious file detected!")
      undefinedprocess = xp
      ba = 12000
      flag = 1
      xp = 0
      f2 = open("savefile", "a")
      f2.write("SUSPICIOUS FILE DETECTED")
    f.close()
  except:
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "Error when loading file")
    xp = 0
    time.sleep(1)

while i == 1:
  f = open("savefile", "r")
  temp = f.read()
  temp = int(temp)
  f.close()
  #if undefinedprocess > temp:
    #print(colorama.Fore.RED + colorama.Style.BRIGHT + "Suspicious file detected! .") # Error Code 03, Anti-Tamper for the savefile
  #elif undefinedprocess < temp:
    #print(colorama.Fore.RED + colorama.Style.BRIGHT + "Suspicious file detected! ,") # Error Code 04, Anti-Tamper for the savefile
  if ph <= 0:
    print(colorama.Fore.RED + "You Died.")
    #--After death save operation--#
    time.sleep(t)
    f = open("score.txt", "a")
    f.write("Player Health: " + ph)
    f.write("Boss Health: " + bh)
    f.write("Coins: " + coins)
    f.write("XP: " + xp)
    f.write("Player Level: " + lvl)
    f.close()
    time.sleep(2)
    os.system('clear') #change to os.system('cls') for windows
    #--After death save operation--#
  coins == xp / 2 * 3 / 2 #coin generating algorithm
  score == xp * 2
  if xp >= xpTlvl:
    h = 1
    while h == 1:
      if xp >= xpTlvl:
        print(colorama.Fore.LIGHTYELLOW_EX + "LEVEL UP!")
        lvl = lvl + 1
        xp = xp - xpTlvl
        xpTlvl = xpTlvl + 20
        xp2 = 6
        ph = ph + 5
        pa = pa + 5
        if xp < xpTlvl:
          h = 0
  br = randrange(3) #assign the random 0-3 for BOSS actions
#-------Beyond here is the main game loop-------#
  playerhealth = colorama.Fore.RED + str(bh)
  if ph <= 10:
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "Player Health: " + str(ph)) #converts ph to string
  elif ph >= 11:
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "Player Health: " + str(ph))
  if bh <= 10:
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "Boss Health: " + str(bh)) #converts bh to string
  elif bh >= 11:
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "Boss Health: " + str(bh)) #converts bh to string
  time.sleep(t)
  print("") #new line
  print(colorama.Fore.GREEN + "Score: " + str(score))
  print(colorama.Fore.GREEN + "Level: " + str(lvl))
  print(colorama.Fore.GREEN + "Coins: " + str(coins))
  print(colorama.Fore.GREEN + "XP: " + str(xp))
  print("") #new line
  time.sleep(t)
  print("Press 1 thru 5 depending on your wanted action.")
  print(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "[Attack]")
  print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "[Defend]")
  print(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "[Heal]")
  print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + "[Potions]")
  print(colorama.Fore.LIGHTMAGENTA_EX + colorama.Style.BRIGHT + "[Pets]")
  print("")
  print("[Save] - Save your current XP, Coins, Level, and Score.")
  print("The work-in-progress save feature does not save HP")
  choice = input("") #input on new line
#-------Beyond here is the PLAYER actions-------#
  if choice == "1": #attack
    print("You attacked the boss.")
    time.sleep(t)
    bh = bh - pa
    xp = xp + xp2
    os.system('clear') #change to os.system('cls') for windows
  elif choice == "2": #defend
    print("You defended yourself against the bosses attack.")
    time.sleep(t)
    ba = 0
    xp = xp + xp2
    os.system('clear') #change to os.system('cls') for windows
  elif choice == "3": #heal
    print("You healed yourself.")
    time.sleep(t)
    ph = ph + heal
    xp = xp + xp2
    os.system('clear') #change to os.system('cls') for windows
  elif choice == "4": #potions
    print("Here are the potions currently avalible")
    os.system('clear') #change to os.system('cls') for windows
    if xp >= 0:
      print("Avalible potions are colored CYAN")
      print("")
      print("[Health Boost]")
      print("[Attack Amplifier]")
      print("[Lethality Syrum]")
      print(colorama.Fore.CYAN + "[Intensify Action]")
      print("[Ninja Squid]")
      print("[Subdefense Limeade]")
      potions = input("Which potion do you choose?")
    if xp >= 20:
      print("Avalible potions are colored CYAN")
      print("")
      print(colorama.Fore.CYAN + "[Health Boost]")
      print("[Attack Amplifier]")
      print("[Lethality Syrum]")
      print(colorama.Fore.CYAN + "[Intensify Action]")
      print("[Ninja Squid]")
      print("[Subdefense Limeade]")
      potions = input("Which potion do you choose?")
    if xp >= 50:
      print("Press 1, 2, or 3 based on the potion you choose.")
      print("")
      print(colorama.Fore.CYAN + "[Health Boost]")
      print("[Attack Amplifier]")
      print(colorama.Fore.CYAN + "[Lethality Syrum]")
      print(colorama.Fore.CYAN + "[Intensify Action]")
      print("[Ninja Squid]")
      print("[Subdefense Limeade]")
      potions = input("Which potion do you choose?")
    if xp >= 80:
      print("Press 1, 2, 3, 4, or 5 based on the potion you choose.")
      print("")
      print(colorama.Fore.CYAN + "[Health Boost]")
      print(colorama.Fore.CYAN + "[Attack Amplifier]")
      print(colorama.Fore.CYAN + "[Lethality Syrum]")
      print(colorama.Fore.CYAN + "[Intensify Action]")
      print(colorama.Fore.CYAN + "[Ninja Squid]")
      print(colorama.Fore.CYAN + "[Subdefense Limeade]")
      potions = input("Which potion do you choose?")
      if potions == "1":
        if xp >= 20:
          print("You have selected the [Health Boost]")
          print("Gives a boost to your health")
          potionselect = input("Do you want this choice? ")
        elif xp <= 19:
          print("You cannot use this yet")
        ph = ph + 12
      elif potions == "2":
        if xp >= 80:
          print("You have selected the [Attack Amplifier]")
          print("Amplifies your attack")
          potionselect = input("Do you want this choice? ")
          pa = pa + 6
        elif xp <= 79:
          print("You cannot use this yet")
      elif potions == "3":
        if xp >= 50:
          print("You have selected the [Lethality Syrum]")
          print("Does 12 damage to the boss automatically (once)")
          potionselect = input("Do you want this choice? ")
          print("The boss was hurt badly")
          bh = bh - 12
        elif xp <= 49:
          print("You cannot use this yet")
      elif potions == "4":
        print("You have selected the [Intensify Action]")
        print("Makes things faster.")
        potionselect = input("Do you want this choice? ")
        t = t - 0.6
      elif potions == "5":
        print("You have selected the [Ninja Squid]")
        print("Makes you harder to hit (random chance for a hit/miss)")
        potionselect = input("Do you want this choice? ")
      elif potions == "6":
        print("You have selected the [Subdefense Limeade]")
        print("Lessens the bosses attack for a short time.")
        potionselect = input("Do you want this choice? ")
  elif choice == "5": #pets
    if petselect == 1:
      print("You have already selected a pet.")
    elif petselect == 0:
      if xp == 20:
        print("Here are the current pets avalible")
        print("[Rock]")
        print("[Fairy]")
      elif xp == 60:
        print("Here are the current pets avalible")
        print("[Rock]")
        print("[Fairy]")
        print("[Faithful Doggo]")
        print("[middle finger]")
        os.system('clear') #change to os.system('cls') for windows
  elif choice == "save":
    print("You are about to save your game.")
    time.sleep(0.2)
    print("Overwrite a save slot, or make a new save.")
    savefile = open("savefile", "a")
    savefile.write(str(xp))
    savefile.close()
    rfile = open("score.txt", "a")
    rfile.write(" Player Health: " + str(ph) )
    rfile.write(" Boss Health: " + str(bh) )
    rfile.write(" Coins: " + str(coins) )
    rfile.write(" XP: " + str(xp) )
    rfile.write(" Player Level: " + str(lvl) )
    rfile.close()
    time.sleep(2)
  print("") #new line
#-------Beyond here is the BOSS actions-------#
  if br == 3: #heal
    if flag == 1:
      ph = ph - ba
    print("The boss has healed itself.")
    time.sleep(t)
    bh = bh + heal
    os.system('clear') #change to os.system('cls') for windows
  elif br == 1: #defend
    if flag == 1:
      ph = ph - ba
    print("The boss has defended itself.")
    time.sleep(t)
    pa = 0
    os.system('clear') #change to os.system('cls') for windows
  elif br == 2: #attack
    if flag == 1:
      ph = ph - ba
    print("The boss attacked you.")
    time.sleep(t)
    ph = ph - ba
    os.system('clear') #change to os.system('cls') for windows
  elif br == 0: #attack
    if flag == 1:
      ph = ph - ba
    print("The boss attacked you.")
    time.sleep(t)
    ph = ph - ba
    os.system('clear') #change to os.system('cls') for windows