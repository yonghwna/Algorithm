"""
data = {
    (0, 1, 3), (0, 3, 4), (0, 4, 1),
    (1, 2, 5), (3, 2, 2), (4, 3, 2)
}
graph = {u: (v, w) for u, v, w in data}
"""

def dijkstra(start: int) -> list[int]:
    heap = [(0, start)]
    dist = [float("inf")] * (n + 1)
    dist[start] = 0

    while heap:
        path_len, node = heapq.heappop(heap)
        if dist[node] < path_len:
            continue
        for (link, length) in graph[node]:
            alt = path_len + length
            if alt < dist[link]:
                dist[link] = alt
                heapq.heappush(heap, (alt, link))
