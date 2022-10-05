import winsound as w
import random as r
import time as t

beeplength = int(input("Beep Length(seconds): "))*1000

def main():
    flist = ['A_440','Bb466','B_493','C_523','Db554','D_587','Eb622','E_659','F_698','Gb739','G_783','Ab830',
                'A_220','Bb233','B_247','C_262','Db277','D_294','Eb311','E_330','F_349','Gb370','G_392','Ab415',]
    fchoice = r.choice(flist)
    if fchoice[1] == "_":
        note = fchoice[0]
    else:
        note = fchoice[:2]
    repeat = True
    while repeat == True:
        w.Beep(int(fchoice[-3:]), 2000)
        guess = input('Guess/"repeat":')
        if guess != "repeat":
            repeat = False
    if guess == note:
        print("Correct!")
        cont = input("Press Enter To Continue")
        main()
    else:
        print("That note was a " + note)
        cont = input("Press Enter To Continue")
        main()
main()
