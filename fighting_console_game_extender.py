import random

# setting a default by initialize any value for player and bot before start game 
Player_life = 100
Bot_life = 100
Damage = {'punch': 5, 'kick': 7, 'jump': 1, 'block': 0}
Bot_ability =  ['punch','kick','jump','block']
# setting a bot start pack before random
Bot_character = []

Character_option = {
    'char-1':'Eddy',
    'char-2':'Amber',
    'char-3':'George',
    'char-4':'Alice',
    'char-5':'Bob',
    'char-7':'Jean'
}

#pull all character option into a Bot_character list
Bot_character.extend(Character_option.values())

Stage_Option = {
    'Stage-1':'Beach',
    'Stage-2':'City',
    'Stage-3':'Forest',
    'Stage-4':'Night club',
    'Stage-5':'Metro station',
    'Stage-6':'Railway station',
    'Stage-7':'Old temple',
    'Stage-8':'Entity Playground',
    'Stage-9':'Graveyard'
}

#game introduction 
print("Welcome a our fighting game ")

#chosen any character in dictionary 
print(" select your character ")
for character in Character_option.items():
    print(character)

#check player input
Plyer_selected = input(" choses a character here : ").capitalize()
if Plyer_selected not in Character_option.values():
    raise Exception(" this character does not exist here now !")
else:
    print(f"Player has selected {Plyer_selected} !! ")

#let's bot random select all character from Bot_character list
Bot_selected = random.choice(Bot_character)
# check if have same character with player input
if Bot_selected in Plyer_selected:
    Character_option.popitem()
else:
    print(f"Bot  has selected {Bot_selected} !!")

#chosen any stage in dictionary 
for palace in Stage_Option.items():
    print(palace)
    
#check choose stage from player
Plyer_stage = input(" choses a stage here : ").capitalize()
if Plyer_stage not in Stage_Option.values():
    raise Exception("This stage does not exist. Please choose again.")
else:
    print(" This stage has selected by player !!! ")

#start counter 1 to 3 before game loop
for i in range (1,4):
    print(f" start in {i} ")
    
#game loop
while True:
    # inside game loop will show your stage from selected than  format by string variable 
    print("##############")
    print("{} stage".format(Plyer_stage))
    print("##############")

    # Player's turn this way let's player input any action to fight with bot only in each a turn.
    player_action = input("Enter your action (punch, Kick, jump, block) or press 'q' to quit: ")
    
    #check plyer input when have any input from them.
    if player_action == 'q':
        print("See you next time, bye!")
        break
    elif player_action not in Damage:
        print("Invalid action. Please choose again.")
        continue
    else:
        print("{} got {}".format(Plyer_selected, player_action))
        Bot_life -= Damage[player_action]


    # Bot's turn and random a chance for choose in any situation  to make a damage to player
    bot_action = random.choice(Bot_ability)
    print("{} got {}".format(Bot_selected,bot_action))
    Player_life -= Damage[bot_action]
    
    # Check for winner by every  situation
    if Player_life <= 0:
        print(f"{Bot_selected} wins!")
        print(" Good bye ! see you next time. ")
        break
    elif Bot_life <= 0:
        print("{} wins!".format(Plyer_selected))
        print(f" Good bye {Plyer_selected} ! see you next time. ")
        break
    else:
        print("{}:/{}  {}:/{}".format(Plyer_selected,100,Bot_selected, 100))