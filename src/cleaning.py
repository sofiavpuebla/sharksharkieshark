import re

def findYear(x):
    """esta función busca el año dentro de la columna de date que tiene más valores aparte del año"""
    res=re.search(r'(\d{4})',x)
    if res:
        x=int(res.group(1))
    else:
        x='no'
    return x


def findMonth(x):
    """esta función sirve para buscar el mes dentro de la columna de case number"""
    res=re.search(r'\.(\w{2})\.', x)
    if res:
        x=res.group(1)
    else:
        x=0
    return x

