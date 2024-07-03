#경로 최적화 프로젝트
#by SY, MH

import sys

input = sys.stdin.readline
INF = int(1e9)

print("노드의 개수, 간선의 개수")
n, m = map(int, input().split())
print("시작 노드 번호")
start_node = int(input())
print("끝 노드 번호")
end_node = int(input())

graph = [[]for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

pre_nodes = [0] * (n + 1)

print("출발 노드, 도착 노드, 거리")
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):

    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        pre_nodes[j[0]] = start
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                pre_nodes[j[0]] = now

    route = []
    current = end_node
    while current != start:
        route.append(current)
        current = pre_nodes[current]
    route.append(start)
    route.reverse()
    return route


route = dijkstra(start_node)

print("최단경로 길이: ", distance[end_node])
print("최단경로: ", *route)
