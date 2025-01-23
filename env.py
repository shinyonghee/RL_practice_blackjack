import random
from enum import IntEnum


class Action(IntEnum):
    STICK = 0
    HIT = 1


class Card:
    def __init__(self, color=None):
        self.num = random.randint(1, 10)

        if color == None:
            rand = random.random()
            if rand < 1 / 3:
                self.color = "R"
            else:
                self.color = "B"
        else:
            self.color = color

    def __repr__(self):
        return str(self.color) + str(self.num)


def update_p(person, card):
    print(f"player picked {card}")
    sum = person

    if card.color == "B":
        sum += card.num
    else:
        sum -= card.num
    return sum


def update_d(person, card):
    print(f"dealer picked {card}")
    sum = person

    if card.color == "B":
        sum += card.num
    else:
        sum -= card.num
    return sum


def step(s, a):
    # choose action!
    reward = None
    next_s = None

    action = a
    if a == 1:
        action = Action.HIT
    if a == 0:
        action = Action.STICK
    dealer = s[0]
    player = s[1]
    # ======================= #
    if action == Action.HIT:
        new = Card()
        player = update_p(player, new)
        next_s = (dealer, player)

    elif action == Action.STICK:
        while dealer < 17:
            new = Card()
            dealer = update_d(dealer, new)
            if dealer > 21 or dealer < 1:
                print(f"delar busts!: {dealer}")
                reward = 1
                next_s = "terminal"
                break
        next_s = "terminal"

    if player > 21 or player < 1:
        print(f"player busts!: {player}")
        reward = -1
        next_s = "terminal"

    if next_s == "terminal" and reward == None:
        game_result = abs(21 - dealer) - abs(21 - player)
        print(dealer, player)
        if game_result > 0:
            reward = 1
        elif game_result == 0:
            reward = 0
        else:
            reward = -1

    return next_s, reward


def reset():
    # game start
    player = 0
    dealer = 0

    new = Card("B")
    player = update_p(player, new)

    new = Card("B")
    dealer = update_d(dealer, new)

    s = (dealer, player)
    return s


if __name__ == "__main__":
    # game start
    player = 0
    dealer = 0

    new = Card("B")
    player = update_p(player, new)

    new = Card("B")
    dealer = update_d(dealer, new)

    s = (dealer, player)
    print(s)
    while s != "terminal":
        print("hit or stick (h/s)")
        a = input(">> ")
        if a == "h":
            action = Action.HIT
        elif a == "s":
            action = Action.STICK
        s, r = step(s, action)
        print(s, r)
