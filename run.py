import time
import random


class Enemy:
    """
    class for all enemies
    """
    def __init__(self, name):
        self.name = name


enemy = Enemy("Sailor")


PASSWORD = ["Nadaren",
            "nadaren",
            "NADAREN",
            "Nadaren.",
            "nadaren.",
            "NADAREN."
            ]

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
ENEMY_HEALTH = 8

MELEE_DAMAGE = 2
MAGIK_DAMAGE = 3


def reset_race():
    """
    resets race to false and used when game is restarted
    """
    global RACE_ONE
    RACE_ONE = False
    global RACE_TWO
    RACE_TWO = False
    global RACE_THREE
    RACE_THREE = False
    global RACE_FOUR
    RACE_FOUR = False
    global RACE_FIVE
    RACE_FIVE = False
    global RACE_SIX
    RACE_SIX = False
    global RACE_SEVEN
    RACE_SEVEN = False


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
    if RACE_ONE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You attack the " + enemy.name + " with your daggers\n"
                  "and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n" 
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_TWO:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print(" You swing with your scythe and hit the " + enemy.name +
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_THREE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print(" You crash down your Vasara and hit the " + enemy.name +
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_FOUR:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You levitate and slash with floating\n"
                  "swords and hit the " + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_FIVE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You slash with your sword and hit the " + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_SIX:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You unleash a powerful martial arts strike and hit the\n"
                  + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("You missed\n")

    elif RACE_SEVEN:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You slash with your sharp, metal claws and hit the "
                  + enemy.name +
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
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
    if RACE_ONE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a jet of water flying at the " + enemy.name +
                  " and hit!\n"
                  " The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Aqua magic misses\n")

    elif RACE_TWO:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send shards of ice flying at the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Cryo magic misses\n")

    elif RACE_THREE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a fireball flying at the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Pyro magic misses\n")

    elif RACE_FOUR:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a blast of wind towards the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  " points left.\n")
        else:
            print("Your zephyr magic misses\n")

    elif RACE_FIVE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You drain some of the " + enemy.name + "soul!"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Soul magic misses\n")

    elif RACE_SIX:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a chunk of rock flying towards the "
                  + enemy.name + " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Terra magic misses\n")

    elif RACE_SEVEN:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a bolt of lightning flying at the " + enemy.name +
                  " and hit!\n"
                  "The " + enemy.name + f" has {ENEMY_HEALTH} hit\n"
                  "points left.\n")
        else:
            print("Your Fulgeration magic misses\n")


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

    print("The " + enemy.name + " tries to melee attack you\n")
    time.sleep(2)
    if enemy_attack_roll() >= 3:
        reduce_player_health_melee()
        print("The " + enemy.name + " hit you with a melee attack!"
              f" You have {PLAYER_HEALTH} hit points left""\n")
        time.sleep(2)
    else:
        print("The " + enemy.name + " missed you with its melee attack\n")
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
    print("The " + enemy.name + " tries to hit you with a magic attack\n")
    time.sleep(2)
    if enemy_magic_roll() >= 5:
        reduce_player_health_magic()
        print("The " + enemy.name + " hit you with a magic attack!"
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
            print("Please enter a valid input\n")
            time.sleep(2)
            combat_encounter()

        if ENEMY_HEALTH > 0:
            enemy_attack_roll()
            enemy_magic_roll()
            enemy_attack_choice_roll()
            enemy_attack_choice()
        elif ENEMY_HEALTH <= 0:
            print("You defeated the " + enemy + "\n")
            time.sleep(2)
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 8
            print("Your hit points have been restored.\n"
                  f"You have {PLAYER_HEALTH} hit points\n"
                  "\n")
            break

        if PLAYER_HEALTH <= 0:
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 8
            print("You Died!")
            time.sleep(2)
            start_menu()


def combat_encounter_capture_or_escape():
    """
    runs combat until enemy or player health is zero.
    if the player loses the capture option will play,
    and if the player wins story part 3 will play.
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
            print("Please enter a valid input\n")
            time.sleep(2)
            combat_encounter()

        if ENEMY_HEALTH > 0:
            enemy_attack_roll()
            enemy_magic_roll()
            enemy_attack_choice_roll()
            enemy_attack_choice()
        elif ENEMY_HEALTH <= 0:
            print("You defeated Razik!\n")
            time.sleep(2)
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 8
            print("Your hit points have been restored.\n"
                  f"You have {PLAYER_HEALTH} hit points\n"
                  "\n"
                  "You over power Razik! He falls to\n"
                  "the ground! You are no longer being\n"
                  "pursued.\n"
                  "\n")
            story_part_3()

        if PLAYER_HEALTH <= 0:
            print("Razik manages to overpower you!\n"
                  "You fall to the floor, barely conscious.\n"
                  "\n")
            time.sleep(2)
            PLAYER_HEALTH = 10
            ENEMY_HEALTH = 8
            option_capture()


def start_menu():
    """
    start menu for game
    """
    reset_race()

    print("Welcome to Potentia text adventure!\n"
          "\n"
          "Potentia is a static world built on magic.\n"
          "Magic makes the world move and change.\n"
          "Even the sun (known as the Vatra) is made\n"
          "everyday by 200 casters channeling magic.\n"
          "to produce a ball of fire to light the world.\n"
          "Without it the world would be dark!\n"
          "\n"
          "In this game\n"
          "You will be given choices or a yes or no question\n"
          "Your choice will change the story as it plays.\n"
          "You will be given a choice of race which will\n"
          "change certian aspects of the game.\n"
          "\n"
          "Have fun!!!\n"
          "\n")
    race = input("choose your race...\n"
                 "A: Vahser\n"
                 "B: Mortem\n"
                 "C: Bascula\n"
                 "D: Hemmel\n"
                 "E: Human\n"
                 "F: Arratoi\n"
                 "G: Fulger\n"
                 "\n"
                 ">>>"
                 )

    global character_name
    character_name = input("Please name your character>>> ")

    while True:

        if race in answer_A:
            global RACE_ONE
            RACE_ONE = "Vahser"
            print(f"you have chosen a {RACE_ONE} called {character_name}""\n"
                  "\n"
                  "The Vahser are an all female race that stand at\n"
                  "about 5 ft. The live in impressive cities under the sea\n"
                  "and use aqua magic to keep there cities in huge bubbles\n"
                  "They are very beautiful and can have any colour hair\n"
                  "but it is always dark in colour.\n"
                  "\n"
                  "Vahser use daggers, Aqua and shadow magic and can seduce"
                  " most men with ease.\n"
                  "\n")
            time.sleep(2)
            print(f"Do you want to play a {RACE_ONE} called {character_name}?"
                  "\n"
                  "yes:\n"
                  "no:")
            start_game()

        elif race in answer_B:
            global RACE_TWO
            RACE_TWO = "Mortem"
            print(f"you have chosen a {RACE_TWO} called {character_name}""\n"
                  "\n"
                  "The Mortem are an undead race that live on a frozen\n"
                  "island to the north. They are skeletal in looks and vary\n"
                  "in size. Depending on what race they were in life\n"
                  "They are completely dependant on sensory magic to\n"
                  "emmulate all their senses as they have no eyes,\n"
                  "skin, ears, ect"
                  "\n"
                  "The Mortem have to hide their skelital appearnce as they\n"
                  "are sworn enemies of all the other races due to the war\n"
                  "of the undead over a thousand years ago."
                  " The mortem haven't been seen in a long time but\n"
                  "the other races haven't forgotten the war\n"
                  "\n"
                  "The Mortem are very differnt these days and seek peace\n"
                  "they use scythe weapons, Sensory and Cryo magic\n"
                  "\n")
            time.sleep(2)
            print(f"Do you want to play a {RACE_TWO} called {character_name}?"
                  "\n"
                  "yes:\n"
                  "no:")
            start_game()

        elif race in answer_C:
            global RACE_THREE
            RACE_THREE = "Bascula"
            print(f"you have chosen a {RACE_THREE} called {character_name}""\n"
                  "\n"
                  "The Bascula are a race of reptilian craftsmen and\n"
                  "businessman. They stand 8 to 10 feet tall and craft\n"
                  "most of the weapons in Potentia.\n"
                  "They live in Volcanoes and are completely immune to fire.\n"
                  "\n"
                  "Bascula use large hammers called vasara's, Pyro\n"
                  "and Hardening magic.\n"
                  "Their large size intimidates most people\n"
                  "\n")
            time.sleep(2)
            print(f"Do you want to play a {RACE_THREE} "
                  f"called {character_name}?"
                  "\n"
                  "yes:\n"
                  "no:")
            start_game()

        elif race in answer_D:
            global RACE_FOUR
            RACE_FOUR = "Hemmel"
            print(f"you have chosen a {RACE_FOUR} called {character_name}""\n"
                  "\n"
                  "The Hemmel are a genderless race that reproduce by\n"
                  "splitting their cells. they stand about 6ft tall\n"
                  "and usually use thier Telekenetic magic to leveitate\n"
                  "rather than walk. Hemmel bodies have no bones so they are\n"
                  "physically the weakest race in Potentia, however\n"
                  "they make up for this with thier vast intelligence and\n"
                  "logical thinking. They live in a floating city,\n"
                  "high in the sky."
                  "\n"
                  "Hemmel use their Telekinesis magic to wield weapons"
                  " as well as creation and zephyr magic\n"
                  "\n")
            time.sleep(2)
            print(f"Do you want to play a {RACE_FOUR} called {character_name}?"
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
            print(f"Do you want to play a {RACE_FIVE} called {character_name}?"
                  "\n"
                  "yes:\n"
                  "no:")
            start_game()

        elif race in answer_F:
            global RACE_SIX
            RACE_SIX = "Arratoi"
            print(f"you have chosen a {RACE_SIX} called {character_name}""\n"
                  "\n"
                  "The Arratoi are a race of ratlike people standing at 6 ft\n"
                  "tall They study martial arts in thier home to the South,\n"
                  "inside a mountian. They have even developed a magic based\n"
                  "on martial arts known as Martial magic. But thier most\n"
                  "dangerous magic is thier teleportation magic as it allows\n"
                  "for instant travel but is incredibly hard to learn\n"
                  "\n"
                  "The Arratoi use martial arts, Terra,\n"
                  "Teleportation and Martial magic\n"
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
                  "The Fulger are a wolflike people that stand at 9ft tall\n"
                  "They are incredible fighters and use a magic called\n"
                  "Beasthood to increase thier senses and physical trait\n"
                  "to ridiculous heights. They live in a city, surrounded\n"
                  "by permanent lighning storm. The Fulger get thier\n"
                  "name from the electrical magic they use known as\n"
                  "Fulgeration magic. Fulger can draw power from a\n"
                  "storm and are immune to electrical attacks"
                  "\n"
                  "Fulger use metal claws, Fulgeration and Beasthood magic\n"
                  "\n")
            time.sleep(2)
            print(f"Do you want to play a {RACE_SEVEN}"
                  f" called {character_name}?"
                  "\n"
                  "yes:\n"
                  "no:")
            start_game()

        else:
            print("\n"
                  "Please enter a valid Race choice.\n"
                  "\n")
            race = input("choose your race...\n"
                         "A: Vahser\n"
                         "B: Mortem\n"
                         "C: Bascula\n"
                         "D: Hemmel\n"
                         "E: Human\n"
                         "F: Arratoi\n"
                         "G: Fulger\n"
                         "\n"
                         ">>> ")


def start_game():
    """
    Asks if user is ready to start the game with chosen name
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


def story_part_1():
    """
    function to start the playthrough
    """

    time.sleep(1)

    print("You wake up on a ship, sailing towards the Human city of Jatorri\n"
          "A friend of yours named Teslora lives there\n"
          "and you are going to visit her.\n"
          "Suddenly, a drunken human\n"
          "approches you and says 'Hello,\n"
          "Mate. I need a drink and you've got that hip flask.\n"
          "give it er!'\n"
          "\n"
          "what will you do?\n"
          "\n"
          "A: Punch him in his gap toothed face?\n"
          "B: Share your flask with him?\n"
          "C: Tell him the flask is full of water?\n"
          "D: Special Race options\n")
    if RACE_ONE:
        print("Vahser: Use seduction.")

    elif RACE_TWO:
        print("Mortem: Reveal your undead face to scare him.\n"
              "\n")

    elif RACE_THREE:
        print("Bascula: intimidate him with your large size.\n"
              "\n")

    elif RACE_FOUR:
        print("Hemmel: Bore him with a long, detailed explination.\n"
              "\n")

    elif RACE_FIVE:
        print("Human: Point out another human with a bigger flask.\n"
              "\n")

    elif RACE_SIX:
        print("Arratoi: Hit him with a martial arts blow to knock him out.\n"
              "\n")

    elif RACE_SEVEN:
        print("Fulger: Surround your body with lightning and growl.\n"
              "\n")

    choice = input(">>> ")

    while True:
        if choice in answer_A:
            option_punch()
        elif choice in answer_B:
            option_share()
        elif choice in answer_C:
            option_lie()
        elif RACE_ONE and choice in answer_D:
            print("You speak softly and tell the sailor you are young"
                  "and innocent.\n"
                  "You bat your eyelids and ask that he please leave such an"
                  " innocent creature be\n"
                  "The sailor sees sense and walks away\n"
                  "\n"
                  "You arrive at the docks and walk towards your\n"
                  "friends house.")
            time.sleep(2)
            story_part_2()
        elif RACE_TWO and choice in answer_D:
            print("You pull down the cloth covering and reveal your face.\n"
                  "The sailor sees the black sockets where your eyes should\n"
                  "be. He turns white and passes out.\n"
                  "\n"
                  "You arrive at the docks and walk towards your\n"
                  "friends house.")
            time.sleep(2)
            story_part_2()

        elif RACE_THREE and choice in answer_D:
            print("You look down on the tiny Human and tell him to walk away!"
                  " The sailor quickly turns tail and runs\n"
                  "\n"
                  "You arrive at the docks and walk towards your\n"
                  "friends house.")
            time.sleep(2)
            story_part_2()

        elif RACE_FOUR and choice in answer_D:
            print("You begin tell the sailor why alcohol is bad for him and"
                  " and explain in explicit detail how alcohol is made"
                  " The sailor falls asleep whilst you're talking\n"
                  "\n"
                  "You arrive at the docks and walk towards\n"
                  "your friends house\n")
            time.sleep(2)
            story_part_2()
        elif RACE_FIVE and choice in answer_D:
            print("You point the sailor towards a man with a flask\n"
                  "twice the size\n"
                  " of yours. The sailor quickly heads over to bother\n"
                  "the man."
                  "\n"
                  "You arrive at the docks and walk towards\n"
                  "your friends house\n")
            time.sleep(2)
            story_part_2()
        elif RACE_SIX and choice in answer_D:
            print("Before the sailor can say another\n"
                  "word you deliver a swift\n"
                  "punch in the solar plexus which knocks him unconscious\n"
                  "\n"
                  "You arrive at the docks and walk towards.\n"
                  "your friends house.\n")
            time.sleep(2)
            story_part_2()
        elif RACE_SEVEN and choice in answer_D:
            print("Lightning begins to crackel from your body and arc out.\n"
                  "You stare at the sailor and let out a guttural growl.\n"
                  "The sailor leaves without saying another word.\n"
                  "\n"
                  "You arrive at the docks and walk towards your\n"
                  "friends house.\n")
            time.sleep(2)
            story_part_2()

        else:
            print("Please select a vaild choice.")
            choice = input(">>> ")


def option_punch():
    """
    Starts a combat encounter
    """
    print("You punch that sailor square in his face and knock out his\n"
          "last tooth!\n"
          "\n"
          "He gets up and charges at you.\n"
          "\n"
          "Time to fight!\n"
          "\n")
    combat_encounter()
    print("\n You drop the sailor but get thrown in the brig for fighting.\n"
          "The next day you are tossed onto the docks\n"
          "\n"
          "Feeling a little beat up you begin to walk towards your friends"
          " house.\n"
          "\n")
    story_part_2()


def option_share():
    """
    option share with sailor
    """
    print("You offer to share what's in your flask. The sailor smiles and"
          " begins drinking with you. You wake up the next day on Jatorri"
          " city docks.\n"
          "You feel a very hungover and decide to walk to your friends house\n"
          "\n")
    time.sleep(2)
    story_part_2()


def option_lie():
    """
    option to lie to sailor
    """
    print("You lie to the salior and tell him your flask is just water\n"
          "The sailor looks ominously at the flask and tries to snatch it!"
          "\n"
          "What will you do?\n"
          "A: Fight the sailor?\n"
          "B: Throw the flask overboard?"
          )
    choice = input(">>>  \n"
                   "\n")

    while True:
        if choice in answer_A:
            print("You decide to fight the sailor and charge at him!")
            combat_encounter()
            time.sleep(2)
            story_part_2()
        elif choice in answer_B:
            print("You throw the flask overboard. The sailor, desprate\n"
                  "for a drink jumps in after the flask\n"
                  "\n"
                  "The rest of your trip is very peaceful and you arrive\n"
                  "at the docks. You begin walking to your friends house.\n"
                  "\n")
            time.sleep(2)
            story_part_2()
        else:
            print("Please select a valid choice.")
            choice = input(">>> ")


def story_part_2():
    """
    function to start the second part of the story
    """
    global enemy
    enemy = Enemy("Soldier, Razik")

    print("You make your way through Jatorri city. The city is a marvel of\n"
          "Human ingenuity. The city is built into a canyon and supended\n"
          "above it. The city is connected by huge suspension bridges.\n"
          "\n"
          "You eventually make it to Teslora's house and knock on the\n"
          "door...\n"
          "\n")
    time.sleep(5)
    print("There is no answer...\n"
          "\n")
    time.sleep(5)
    print("You look at the door lock and notice that it is broken\n"
          "You slowly push the door open to reveal Tesloras' corpse.\n"
          "\n"
          "The room is covered in blood and Teslora is slumped in\n"
          "her chair with a bloody note stuck into her body.\n"
          "\n"
          "What do you do?\n"
          "\n"
          "A: Search the room?\n"
          "B: Read the bloody note?\n"
          "C: Find a member of the Jatorri city gaurd to report a murder?\n")

    choice = input(">>> ")

    while True:
        if choice in answer_A:
            option_search()
        elif choice in answer_B:
            read_bloody_note()
        elif choice in answer_C:
            find_gaurd()
        else:
            print("Please select a valid choice.")
            choice = input(">>> ")


def option_search():
    """
    function to allow player to search the room
    and then either escape or be captured.
    """
    global character_name
    print("You begin frantically searching the room, looking for anything!\n")
    print(f"You find a sealed letter with '{character_name}' written on it\n"
          "\n")
    print(f"The letter reads 'Dear, {character_name}.\n"
          "\n"
          "I had hoped to see you one last time but it looks like my\n"
          "death is inevitable. A killer has been hunting Jattori council\n"
          "members and I fear I am next. if you find me, please grant my\n"
          "body liberation. \n"
          "I know we didn't see each other as often as we should but you\n"
          "were my best friend in my lonely life.\n"
          "\n"
          "please leave Jatorri and never look back... But\n"
          "if you wish to avenge me then go to the place\n"
          "where light is born.\n"
          "\n")
    print(f"Thank you, {character_name}.")
    time.sleep(2)
    print("\n"
          "Will you grant Tesloras' body liberation?\n"
          "It is a ritual to disperse a persons body into magical energy\n"
          "but it takes a few minutes to preform\n"
          "\n"
          "yes?\n"
          "No?")
    choice = input(">>> ")

    while True:

        if choice in yes:
            print("You perform the ritual and Tesloras' body falls away into\n"
                  "shimmering colours... She is at peace.\n"
                  "\n")
            time.sleep(2)
            print("Suddenly the Jatorri city military burst through the\n"
                  "door!\n Before you know what's\n"
                  "happening you are tackeled and bound\n"
                  "\n")
            time.sleep(2)
            option_capture()
        elif choice in no:
            print("You hear a noise outside the house. It sounds like 10 or \n"
                  "more people about to burst through the door.\n"
                  "\n"
                  "What do you do?\n"
                  "A: Hide\n"
                  "B: Run\n"
                  "C: Special Race option:\n")

            if RACE_ONE:
                print("Vahser: Use your Shadow magic to hide."
                      "\n")
            elif RACE_TWO:
                print("Mortem: Use your Sensory magic to try and locate\n"
                      "the best way out.\n"
                      "\n")
            elif RACE_THREE:
                print("Bascula: Use your Hardening magic to harden your.\n"
                      "body and try to break down a wall and escape."
                      "\n")
            elif RACE_FOUR:
                print("Hemmel: Use your creation magic to try and\n"
                      "fabricate a wall to hide behind."
                      "\n")
            elif RACE_FIVE:
                print("Human: Use your Soul magic to try and make yourself\n"
                      "ethereal and pass through the building."
                      "\n")
            elif RACE_SIX:
                print("Arratoi: Use your teleportation magic to try to\n"
                      "teleport out of the building."
                      "\n")
            elif RACE_SEVEN:
                print("Fulger: Activate your Beasthood magic to increase\n"
                      "your. strength and try to tear your way out of\n"
                      "the building."
                      "\n")

            choice = input(">>> ")
            while True:
                if choice in answer_A:
                    print("You hide in a nearby cupboard. The military\n"
                          "breaksthrough The door and begins seraching \n"
                          "the house. It doesnt take long before you are\n"
                          "found. You are bound and taken away\n"
                          "\n")
                    time.sleep(2)
                    option_capture()
                elif choice in answer_B:
                    print("You run out the back door! You can hear\n"
                          "The front door burst open as you flee the\n"
                          "scene but you manage to escape\n"
                          "\n")
                    time.sleep(2)
                    option_escape()
                elif RACE_ONE and choice in answer_C:
                    print("You surround yourself in shadows and become\n"
                          "completely invisible. You watch as the\n"
                          "military pour into the house and find\n"
                          "the body. You take this chance to escape.\n"
                          "\n")
                    time.sleep(2)
                    option_escape()
                elif RACE_TWO and choice in answer_C:
                    print("You begin scanning the house with your\n"
                          "Sensory magic and discover a secret\n"
                          "passage under the house. You run to\n"
                          "The basement and escape.\n"
                          "\n")
                    time.sleep(2)
                    option_escape()
                elif RACE_THREE and choice in answer_C:
                    print("You Harden your body and smash through\n"
                          "A wall! it makes a lot of noise and\n"
                          "military hear and chase you.\n"
                          "They manage to capture you.\n"
                          "\n")
                    time.sleep(2)
                    option_capture()
                elif RACE_FOUR and choice in answer_C:
                    print("You make a wall in front of you.\n"
                          "The military don't suspect anything\n"
                          "but you are stuck! Eventually your magic\n"
                          "runs out and you are discovered and taken\n"
                          "away.\n"
                          "\n")
                    time.sleep(2)
                    option_capture()
                elif RACE_FIVE and choice in answer_C:
                    print("You try to use Soul magic to become\n"
                          "ethereal but it is a very high level\n"
                          "form of magic that takes time.\n"
                          "unfortunatly, you are not fast enough\n"
                          "and you are taken by the Military.\n"
                          "\n")
                    time.sleep(2)
                    option_capture()
                elif RACE_SIX and choice in answer_C:
                    print("You easily teleport a small distance\n"
                          "Away from the house and escape.\n"
                          "\n")
                    time.sleep(2)
                    option_escape()
                elif RACE_SEVEN and choice in answer_C:
                    print("You increase your strength and start\n"
                          "tearing through the building.\n"
                          "But you are not able to get through\n"
                          "the wall before the military captures you.\n"
                          "\n")
                    time.sleep(2)
                    option_capture()
                else:
                    print("Please select a vaild choice.")
                    choice = input(">>> ")
        else:
            print(f"Please type {yes} or {no}.\n")
            choice = input(">>> ")


def read_bloody_note():
    """
    function to allow player to read the bloody note
    and then either escape or be captured.
    """
    print("You peel the note from Tesloras' body\n"
          "and begin to read. The note reads.\n"
          "\n"
          "ANY WHO WORK FOR OR UNDER THE COUNCIL\n"
          "SHALL FALL VICTIM TO THE JATORRI CITY\n"
          "SLAYER! NO ONE AND NOTHING CAN STOP ME!\n"
          "\n"
          "IF YOU WISH TO STOP ME YOU'RE WELCOME TO\n"
          "TRY. YOU WILL FIND ME WHERE LIGHT IS BORN.")
    time.sleep(2)
    print("As you finish reading the note you hear\n"
          "a commotion from outside!\n"
          "\n"
          "What do you do?\n"
          "A: Hide?\n"
          "B: Run?\n"
          "C: Special Race option")
    if RACE_ONE:
        print("Vahser: Use your Shadow magic to hide."
              "\n")
    elif RACE_TWO:
        print("Mortem: Use your Sensory magic to try and locate\n"
              "the best way out.\n"
              "\n")
    elif RACE_THREE:
        print("Bascula: Use your Hardening magic to harden your.\n"
              "body and try to break down a wall and escape."
              "\n")
    elif RACE_FOUR:
        print("Hemmel: Use your creation magic to try and fabricate a\n"
              "wall to hide behind."
              "\n")
    elif RACE_FIVE:
        print("Human: Use your Soul magic to try and make yourself\n"
              "ethereal and pass through the building."
              "\n")
    elif RACE_SIX:
        print("Arratoi: Use your teleportation magic to try to\n"
              "teleport out of the building."
              "\n")
    elif RACE_SEVEN:
        print("Fulger: Activate your Beasthood magic to increase\n"
              "your. strength and try to tear your way out of\n"
              "the building."
              "\n")

    choice = input(">>> ")

    while True:

        if choice in answer_A:
            print("You hide in a nearby cupboard. The military\n"
                  "breaksthrough The door and begins seraching \n"
                  "the house. It doesnt take long before you are\n"
                  "found. You are bound and taken away"
                  "\n")
            time.sleep(2)
            option_capture()
        elif choice in answer_B:
            print("You run out the back door! You can hear\n"
                  "The front door burst open as you flee the\n"
                  "scene but you manage to escape\n"
                  "\n")
            time.sleep(2)
            option_escape()
        elif RACE_ONE and choice in answer_C:
            print("You surround yourself in shadows and become\n"
                  "completely invisible. You watch as the\n"
                  "military pour into the house and find\n"
                  "the body. You take this chance to escape.\n"
                  "\n")
            time.sleep(2)
            option_escape()
        elif RACE_TWO and choice in answer_C:
            print("You begin scanning the house with your\n"
                  "Sensory magic and discover a secret\n"
                  "passage under the house. You run to\n"
                  "The basement and escape.\n"
                  "\n")
            time.sleep(2)
            option_escape()
        elif RACE_THREE and choice in answer_C:
            print("You Harden your body and smash through\n"
                  "A wall! it makes a lot of noise and\n"
                  "military hear and chase you.\n"
                  "They manage to capture you.\n"
                  "\n")
            time.sleep(2)
            option_capture()
        elif RACE_FOUR and choice in answer_C:
            print("You make a wall in front of you.\n"
                  "The military don't suspect anything\n"
                  "but you are stuck! Eventually your magic\n"
                  "runs out and you are discovered and taken\n"
                  "away.\n"
                  "\n")
            time.sleep(2)
            option_capture()
        elif RACE_FIVE and choice in answer_C:
            print("You try to use Soul magic to become\n"
                  "ethereal but it is a very high level\n"
                  "form of magic that takes time.\n"
                  "unfortunatly, you are not fast enough\n"
                  "and you are taken by the Military.\n"
                  "\n")
            time.sleep(2)
            option_capture()
        elif RACE_SIX and choice in answer_C:
            print("You easily teleport a small distance\n"
                  "Away from the house and escape.\n"
                  "\n")
            time.sleep(2)
            option_escape()
        elif RACE_SEVEN and choice in answer_C:
            print("You increase your strength and start\n"
                  "tearing through the building.\n"
                  "But you are not able to get through\n"
                  "the wall before the military captures you.\n"
                  "\n")
            time.sleep(2)
            option_capture()
        else:
            print("Please select a vaild choice.")
            choice = input(">>> ")


def find_gaurd():
    """
    function to allow player to find a gaurd
    and then be captured.
    """
    print("You run out the door as fast as\n"
          "you can to find a gaurd, but as you\n"
          "open the front door a group of\n"
          "military miltia are standing in\n"
          "front of you. They see the body behind\n"
          "you and quickly arrest you.\n"
          "A bag is thrown over your head\n"
          "and you are taken away.\n"
          "\n")
    time.sleep(2)
    option_capture()


def option_capture():
    """
    function if player is captured.
    """
    global PLAYER_HEALTH
    print("A bag is thrown over your head.\n"
          "\n")
    time.sleep(2)
    print("You are taken to an unkown location.\n"
          "and placed in a secure room.\n"
          "Your hands are chained and you can\n"
          "feel that your magic is being blocked\n"
          "somehow.\n"
          "\n")
    time.sleep(2)
    print("The door opens and a beautiful Vahser woman steps\n"
          "through. She sits across from you and in a\n"
          "menacing voice says 'I'm going to ask you\n"
          "some questions and you're going to answer.\n"
          "them. Because if you don't it will be...\n"
          "painfull.'\n"
          "\n"
          "Are you the Jatorri city slayer?\n"
          "\n"
          "What will you do?\n"
          "\n"
          "A: Tell her your're not the slayer?\n"
          "B: Tell her Your're not answering any questions?\n"
          "C: Spit in her face!?")

    choice = input(">>> ")

    while True:
        if choice in answer_A:
            print("You tell her that you're not the slayer.\n"
                  "She looks at you and says 'I believe you.\n"
                  "You look far too stupid to be the real slayer.\n"
                  "\n"
                  "So... who are you?'\n"
                  "\n"
                  "A: Tell her who you are?\n"
                  "B: Tell her you're nobody?\n"
                  "C: Spit in her face?")
            choice = input(">>> ")
            while True:
                if choice in answer_A:
                    print(f"You tell her your name is {character_name}\n"
                          "and that you were just here visiting your\n"
                          "friend.\n"
                          "\n")
                    time.sleep(2)
                    print("The woman then asks 'So say I were to\n"
                          "release you, what would you do next?\n"
                          "\n"
                          "A: Find the Slayer?\n"
                          "B: Go home, you've had enough of this place?")
                    choice = input(">>> ")

                    while True:

                        if choice in answer_A:
                            print("You tell her you are going to find the\n"
                                  "Slayer and make him pay for killing\n"
                                  "your friend!")
                            time.sleep(2)
                            print("The woman smiles and says 'Good!\n"
                                  "I was hoping you'd say that. My\n"
                                  "name is Harika and I work for the\n"
                                  "The Council of Strazar. We oversee\n"
                                  "Everything in Potentia. I'm willing\n"
                                  "to let yo go on this little vengance\n"
                                  "quest. Anything that causes the Slayer\n"
                                  "a problem is good for us.")
                            time.sleep(2)
                            print("Harika signals a gaurd\n"
                                  "and he unchains you\n"
                                  "Harika says 'there, you're free to go\n"
                                  "\n"
                                  "Some advise, the slayer often leaves a\n"
                                  "a calling card which goads the reader\n"
                                  "into going to the place where\n"
                                  "light is born.\n"
                                  "\n"
                                  "Any idiot could tell you that, that would\n"
                                  "be the Vatra tower but we've searched and\n"
                                  "found nothing. I trust you'll have more\n"
                                  "luck. Good hunting!\n"
                                  "\n")
                            story_part_3()
                        elif choice in answer_B:
                            print("You tell the woman you're sick of this\n"
                                  "city and just want to leave. The woman\n"
                                  "says 'How disappointing.\n"
                                  "But we can't have\n"
                                  "word of the Slayer getting out. I'm\n"
                                  "afraid you'll have to stay here.\n"
                                  "\n")
                            time.sleep(2)
                            print("You're taken to a cell and left to rot\n")
                            time.sleep(2)
                            print("You died!")
                            time.sleep(2)
                            start_menu()
                        else:
                            print("Please select a valid choice\n")
                            choice = input(">>> ")

                elif choice in answer_B:
                    print("You tell her you're nobody and was just\n"
                          "in the wrong place at the wrong time\n"
                          "\n")
                    time.sleep(2)
                    print("The woman stands and pulls a knife from her\n"
                          "hip and slowly stabs it into your hand.\n"
                          "\n"
                          "The knife digs into your hand!")
                    PLAYER_HEALTH = 8
                    print(f"You have {PLAYER_HEALTH} hit points left\n"
                          "\n"
                          "The woman asks again. Who are you?\n"
                          "\n"
                          "A: Tell her who you are?\n"
                          "B: Spit in her face?")
                    choice = input(">>> ")

                    while True:
                        if choice in answer_A:
                            print("You tell her your name is\n"
                                  f"{character_name}\n"
                                  "and that you were just here visiting your\n"
                                  "friend.\n"
                                  "\n")
                            time.sleep(2)
                            print("The woman then asks 'So say I were to\n"
                                  "release you, what would you do next?\n"
                                  "\n"
                                  "A: Find the Slayer?\n"
                                  "B: Go home.\n"
                                  "You've had enough of this place?\n")
                            choice = input(">>> ")
                            while True:
                                if choice in answer_A:
                                    print("You tell her you are going to\n"
                                          "find the Slayer and make\n"
                                          "him pay for killing\n"
                                          "your friend!\n"
                                          "\n")
                                    time.sleep(2)
                                    print("The woman smiles and says 'Good!\n"
                                          "I was hoping you'd say that. My\n"
                                          "name is Harika and I work for the\n"
                                          "The Council of Strazar.\n"
                                          "We oversee\n"
                                          "Everything in Potentia.\n"
                                          "I'm willing\n"
                                          "to let yo go on this\n"
                                          "little vengance\n"
                                          "quest. Anything that causes the\n"
                                          "Slayer a problem is good for us.")
                                    time.sleep(2)
                                    print("Harika signals a gaurd and\n"
                                          "he unchains you\n"
                                          "Harika says 'there, you're \n"
                                          "free to go good hunting!\n"
                                          "\n")
                                    story_part_3()
                                elif choice in answer_B:
                                    print("You tell the woman you're sick\n"
                                          "of this city and just want\n"
                                          "to leave. The woman\n"
                                          "says 'How disappointing. But we\n"
                                          "can't have word of the Slayer\n"
                                          "getting out. I'm\n"
                                          " afraid you'll have to stay here.\n"
                                          "\n")
                                    time.sleep(2)
                                    print("You're taken to a cell and left\n"
                                          "to rot\n")
                                    time.sleep(2)
                                    print("You died!")
                                    time.sleep(2)
                                    start_menu()
                                else:
                                    print("Please select a valid choice\n")
                                    choice = input(">>> ")

                        elif choice in answer_B:
                            print("You spit in her face!\n"
                                  "The woman pulls a knife from her hip and\n"
                                  "stabs you in the throat!!!\n")
                            time.sleep(2)
                            print("You died!\n"
                                  "\n")
                            PLAYER_HEALTH = 10
                            start_menu()
                        else:
                            print("Please select a valid choice?\n")
                            choice = input(">>> ")

                elif choice in answer_C:
                    print("You spit in her face!\n"
                          "The woman pulls a knife from her hip and\n"
                          "stabs you in the throat!!!\n")
                    time.sleep(2)
                    print("You died!\n"
                          "\n")
                    PLAYER_HEALTH = 10
                    start_menu()
                else:
                    print("Please select a valid choice?\n")
                    choice = input(">>> ")

        elif choice in answer_B:
            print("You refuse to answer any questions.\n"
                  "The woman stands and pulls a knife from her\n"
                  "hip and slowly stabs it into your hand.\n"
                  "\n"
                  "The knife digs into your hand!")
            PLAYER_HEALTH = 8
            print(f"You have {PLAYER_HEALTH} hit points left\n"
                  "\n"
                  "The woman asks again. Who are you?\n"
                  "\n"
                  "A: Tell her who you are?\n"
                  "B: Spit in her face?")

            choice = input(">>> ")
            while True:

                if choice in answer_A:
                    print(f"You tell her your name is {character_name}\n"
                          "and that you were just here visiting your\n"
                          "friend.\n"
                          "\n")
                    time.sleep(2)
                    print("The woman then asks 'So say I were to\n"
                          "release you, what would you do next?\n"
                          "\n"
                          "A: Find the Slayer?\n"
                          "B: Go home, you've had enough of this place?")
                    choice = input(">>> ")

                    while True:
                        if choice in answer_A:
                            print("You tell her you are going to find the\n"
                                  "Slayer and make him pay for killing\n"
                                  "your friend!\n"
                                  "\n")
                            time.sleep(2)
                            print("The woman smiles and says 'Good!\n"
                                  "I was hoping you'd say that. My\n"
                                  "name is Harika and I work for the\n"
                                  "The Council of Strazar. We oversee\n"
                                  "Everything in Potentia. I'm willing\n"
                                  "to let yo go on this little vengance\n"
                                  "quest. Anything that causes the Slayer\n"
                                  "a problem is good for us.")
                            time.sleep(2)
                            print("Harika signals a gaurd and he unchains\n"
                                  "you. Harika says 'there, you're \n"
                                  "free to go, good hunting!")
                            story_part_3()
                        elif choice in answer_B:
                            print("You tell the woman you're sick of this\n"
                                  "city and just want to leave. The woman\n"
                                  "says 'How disappointing. But we can't\n"
                                  "have word of the Slayer getting out.\n"
                                  "I'm afraid you'll have to stay here.\n"
                                  "\n")
                            time.sleep(2)
                            print("You're taken to a cell and left to rot\n")
                            time.sleep(2)
                            print("You died!")
                            time.sleep(2)
                            start_menu()
                        else:
                            print("Please select a valid choice\n")
                            choice = input(">>> ")

                elif choice in answer_B:
                    print("You spit in her face!\n"
                          "The woman pulls a knife from her hip and\n"
                          "stabs you in the throat!!!\n")
                    time.sleep(2)
                    print("You died!\n"
                          "\n")
                    PLAYER_HEALTH = 10
                    start_menu()
                else:
                    print("Please select a valid choice?\n")
                    choice = input(">>> ")

        elif choice in answer_C:
            print("You spit in her face!\n"
                  "The woman pulls a knife from her hip and\n"
                  "stabs you in the throat!!!\n")
            time.sleep(2)
            print("You died!\n"
                  "\n")
            PLAYER_HEALTH = 10
            start_menu()

        else:
            print("Please select a valid choice?\n")
            choice = input(">>> ")


def option_escape():
    """
    function if player escapes.
    """
    print("You manage to get away from the house but\n"
          "but hear a man from behind you shout\n"
          "'over there, they're escaping!'\n"
          "\n"
          "Gaurds and solders start running after you.\n"
          "\n"
          "What do you do\n"
          "A: Take to the rooftops?\n"
          "B: Head for the back alleys?")
    choice = input(">>> ")

    while True:
        if choice in answer_A:
            print("You climb up a window ledge and get to\n"
                  "the rooftops. You jump from rooftop to rooftop\n"
                  "and lose all but one of the solders.\n"
                  "\n"
                  "You see a 10 ft gap up ahead!\n"
                  "\n"
                  "do you jump?\n"
                  "Yes:\n"
                  "No:\n"
                  "\n")
            choice = input(">>> ")
            while True:
                if choice in yes:
                    time.sleep(2)
                    print("You jump the gap! You land on the other\n"
                          "side and continue running")
                    time.sleep(2)
                    print("The soldier chasing you leaps the gap!"
                          "You get a good look at him. He is a\n"
                          "Fulger with a look of determination in\n"
                          "his eyes!\n"
                          "\n"
                          "He starts casting bolts of lightning at you\n"
                          "What do you do?\n"
                          "A: Stop and fight the soldier?\n"
                          "B: Jump the 20 ft drop to the street below?\n"
                          "\n")
                    choice = input(">>> ")
                    while True:

                        if choice in answer_A:
                            print("You stop and stand your ground!\n"
                                  "prepare to fight!!!")
                            time.sleep(2)
                            combat_encounter_capture_or_escape()
                        elif choice in answer_B:
                            print("You jump to the ground below and\n"
                                  "manage to not break your legs! The\n"
                                  "soldier hesitates and you manage\n"
                                  "to escape.\n"
                                  "\n")
                            story_part_3()
                        else:
                            print("Please select a valid choice")
                            choice = input(">>> ")

                elif choice in no:
                    time.sleep(2)
                    print("You can't bring yourself to jump\n"
                          "You stop running and are quickly taken\n"
                          "down by the solder! He handcuffs you and\n"
                          "takes you in.")
                    option_capture()

                else:
                    print(f"Please type {yes} or {no}.\n")
                    choice = input(">>> ")

        elif choice in answer_B:
            print("You head into the back alleys.\n"
                  "They twist and turn. Eventually\n"
                  "you come to a fork.\n"
                  "What do you do?\n"
                  "\n"
                  "A: Go left?\n"
                  "B: Go right?\n"
                  "\n")
            choice = input(">>> ")
            while True:
                if choice in answer_A:
                    print("You take the left path.\n"
                          "The path leads to a dead\n"
                          "end. Gaurds quickly find\n"
                          "you and take you down!\n"
                          "\n")
                    option_capture()
                elif choice in answer_B:
                    print("You take the right path.\n"
                          "The alley comes to an end\n"
                          "and you come out at a small\n"
                          "square that leads to a\n"
                          "suspension bridge.\n"
                          "\n"
                          "You run across the bridge.\n"
                          "You get half way across before\n"
                          "you notice that some guards have\n"
                          "followed you!\n"
                          "\n"
                          "What do you do?\n"
                          "A: Shake the bridge?\n"
                          "B: Carry on running?\n"
                          "\n")
                    choice = input(">>> ")
                    while True:
                        if choice in answer_A:
                            print("You shake the bridge from left\n"
                                  "to right! The gaurds have\n"
                                  "trouble hanging on and fall\n"
                                  "over the sides! you take this\n"
                                  "chance and manage to escape\n"
                                  "completely.\n"
                                  "\n")
                            story_part_3()
                        elif choice in answer_B:
                            print("You carry on run but it is\n"
                                  "difficult to get your footing\n"
                                  "now that so many people are on\n"
                                  "the bridge\n"
                                  "\n"
                                  "The gaurds eventually manage to catch\n"
                                  "you and you are taken in.\n"
                                  "\n")
                            option_capture()
                        else:
                            print("Please select a valid choice")
                        choice = input(">>> ")

                else:
                    print("Please select a valid choice")
                    choice = input(">>> ")
        else:
            print("Please select a valid choice?")
            choice = input(">>> ")


def story_part_3():
    """
    function to start the third part of the story.
    """
    global enemy
    enemy = Enemy("Slayer")

    print("Now that you're not being persued you\n"
          "can begin your search for the Slayer.\n"
          "\n"
          "You begin your search by heading to\n"
          "Vatra tower. You search the tower for\n"
          "hours but find nothing.\n"
          "\n")
    time.sleep(2)
    print("Suddenly you feel a pull towards a door\n"
          "in the tower. You go towards the door and\n"
          "can't stop yourself from reaching out.\n"
          "You touch the door and symbols begin to\n"
          "circle around you. The symbols are a\n"
          "series of numbers and letters which read\n"
          "\n"
          "14 = N\n"
          "N - 13\n"
          "N - 10\n"
          "D - 3\n"
          "A + N + 3\n"
          "D + A\n"
          "R - D\n"
          "\n")
    print("You hear a voice in your head that\n"
          "tells you to speak the\n"
          "word it wants to hear.\n"
          "\n"
          "What do you say to the door?\n")

    choice = input(">>> ")
    while True:
        if choice in PASSWORD:
            print("\n"
                  "You say the word 'Nadaren' and\n"
                  "the door begins to distort and you\n"
                  "are sucked through a dimensional\n"
                  "space.")
            time.sleep(2)
            print("You find yourself in a large chamber\n"
                  "\n"
                  "There is a masked person standing in the\n"
                  "room with you who says\n"
                  f"'Welcome {character_name}. you have no idea\n"
                  "how long i've been waiting for you.\n"
                  "There's something special about you\n"
                  f"{character_name}. Only a master in\n"
                  "the art of magic can get to this place\n"
                  "... a master or a Nadaren! You, you\n"
                  "possess an incredible power! The power\n"
                  "to level an entire continent!\n"
                  "But your power is not been yet realised.\n"
                  "\n"
                  f"So, will you join me {character_name}?'\n"
                  "\n"
                  "Yes:\n"
                  "No:\n")
            choice = input(">>> ")
            while True:
                if choice in yes:
                    print("You accept the masked strangers offer\n"
                          "\n"
                          "The stranger pulls takes off thier mask\n"
                          "to reveal the face of your friend, Teslora\n"
                          "She says 'I'm sorry for the deceit,\n"
                          f"{character_name} but I had to fake my\n"
                          "death to throw off the council. I used\n"
                          "the body of the last council member I\n"
                          "killed and used Soul magic to change thier\n"
                          "appearance to look like me.\n"
                          "\n"
                          "The council would have killed\n"
                          "you if they knew what\n"
                          "you were. I acted as the Slayer to take\n"
                          "down council members and draw you too me\n"
                          "\n"
                          "Now, together we can destroy the rulers of\n"
                          "this world!\n"
                          "\n")
                    end()
                elif choice in no:
                    print("You refuse the strangers offer.\n"
                          "\n"
                          "They look at you and say 'Well, if\n"
                          "you're not with me then you're against\n"
                          "me! and the Slayer can't have you falling\n"
                          "into the Councils hands!\n"
                          "\n"
                          "The Slayer runs at you to attack!!!\n"
                          "\n")
                    combat_encounter()
                    print("You defeat the Slayer. The Slayer lies\n"
                          "on the ground in a pool of blood.\n"
                          "You walk up to the lifeless body and\n"
                          "take off the Slayers mask to reveal\n"
                          "the face of Teslora. You struggle to\n"
                          "understand how she can be alive but\n"
                          "you will now never have the answers\n"
                          "\n"
                          "You leave your friend and leave to disover\n"
                          "what a Nadaren is.")
                    end()
                else:
                    print(f"Please type {yes} or {no}.\n")
                    choice = input(">>> ")
        else:
            print("Please type the correct word.")
            choice = input(">>> ")


def end():
    """
    function for end game credits and to restart the game.
    """
    print("congratulations on reaching the end!\n"
          "\n"
          "I hope you enjoyed my game!\n"
          "\n"
          "This game was written and coded by\n"
          "Gary Lowles.\n"
          "\n"
          "The game was tested by:\n"
          "Rachel Lowles\n"
          "Charlotte Aling-Case\n"
          "lysette Reed\n"
          "Aaron Harvey\n"
          "Dale Millward\n"
          "Natalie March\n"
          "Emma Skinner\n"
          "\n"
          "Thanks for playing.\n"
          "\n")
    start_menu()


start_menu()
