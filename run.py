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
              f" You have {PLAYER_HEALTH} hit points left""\n")
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
              f" You have {PLAYER_HEALTH} hit points left""\n")
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
        time.sleep(2)
        story_part_1()
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
    global PLAYER_HEALTH
    global ENEMY_HEALTH
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
        else:
            print("Please enter a valid input")
            time.sleep(2)
            combat_encounter()

        if ENEMY_HEALTH > 0:
            enemy_attack_roll()
            enemy_magic_roll()
            enemy_attack_choice_roll()
            enemy_attack_choice()
        elif ENEMY_HEALTH <= 0:
            print("You defeated the enemy!\n")
            time.sleep(2)
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 6
            print("Your hit points have been restored.\n"
                  f"You have {PLAYER_HEALTH} hit points")
            break
        elif PLAYER_HEALTH <= 0:
            print("You Died!")
            time.sleep(2)
            start_menu()


def start_menu():
    """
    start menu for game
    """

    print("Welcome to Potentia text adventure!\n"
          "You will be given choices or a yes or no question\n"
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
              "magic. Their large size intimidates most people")
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


def story_part_1():
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
          "B: Share your flask with him.?\n"
          "C: Tell him the flask is full of water\n"
          "D: Special Race options\n"
          "\n"
          "Vahser: Use seduction\n"
          "Mortem: Reveal your undead face to scare him\n"
          "Bascula: intimidate him with your large size\n"
          "Hemmel: Bore him with a long, detailed explination\n"
          "Human: Point out another human with a bigger flask\n"
          "Arratoi: Hit him with a martial arts blow to knock him out\n"
          "Fulger: Surround your body with crackeling lightning and growl")

    choice = input(">>>  ")

    if choice in answer_A:
        option_punch()
    elif choice in answer_B:
        option_share()
    elif choice in answer_C:
        option_lie()
    elif RACE_ONE and choice in answer_D:
        print("\n")
        race_option_1()
    elif RACE_TWO and choice in answer_D:
        print("\n")
        race_option_1()
    elif RACE_THREE and choice in answer_D:
        print("\n")
        race_option_1()
    elif RACE_FOUR and choice in answer_D:
        print("\n")
        race_option_1()
    elif RACE_FIVE and choice in answer_D:
        print("\n")
        race_option_1()
    elif RACE_SIX and choice in answer_D:
        print("\n")
        race_option_1()
    elif RACE_SEVEN and choice in answer_D:
        print("\n")
        race_option_1()
    else:
        print("Please select a vaild choice\n"
              "\n")
        time.sleep(2)
        story_part_1()


def option_punch():
    """
    Starts a combat encounter
    """
    print("You punch that sailor square in his face and knock out his"
          " last tooth!"
          " He gets up and charges at you.\n Time to fight!")
    combat_encounter()
    print("\n You drop the sailor but get thrown in the brig for fighting.\n"
          "The next day you are tossed onto the docks\n"
          "\n"
          "Feeling a little beat up you begin to walk towards your friends"
          " house.")


def option_share():
    """
    option share with sailor
    """
    print("You offer to share what's in your flask. The sailor smiles and"
          " begins drinking with you. You wake up the next day on Jatorri"
          " city docks.")


def option_lie():
    """
    option to lie to sailor
    """
    print("You lie to the salior and tell him your flask is just water")


def race_option_1():
    """
    lets the player choose an option depending on what race they are
    """
    if RACE_ONE:
        print("You speak softly and tell the sailor you are young"
              "and innocent.\n"
              "You bat your eyelids and ask that he please leave such an"
              " innocent creature be\n"
              "The sailor sees sense and walks away")

    elif RACE_TWO:
        print("You pull down the cloth covering and reveal your face"
              " The sailor sees the black sockets where your eyes should be."
              "\nHe turns white and passes out.")

    elif RACE_THREE:
        print("You look down on the tiny Human and tell him to walk away!"
              " The sailor quickly turns tail and runs")

    elif RACE_FOUR:
        print("You begin tell the sailor why alcohol is bad for him and"
              " and explain in explicit detail how alcohol is made"
              " The sailor falls asleep whilst you're talking")

    elif RACE_FIVE:
        print("You point the sailor towards a man with a flask twice the size"
              " of yours. The sailor quickly heads over to bother the man.")

    elif RACE_SIX:
        print("Before the sailor can say another word you deliver a swift"
              " punch in the solar plexus which knocks him unconscious")

    elif RACE_SEVEN:
        print("Lightning begins to crackel from your body and arc out."
              " You stare at the sailor and let out a guttural growl."
              " The sailor leaves without saying another word.")


start_menu()
