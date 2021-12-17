from collections import deque


def width_find(graph, first_vertex):
    search_queue = deque()
    search_queue.append(first_vertex)
    search_queue += graph[first_vertex]
    checked = []
    while search_queue:
        vertex = search_queue.popleft()
        if vertex not in checked:
            print(vertex)
            search_queue += graph[vertex]
            checked.append(vertex)


def depth_find(graph, first_vertex, checked=None):
    if not checked:
        checked = []
    checked.append(first_vertex)
    print(first_vertex)
    for vertex in graph[first_vertex]:
        if vertex not in checked:
            depth_find(graph, vertex, checked)
    return checked


def make_graph(graph, start, end, flag=True):
    if start not in graph:
        graph[start] = {end}
    else:
        graph[start].add(end)
    if flag:
        if end not in graph:
            graph[end] = {start}
        else:
            graph[end].add(start)


my_graph = {}


def main():
    make_graph(my_graph, 1, 3)
    make_graph(my_graph, 1, 2)
    make_graph(my_graph, 1, 5)
    make_graph(my_graph, 2, 3)
    make_graph(my_graph, 2, 4)
    make_graph(my_graph, 5, 4)

    # print(my_graph[2])
    #width_find(my_graph, 1)
    depth_find(my_graph, 1)

main()
