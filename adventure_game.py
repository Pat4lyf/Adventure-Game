import time
import random


def print_sleep(message):
    print(message)
    time.sleep(2)


def intro(first, second):
    print_sleep("You find yourself standing in a room, "
                "with two closed doors, one coloured, "
                f"{first} and the other coloured, {second}.")
    print_sleep(f"Behind one of the closed doors is a deadly creature "
                f"and behind the second is a weapon.")
    print_sleep("Which of the doors will you open first?\n")


def restart_game():
    print_sleep("Awesome!!! Restarting the game ...")
    start_game()


def validate_input(question, list_of_response):
    while True:
        response = input(question).lower()
        if response in list_of_response:
            return response
        print_sleep(f"Sorry, {response} is invalid!!! "
                    "Please, enter a valid answer.")


def choice_to_either_play_again_or_not():
    player_input = validate_input(
        "Would you like to play again? (yes/no)\n", ["yes", "no"])
    if player_input == "no":
        print_sleep("Sorry to see you go!!! See you next time.")
        exit(0)
    else:
        restart_game()


def victorious_outcome(option, creature):
    print_sleep(f"You have the {option} in your hand.")
    print_sleep(f"As the {creature} moves to attack, you weild your {option}.")
    print_sleep("The battle was fierce, but at the last, "
                f"you were able to conquer the {creature}.")
    print_sleep("Yay!!! You are victorious.")


def count_of_weapons_in_the_list(list, weapons):
    count = 0
    for item in list:
        if item in weapons:
            count += 1
            break
    return count


def player_defeat(option):
    print_sleep(f"You find a {option}")
    print_sleep(f"Alas!!! The {option} is behind the door")
    print_sleep(f"And you do not have any weapon to fight it")
    print_sleep(f"The {option} attacks you")
    print_sleep("You are over-powered.\n")
    choice_to_either_play_again_or_not()


def weapon_found(option):
    print_sleep(f"Hurray!!! You have found the {option}"
                " with which to defeat the lethal creature.")
    print_sleep("You step out of the room.")


def empty_room(option):
    print_sleep("The room is empty.")
    print_sleep("You have previously been here")
    print_sleep(f"And have taken the {option}")
    print_sleep("You step back out of the room.")


def first_door(first, second, option, creatures, list, creature, weapons):
    print_sleep(f"You push open the {first} door.")

    if '2' in list and option in list:
        list.append("1")
        victorious_outcome(option, creature)
        choice_to_either_play_again_or_not()
    else:
        count_of_weapons = count_of_weapons_in_the_list(list, weapons)
        if option in creatures and count_of_weapons < 1:
            player_defeat(option)
        elif option not in creatures:
            if option not in list and '1' not in list:
                list.append(option)
                list.append("1")
                weapon_found(option)
            else:
                empty_room(option)
            print_sleep("Which door will you open next?\n")
            get_player_input(list, first, second, option,
                             creatures, creature, weapons)


def second_door(first, second, option, creature, creatures, weapons, list):
    print_sleep(f"You push open the {second} door.")
    if '1' in list and option in list:
        list.append("2")
        victorious_outcome(option, creature)
        choice_to_either_play_again_or_not()
    else:
        count_of_weapons = count_of_weapons_in_the_list(list, weapons)
        if option in creatures and count_of_weapons < 1:
            player_defeat(option)
        elif option not in creatures:
            if option not in list and '2' not in list:
                list.append(option)
                list.append("2")
                weapon_found(option)
            else:
                empty_room(option)
            print_sleep("Which door will you open next?\n")
            get_player_input(list, first, second, option,
                             creatures, creature, weapons)


def get_player_input(list, first, second, option,
                     creatures, creature, weapons):
    print_sleep(f"Enter 1 to open the {first} door.")
    print_sleep(f"Enter 2 to open the {second} door.")
    print_sleep("What would you like to do?")
    choice = validate_input("(Please enter 1 or 2)\n", ["1", "2"])
    if choice == "1":
        first_door(first, second, option,
                   creatures, list, creature, weapons)
    else:
        second_door(first, second, option,
                    creature, creatures, weapons, list)


def start_game():
    list_of_first_door_colors = ["red", "green", "blue", "indigo"]
    list_of_second_door_colors = ["yellow", "orange", "purple", "brown"]
    creatures = ["werewolf", "vampire", "scorpion"]
    weapons = ["Silver Sword", "Gun", "Golden Knife"]
    options = ["werewolf", "vampire", "scorpion", ""
               "Silver Sword", "Gun", "Golden Knife"]
    list = []

    first_door_color = random.choice(list_of_first_door_colors)
    second_door_color = random.choice(list_of_second_door_colors)
    creature = random.choice(creatures)
    option = random.choice(options)

    intro(first_door_color, second_door_color)
    get_player_input(list, first_door_color, second_door_color,
                     option, creatures, creature, weapons)


start_game()
