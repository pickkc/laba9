from queue import Queue
import random
import time

size1 = int(input("Введитеразмерматрицы M1: "))
M1 = []
start_vertex = 0
for i in range(size1):
    row = []
    for j in range(size1):
row.append(0)
    M1.append(row)

for i in range(size1):
    for j in range(i + 1, size1):
        M1[i][j] = M1[j][i] = random.randint(0, 1)

lists = [[] for _ in range(size1)]
for i in range(size1):
    for j in range(size1):
        if M1[i][j] == 1:
            lists[i].append(j)

defbreadth_first_search_distance(G, v):
size_G = len(G)
    DIST = [-1] * size_G

def BFSD(start_vertex):
        Q = Queue()
Q.put(start_vertex)
        DIST[start_vertex] = 0

        while not Q.empty():
current_vertex = Q.get()
print(current_vertex, end=' ')

            for i in range(size_G):
                if G[current_vertex][i] == 1 and DIST[i] == -1:
Q.put(i)
                    DIST[i] = DIST[current_vertex] + 1

    BFSD(v)

    return DIST

defbreadth_first_search_distance_list(adj_list, start_vertex):
num_vertices = len(adj_list)
    DIST = [-1] * num_vertices

def BFSD(start):
        queue = Queue()
queue.put(start)
        DIST[start] = 0

        while not queue.empty():
current_vertex = queue.get()
print(current_vertex, end=' ')

            for neighbor in adj_list[current_vertex]:
                if DIST[neighbor] == -1:
queue.put(neighbor)
                    DIST[neighbor] = DIST[current_vertex] + 1

    BFSD(start_vertex)

    return DIST

defdepth_first_search_distance(G):
defDFS(v, distance):
        NUM[v] = True
        DIST[v] = distance
print(v, end=' ')

        for i in range(size_G):
            if G[v][i] == 1 and not NUM[i]:
DFS(i, distance + 1)

size_G = len(G)
    NUM = [False] * size_G
    DIST = [-1] * size_G

    for i in range(size_G):
        if not NUM[i]:
DFS(i, 0)

    return DIST

defdepth_first_search_distance_list(adj_list):
num_vertices = len(adj_list)
    DIST = [-1] * num_vertices

defDFS(vertex, distance):
        NUM[vertex] = True
        DIST[vertex] = distance
print(vertex, end=' ')

        for neighbor in adj_list[vertex]:
            if not NUM[neighbor]:
DFS(neighbor, distance + 1)

    NUM = [False] * num_vertices

    for vertex in range(num_vertices):
        if not NUM[vertex]:
DFS(vertex, 0)

    return DIST

print("Матрицасмежностидля M1:")
for row in M1:
    print(row)

print("\nСписок смежности для M1: ")
for i, verticles in enumerate(lists):
print(f"Вершина {i}: {verticles}")

print("\nРезультат обхода в ширину с расстояниями:")
start_time = time.time()
distances = breadth_first_search_distance(M1, start_vertex)
elapsed_time = time.time() - start_time
print("\nВекторрасстоянийотвершины", start_vertex, ":", distances)
print(f"Времяработы: {elapsed_time} секунд")

print("\nРезультат обхода в ширину с расстояниями для списка смежности:")
distances = breadth_first_search_distance_list(lists, start_vertex)
print("\nВекторрасстоянийотвершины", start_vertex, ":", distances)

print("\nРезультат обхода в глубину с расстояниями:")
start_time = time.time()
distances = depth_first_search_distance(M1)
elapsed_time = time.time() - start_time
print("\nВекторрасстояний:", distances)
print(f"Времяработы: {elapsed_time} секунд")

print("\nРезультат обхода в глубину с расстояниями для списка смежности:")
distances = depth_first_search_distance_list(lists)
print("\nВектор расстояний:", distances) 
