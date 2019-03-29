sym_tab = {}


def symbol(identifier, position, line, value=""):
    if identifier in sym_tab.keys():
        pass
    else:
        sym_tab[identifier] =[value, position, line]

    return sym_tab
