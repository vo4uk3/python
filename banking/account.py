import sqlite3
import sys

from utils import *

class Account():
    def __init__(self, card, pin):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.logged_in = True
        self.card = card
        self.pin = pin
        self.balance = 0


    def get_balance(self):
        return self.balance

    def add_income(self, income):
        new_balance = self.balance + income
        self.balance = new_balance
        update_balance = """UPDATE card SET balance = ? WHERE number = ?; """
        data = (new_balance, self.card)
        self.cur.execute(update_balance, data)
        self.conn.commit()

    def menu(self):
        while self.logged_in:
            print('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')
            choice = input()
            if choice == '1':
                balance = self.get_balance()
                print(f'Balance: {balance}')
            elif choice == '2':
                print('Enter income:')
                income = int(input())
                self.add_income(income)
                print('Income was added!')
            elif choice == '3':
                print('Transfer')
                print('Enter card number:')
                card = input()
                if not cardLuhnChecksumIsValid(card):
                    print('Probably you made a mistake in the card number. Please try again!')
                    continue
                query = """SELECT number FROM card WHERE number = ?"""
                data_tuple = (card,)
                self.cur.execute(query, data_tuple)
                row = self.cur.fetchone()
                if not row:
                    print('Such a card does not exist.')
                    continue
                if card == self.card:
                    print("You can't transfer money to the same account!")
                    continue
                print('Enter how much money you want to transfer:')
                amount = int(input())
                if amount > self.balance:
                    print('Not enough money!')
                    continue
                new_balance = self.balance - amount
                self.balance = new_balance
                query = """UPDATE card SET balance = ? WHERE number = ?"""
                data_tuple = (amount,card)
                self.cur.execute(query, data_tuple)
                self.conn.commit()

                query = """UPDATE card SET balance = ? WHERE number = ?"""
                data_tuple = (new_balance,self.card)
                self.cur.execute(query, data_tuple)
                self.conn.commit()
            elif choice == '4':
                query = """DELETE FROM card WHERE number = ?"""
                data_tuple = (self.card,)
                self.cur.execute(query, data_tuple)
                self.conn.commit()
            elif choice == '5':
                break
            elif choice == '0':
                print('Bye')
                self.conn.close()
                sys.exit()
