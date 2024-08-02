graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['finish'] = 1
                        # таблица графов (ребра и узлы , и их веса )
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['finish'] = 5

graph['finish'] = {}


infinity = float("inf")
costs = {}
costs['a'] = 6                      # таблица стоимостей
costs['b'] = 2
costs['finish'] = infinity


perents = {}
perents['a'] = 'start'
perents['b'] = 'start'                  #таблица родителей
perents['in'] = None


processed = []                             # массив проверенных узлов


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost  = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            perents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)





# эту часть кода сделал чат gpt :)

# Вывод кратчайшего пути к финишу
def print_shortest_path(perents, start, finish):
    path = []
    current_node = finish
    while current_node is not None:
        path.append(current_node)
        current_node = perents.get(current_node)  # Используем .get() для предотвращения KeyError
    path.reverse()
    # Удаляем стартовый узел, если он присутствует в пути
    if path[0] == start:
        path.pop(0)
    return path

# Получаем кратчайший путь
shortest_path = print_shortest_path(perents, 'start', 'finish')
print("Кратчайший путь к финишу:", shortest_path)
print("Стоимость этого пути:", costs['finish'])
