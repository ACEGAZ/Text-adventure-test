import time
import random

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
answer_E = ["E", "e"]
answer_F = ["F", "f"]
answer_G = ["G", "g"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# race choice for player
RACE_ONE = False
RACE_TWO = False
RACE_TWO = False
RACE_THREE = False
RACE_FOUR = False
RACE_FIVE = False
RACE_SIX = False
RACE_SEVEN = False

print(bool(RACE_ONE))
PLAYER_HEALTH = 10
ENEMY_HEALTH = 6

MELEE_DAMAGE = 2
MAGIK_DAMAGE = 3


def reduce_enemy_health_melee():
    """
    reduces enemy health by 2
    """
    global ENEMY_HEALTH
    ENEMY_HEALTH -= MELEE_DAMAGE


def reduce_player_health_melee():
    """
    reduces player health by 2
    """
    global PLAYER_HEALTH
    PLAYER_HEALTH -= MELEE_DAMAGE


def reduce_enemy_health_magic():
    """
    reduces enemy health by 3
    """
    global ENEMY_HEALTH
    ENEMY_HEALTH -= MAGIK_DAMAGE


def reduce_player_health_magic():
    """
    reduces player health by 3
    """
    global PLAYER_HEALTH
    PLAYER_HEALTH -= MAGIK_DAMAGE


def player_attack_roll():
    """
    returns a random number between 1 and 6 for player melee attack
    """
    while True:
        player_attack = random.randint(1, 6)
        return player_attack


def player_melee_combat():
    """
    player melee combat engine for game
    """
    if player_attack_roll() >= 4:
        reduce_enemy_health_melee()
        print(f" hit! enemy has {ENEMY_HEALTH} hit points left""\n")
    else:
        print("You missed\n")


def player_magic_roll():
    """
    returns a random number between 1 and 6 for player magic attack
    """
    while True:
        player_magic = random.randint(1, 6)
        return player_magic


def player_magic_combat():
    """
    player magic combat engine for game
    """ 

    if player_magic_roll() >= 5:
        reduce_enemy_health_magic()
        print(f"You hit with magic attack!, enemy has {ENEMY_HEALTH} hit points left""\n")
    else:
        print("You hurl magical energy at the enemy but miss\n")


def enemy_attack_roll():
    """
    returns a random number between 1 and 6 for enemy melee attack
    """
    while True:
        enemy_attack = random.randint(1, 6)
        return enemy_attack


def enemy_melee_combat():
    """
    enemy melee combat engine for game
    """

    print("The enemy tries to melee attack you\n")
    time.sleep(2)
    if enemy_attack_roll() >= 4:
        reduce_player_health_melee()
        print(f"The enemy hit you with a melee attack! You have {PLAYER_HEALTH} hit points left""\n")
        time.sleep(2)
    else:
        print("The enemy missed you with its melee attack\n")
        time.sleep(2)


def enemy_magic_roll():
    """
    returns a random number between 1 and 6 for enemy magic attack
    """
    while True:
        enemy_magic = random.randint(1, 6)
        return enemy_magic


def enemy_magic_combat():
    """
    computer magic combat engine for game
    """ 
    print("The enemy tries to hit you with a magic attack\n")
    time.sleep(2)
    if enemy_magic_roll() >= 5:
        reduce_player_health_magic()
        print(f"The enemy hit you with a magic attack! You have {PLAYER_HEALTH} hit points left""\n")
        time.sleep(2)
    else:
        print("The enemy missed you with its magic attack\n")
        time.sleep(2)
       

def enemy_attack_choice_roll():
    """
    returns a random number between 1 and 6 for enemy attack choice
    """
    while True:
        enemy_attack_or_magic_choice_generator = random.randint(1, 6)
        return enemy_attack_or_magic_choice_generator


def enemy_attack_choice():
    
    """
    decides which attack the enemy will use.
    """
    if enemy_attack_choice_roll() <= 4:
        enemy_melee_combat()
    elif enemy_attack_choice_roll() >= 5:
        enemy_magic_combat()


def combat_encounter():
    """
    runs combat until enemy or player is dead
    """
    while ENEMY_HEALTH > 0 or PLAYER_HEALTH > 0:
        print("A: melee attack\n"
              "B: magic attack\n")
        choice = input(">>>  ")
        if choice in answer_A:
            player_attack_roll()
            player_melee_combat()
            time.sleep(2)
        elif choice in answer_B:
            player_magic_roll()
            player_magic_combat()
            time.sleep(2)
        if ENEMY_HEALTH > 0:
            enemy_attack_roll()
            enemy_magic_roll()
            enemy_attack_choice_roll()
            enemy_attack_choice()
        if ENEMY_HEALTH <= 0:
            print("You defeated the enemy!\n")
            time.sleep(2)
            break
        if PLAYER_HEALTH <= 0:
            print("You Died!")
            time.sleep(2)
            start_menu()
 

def start_menu():
    """
    start menu for game
    """     

    print("Welcome to Potentia text adventure!\n"
    "You will be given 3 choices or a yes or no question\n"
    "Your choice will change the story as it plays.\n"
    "You will be given a choice of race which will change certian aspects of the game.\n"
    "Have fun!!!") 
    race = input("choose your race...\n"
                 "A Vahser\n"
                 "B Mortem\n"
                 "C Bascula\n"
                 "D Hemmel\n"
                 "E Human\n"
                 "F Arratoi\n"
                 "G Fulger\n"
                 "\n"
                 ">>>"
                 )
    character_name = input("Please name your character>>> ")

    if race in answer_A:
        global RACE_ONE
        RACE_ONE = "Vahser"
        print(f"you have chosen a {RACE_ONE} called {character_name}")
        time.sleep(2)
        story()
    elif race in answer_B:
        global RACE_TWO
        RACE_TWO = "Mortem"
        print(f"you have chosen a {RACE_TWO} called {character_name}")
        time.sleep(2)
        story()
    elif race in answer_C:
        global RACE_THREE
        RACE_THREE = "Bascula"
        time.sleep(2)
        story()
        print(f"you have chosen a {RACE_THREE} called {character_name}")
    elif race in answer_D:
        global RACE_FOUR
        RACE_THREE = "Hemmel"
        time.sleep(2)
        story()
        print(f"you have chosen a {RACE_FOUR} called {character_name}")
    elif race in answer_E:
        global RACE_FIVE
        RACE_THREE = "Human"
        time.sleep(2)
        story()
        print(f"you have chosen a {RACE_FIVE} called {character_name}")
    elif race in answer_F:
        global RACE_SIX
        RACE_THREE = "Arratoi"
        time.sleep(2)
        story()
        print(f"you have chosen a {RACE_SIX} called {character_name}")
    elif race in answer_G:
        global RACE_SEVEN
        RACE_THREE = "Fulger"
        time.sleep(2)
        story()
        print(f"you have chosen a {RACE_SEVEN} called {character_name}")
    else:
        print("Please enter a valid Race choice. ")
        time.sleep(2)
        start_menu()
        

def story():
    
    """
    function to start vahser playthrough
    """ 

    time.sleep(1)
    print("\n"
    "The Vahser are a female only race of beautiful women who live in strange cities, under the sea.\n"
    "they use daggers and Aqua magic\n"
    )

    print("You wake up on a ship, sailing towards the Human city of Ronmara\n"
           "You have been given a quest by Queen Callista to investigate to infiltrate a secret council meeting\n"
           "Suddenly, a drunken sailor approches you and says 'Hello, swethart. I heard you Vahser will get with anyone. How bout a kiss?'\n"
           "what will you do?\n"
           "A: Punch him in his gap toothed face?\n"
           "B: Use your charm and good looks to talk him down?\n"
           "C: Tell him he has has no chance with you and walk away?\n"
           "D: Special Race option")

    choice = input(">>>  ")

    if choice in answer_A:
        option_punch()
    elif choice in answer_B:
        option_use_charm()
    elif choice in answer_C:
        option_no_chance()
    elif RACE_ONE and choice in answer_D:
        vahser_option_1()
    elif RACE_TWO and choice in answer_D:
        mortem_option_1()
    elif RACE_THREE and choice in answer_D:
        bascula_option_1()
    elif RACE_FOUR and choice in answer_D:
        hemmel_option_1()
    elif RACE_FIVE and choice in answer_D:
        human_option_1()
    elif RACE_SIX and choice in answer_D:
        Arratoi_option_1()
    elif RACE_SEVEN and choice in answer_D:
        fulger_option_1()


def option_punch():
    print("You punch that sailor square in his face and knock out his last tooth!"
          "He gets up and charges at you. Time to fight!")
    combat_encounter()


def option_use_charm():
    print("You speak softly and tell the sailor you are young and innocent\n"
          "You bat your eyelids and ask that he please leave such an innocent creature be\n"
          "The sailor sees sence and walks away")


def option_no_chance():
    print("You laugh at the sailor and tell him that a bottom feeder like him\n"
           "has no chance with a girl as beautiful as you\n"
           "The sailors eyes well and he walks away sobbing")


def vahser_option_1():
    print("You are a Vahser")


def mortem_option_1():
    print("you are a Mortem")


def bascula_option_1():
    print("you are a Bascula")


def hemmel_option_1():
    print("you are a Hemmel")


def human_option_1():
    print("you are a Human")


def Arratoi_option_1():
    print("you are a Arratoi")


def fulger_option_1():
    print("you are a Fulger")
   

start_menu()

