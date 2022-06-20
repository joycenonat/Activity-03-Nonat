class evcalc():
    def computeEV (b, iv, ev, lvl, mdfr, stats):
        A=(((2*b)+iv+(ev/4)) * ( lvl/100))
        statmdfr = stats/mdfr
        return (((((statmdfr - A) * 400 )) / lvl) / 4 ) * 4