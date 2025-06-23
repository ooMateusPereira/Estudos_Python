def is_leap_year(year):
    if year / 4:
        if year % 4 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
print(is_leap_year(2020))

# Solução
def is_leap_year(year):
    
    '''Verifica se o ano é bissexto.'''

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False