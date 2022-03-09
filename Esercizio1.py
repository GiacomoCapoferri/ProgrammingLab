my_list=[1,2,3,4]

def somma(my_list):
    sum=0
    for element in my_list:
        sum=sum+element
    return sum
result=somma(my_list)
print('somma della lista:{}'.format(result))