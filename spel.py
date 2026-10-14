import random
import os


## BECOMES AN GUI LATER

alphabet = "abcdefghijklmnopqrstuvwxyzäåö"

Play = True

class Player:
    def __init__(self, name):
        self.__name = name
        self.__score = 0

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score += score

    def guess(self):
        return input("NOGUI_DEBUG guess: ")


class MainGame:

    global Play

    def __init__(self, player):
        self.__player = player
        self.__word = random.choice(["test", "appel", "banaan", "volvo"]) #maybe gonna add json file with alot of words
        self.__guessed = []
        self.__guessed_wrong = []
        self.__wrong_guess_count = 0


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def current_state(self):
        current_word = []

        for letter in self.__word:
            if letter in self.__guessed:
                current_word.append(letter)
            else:
                current_word.append("_")

        #print("DEBUG word: ", self.__word)  # REMOVE LATER
        print("\nNOGUI_DEBUG word: ", current_word)
        print("NOGUI_DEBUG wrong guessed letters: ", self.__guessed_wrong)
        print("NOGUI_DEBUG tries left: ", self.try_count() - self.__wrong_guess_count)
        print("NOGUI_DEBUG points: ", self.__player.get_score())

    def handle_guess(self, letter):
        letter = letter.strip().lower()

        if len(letter) != 1 or letter not in alphabet:
            print("NOGUI_DEBUG only one letter thats in the alphabet")
            return

        if letter in self.__guessed:
            print("NOGUI_DEBUG already guessed")
            return

        self.__guessed.append(letter)

        if letter in self.__word:
            print("NOGUI_DEBUG right guess!")
        else:
            print("NOGUI_DEBUG wrong guess!")
            self.__wrong_guess_count += 1
            self.__guessed_wrong.append(letter)

    def game_won(self):
        for letter in self.__word:
            if letter not in self.__guessed:
                return False
        return True

    def game_ended(self):
        return self.game_won() or self.__wrong_guess_count >= self.try_count()

    def play(self):

        global Play

        #print("DEBUG max tries: ", self.try_count())

        while not self.game_ended():

            self.clear_screen()

            self.current_state()

            guessed_letter = self.__player.guess()
            self.handle_guess(guessed_letter)

        self.clear_screen()
        if self.game_won():

            points = 10 - self.try_count()
            bonus_points = 8 - self.__wrong_guess_count
            print("NOGUI_DEBUG points earned this round. round points: ", points, " bonus points: ", bonus_points)
            self.__player.set_score(points+bonus_points)
            print("NOGUI_DEBUG won! Play again? [Y/N]")
        else:
            print("NOGUI_DEBUG lost! Play again? [Y/N]")

        choice = input("")

        self.clear_screen()

        if choice.lower() != "y":
            Play = False



class DebugGameMode(MainGame):
    def try_count(self):
        return 1

class EasyGamemode(MainGame):

    def try_count(self):
        return 8

class MediumGamemode(MainGame):

    def try_count(self):
        return 6

class HardGamemode(MainGame):

    def try_count(self):
        return 4




## ONLY FOR TESTING PURPOSES. WILL BE DOING INPUTS LATER


name = input("NOGUI_DEBUG Enter player name: ")
player = Player(name)

while Play:

    mode = input("NOGUI_DEBUG Enter player mode 1 = easy, 2 = medium, 3 = hard: ")


    if mode == "1":
        game = EasyGamemode(player)

    elif mode == "2":
        game = MediumGamemode(player)

    elif mode == "3":
        game = HardGamemode(player)

    else:
        game = DebugGameMode(player)

    game.play()

points = player.get_score()
print("NOGUI_DEBUG total earned points: ", points)
