import sys

sym_tab = {}


def symbol_(identifier, position="", line="", value="-1",size="",type_of=""):
    if identifier in sym_tab.keys() and sym_tab[identifier][0]==value:
        pass
    else:
        if size=="":
            sym_tab[identifier] =[value, position, line, size,type_of]
        elif type_of=="":
            sym_tab[identifier] =[value,sym_tab[identifier][1],sym_tab[identifier][2], size,sym_tab[identifier][4]]
        else:
            sym_tab[identifier] =[value,sym_tab[identifier][1],sym_tab[identifier][2], size,type_of]
    return sym_tab
