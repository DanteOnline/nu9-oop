# 1. True == True
# 2. Приведение типов к логискому

def is_logic():
    # if 2 > 1:
    #     return True
    # else:
    #     return False
    return 2 > 1


# True == True, False == True = False
if is_logic():
    print('Все хорошо')

if 2 > 1:
    print('Все хорошо')

if (True if 2 > 1 else False) == True:
    print('Все хорошо')
