import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes with their current minimum distance
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If current distance is greater than stored distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If found shorter path to neighbor, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage:
if __name__ == "_main_":
    # Example graph representing connections and distances between cities
    graph = {
        'Hyderabad': {'Mumbai': 500, 'Delhi': 1500, 'Chennai': 300},
        'Mumbai': {'Hyderabad': 500, 'Delhi': 1200},
        'Delhi': {'Hyderabad': 1500, 'Mumbai': 1200, 'Kolkata': 1500},
        'Chennai': {'Hyderabad': 300, 'Kolkata': 1800},
        'Kolkata': {'Delhi': 1500, 'Chennai': 1800},
        'Dudh Kosi': {'Kolkata': 1000}
    }
    
    start_node = 'Hyderabad'
    end_node = 'Dudh Kosi'
    
    # Run Dijkstra's algorithm from start_node
    shortest_distances = dijkstra(graph, start_node)
    
    # Find the shortest distance to end_node
    shortest_distance = shortest_distances.get(end_node, float('inf'))
    
    if shortest_distance == float('inf'):
        print(f"No path found from {start_node} to {end_node}.")
    else:
        print(f"Shortest distance from {start_node} to {end_node}: {shortest_distance} km.")
# Time complexity:O((V+E)logV
    #heapq-insertion,deletion O(logv)
# space complexity:O(V+E)