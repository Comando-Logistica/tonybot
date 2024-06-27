def converter_placa(placa):

    digito = placa[4]

    conversor = {
        '0': 'A',
        '1': 'B',
        '2': 'C',
        '3': 'D',
        '4': 'E',
        '5': 'F',
        '6': 'G',
        '7': 'H',
        '8': 'I',
        '9': 'J',
        "A": "0",
        "B": "1",
        "C": "2",
        "D": "3",
        "E": "4",
        "F": "5",
        "G": "6",
        "H": "7",
        "I": "8",
        "J": "9"
    }
    
    mercosul = 'ABCDEFGHIJ'
    cinza = '0123456789'
 
    if digito in mercosul:
        placa_cinza = f'{placa[0:4]}{conversor[placa[4]]}{placa[5:]}'
        placa_mercosul = placa
    elif digito in cinza:
        placa_mercosul = f'{placa[0:4]}{conversor[placa[4]]}{placa[5:]}'
        placa_cinza = placa

    return [placa_cinza, placa_mercosul]