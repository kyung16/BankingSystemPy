import json 
from string import digits
import random 
import os 
from colorama import Fore 

class BankFunction: 
    def __init__(self):
        self.initialMoney = 0
    
    def process(self, cardNumber, cardPIN):
        self.list1 = []
        try:
            with open("day1/BankingSystem/info.json", "r+") as file:
                self.read = json.load(file)
        except json.JSONDecodeError:
            print("Invalid!")
            
        for i in self.read:    
            if i.get("Card Number") == cardNumber and i.get("Card PIN") == cardPIN:
                os.system("cls")
                self.initialMoney = i.get("Initial Money")
                self.cardHolder = i.get("Card Holder")
                print(f"Card Information: {Fore.GREEN}{self.cardHolder}{Fore.RESET} ({cardNumber})")
                print(f"Initial Money: {self.initialMoney}")
                while True:
                    print()
                    self.initialMoney = i.get("Initial Money")
                    self.choice: int = int(input("[1] Withdraw\n[2] Deposit\n[3] Transfer Money\n[4] See Balance\n[5] Exit\n\nChoice: "))
                    if self.choice == 1:
                        self.choice1: int = int(input("Input the amount of money: "))
                        if self.choice1 < i.get("Initial Money"):
                            self.initialMoney -= int(self.choice1)
                            i["Initial Money"] = self.initialMoney
                            with open("day1/BankingSystem/info.json", "w+") as file:
                                json.dump(self.read, file, indent=4)
                            print("Succesfully withdrawn an amount of money!")
                        else:
                            print("Insufficient amount.")
                            
                    elif self.choice == 2:
                        self.choice2: int = int(input("Input the amount of money: "))
                        self.initialMoney += int(self.choice2)
                        i["Initial Money"] = self.initialMoney
                        with open("day1/BankingSystem/info.json", "w+") as file:
                            json.dump(self.read, file, indent=4)
                        print("Succesfully deposited money!")
                        
                    elif self.choice == 3:
                        try:
                            with open("day1/BankingSystem/info.json", "r") as file:
                                self.read = json.load(file)
                        
                        except json.JSONDecodeError:
                            print("No information!")
                            self.read: list = []
                            
                        self.transferMoneyTo: int = int(input("Enter the card number of the account who will receive: ")) 
                        self.amount: int = int(input("Enter the amount of money that will be transferred: "))
                        
                        if self.transferMoneyTo != i.get("Card Number"):     
                            for j in self.read:
                                if self.transferMoneyTo == j.get("Card Number"):
                                    self.InitialMoney2 = j.get("Initial Money")
                                    self.InitialMoney2 += self.amount
                                    j["Initial Money"] = self.InitialMoney2
                                    
                    
                            for k in self.read:
                                if cardNumber == k.get("Card Number"):
                                    if self.amount > k.get("Initial Money"):
                                        print("Not enough amount.")
                                    else:
                                        self.InitialMoney1 = k.get("Initial Money")
                                        self.InitialMoney1 -= self.amount 
                                        k["Initial Money"] = self.InitialMoney1
                                        
                            with open("day1/BankingSystem/info.json", "w") as file:
                                json.dump(self.read, file, indent=4)
                            print("Succesfully transferred money.")
                        elif self.transferMoneyTo == i["Card Number"]:
                            print("Invalid card number.")
                        else:
                            print("Same card number!")
                                    
                        
                    elif self.choice == 4:
                        self.seeBalance(cardNumber)            
                        
                    elif self.choice == 5:
                        main()
                    
                    else:
                        print("Invalid!")
                        
    def seeBalance(self, cardNumber):
        os.system("cls")
        try:
            with open("day1/BankingSystem/info.json", "r") as file:
                self.read = json.load(file)
        except json.JSONDecodeError:
            self.read: list = []
            print("No informations!")
        
        self.valid = False
        for i in self.read:
            if cardNumber == i["Card Number"]:
                print(f"Your balance is {i.get("Initial Money")}")
                self.valid = True 
        
        if not self.valid:
            print("Invalid Card Number")
            
                    
                    

    def login(self):
        try:
            with open("day1/BankingSystem/info.json", "r") as file:
                self.read = json.load(file)
        except json.JSONDecodeError:
            print("No information!")
            self.read: list = []
            
        self.cardNumber: int = int(input("Card Number: "))
        self.cardPIN: int = input("Card PIN (6 digits): ")
        self.valid = False 
        
        for i in self.read:
            self.getCardNumber = i.get("Card Number")
            self.getCardPIN = i.get("Card PIN")
            if self.getCardNumber == self.cardNumber :
                if self.getCardPIN == self.cardPIN:
                    print(f"Card Number: {self.cardNumber}\nInitial Money: {i.get("Initial Money")}")
                    self.process(self.cardNumber, self.cardPIN)
                    self.valid = True 
                    break
                else:
                    print("Wrong PIN number.")
                    os.system("pause")
                    break
                
        if not self.valid:
            print("Invalid Card Number.")
            os.system("pause")
        
        
                
            
    def registerCard(self):
        self.list: list = []
        self.string = digits
        self.random = random.choices(digits, k = 9)
        self.string = "".join(self.random)
        self.cardHolderfname: str = str(input("Enter your first name: ").capitalize())
        self.cardHolderlname: str = str(input("Enter your last name: ").capitalize())
        self.cardPIN: int = input("Enter your card pin (6 digits): ")
        
        if type(self.cardHolderfname) == int and type(self.cardHolderlname) == int:
            print(f"{Fore.YELLOW}Digits or numbers are not allowed!{Fore.RESET}")
            os.system("pause")
        elif type(self.cardHolderfname) == int:
            print(f"{Fore.YELLOW}Digits or numbers are not allowed!{Fore.RESET}")
            os.system("pause")
        elif type(self.cardHolderlname) == int:
            print(f"{Fore.YELLOW}Digits or numbers are not allowed!{Fore.RESET}")
            os.system("pause")
            
        elif type(self.cardHolderfname) == str and type(self.cardHolderlname) == str:
            if len(self.cardPIN) == 6:   
                print(f"Card Number: {self.string}\nCard PIN: {self.cardPIN}")
                self.data: dict = {
                    "Card Holder" : str(self.cardHolderfname) + " " + str(self.cardHolderlname),
                    "Card Number" : int(self.string),
                    "Card PIN" : self.cardPIN,
                    "Initial Money" : 1000
                }
                
                try:
                    with open("day1/BankingSystem/info.json", "r+") as file:
                        self.list = json.load(file)
                except json.JSONDecodeError:
                    self.list: list = []
                self.list.append(self.data)
                with open("day1/BankingSystem/info.json", "w") as file:
                    json.dump(self.list, file, indent = 4)
                print("Thank you for using our service, you acquired our free 1000 pesos in your registered credit card! Enjoy!")
                os.system("pause")
                
            else:
                print(f"Can't register!{Fore.YELLOW}Minimum and maximum of 6 digits!{Fore.RESET}")
                os.system("pause")
        else:
            print(f"{Fore.YELLOW}Can't register the card, you didn't read the instruction!{Fore.RESET}")
            os.system("pause")
            

def main():
    while True:
        os.system("cls")
        print()
        print(f"Welcome to our {Fore.BLUE}Bank{Fore.RESET}")
        print()
        choice: int = int(input(f"[{Fore.BLUE}1{Fore.RESET}] Register Card\n[{Fore.BLUE}2{Fore.RESET}] Withdraw/Deposit\n[{Fore.BLUE}3{Fore.RESET}] Exit\n\n{Fore.YELLOW}Choice{Fore.RESET}: "))   
        if choice == 1:
            os.system("cls")
            BankFunction().registerCard()
        elif choice == 2:
            os.system("cls")
            BankFunction().login()
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid!")
            break
        
if __name__ == "__main__":
    main()
        
        

