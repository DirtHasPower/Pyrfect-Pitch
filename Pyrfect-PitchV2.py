#importing
import winsound as w
import random as r
import time as t

#setting the length of the tone/beep
beeplength = int(input("Beep Length(seconds): "))*1000

#declaring main loop
def main():
    #declaring all note names and frequencies
    flist = ['A_440','Bb466','B_493','C_523','Db554','D_587','Eb622','E_659','F_698','Gb739','G_783','Ab830',
                'A_220','Bb233','B_247','C_262','Db277','D_294','Eb311','E_330','F_349','Gb370','G_392','Ab415',]
    
    #choosing random note and seperating information
    fchoice = r.choice(flist)
    if fchoice[1] == "_":
        note = fchoice[0]
    else:
        note = fchoice[:2]
    
    #repeats tone until answer is submitted
    repeat = True
    while repeat == True:
        w.Beep(int(fchoice[-3:]), 2000)
        guess = input('Guess/"repeat":')
        if guess != "repeat":
            repeat = False
    
    #checks if guess is correct
    if guess == note:
        print("Correct!")
        cont = input("Press Enter To Continue")
        main()
    else:
        print("That note was a " + note)
        cont = input("Press Enter To Continue")
        main()

#starts main loop
main()
