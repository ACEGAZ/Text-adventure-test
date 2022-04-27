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
RACE_THREE = False
RACE_FOUR = False
RACE_FIVE = False
RACE_SIX = False
RACE_SEVEN = False

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
        print(f"You hit with magic attack!, enemy has {ENEMY_HEALTH} hit"
              "points left""\n")
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
        print("The enemy hit you with a melee attack!"
              f"You have {PLAYER_HEALTH} hit points left""\n")
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
        print("The enemy hit you with a magic attack!"
              f"You have {PLAYER_HEALTH} hit points left""\n")
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


def start_game():
    """
    Asks if user is ready to start the game with chosen name and race
    """
    choice = input(">>>  ")
    if choice in yes:
        time.sleep(2)
        print("\n")
        story()
    elif choice in no:
        time.sleep(2)
        start_menu()
    else:
        print(f"invalid input. Please type {yes} or {no}"
              "\n")
        time.sleep(4)
        start_game()


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
          "You will be given a choice of race which will\n"
          "change certian aspects of the game.\n Have fun!!!\n"
          "\n")
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
        print(f"you have chosen a {RACE_ONE} called {character_name}""\n"
              "\n"
              "The Vahser are an all female race that stand at about 5 ft.\n"
              "The live in impressive cities under the sea and use aqua\n"
              "magic to keep there cities in huge bubbles\n"
              "They are very beautiful and can have any colour hair\n"
              "but it is always dark in colour.\n"
              "\n"
              "Vahser use daggers, Aqua and shadow magic and can seduce"
              " most men with ease.\n"
              "\n")
        time.sleep(2)
        print(f"Do you want to play a {RACE_ONE} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()

    elif race in answer_B:
        global RACE_TWO
        RACE_TWO = "Mortem"
        print(f"you have chosen a {RACE_TWO} called {character_name}""\n"
              "\n"
              "The Mortem are an undead race that live on a frozen island\n"
              "to the north. They are skeletal in looks and vary in size\n"
              "depending on what race they were in life\n"
              "They are completely dependant on sensory magic to emmulate\n"
              "all their senses as they have no eyes, skin, ears, ect"
              "\n"
              "The Mortem have to hide their skelital appearnce as they\n"
              "are sworn enemies of all the other races due to the war\n"
              "of the undead over a thousand years ago"
              " The mortem haven't been seen in a long time but\n"
              "the other races haven't forgotten the war\n"
              "\n"
              "The Mortem are very differnt these days and seek peace\n"
              "they use many melee weapons, Sensory and Cryo magic\n"
              "\n")
        time.sleep(2)
        print(f"Do you want to play a {RACE_TWO} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()

    elif race in answer_C:
        global RACE_THREE
        RACE_THREE = "Bascula"
        print(f"you have chosen a {RACE_THREE} called {character_name}""\n"
              "\n"
              "The Bascula are a race of reptilian craftsmen and businessman\n"
              "They stand 8 to 10 feet tall and craft most of the weapons"
              "in Potentia.\n"
              "They live in Volcanoes and are completely immune to fire.\n"
              "\n"
              "Bascula use large hammers called vasara's, Pyro and Hardening"
              "magic. their large size intimidates most people")
        time.sleep(2)
        print(f"Do you want to play a {RACE_THREE} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()
        
    elif race in answer_D:
        global RACE_FOUR
        RACE_FOUR = "Hemmel"
        print(f"you have chosen a {RACE_FOUR} called {character_name}""\n"
              "\n"
              "The Hemmel are a genderless race that reproduce by splitting" 
              " their cells. they stand about 6ft tall and usually use"
              " thier Telekenetic magic to leveitate rather than walk."
              " Hemmel bodies have no bones so they are physically the"
              " weakest race in Potentia, however they make up for this"
              " with thier vast intelligence and logical thinking."
              " They live in a floating city, high in the sky\n"
              "\n"
              "Hemmel use their Telekinesis magic to wield weapons"
              " as well as creation and zephyr magic\n"
              "\n")
        time.sleep(2)
        print(f"Do you want to play a {RACE_FOUR} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()

    elif race in answer_E:
        global RACE_FIVE
        RACE_FIVE = "Human"
        print(f"you have chosen a {RACE_FIVE} called {character_name}""\n"
              "\n"
              "Humans stand anywhere from 5 to 7 ft tall and rule"
              " Potentia. They are the most dominant race of all and"
              " they are the only race able to use Soul magic but"
              " it is completely forbidden.\n"
              "\n"
              "Humans are known to use many types of weapons and"
              " magics, the only magic that is their own is Soul magic\n"
              "\n")
        time.sleep(2)
        print(f"Do you want to play a {RACE_FIVE} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()

    elif race in answer_F:
        global RACE_SIX
        RACE_SIX = "Arratoi"
        print(f"you have chosen a {RACE_SIX} called {character_name}""\n"
              "\n"
              "The Arratoi are a race of ratlike people standing at 6 ft tall"
              " They study martial arts in thier home to the South, inside a"
              " mountian. They have even developed a magic based on martial"
              " arts known as Martial magic. But thier most dangerous magic is"
              " thier teleportation magic as it allows for instant travel"
              " but is incredibly hard to learn\n"
              "\n"
              "The Arratoi use martial arts, Terra, Teleportation and Martial"
              " magic\n"
              "\n")
        time.sleep(2)
        print(f"Do you want to play a {RACE_SIX} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()

    elif race in answer_G:
        global RACE_SEVEN
        RACE_SEVEN = "Fulger"
        print(f"you have chosen a {RACE_SEVEN} called {character_name}""\n"
              "\n"
              "The Fulger are a wolflike people that stand at 9ft tall"
              "They are incredible fighters and use a magic called Beasthood"
              " to increase thier senses and physical trait to ridiculous"
              " heights. They live in a city, surrounded by permanent lighning"
              "storm. The Fulger get thier name from the electrical magic they"
              " use known as Fulgeration magic. Fulger can draw power from a"
              "storm and are immune to electrical attacks\n"
              "\n"
              "Fulger use metal claws, Fulgeration and Beasthood magic")
        time.sleep(2)
        print(f"Do you want to play a {RACE_SEVEN} called {character_name} ?"
              "\n"
              "yes:\n"
              "no:")
        start_game()
        
    else:
        print("Please enter a valid Race choice. ")
        time.sleep(2)
        start_menu()


def story():
    """
    function to start the playthrough
    """

    time.sleep(1)

    print("You wake up on a ship, sailing towards the Human city of Jatorri\n"
          "A friend of yours named Teslora lives there"
          " and you are going to visit her"
          " Suddenly, a drunken human sailor approches you and says 'Hello,"
          " Mate. I need a drink and you've got that hip flask."
          " give it er'\n"
          "\n"
          "what will you do?\n"
          "A: Punch him in his gap toothed face?\n"
          "B: Tell him the flask is full of water?\n"
          "C: Tell him it's your booze and he can sod off?\n"
          "D: Special Race options\n"
          "Vahser: Use seduction\n"
          "Mortem: Reveal your undead face to scare him\n"
          "Bascula: intimidate him with your large size\n"
          "Hemmel: Outsmart him with overwhelming intellect\n"
          "Human: Offer to share with a feloow human\n"
          "Arratoi: Hit him with a martial arts blow to knock him out\n"
          "Fulger: Surround your body with crackeling lightning and growl")

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
