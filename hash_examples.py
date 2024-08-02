hash = {'tom':'+','alex':"+"}

def aboba(number):
    if hash.get(number):
        print('ar')

    else:
        print('o')
        hash[number] = '+'


(aboba('tom'))