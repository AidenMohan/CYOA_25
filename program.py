# Game is complete
#README!!!
# If the game stops with the error code (NameError: name 'X' is not defined) then that means that path is not finshed.
#    _               _    _     _              __  __       _                 
#   / \   _ __      / \  (_) __| | ___ _ __   |  \/  | ___ | |__   __ _ _ __  
#  / _ \ | '_ \    / _ \ | |/ _` |/ _ \ '_ \  | |\/| |/ _ \| '_ \ / _` | '_ \ 
# / ___ \| | | |  / ___ \| | (_| |  __/ | | | | |  | | (_) | | | | (_| | | | |
#/_/__ \_\_| |_| /_/  _\_\_|\__,_|\___|_| |_| |_|  |_|\___/|_| |_|\__,_|_| |_|
#|  _ \ _ __ ___   __| |_   _  ___| |_(_) ___  _ __                           
#| |_) | '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \                          
#|  __/| | | (_) | (_| | |_| | (__| |_| | (_) | | | |                         
#|_|   |_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|                         

import random
import time

print(r"""
    _                               ____                      _
   / \  _   _ _ __ ___  _ __ __ _  |  _ \  _____      ___ __ | |
  / _ \| | | | '__/ _ \| '__/ _` | | | | |/ _ \ \ /\ / / '_ \| |
 / ___ \ |_| | | | (_) | | | (_| | | |_| | (_) \ V  V /| | | |_|
/_/   \_\__,_|_|  \___/|_|  \__,_| |____/ \___/ \_/\_/ |_| |_(_)
""")
def start_AD():
    print("Welcome to the Choose Your Own Adventure Game!")
    print("You are a commander on your ship the Aurora, a destroyer class ship built by the United Nations Space Command Navy")
    print("You and your ship are coming back from a support mission in the nexus galaxy")
    print("You are commanding your crew in the control center, the bridge of the ship")
    print("Then BANG!")
    print("You pull your self up from the floor of the bridge, with alarms going off all round you, you think about what to do.")
    print("Do you try find out what happened, or do you run to the main hallway that connects to the rest of the ship?.")
    choice = input("Type 'stay' or 'run': ").strip().lower()
    
    if choice == 'stay':
        stay_path()
    elif choice == 'run':
        run1_path()
    elif choice == 'credits':
        creds()
    else:
        print("Invalid choice. Please try again.")
        start_AD()

def stay_path():
    print('You ask an officer what has happened, they shout back "Sir!, we have been hit by an enemy ship!" ')
    print('Should we attack or evacuate?"')
    choice = input("Type 'attack' or 'evacuate': ").strip().lower()
    
    if choice == 'attack':
        attack_path()
    elif choice == 'evacuate':
        stayevac_path()
    else:
        print("Invalid choice. Please try again.")
        stay_path()

def stayevac_path():
  print('Understood Sir.')
  print('Should we evacuate a smaller group of high ranking people like you?')
  print('Or should we evacuate a large group of non-essential personnel?')
  print("If you evacuate a large group you may not get a pod!")
  choice = input("Type 'small' or 'large': ").strip().lower()
  if choice == 'small':
      smallbridgeevac()
  elif choice == 'large':
        bigbridgeevac()
  else:
       print("Invalid choice. Please try again.")
       stayevac_path()
def bigbridgeevac():
  print("Understood Sir!")
  print("I'm going to get in a pod, you should try get in one too!")
  print("Do you go to the Commander's lifepod or head to the main set of life pods?")
  choice = input("Type 'commanders' or 'main': ").strip().lower()
  if choice == 'commanders':
      bigevaccommanders()
  elif choice == 'main':
      bigevacmainlifepods()
  else:
       print("Invalid choice. Please try again.")
       bigbridgeevac()
def bigevacmainlifepods():
  print("You arrive at the main set of lifepod to see chaos unfolding.")
  print("From what you can see there is 15 lifepods left")
  print("Do you attempt to escape by your self in a empty lifepod that seems to good to be true?")
  print("Or do you attempt to escape in a lifepod with 2 others?")
  choice = input("Type 'self' or 'others': ").strip().lower()
  if choice == 'self':
      bigevacescapeself()
  elif choice == 'others':
       bigevacescapeothers()
  else:
       print("Invalid choice. Please try again.")
       bigevacmainlifepods()
def bigevacescapeothers():
  print("With no time for introductions, you start the launch process")
  print("You and the others in the pod breath a sigh of relief as you feel the boosters come on")
  print("As you start to talk with the others in the pod, you feel a vibration from the control panel")
  print("You get a prompt from the autopliot")
  print("AUTO-PLIOT V.23.1: SYSTEM UNCALIBRATED")
  print("CONTINUE USE OR PILOT MANUALLY?")  
  choice = input("Type 'contiune' or 'manual': ").strip().lower()
  if choice == 'contiune':
      evacauto()
  elif choice == 'manual':
       evacmanual()
  else:
       print("Invalid choice. Please try again.")
       bigevacescapeothers()
def evacmanual():
  print("You take hold of the controls and make a hard right directly to the nearest friendly ship")
  print("As the ship explodeds behind you, you start talking with the people that you escaped with")
  print(r"""Soon you turn into a dot in space
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")

def evacauto():
  print("You sit back and talk to the others in your pod about what happened.")
  print("While talking you notice an asteroid cluster ahead of the pod.")
  print("You assume that the autopilot will deal with it")
  print(r"""You get closer and closer then you realise that the autopilot won't help 
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("You have got 1 of 20 possible endings, try to get them all!") 
def bigevacescapeself():
  print(r"""You get in, start the launch and after the sounds of metal warping, you get thrust forwards into the unknown.
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/  """)
  print("You think back to yourself, about if you could of saved the other 2 in the lifepod")
  print("You have got 1 of 20 possible endings, try to get them all!")

def bigevaccommanders():
  print("You attempt to access the commander's lifepod only to see that it is blocked off.")
  print("You decide to head to the mainset of lifepods instead.")
  bigevacmainlifepods()
def smallbridgeevac():
  print("As you are getting escorted to the commander's lifepod with other high ranking officers.")
  print("You feel like you are being watched.")
  print(r"""You hear something hitting metal and you look behind to see someone standing with a crowbar over your guards body.
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| 
""")
  print("Your group was ambushed.")
  print("People put them self over others during conflict, can you put others over your self?")
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(I would recommend playing a different pathway as this is one of the shortest!)")

def attack_path():
  print('Understood Sir, Where should we attack?')
  choice = input("Type 'bridge' or 'boosters': ").strip().lower()
  if choice == 'bridge':
        bridge_attack_path()
  elif choice == 'boosters':
        booster_attack_path()
  else:
        print("Invalid choice. Please try again.")
        attack_path()
  
def bridge_attack_path():
  print('Good hit sir! Where should we attack next?')
  choice = input("Type 'weapons' or 'hull': ").strip().lower()
  if choice == 'weapons':
        bridge_weapons_attack_path()
  elif choice == 'hull':
        bridge_hull_attack_path()
  else:
        print("Invalid choice. Please try again.")
        bridge_attack_path()
def bridge_weapons_attack_path():
  print(r"""
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
""")
  print("You hit the bridge, the nerve center of the ship")
  print(r"""With the weapons disabled and the crew in disarray, you go in for the kill.
   ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/  
""")
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(I would recommend playing a different pathway as this is one of the shortest!)")
  
def bridge_hull_attack_path():
  print(r"""
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
""")
  print("You hit the bridge, the nerve center of the ship")
  print(r"""But taking out the bridge doesn't stop everything, the Aurora exploded due to the damage by the attackers.")
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_|  """)
  print("You were close, but not close enough.")
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(I would recommend playing a different pathway as this is one of the shortest!)")
  
def booster_attack_path():
  print('Good hit sir! Where should we attack next?')
  choice = input("Type 'weapons' or 'hull': ").strip().lower()
  if choice == 'weapons':
        booster_weapons_attack_path()
  elif choice == 'hull':
        booster_hull_attack_path()
  else:
        print("Invalid choice. Please try again.")
        booster_attack_path()
def booster_hull_attack_path():
  print(r"""
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
""")
  print("You rendered them unable to move, allowing you to hit them easier.")
  print(r"""By hitting the hull you caused the ship to implode.
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/  
""")
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(I would recommend playing a different pathway as this is one of the shortest!)")
def booster_weapons_attack_path():
  print(r"""
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
""")
  print("You rendered them unable to move, allowing you to hit them easier.")
  print(r"""But as you started attacking the weapons, they got the final blow on you.
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_|  """)
  print("You were close, but not close enough.")
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(I would recommend playing a different pathway as this is one of the shortest!)")
def run1_path():
    print("Without asking questions you run, as you run into the main sector, you read the signs that you pass.")
    print("Do you turn left towards the main lifepod launcher, or do turn right towards the commander's officer and armory.")
    choice = input("Type 'left' or 'right': ").strip().lower()
    
    if choice == 'left':
        runleftpath()
    elif choice == 'right':
        runrightpath()
    else:
        print("Invalid choice. Please try again.")
        run1_path()
def runleftpath():
  print("You run past people with the same destination")
  print("You look up ahead to see someone resting on a wall with blood on their thigh")
  print("Do you stop and help or keep running?")
  choice = input("Type 'help' or 'run': ").strip().lower() 
  
  if choice == 'help':
        lefthelp()
  elif choice == 'run':
        leftrun()
  else:
        print("Invalid choice. Please try again.")
        runleftpath()
def lefthelp():
  print("You try to ask what happened but you get cut off")
  print('"I\'m ready to die but you shouldn\'t be."')
  print('"Most people don\'t know but lifepod 9, 18 and 21 are ready to be launched"')
  print('"Don\'t use them, now go"')
  print("You go back on your path to the main lifepod launcher")
  time.sleep(2.5)
  print("You arrive at the main lifepod launcher to only 3 left.")
  print("You go a seemingly working pod and notice next to you is a working pod with a broken door.")
  print("Someone else is getting in lifepod 9, you remember that lifepod was not working correctly.")
  print("Do you tell him about the broken pod or leave ASAP?")
  choice = input("Type 'tell' or 'leave': ").strip().lower()
  
  if choice == 'tell':
        helptell()
  elif choice == 'leave':
        helpleave()
  else:
        print("Invalid choice. Please try again.")
        lefthelp()
def helptell():
  print('After you tell them that the pod is broken they respond with "Well I might as well be dead then"')
  print('"The only reason I\'m getting in pod 9 is because the other pods door is broken"')
  print('"I\'m going to try open it, I could use a hand?"')
  choice = input("Type 'help' or 'leave': ").strip().lower()
  
  if choice == 'help':
        tellhelp()
  elif choice == 'leave':
        tellleave()
  else:
        print("Invalid choice. Please try again.")
        helptell()
def tellleave():
  print('You turn back towards your escape pod and start the launch process')
  print('Behind you hear "So you leave me to die? Fine, I\'ll live and show you that you shouldn\'t have left me"')
  print("As you strap in you brace your self for the incoming Gs")
  print("3,2,1... Then you feel the force of one RS-25 booster behind you")
  print(r""" Then 
                ____   ___   ___  __  __ _ 
               | __ ) / _ \ / _ \|  \/  | |
               |  _ \| | | | | | | |\/| | |
               | |_) | |_| | |_| | |  | |_|
               |____/ \___/ \___/|_|  |_(_) 

                    __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ") """)
  print('"The aurora has exploded, the your lifepod\'s AI announces "WARNING INCOMING DEBRIS TO BACK OF POD"')
  print("You spin around to see the incoming debris and the possible extent of the damage")
  print("Only to see a lifepod coming directly at you, as you squint your eyes you make out a number")
  print("You realise that the number is 9, lifepod 9 the one that you left behind")
  print(r"""Now thats the reason of your death
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_|  """)
  print("Karma at it's finest")
  print("You have got 1 of 20 possible endings, try to get them all!")
def tellhelp():
  print("You run over and grab a crowbar from the floor and try force the door open")
  print("You start to see the door warp and hear the door screech as the door breaks revealing a lifepod")
  print("The other escapee thanks you for your help and you get in your pod")
  print("You wait to be thrust into space.")
  print(r"""3,2,1... then a blast echoes in your pod as you fly into the unknown
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(You saved the other person, well done!)")
  
def helpleave(): 
  print("You run towards your chosen lifepod and you get in and slam the launch button.")
  print("You feel your escape pod shudder as the engines roar to life.")
  print(r"""You feels the force of 3gs on your face as your pod plows into the unknown.
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You think back to yourself, about if you could of saved the other person in the lifepod 9")
  print("You have got 1 of 20 possible endings, try to get them all!")
def doordeath():
    print("You run towards your chosen lifepod and you get in and slam the launch button.")
    print("You wait to be thrust into space.")
    print("3,2,1... then nothing")
    print(r"""then fire. 
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
    print("You have got 1 of 20 possible endings, try to get them all!")
    print("(I would recommend playing a different pathway as this is one of the shortest!)")
    print("[As this pathway is very short I have made it so you have a 1 out of 5 chance to live]")
    print("[Better luck next time!]")
def door_4():
  print("You run towards your chosen lifepod and you get in and slam the launch button.")
  print("You wait to be thrust into space.")
  print(r"""3,2,1... then a blast echoes in your pod as you fly into the unknown
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("(I would recommend playing a different pathway as this is one of the shortest!)")
  print("[As this pathway is very short I have made it so you have a 1 out of 5 chance to live]")
  print("[You got lucky!]")
  
def choose_door(door_number):
    if door_number == 1:
        return doordeath()
    elif door_number == 2:
        return doordeath()
    elif door_number == 3:
        return doordeath()
    elif door_number == 4:
        return door_4()
    elif door_number == 5:
        return doordeath()
    else:
        return "Invalid choice. Please choose a lifepod between 1 and 5."
def leftrun():
  print("You arrive at the main lifepod bay to chaos.")
  print("You look around to see 5 lifepods that are open, but is it too good to be true?")
  user_choice = int(input("Choose a lifepod (1-5): "))
def runrightpath():
  print("You get to the main intersection")
  print("You face a choice")
  print("Do you raid the armoury or go to the commanders lifepod?")
  choice = input("Type 'armoury' or 'commanders': ").strip().lower()
  
  if choice == 'armoury':
        armoury()
  elif choice == 'commanders':
        rightcommanders()
  else:
        print("Invalid choice. Please try again.")
        runrightpath()
def rightcommanders():
  print("You arrive at the lifepod to see a small group of people attempting to access the pod")
  print("But people are flooding in from behind, you guess that in a few minutes the room will be flooded")
  print("As an alternative you can head to the cargo bay instead")
  print("Do you go into the commander's lifepod or head to the cargo bay?")
  choice = input("Type 'access' or 'cargo': ").strip().lower()
  
  if choice == 'access':
        rightcmdaccess()
  elif choice == 'cargo':
        cargobay()
  else:
        print("Invalid choice. Please try again.")
        rightcommanders()
def cargobay():
  print("You arrive at the bay to see open spacewalk module")
  print("You go in to see 4 ready to go spacesuits and a box of 20 new spacesuits")
  print("Do you use a new spacesuit or a used spacesuit?")
  choice = input("Type 'used' or 'new': ").strip().lower()
  
  if choice == 'used':
        usedsuit()
  elif choice == 'new':
        newsuit()
  else:
        print("Invalid choice. Please try again.")
        cargobay()
def usedsuit():
  print("You put on your spacesuit and step into the decompression chamber as you lock the doors and the decompression process starts")
  print("You feel around at the back of your spacesuit for the oxygen tank and then feel secure in the fact that locked in")
  print("You look around and see the void of space infront of you, there are 2 object that don't blend into void of space")
  print("On your left you see a communication and support satellite and on your right you see an out of ship lifepod")
  print("Where do you go?")
  choice = input("Type 'support' or 'lifepod': ").strip().lower()
  
  if choice == 'support':
        supportpod()
  elif choice == 'lifepod':
        lifepodpod()
  else:
        print("Invalid choice. Please try again.")
        usedsuit()
def lifepodpod():
  print("You use your manned maneuvering unit (Space jetpack) to make your way over to the lifepod")
  print("You get in and slam the launch button.")
  print("Then it finally dawns on you, that you are going home")
  print("You wait to be thrust into space.")
  print(r"""3,2,1... then a blast echoes in your pod as you fly into the unknown
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")
  
  

def supportpod():
  print("You use your manned maneuvering unit (Space jetpack) to make your way over to the support satellite")
  print("After entering the pod, you send out a SOS message to anyone able to help")
  print("But you realise you are out of range from the main ship")
  print("You attempt to move closer using the boosters, as you start the boosters you see a faint note on the dashboard")
  print(R'''It reads "Liquid O2 leaking, DO NOT USE BOOSTERS"
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| ''')
  print("You have got 1 of 20 possible endings, try to get them all!")
  
        
def newsuit():
  print("You put on your new suit and step into the decompression chamber as you lock the doors and the decompression process starts")
  print("You feel around at the back of your spacesuit for the oxygen tank")
  print(r"""Only to realise its not there 
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("If you can't do something, then don't do it")
  print("You have got 1 of 20 possible endings, try to get them all!")

def rightcmdaccess():
  print("You barge your way through the crowd and reach the keycard scanner")
  print("You unhook your access keycard and get shoved to the side, you pick your self up from the ground and look around for your keycard")
  print("Only to see someone using your card to access the lifepod, as the door opens you attempt to follow the people through the door")
  print(r"""As you enter you realise the door has been shut behind you and the escape pod launch doors have closed 
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("You are now a corpse floating around in space")
  print("You have got 1 of 20 possible endings, try to get them all!")
  def armoury():
  print("You arrive at the armoury and swipe your self in with your keycard")
  print("It seems like most of the lethal weapons have been taken already")
  print("You eye a stab-proof vest and put it on")
  print("The only other things that seem to be of worth are a taser and a crowbar")
  print("What do you choose?")
  choice = input("Type 'taser' or 'crowbar': ").strip().lower()
  
  if choice == 'taser':
        taser()
  elif choice == 'crowbar':
        crowbar()
  else:
        print("Invalid choice. Please try again.")
        armoury()
def crowbar():
  print(r"""
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣶⡄⠱⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⡙⣿⣿⡄⢹⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⢋⣠⠾⠋⠉⢹⣿⣷⢸⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠏⣠⠞⠁⠀⠀⠀⢸⣿⣿⢸⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⢡⡾⠋⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠁⣴⡟⠁⠀⠀⠀⠀⠀⠀⣿⡿⠀⣾⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⣼⠟⢁⣼⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣄⠁⠰⡿⠃⠀⠀⠀⠀⠀⠀⢠⡾⠁⣴⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⢀⡿⢀⣾⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⣼⡿⢃⣿⣿⠇⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣼⠟⠁⣸⣿⠏⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠃⠀⠀⠀⠀⠀
⠀⣾⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
  print("With your new found weapon you decide to find a way out")
  print("Do you head towards the mainlife pod launcher or head to the commanders lifepod?")
  choice = input("Type 'main' or 'commanders': ").strip().lower()
  
  if choice == 'main':
        crowbarmain()
  elif choice == 'commanders':
        crowbarcommanders()
  else:
        print("Invalid choice. Please try again.")
        crowbar()
def crowbarcommanders():
  print("You arrive to the commanders lifepod to see chaos unfolding, people banging on the door to the commanders lifepod")
  print("You tighten your grasp on the crowbar and squeeze your way through the crowd")
  print("You ask someone standing near the keycard scanner to move, they respond with force")
  print("You swing your crowbar at the attacker, but in the process hit someone else")
  print("One thing leads to another and a full scale riot breaks out")
  print(r"""Before you know it, you are lying on the on the floor out cold
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("Watch where you swing that thing!")
  print("You have got 1 of 20 possible endings, try to get them all!")
  
def crowbarmain():
  print("You arrive to an empty lifepod launcher, you see 3 lifepods and one with a broken door and one with no power")
  print("You think that you can use your crowbar to force open the broken door lifepod")
  print("Do you use your crowbar to open the lifepod or use a seemingly working lifepod?")
  choice = input("Type 'crowbar' or 'leave': ").strip().lower()
  
  if choice == 'crowbar':
        crowbarbreak()
  elif choice == 'leave':
        crowbarleave()
  else:
        print("Invalid choice. Please try again.")
        crowbar()
def crowbarleave():
  print("You run towards your chosen lifepod and you get in and slam the launch button.")
  print("You wait to be thrust into space.")
  print("3,2,1... then nothing")
  print(r"""then fire. 
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("You have got 1 of 20 possible endings, try to get them all!")
def crowbarbreak():
  print("You grab your crowbar and shove the end point of it into the door mechanism and attempt to pry it open")
  print("You hear the metal warping and feel the grasp of the doors loosen")
  print(r"""Then you feel the power against the crowbar disappear and see an open and working lifepod
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")
  
def taser():
  print(r"""
  +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / TASER  /'|       /'
    / TASER  /  `\    /'
   / TASER  /`-------'
  / TASER  /
 / TASER  /
(________(   
 `------'   """) 
  print("On your way out you grab a holster and strap it to your side")
  print("With your new found weapon you decide to find a way out")
  print("Do you head towards the mainlife pod launcher or head to the commanders lifepod?")
  choice = input("Type 'main' or 'commanders': ").strip().lower()
  
  if choice == 'main':
        tasermain()
  elif choice == 'commanders':
        tasercommanders()
  else:
        print("Invalid choice. Please try again.")
        taser()
def tasermain():
  print("You arrive at the lifepod launcher to see little to no lifepods left")
  print("You see an older model of lifepod open and someone getting in a newer model of lifepod")
  print("Do you take the older lifepod and possibly risk dying or tase the other person for access to theirs")
  choice = input("Type 'tase' or 'old': ").strip().lower()
  
  if choice == 'tase':
        maintaser()
  elif choice == 'old':
        mainold()
  else:
        print("Invalid choice. Please try again.")
        tasermain()
def maintaser():
  print("You sneak up behind the person, then aim and pull the trigger")
  print("A sharp ZAP sound echos around the lifepod as the person collapses")
  print("You dump the person outside the lifepod and start the launch")
  print("As you strap in you brace your self for the incoming Gs")
  print("3,2,1... Then you feel the force of one RS-25 booster behind you")
  print(r"""Then you look back and see the ship explode
  
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")
  print("You wonder if you didn't need to tase and kill that person to live")
def mainold():
  print("You slam the launch button and wait for the old booster to shock to life")
  print("But you hear nothing?")
  print(r"""Then you see a flash in the pod, then you are flying in the unknown
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/ """)
  print("You have got 1 of 20 possible endings, try to get them all!")
    
def tasercommanders():
  print("You arrive to the commanders lifepod to see chaos unfolding, people banging on the door to the commanders lifepod")
  print("You unhostler your taser and point it at the crowd and demand people to move out of the way, they comply")
  print("You shut the door behind you and relax a little at the sight of a seemingly working lifepod")
  print('As you start the launch process, you hear someone on the other side of the door shout "Don\'t leave us to die!')
  print("You can save the other people or save your self at the cost of the others")
  choice = input("Type 'save' or 'launch': ").strip().lower()
  
  if choice == 'save':
        tacmdsave()
  elif choice == 'launch':
        tacmdleave()
  else:
        print("Invalid choice. Please try again.")
        tasercommanders()
def tacmdleave():
  print("You ignore the cries for help and keep working on launching the lfepod")
  print("You strap in and get ready for the launch")
  print("You prepare for the incomming force upon your body")
  print("3,2,1... then nothing?")
  print(r"""
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("You died due a broken fuel line catching on fire")
  print("Maybe if someone else was there they could of warned you of this issue...  ")
  print("You have got 1 of 20 possible endings, try to get them all!")
  
def tacmdsave():
  print("You open the door and people rush in, then you shut the door and start the launch process again")
  print('Before you hit the launch button, someone shouts "WAIT, THE FUEL LINE IS BROKEN!"')
  print('The person who reveals them self as an engineer says')
  print('"If you were to start the boosters it would ignite the fuel killing us all!"')
  print('"I can fix it but I just need time"')
  print("Do you heed the warning and have it fixed or launch at the risk of kill everyone?")
  choice = input("Type 'fix' or 'launch': ").strip().lower()
  
  if choice == 'fix':
        savefix()
  elif choice == 'launch':
        savelaunch()
  else:
        print("Invalid choice. Please try again.")
        tacmdsave()
def savelaunch():
  print("You ignore the engineer and start the launch process")
  print("You prepare for the incomming force upon your body")
  print("3,2,1... then nothing?")
  print(r"""
 ____  _____    _  _____ _   _ 
|  _ \| ____|  / \|_   _| | | |
| | | |  _|   / _ \ | | | |_| |
| |_| | |___ / ___ \| | |  _  |
|____/|_____/_/   \_\_| |_| |_| """)
  print("You died due a broken fuel line catching on fire...")
  print("You ought to heed the warning from those who know more")
  print("You have got 1 of 20 possible endings, try to get them all!")


def savefix():
  print("You nod to the engineer and they begin fixing the fuel line")
  print("Then out of the PA system an automated voice shouts, HULL DAMAGE EXCEEDS CAPABILITY OF ARMOR, IMPLOSION IMMINENT")
  print('"Alright it\'s fixed, HOLD ON!"')
  print("The boosters roar to life and you feel the G-force on your face")
  print(r"""Then you look back and see the ship, then you see a blinding light 
                      __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")""")
  print(r"""The aurora is gone, but you and the others you escaped with aren't.
 ____  _   _ ______     _______     _______ ____  
/ ___|| | | |  _ \ \   / /_ _\ \   / / ____|  _ \ 
\___ \| | | | |_) \ \ / / | | \ \ / /|  _| | | | |
 ___) | |_| |  _ < \ V /  | |  \ V / | |___| |_| |
|____/ \___/|_| \_\ \_/  |___|  \_/  |_____|____/  """)
  print("You have got 1 of 20 possible endings, try to get them all!")


        
### below is the most important bit of code 
start_AD()

