import random # import random libraries


#setting default game system
#Stage Option in dictionary
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
#Bot ability configure setting in list
Bot_ability =  ['punch','kick','jump','block']

#Player and bot life configure setting
Player_life = 100
Bot_life = 100

#Damage action setting in dictionary
Damage = {'punch': 5, 'kick': 7, 'jump': 1, 'block': 0}

# Introduction for collect player name and formatting their username.
print("Welcome to our fighting game")
player_name = input("Please enter your user name: ")

# Select stage by showing all  list of stage into console output.  
for palace in Stage_Option.items():
    print(palace)

# let player select one stage from dict and check name of stage.
player_stage = input("Select your stage: ").capitalize()
if player_stage not in Stage_Option.values():
    raise Exception("This stage does not exist. Please choose again.")
else:
    print(" This stage has selected by player !!! ")

#show a counter 1 to 3 with for loop
for i in range(1, 4):
    print(i)
    
# Game loop
while True:
    # inside game loop will show your stage from selected than  format by string variable 
    print("##############")
    print("{} stage".format(player_stage))
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
        print("{} got {}".format(player_name, player_action))
        Bot_life -= Damage[player_action]


    # Bot's turn and random a chance for choose in any situation  to make a damage to player
    bot_action = random.choice(Bot_ability)
    print("Bot got {}".format(bot_action))
    Player_life -= Damage[bot_action]
    
    # Check for winner by every  situation
    if Player_life <= 0:
        print("Bot wins!")
        print(" Good bye ! see you next time. ")
        break
    elif Bot_life <= 0:
        print("{} wins!".format(player_name))
        print(f" Good bye {player_name} ! see you next time. ")
        break
    else:
        print("Player: {}/{}  Bot: {}/{}".format(Player_life, 100, Bot_life, 100)) # show a Hp of both plyer during fighting