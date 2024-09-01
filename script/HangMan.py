import random 
from colorama import Fore
import os 

class HangMan:
    def __init__(self):
        self.choices = ["paul"]
        
    def getWord(self):
        return random.choice(self.choices)
    
    def displayWord(self):
        return "     " + " ".join([self.letter if self.letter in self.guessed_letters else "_" for self.letter in self.word])
        
    
    def onPlay(self):
        self.word = self.getWord()
        self.guessed_letters = set()
        self.attempts = 6
        os.system("cls") 
        print()
        while True:
            print(f" Welcome to {Fore.LIGHTYELLOW_EX}Hang{Fore.RESET}{Fore.MAGENTA}Man{Fore.RESET}\n")
            print(f"It's a {len(self.word)} letter word\n")
            print(f"    Attempts: {self.attempts}")
            print("\n", self.displayWord())

            self.guess = input("\n\n  Enter a letter: ")
            
            if self.guess in self.guessed_letters:
                os.system("cls")
                print("You have already guessed that letter!")
    
            elif self.guess in self.word:
                os.system("cls")
                self.guessed_letters.add(self.guess)
                
            else:
                os.system("cls")
                self.attempts -= 1
                print(f"\nWrong guess. The letter {self.guess} is not in the word!")
            
            if all(self.letter in self.guessed_letters for self.letter in self.word):
                os.system("cls")
                print(self.word)
                print("You guessed all the letters in the word!")
                break 
            
            if self.attempts == 0:
                os.system("cls")
                print(f"Sorry, you are out of attempts. The word was: {self.word}")
                break

def main():
    play = HangMan()
    play.onPlay()

if __name__ == "__main__":
    main()
            
        
    

                
            