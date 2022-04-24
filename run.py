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

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication

# race choice for player
RACE_ONE = "Vasher"
RACE_TWO = "Mortem"
RACE_THREE = "Bascula" 
RACE_FOUR = "Hemmel"
RACE_FIVE = "Human"
RACE_SIX = "Arratoi"
RACE_SEVEN = "Fulger"


PLAYER_HEALTH = 6
ENEMY_HEALTH = 4

MELEE_DAMAGE = 2
MAGIK_DAMAGE = 3


def player_attack_roll():
    while True:
        player_attack = random.randint(1, 6)
        return player_attack


def player_magic_roll():
    while True:
        player_magic = random.randint(1, 6)
        return player_magic


def enemy_attack_roll():
    while True:
        enemy_attack = random.randint(1, 6)
        return enemy_attack


def enemy_magic_roll():
    while True:
        enemy_magic = random.randint(1, 6)
        return enemy_magic


def enemy_attack_choice_roll():
    while True:
        enemy_attack_or_magic_choice_generator = random.randint(1, 6)
        return enemy_attack_or_magic_choice_generator


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


def player_melee_combat():
    """
    player melee combat engine for game
    """
    if player_attack_roll() >= 4:
        reduce_enemy_health_melee()
        print(f" hit! enemy has {ENEMY_HEALTH} hit points left")
    else:
        print("You missed")
    

def player_magic_combat():
    """
    player magic combat engine for game
    """ 

    if player_magic_roll() >= 5:
        reduce_enemy_health_magic()
        print(f"You hit with magic attack!, enemy has {ENEMY_HEALTH} hit points left")
    else:
        print("You hurl magical energy at the enemy but miss")


def enemy_melee_combat():
    """
    enemy melee combat engine for game
    """ 

    print("The enemy tries to melee attack you")
    time.sleep(2)
    if enemy_attack_roll() >= 4:
        reduce_player_health_melee()
        print(f"The enemy hit you with a melee attack! You have {PLAYER_HEALTH} hit points left")
    else:
        print("The enemy missed you with its melee attack")


def enemy_magic_combat():
    """
    computer magic combat engine for game
    """ 
    print("The enemy tries to hit you with a magic attack")
    time.sleep(2)
    if enemy_magic_roll() >= 5:
        reduce_player_health_magic()
        print(f"The enemy hit you with a magic attack! You have {PLAYER_HEALTH} hit points left")
    else:
        print("The enemy missed you with its magic attack")
    

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
        print("A melee attack\n"
              "B magic attack")
        choice = input(">>> ")
        if choice in answer_A:
            player_attack_roll()
            player_melee_combat()
            time.sleep(2)
        if choice in answer_B:
            player_magic_roll()
            player_magic_combat()
            time.sleep(2)
        if ENEMY_HEALTH > 0:
            enemy_attack_roll()
            enemy_magic_roll()
            enemy_attack_choice_roll()
            enemy_attack_choice()
        if ENEMY_HEALTH <= 0:
            print("You defeated the enemy!")
            time.sleep(2)
            start_menu()
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
        print(f"you have chosen a {RACE_ONE} called {character_name}")
        time.sleep(2)
        vahser_story()
    elif race in answer_B:
        print(f"you have chosen a {RACE_TWO} called {character_name}")
    elif race in answer_C:
        print(f"you have chosen a {RACE_THREE} called {character_name}")
    elif race in answer_D:
        print(f"you have chosen a {RACE_FOUR} called {character_name}")
    elif race in answer_E:
        print(f"you have chosen a {RACE_FIVE} called {character_name}")
    elif race in answer_F:
        print(f"you have chosen a {RACE_SIX} called {character_name}")
    elif race in answer_G:
        print(f"you have chosen a {RACE_SEVEN} called {character_name}")
    else:
        print("Please enter a valid Race choice. ")
        time.sleep(2)
        start_menu()
        

def vahser_story():
    
    """
    function to start vahser playthrough
    """ 

    time.sleep(1)
    print("\n"
    "The Vahser are a female only race of beautiful women who live in strange cities, under the sea.\n"
    "they use daggers and Aqua magic\n"
    )

    print("Fight!")
    combat_encounter()
    

start_menu()

