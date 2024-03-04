from scipy.io import mmread


# funzione che scorre tutti i dataframe e li legge
def read(filename):
    with open(filename) as mass_file:
        m = mmread(mass_file)
    return m.tocsr()
