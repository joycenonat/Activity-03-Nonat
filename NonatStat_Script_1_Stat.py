class statcalc ():
    def health (b, ev, lvl, iv):
        return ((((2*b+iv+(ev/4))*lvl)/100))+lvl+10
        
    def otherstat(b, iv, ev, lvl, ntr):
        return ((((((2 * b) + iv + (ev /4) ) * lvl)) / 100 ) + 5 ) * ntr