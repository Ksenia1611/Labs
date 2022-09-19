from enum import Enum

class  StateType(Enum):
    s0 = 's0'
    NXTLIT  = 'NXTLIT'
    stop    = 'stop'
    error   = 'error'

class Lexer:
    
    def __init__(self, letter):
        self.current_state =  StateType.s0
        self.w = []
        self.letter = letter

    def main(self):
        for letter in word:
            if self.current_state ==  StateType.s0:
                if (letter == ' ') or (letter == '\n'):
                    continue
                if (letter >= 'a' and letter <= 'z') or (letter >='A' and letter <='Z'):
                    self.w.append(letter)
                    self.current_state =  StateType.NXTLIT
                    continue
                if (letter >= '0' and letter <= '9'):
                    self.current_state =  StateType.error
                    continue
                else:
                    self.current_state =  StateType.error
                    continue
            if self.current_state ==  StateType.NXTLIT:
                if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):                
                    self.w.append(letter)
                    continue
                if letter == ' ' or letter =='\n':
                    self.current_state =  StateType.s0
                    print("".join(self.w))
                    self.w = []
                    continue 
                if (letter >= '0' and letter <= '9'):
                    self.current_state =  StateType.error
                    continue  
                else:
                    self.current_state =  StateType.error
                    continue

word = []
with open("D:\\laba_1\\text.txt") as file:
    for letter in file.read():
        word.append(letter)
lexer = Lexer(letter) 
lexer.main()

if  len(lexer.w) != 0:
     print("".join(lexer.w))
     lexer.current_state = StateType.stop

if lexer.current_state ==  StateType.error:
    print('ERROR')
    exit()
    
if lexer.current_state ==  StateType.stop:
    print('Stop')
    exit()