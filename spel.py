import random



## BECOMES AN GUI LATER

alphabet = "abcdefghijklmnopqrstuvwxyzäåö"


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

    def __init__(self, player):
        self.__player = player
        self.__word = random.choice(["test", "appel", "banaan", "volvo"]) #maybe gonna add json file with alot of words
        print("DEBUG word: ", self.__word) #REMOVE LATER
        self.__guessed = []
        self.__guessed_wrong = []
        self.__wrong_guess_count = 0


    def current_state(self):
        current_word = []

        for letter in self.__word:
            if letter in self.__guessed:
                current_word.append(letter)
            else:
                current_word.append("_")

        print("\nNOGUI_DEBUG word: ", current_word)
        print("NOGUI_DEBUG wrong guessed letters: ", self.__guessed_wrong)
        print("NOGUI_DEBUG tries left: ", self.try_count() - self.__wrong_guess_count)

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
        print("DEBUG max tries: ", self.try_count())

        while not self.game_ended():

            self.current_state()

            guessed_letter = self.__player.guess()
            self.handle_guess(guessed_letter)

        if self.game_won():
            print("NOGUI_DEBUG won! Play again?") # TODO: add play again thingamabob here.
        else:
            print("NOGUI_DEBUG lost! Play again?")



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

name = "test"

player = Player(name)

game = DebugGameMode(player)

game.play()
