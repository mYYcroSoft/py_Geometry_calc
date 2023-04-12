import time

def obsah_ctverce(strana):
    """Vypočte obsah čtverce."""
    return strana ** 2

def obsah_kruhu(polomer):
    """Vypočte obsah kruhu."""
    return 3.14 * polomer ** 2

def obsah_trojuhelniku(zakladna, vyska):
    """Vypočte obsah trojúhleníku."""
    return 0.5 * zakladna * vyska

def obvod_ctverce(strana):
    """Vypočte obvod čtverce."""
    return 4 * strana

def obvod_kruhu(polomer):
    """Vypočte obvod kruhu."""
    return 2 * 3.14 * polomer

def obvod_trojuhelniku(strana_a, strana_b, strana_c):
    """Vypočte obvod trojúhleníku."""
    return strana_a + strana_b + strana_c






def select():
 
    print("____________________")
    print("> obsah_ctverce [1]")
    print("> obsah_kruhu [2]")
    print("> obsah_trojuhelniku [3]")
    print("____________________")

    print("> obvod_ctverce [4]")
    print("> obvod_kruhu [5]")
    print("> obvod_trojuhelniku [6]")
    print("____________________")
    action = input("> [AKCE] ")
  


    # obsah_ctverce
    if action == '1':
        strana = int(input("Velikost strany  v CM: "))
        print("                  [Výsledek] ", obsah_ctverce(strana) , "cm2")
        time.sleep(1)
        select()
    elif action == '2':
        # obsah_kruhu
        polomer = int(input("Poloměr kruhu: "))
        print("                  [Výsledek] ",obsah_kruhu(polomer) ,"cm2")
        select()
    elif action == '3':
        # obsah_trojuhelniku
        zakladna = int(input("Velikost základny v CM: "))
        vyska = int(input("Výška v CM: "))
        print("                  [Výsledek] ",obsah_trojuhelniku(zakladna, vyska) , "cm2")
        time.sleep(1)
                
        select()
    elif action == '4':
        # obvod_ctverce
        strana = int(input("Velikost strany  v CM: "))
        print("                  [Výsledek] ", obvod_ctverce(strana) , "cm")
        time.sleep(1)
        select()
    elif action == '5':
        # obvod_kruhu
        polomer = int(input("Poloměr kruhu: "))
        print("                  [Výsledek] ",obvod_kruhu(polomer) ,"cm")
        time.sleep(1)
        select()
    elif action == '6':
        # obvod_trojuhelniku
        strana_a = int(input("Velikost strany A v CM: "))
        strana_b = int(input("Velikost strany B v CM: "))
        strana_c = int(input("Velikost strany C v CM: "))
        print("                  [Výsledek] ",obvod_trojuhelniku(strana_a, strana_b, strana_c) , "cm")
        time.sleep(1)
        select()
    else:
        select()
        print("> Chybná volba.")


select()