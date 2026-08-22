import heapq
import csv
from collections import defaultdict

# build graph using the route table
 
def build_graph(csv_file):
    graph = defaultdict(list)
    try:

        with open(csv_file, newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            # reads columns - assigns nodes and gets distance between nodes
            for row in reader:
                start = row['from_warehouse']
                end = row['to_warehouse']
                distance = int(row['distance'])

                graph[start].append((end, distance))
                graph[end].append((start, distance))
    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")  

    return graph




def shortest_path(graph, start, end):
    # priority queue stores (distance, current_node, path_taken)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        distance, current, path = heapq.heappop(pq)

        # skips if already processed
        if current in visited:
            continue

        visited.add(current)

        #found destination
        if current == end:
            return distance, path
  
        #explore other nodes

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (distance + weight, neighbor, path + [neighbor])
                )

    return float('inf'), []

def get_path(graph, start, end):
    _, path = shortest_path(graph, start, end)
    return path

