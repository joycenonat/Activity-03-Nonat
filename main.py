import NonatEV_Script_2_EV as EV
import NonatStat_Script_1_Stat as ST
import math 

def ContinueOrExit():
    opt = int(input("\nDo you want to try once more? \n[1] YES  [2] NO \nOption: "))
    if opt == 1: main()
    elif opt == 2: exit()
    else: 
        print("INVALID!")
        ContinueOrExit()
        

def main():

    print("******************WELCOME TO POKEMON STAT & EV CALCULATOR!******************\n\n")
    while True:
        b = int ( input ("BASE HP: "))
        lvl = int ( input ("LEVEL: "))
        ev = int ( input ("EV must be [0 - 255] \nEV: "))
        iv = int ( input ("IV must be [0 - 31] \nIV: "))
            
        if iv > 31:
            print("IV Exceeds\n")  
            main() 

        if ev > 255:
            print("EV Exceeds\n") 
            main()

        else:    
            print("PROCEEDING...")
            break

    while True:
        print("\nCHOOSE A POKEMON CALCULATOR TYPE \n[1] EV CALCULATOR \n[2] STAT CALCULATOR ")
        choice = int(input("\nPlease Input Your Choice: "))
    
        if choice == 1:
            stats = int(input("STATS: "))
            pk = int(input("[1] BENEFICIAL [2] HINDERING \nMODIFIER: "))
            if pk == 1:
                mdfr = 1.1

            elif pk == 2:
                mdfr = 0.9

            else:
                print("INVALID INPUT!")
            
            totalEV = EV.evcalc.computeEV(b, iv, ev, lvl, mdfr, stats)
            if totalEV <=500:
                print("TOTAL EV:", totalEV)
            
            else:
                print("POKEMON'S TOTAL EV EXCEEDS")
            ContinueOrExit()
        

        elif choice == 2:
            a = int(input("\nCompute other stats? [1] YES [2] NO \nSELECT: "))
            if a == 1: 
                b = int(input("\n[1]attack [2]def [3]spclatt [4]spcldef [5]speed\nWhat Stat would you like to compute?: "))    
                if  b== 1: 
                    s = 'ATTACK'   
                    c = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if c == 1:
                        ntr = 1.1

                    elif c == 2:
                        ntr = 0.9
                
                if b == 2:
                    s = 'DEFENSE'    
                    c = int(input("\n[1] BENEFICIAL [2] HINDERING \nNature: "))   
                    if c == 1:
                        ntr = 1.1

                    elif c == 2:
                        ntr = 0.9
                
                if b == 3:  
                    s = 'SPECIAL ATTACK'  
                    c = int(input("\n[1] BENEFICIAL [2] HINDERING \nNature: "))   
                    if c == 1:
                        ntr = 1.1

                    elif c == 2:
                        ntr = 0.9

                if b == 4:  
                    s = 'SPECIAL DEFENSE'  
                    c = int(input("\n[1] BENEFICIAL [2] HINDERING \nNature: "))   
                    if c == 1:
                        ntr = 1.1

                    elif c == 2:
                        ntr = 0.9

                if b == 5:    
                    s = 'SPEED'
                    c = int(input("\n[1] BENEFICIAL [2] HINDERING \nNature: "))   
                    if c == 1:
                        ntr = 1.1

                    elif c == 2:
                        ntr = 0.9
                
                other = ST.statcalc.otherstat(b, iv, ev, lvl, ntr)
                if other <= 510:
                    print("\nCOMPUTING", s,"VALUE =", other)
                
                else:
                    print("POKEMON'S TOTAL EV EXCEEDS")
                ContinueOrExit()

            elif a == 2:
                ch = ST.statcalc.health(b, ev, lvl, iv)
                if ch <= 510:
                    print ("HP VALUE:", ch)
                else:
                    print("POKEMON'S TOTAL EV EXCEEDS")
                ContinueOrExit()

            else:
                print("INVALID INPUT!")
                       
        else:
            print("INVALID INPUT!")
main()

