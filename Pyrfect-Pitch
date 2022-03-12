import winsound
import random
import time
r = random
w = winsound
t = time
def main():
    flist = ['A_440',
             'Bb446',
             'B_493',
             'C_523',
             'Db554',
             'D_587',
             'Eb622',
             'E_659',
             'F_698',
             'Gb739',
             'G_783',
             'Ab830'
             ]
    fchoice = random.choice(flist)
    if fchoice[1] == "_":
        note = fchoice[0]
    else:
        note = fchoice[0] + fchoice[1]
    #print(note)
    w.Beep(int(fchoice[-3] + fchoice[-2] + fchoice[-1]), 2000)
    #print(fchoice[-3] + fchoice[-2] + fchoice[-1])
    guess = input("Guess: ")
    if guess == note:
        print("Correct!")
        t.sleep(1)
        main()
    else:
        print("That note was a " + note)
        t.sleep(1)
        main()
main()
