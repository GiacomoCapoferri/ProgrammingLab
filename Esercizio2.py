def sum_csv(file_name):
    pass
    values = []
    somma = 0
    my_file = open('shampoo_sales.csv', 'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
    for element in values:
        somma=somma+element
    return somma
result=sum_csv('shampoo_sales.csv')
print('somma del file:{}'.format(result))