import sys

sym_tab = {}


def symbol_(identifier, position="", line="", value="-1",size=""):
    if identifier in sym_tab.keys() and sym_tab[identifier][0]==value:
        pass
    else:
        if size=="":
            sym_tab[identifier] =[value, position, line, size]
        else:
            sym_tab[identifier] =[value,sym_tab[identifier][1],sym_tab[identifier][2], size]
    return sym_tab
