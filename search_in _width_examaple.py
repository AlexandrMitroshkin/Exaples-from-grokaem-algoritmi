from collections import *

list_of_seller_mango = ['Akeq','axmet']

graph = {}
graph['you'] = ['Lecha','Andrei']
graph['Lecha'] = ['Nastya']
graph['Andrei'] = ['Alena']
graph['Nastya'] = ['Lecha']
graph['Alena'] = ['Aksanya','Cergey']
graph['Aksanya'] = []
graph['Cergey'] = []

def person_is_seller(name):
    if name in list_of_seller_mango:
        return True

def search_in_width(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True

            else :
                search_queue += graph[person]
                searched.append(person)

    print('В вашей родне нема продавцов манго')
    return False



search_in_width('you')







