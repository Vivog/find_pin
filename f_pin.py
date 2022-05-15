# 123
# 456
# 789
#  0
# The case of horizontal and vertical options
def get_pin(observed):
    dic_pin = {'1':('1','2','4'), '2':('2','1','3','5'), '3':('3','2','6'),
               '4':('4','1','5','7'), '5':('5','2','4','6','8'),
               '6':('6','3','5','9'), '7':('7','4','8'), '8':('8','5','7','9','0'),
               '9':('9','6','8'), '0':('0','8')}
    from itertools import product
    rezult = [''.join(i) for i in product(*(dic_pin[d]) for d in observed)]
    return rezult
print(get_pin('12'))