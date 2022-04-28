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
    if RACE_ONE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You attack with your daggers and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("You missed\n")

    elif RACE_TWO:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print(" You swing with your scythe and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("You missed\n")

    elif RACE_THREE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print(" You crash down your Vasara and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("You missed\n")

    elif RACE_FOUR:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You levitate and slash with floating swords and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("You missed\n")

    elif RACE_FIVE:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You slash with your sword and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("You missed\n")

    elif RACE_SIX:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You unleash a powerful martial arts strike and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("You missed\n")

    elif RACE_SEVEN:
        if player_attack_roll() >= 4:
            reduce_enemy_health_melee()
            print("You slash with your sharp, metal claws and hit!"
                  f" Enemy has {ENEMY_HEALTH} hit points left""\n")
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
            print("You send a jet of water flying at the enemy and hit!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("Your Aqua magic misses\n")

    elif RACE_TWO:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send shards of ice flying at the enemy and hit!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("Your Cryo magic misses\n")

    elif RACE_THREE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a fireball flying at the enemy and hit!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("Your Pyro magic misses\n")

    elif RACE_FOUR:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a blast of wind towards the enemy and hit!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("Your zephyr magic misses\n")

    elif RACE_FIVE:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You drain some of the enemies soul!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("Your Soul magic misses\n")

    elif RACE_SIX:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a chunk of rock flying towards the enemy and hit!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
        else:
            print("Your Terra magic misses\n")

    elif RACE_SEVEN:
        if player_magic_roll() >= 5:
            reduce_enemy_health_magic()
            print("You send a blot of lighning flying at the enemy and hit!"
                  f" The enemy has {ENEMY_HEALTH} hit points left""\n")
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

    global character_name
    character_name = input("Please name your character>>> ")

    while True:

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
                  "they use scythe weapons, Sensory and Cryo magic\n"
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
            print("\n"
                  "Please enter a valid Race choice.\n"
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
                         ">>> ")


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
          "\n"
          "A: Punch him in his gap toothed face?\n"
          "B: Share your flask with him.?\n"
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
            print("Please select a vaild choice.")
            choice = input(">>> ")


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
          " house.\n"
          "\n")


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
                  "The rest of your trip is very peaceful and you arrive at the\n"
                  "docks. You begin walking to your friends house.\n"
                  "\n")
            time.sleep(2)
            story_part_2()
        else:
            print("Please select a valid choice.")
            choice = input(">>> ")


def race_option_1():
    """
    lets the player choose an option depending on what race they are
    """
    if RACE_ONE:
        print("You speak softly and tell the sailor you are young"
              "and innocent.\n"
              "You bat your eyelids and ask that he please leave such an"
              " innocent creature be\n"
              "The sailor sees sense and walks away\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)      
        story_part_2()

    elif RACE_TWO:
        print("You pull down the cloth covering and reveal your face"
              " The sailor sees the black sockets where your eyes should be."
              "\nHe turns white and passes out.\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)
        story_part_2()

    elif RACE_THREE:
        print("You look down on the tiny Human and tell him to walk away!"
              " The sailor quickly turns tail and runs\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)
        story_part_2()

    elif RACE_FOUR:
        print("You begin tell the sailor why alcohol is bad for him and"
              " and explain in explicit detail how alcohol is made"
              " The sailor falls asleep whilst you're talking\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)
        story_part_2()

    elif RACE_FIVE:
        print("You point the sailor towards a man with a flask twice the size"
              " of yours. The sailor quickly heads over to bother the man.\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)
        story_part_2()

    elif RACE_SIX:
        print("Before the sailor can say another word you deliver a swift\n"
              "punch in the solar plexus which knocks him unconscious\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)
        story_part_2()

    elif RACE_SEVEN:
        print("Lightning begins to crackel from your body and arc out.\n"
              "You stare at the sailor and let out a guttural growl.\n"
              "The sailor leaves without saying another word.\n"
              "\n"
              "You arrive at the docks and walk towards your friends house")
        time.sleep(2)
        story_part_2()


def story_part_2():
    """
    function to start the second part of the story
    """

    print("You make your way through Jatorri city. The city is a marvel of\n"
          "Human ingenuity. The city is built into a canyon and supended\n"
          "above it. The city is connected by huge suspension bridges\n"
          "\n"
          "You eventually make it to Teslora's house and knock on the\n"
          "door...\n"
          "\n")
    time.sleep(3)
    print("There is no answer\n"
          "\n")
    time.sleep(3)
    print("You look at the door lock and notice that it is broken\n"
          "You slowly push the door open to reveal Tesloras' corpse\n"
          "\n"
          "The room is covered in blood and Teslora is slumped in\n"
          "her chair with a bloody note stuck into her body\n"
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


def option_search():
    """
    function to allow player to search the room
    """
    global character_name
    print("You begin frantically searching the room, looking for anything!\n")
    print(f"You find a sealed letter with '{character_name}' written on it"
          "\n")
    print(f"The letter reads 'Dear, {character_name}.\n"
          "\n"
          "I had hoped to see you one last time but it looks like my\n"
          "death is inevitable. A killer has been hunting Jattori council\n"
          "members and I fear I am next. if you find me, please grant my\n"
          "body liberation. \n"
          "I know we didn't see each other as often as we should but you\n"
          "were my best friend in my lonely life.\n"
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
                  "shimmering colours... She is at peace."
                  "\n")
            time.sleep(2)
            print("Suddenly the Jatorri city military burst through the\n"
                  "door!\n Before you know what's\n"
                  "happening you are tackeled and bound")
        elif choice in no:
            print("You hear a noise outside the house. It sounds like 10 or \n"
                  "more people about to burst through the door.\n"
                  "\n"
                  "What do you do?"
                  "A: Hide\n"
                  "B: Run\n"
                  "C: Special Race option:\n")
        else:
            print(f"Please type {yes} or {no}.\n")
            choice = input(">>> ")

    while True:
        if choice in answer_A:
            print("You hide in a nearby cupboard. The military breaks through\n"
                  "The door and begins seraching the house. it doesnt take\n"
                  "long before you are found.")


start_menu()
