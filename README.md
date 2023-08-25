# Documentation v1
1. sav1.sav/sav2.sav are required for the game to run with save features, these files will be created automatically. If there are any issues with saving / loading, make sure those .sav files are present. The values can be modified for any custom game modes.
sav1.sav is Player and sav2.sav is Boss
2. For any OS based issues, post a new issue in the heyitsbraden/riftSource github.
3. For a multi-platform build, check the repo: heyitsbraden/riftHTML

# OS Based Modifications
### MacOS / Linux
1. Command for clearing the screen as used in the code, os.system('clear')

### Windows
1. Command for clearing the screen as used in the code, os.system('cls')

### Other
N/A

# Features
1. Potions become unlocked after a certain amount of xp is obtained.
2. Clears the screen after you select your action for a cleaner overall experience.
3. More reliablility, plus new added features since the code isn't as messy.

# Error Codes and what they mean.
1) 01: Either the file does not exist, or the file is empty (savefile)
*Report any and all errors w/out err codes here: heyitsbraden/rift.py*
2) Suspicious file detected! A number that is high in the save file.


# To-Do List

### TOTAL COMPLETION OF GAME: [NULL]

1. Add "Attack" as an action [DONE]
2. Add "Defend" as an action [DONE]
3. Add "Heal" as an action [DONE]
4. Add "Potions" as an action [75% - 3/6 Potions complete! ~50%]

i. Add "Health Boost" [DONE]

ii. Add "Attack Amplifier" [DONE]

iii. Add "Lethality Syrum" [DONE]

Add "Permanent Attack Boost" (REMOVED - KEPT FOR FUTURE REFERENCE)

iv. Add "Intensify Action" [50% - does nothing]

v. Add "Ninja Squid" [50% - does nothing]

vi. Add "Subdefense Limeade" [50% - does nothing]

5. Add "Pets" as an action [4/5 have placeholders | 0/5 function (20%)]

i. Add "Rock Pet" [50% - does nothing]

ii. Add "Fairy Pet" [50% - does nothing]

iii. Add "Faithful Doggo" [50% - does nothing]

iv. Add "middle finger" [50% - does nothing]

v. Add "Inkling" [null]

6. Add coins [DONE]
7. Add score [DONE]
8. Add XP [DONE]
9. Add Level System [DONE]
10. Add save/load feature [DONE]
11. Make the game screen less messy [DONE]
12. Add in custom damage modifiers [10% - Added the variables]

### Possible Editions to the game.
1. Graphics [pygame | 0%]
2. Sound [pygame | 0%]
3. Add multiplayer [unknown library | 0%]
4. Add color to the game's text [Colorama | 25%]

# Changelog v1 (C++ Conversion)
1. Added Colorama for text color.
2. Added 2 more potions for more gameplay options.
3. Added more reliable save feature different to the C++ ver.
4. Added 1 more pet for more gameplay options.
5. Removed "Permanent Attack Boost" for redundancy.
6. Added a clear option to make the screen less messy.
7. Added Sound/Graphics library (pygame)
8. Added a maximum value for XP, which is 500
