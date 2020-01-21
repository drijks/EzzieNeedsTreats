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


def time_of_day(trn):
    if trn < 12:
        hr = trn/4 + 10
    else:
        hr = trn/4 - 2
    mins = (trn % 4) * 15
    if trn < 8:
        ampm = "AM"
    else:
        ampm = "PM"
    if mins == 0:
        print("It is now " + str(int(hr)) + ":00 " + ampm + ".")
    else:
        print("It is now " + str(int(hr)) + ":" + str(mins) + " " + ampm + ".")


def place_players():
    axy = [random.randint(0, 650) + 25, random.randint(0, 650) + 25]
    dxy = [random.randint(0, 650) + 25, random.randint(0, 650) + 25]
    exy = [random.randint(0, 650) + 25, random.randint(0, 650) + 25]
    return [which_room(axy), which_room(dxy), which_room(exy), axy, dxy, exy]


def the_decision(t, pl, annie, david, ezzie):
    decision = input("1 to poop, 2 to pretend to poop, 3 to bark incessantly, or any other key to skip this turn")
    if decision == "1" and pl > 0:
        treat_get = poop(pl)
        pl -= 1
    elif decision == "2":
        treat_get = pretend_to_poop(annie, david, ezzie)
        if treat_get:
            print("They fell for it! Good job with that fake pooping!")
        else:
            print("Nice try, faker.")
    elif decision == "3":
        treat_get = bark_incessantly()
    else:
        treat_get = False
    return [treat_get, pl]


def choose_action(t, pl, tg):
    annie, david, ezzie, aloc, dloc, eloc = place_players()
    print("Annie is in the " + annie + ". David is in the " + david
          + ". You are in the " + ezzie + ". What will you do?")
    if t == 48:
        print("It's DT time! You don't have to do anything!")
        input("Hit the 'Enter' key to continue.")
        treat_get = True
    else:
        treat_get, pl = the_decision(t, pl, annie, david, ezzie)
    if treat_get:
        print("You got a treat! You've gotten " + str(tg + 1) + " treat(s) so far.")
        print("")
    else:
        print("No luck this time. You've gotten " + str(tg) + " treat(s) so far.")
        print("")
    return [pl, treat_get]


def take_turn(tern, poop_left, trts):
    time_of_day(tern)
    print("Turn " + str(tern) + ". You have " + str(poop_left) + " poop(s) left.")
    poops_left, got_trt = choose_action(tern, poop_left, trts)
    tern += 1
    pooped = poop_left != poops_left and poop_left > 0
    return [got_trt, pooped]


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


def bark_incessantly():
    odds = random.randint(0, 101)
    if odds >= 95:
        print("It worked! That's surprising...")
        return True
    else:
        print("They didn't go for it. Oh, well, it was worth a shot...")
        return False


turn = 46
poops = 5
treats = 0
while turn <= 56:
    got_a_treat, did_a_poop = take_turn(turn, poops, treats)
    if got_a_treat:
        treats += 1
    if did_a_poop:
        poops -= 1
    turn += 1


