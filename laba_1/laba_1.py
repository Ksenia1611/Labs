from enum import Enum

class  StateType(Enum):
    s0 = 's0'
    NXTLIT  = 'NXTLIT'
    stop    = 'stop'
    error   = 'error'

class Lexer:
    
    def __init__(self):
        self.StateType =  StateType
        self.w = []
        self.current_state = self.StateType.s0

    def main(self, letter):
        match self.current_state:
            case self.StateType.s0:
                self.First_litera(letter)

            case self.StateType.NXTLIT:
                self.Next_litera(letter)

            case self.StateType.error:
                self.error()

    def First_litera(self, letter):
        if (letter >= 'a' and letter <= 'z') or (letter >='A' and letter <='Z') or (letter >= 'а' and letter <= 'я') or (letter >= 'А' and letter <= 'Я'):
            self.current_state = self.StateType.NXTLIT
            self.w.append(letter)
            return
        else:
            self.current_state = self.StateType.error

    def Next_litera(self, letter):
        if letter == ' ' or letter =='\n':
            self.current_state = self.StateType.s0
            print("".join(self.w))
            self.w = []
            return
        if (letter >= 'a' and letter <= 'z') or (letter >='A' and letter <='Z') or (letter >= 'а' and letter <= 'я') or (letter >= 'А' and letter <= 'Я'):
            self.w.append(letter)
            return
        else:
            self.current_state = self.StateType.error    

    def error (self):
        print('ERROR')
        exit() 

letter = []
lexer = Lexer() 
with open("D:\\Lab\\laba_1\\text.txt", encoding = "utf-8") as file:
    for letter in file.read():
        lexer.main(letter)

if  len(lexer.w) != 0:
     print("".join(lexer.w))
     lexer.current_state = StateType.stop

if lexer.current_state ==  StateType.stop:
    print('Stop')
    exit()

