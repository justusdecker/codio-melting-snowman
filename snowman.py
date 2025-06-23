import random

from bin.secret_words import WORDS
from bin.ascii_art import STAGES
class App:
    def __init__(self):
        self.mistakes = 0
        self.max_mistakes = 4 # look at step 4 Additional Stages - this makes more than 3 attempts i hope this is okay😅
        self.secret_word = None
        self.is_running = True
    def get_secret(self) -> str:
        """
        Constructs and returns the current masked version of the secret word.

        This method iterates through each letter of the `self.secret_word`.
        If a letter has been correctly guessed (i.e., it is present in the
        `self.already_guessed` set), the letter is revealed. Otherwise, it
        is replaced by an asterisk ('*'). The method then joins these
        characters to form the masked word string.

        Returns:
            str: The masked secret word, with unguessed letters replaced by asterisks.
            
        **You can use this to determine the win state**
        """
        return "".join([i if i in self.already_guessed else '*' for i in self.secret_word])
    
    def display_game_state(self,losed: bool = False) -> None:
        """
        Displays the current state of the game, including the hangman stage and the secret word progress.

        This method uses the number of `self.mistakes` to determine which hangman stage
        to display from the `STAGES` constant.

        If the `losed` parameter is True, it indicates the game has been lost, and
        the full `self.secret_word` is revealed. Otherwise, it shows the current
        progress of the `self.secret_word` with unguessed letters masked, by calling
        the `self.get_secret()` method.

        Args:
            losed (bool, optional): A flag indicating whether the game has been lost.
                                    Defaults to False. If True, the secret word is revealed.
        """
        print(STAGES[self.mistakes])
        if losed:
            print(f'The secret word was: {self.secret_word}')
        else:
            print(self.get_secret())
        
    def play_game(self) -> None:
        """
        Manages the main game loop for "Snowman Meltdown".

        This method initializes and runs the Snowman Meltdown game. It continuously
        selects a random secret word for each round, resets the game state, and
        prompts the user for letter guesses.
        """
        print("Welcome to Snowman Meltdown!")
        while self.is_running:
            self.secret_word = App.get_random_word(WORDS)
            self.already_guessed = set()
            while self.mistakes < self.max_mistakes:
                print(f'\n<---[Attemps left: {self.max_mistakes - self.mistakes}]--->')
                self.display_game_state()
                guess = input("Guess a letter: ").lower()
                if guess == 'exit':
                    return
                # user input is empty or not a letter
                if not guess or len(guess) > 1:
                    print('You need to guess one letter!')
                    continue
                
                # check for guess duplicates
                if guess in self.already_guessed:
                    print(f'You already guessed: {guess}')
                    continue
                else:
                    self.already_guessed.add(guess)
                    print(f"You guessed: {guess}")
                
                if guess in self.secret_word:
                    print('This letter is in the word')
                    if '*' not in self.get_secret():
                    # No open letters so the user has completed the quiz
                        print('You saved uncle snowman😁')
                        break
                    # Otherwise the user guessed one letter correctly and the game goes on
                    continue

                self.mistakes += 1
                # User has not guessed correctly 3 times, so GAME OVER
                if self.mistakes == self.max_mistakes:
                    self.display_game_state(True)
                    print('Uncle snowman is dead! Try again')
                    break
                
            user_input = ''
            while user_input != 'y' and user_input != 'n':
                user_input = input('Do you want to play again? [y/n]')
            if user_input == 'y':
                self.mistakes = 0 # reset mistakes
            else:
                return
             
    def get_random_word(list_object: list) -> str:
        """
        Selects and returns a random word from the provided list.

        This function takes a list of strings (words) and uses the `random` module
        to pick one word at a random index.
        """
        return list_object[random.randint(0, len(list_object) - 1)]
    
    
if __name__ == "__main__":
    APP = App()
    APP.play_game()