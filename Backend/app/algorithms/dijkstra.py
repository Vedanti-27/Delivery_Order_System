import heapq


def dijkstra(graph, start):
    """
    Find the shortest distance from start node
    to every other node.
    """

    # Initially, all distances are infinity
    distances = {node: float("inf") for node in graph}

    # Distance from starting point to itself is 0
    distances[start] = 0

    # Store previous node to reconstruct shortest path
    previous = {node: None for node in graph}

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        # Ignore outdated information
        if current_distance > distances[current_node]:
            continue

        # Check all neighboring nodes
        for neighbor, distance in graph[current_node]:

            new_distance = current_distance + distance

            # Found a shorter path
            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def get_shortest_path(previous, start, destination):
    """
    Reconstruct the shortest path.
    """

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] != start:
        return []

    return path