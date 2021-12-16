from collections import deque


def width_find(graph, first_vertex):
    search_queue = deque()
    search_queue += graph[first_vertex]
    checked = []
    while search_queue:
        vertex = search_queue.popleft()
        if vertex not in checked:
            print(vertex)
            search_queue += graph[vertex]
            checked.append(checked)


def depth_find(graph, first_vertex):
