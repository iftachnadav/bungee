import random
import copy
<<<<<<< HEAD:Game/Player.py
from Game.IO_Class import Input
=======
>>>>>>> GameAPIGUI:Player.py


class Player:

<<<<<<< HEAD:Game/Player.py
    # lucky card

    def __init__(self, game, print_func, user_func, conn=None):
=======
    def __init__(self, game):
>>>>>>> GameAPIGUI:Player.py
        self.game = game
        self.my_cards = []
        for i in range(5):
            card = self.game.card_from_stack()
            self.my_cards.append(card)
        self.lucky_card = self.game.get_lucky_card()
        self.sort_array()
        self.lost_card = self.game.get_lost_card()
        self.bungee_mode = False
        self.my_score = self.my__score()
        self.stick_factor = 0.5
<<<<<<< HEAD:Game/Player.py
        self.inp = Input(conn, user_func)
        self.user_func = user_func

    # def say_bungee(self):
    #     if sum(self.my_cards) <= 5:
    #         self.bungee_mode = True
    #     else:
    #         self.print_func("ERROR!")
=======
>>>>>>> GameAPIGUI:Player.py

    def turn(self, throw_index, from_stack):

        do_stick = None

        old_my_cards = copy.copy(self.my_cards)
        self.lost_card = self.game.get_lost_card()

        # get card
        if from_stack:
            card = self.game.card_from_stack()
        else:
            card = self.game.card_from_lost()
        print(f"  Get - {card}")
        # throw the cards
        for i in range(len(throw_index)):
            self.game.throw_card(self.my_cards[throw_index[- (i + 1)]])
            del(self.my_cards[throw_index[-(i + 1)]])

        # try to stick
        if from_stack and card == old_my_cards[throw_index[0]]:
            rand = random.random()
            if rand > self.stick_factor:
<<<<<<< HEAD:Game/Player.py
                self.print_func(" well done! you stick, rand: {}".format(rand))
=======
                do_stick = True
>>>>>>> GameAPIGUI:Player.py
                self.game.throw_card(card)
                if card == 6:
                    return True, 1
            else:
<<<<<<< HEAD:Game/Player.py
                self.print_func(" oh no! you can't stick, rand: {}".format(rand))
=======
                do_stick = False
>>>>>>> GameAPIGUI:Player.py
                self.my_cards.append(card)
        else:
            self.my_cards.append(card)
        self.sort_array()
        return 0, do_stick

    def get_state(self):
        lost_card = self.game.get_lost_card()
        score = self.my__score()
        return self.my_cards, self.lucky_card, lost_card, self.bungee_mode, score

    def my__score(self):
        sam = 0
        for i in self.my_cards:
            if i == self.lucky_card:
                i = 0
            sam = sam + i
        return sam

    def __repr__(self):
        return {
            "score": self.my__score(),
            "cards": self.my_cards,
            "luckyCard": self.lucky_card,
            "lostCard": self.game.get_lost_card(),
            "bungeeMode": self.bungee_mode
           }

    def get_lucky_card_to_zero(self):
        for i in range(len(self.my_cards)):
            if self.my_cards[i] == self.lucky_card:
                self.my_cards[i] = 0

    def get_my_cards_to_maneger(self):
        return self.my_cards

    def sort_array(self):
        array = []
        for i in range(len(self.my_cards) - 2):
            if self.my_cards[i] == self.lucky_card:
                array.append(self.my_cards[i])
                del(self.my_cards[i])
        self.my_cards.sort()
        for i in self.my_cards:
            array.append(i)
        self.my_cards = array
