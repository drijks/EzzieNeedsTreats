import math
import random


def which_room(location):
    bedroom = [[00, 0], [0, 225]]
    closet = [[350, 0], [700, 125]]
    bathroom = [[350, 125], [700, 325]]
    living_room = [[0, 225], [350, 475]]
    # kitchen = [[350, 325], [700, 700]]
    dining_area = [[0, 475], [350, 700]]
    if bedroom[0][0] <= location[0] <= bedroom[1][0] and bedroom[0][1] <= location[1] <= bedroom[1][1]:
        return "bedroom"
    elif closet[0][0] <= location[0] <= closet[1][0] and closet[0][1] <= location[1] <= closet[1][1]:
        return "closet"
    elif bathroom[0][0] <= location[0] <= bathroom[1][0] and bathroom[0][1] <= location[1] <= bathroom[1][1]:
        return "bathroom"
    elif living_room[0][0] <= location[0] <= living_room[1][0] and living_room[0][1] <= location[1] <= living_room[1][1]:
        return "living_room"
    elif dining_area[0][0] <= location[0] <= dining_area[1][0] and dining_area[0][1] <= location[1] <= dining_area[1][1]:
        return "dining_area"
    else:
        return "kitchen"


def place_players():
    axy = [random.randint(0, 650) + 25, random.randint(0, 650) + 25]
    dxy = [random.randint(0, 650) + 25, random.randint(0, 650) + 25]
    exy = [random.randint(0, 650) + 25, random.randint(0, 650) + 25]
    return [which_room(axy), which_room(dxy), which_room(exy), axy, dxy, exy]


def choose_action(t, pl):
    annie, david, ezzie, aloc, dloc, eloc = place_players()
    print("Annie is in the " + annie + ". David is in the " + david
          + ". You are in the " + ezzie + ". What will you do?")
    decision = input("1 to poop, 2 to pretend to poop")
    if decision == "1" and pl > 0:
        treat_get = poop(pl)
        pl -= 1
    else:
        treat_get = pretend_to_poop(annie, david, ezzie)
    if treat_get:
        print("You got a treat!")
        print("")
    else:
        print("Nice try, faker.")
        print("")
    return pl


def take_turn(tern, poop_left):
    print("Turn " + str(tern) + ". You have " + str(poop_left) + " poop(s) left.")
    poops_left = choose_action(tern, poop_left)
    tern += 1
    pooped = poop_left != poops_left and poop_left > 0
    return pooped


def poop(p):
    if p > 0:
        print("You pooped!")
        return True
    return False


def pretend_to_poop(aloc, dloc, eloc):
    print("Maybe if I pretend to poop...")
    if dloc == "kitchen":
        print("what are you even trying?")
        return False
    elif aloc == "kitchen":
        print("Quite a risky move, there!")
        return random.choice([True, False, False, False, False])
    elif eloc == "kitchen" and aloc != "kitchen" and dloc != "kitchen":
        print("could be!")
        return random.choice([True, True, True, False])
    else:
        print("hmm...")
        return random.choice([True, False])


turn = 0
poops = 2
while turn < 5:
    did_a_poop = take_turn(turn, poops)
    if did_a_poop:
        poops -= 1
    turn += 1


