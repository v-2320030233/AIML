class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph  # Adjacency list of the map (each key is a region, values are neighbors)
        self.colors = colors  # List of available colors
        self.color_assignment = {}  # Dictionary to store color assigned to each region

    # Function to check if the current color assignment is valid for a region
    def is_valid_color(self, region, color):
        for neighbor in self.graph[region]:
            if neighbor in self.color_assignment and self.color_assignment[neighbor] == color:
                return False
        return True

    # Backtracking function to solve the coloring problem
    def solve_map_coloring(self, region_index=0):
        # If all regions have been assigned a color, we are done
        if region_index == len(self.graph):
            return True

        region = list(self.graph.keys())[region_index]

        # Try assigning each color to the current region
        for color in self.colors:
            if self.is_valid_color(region, color):
                # Assign color to the region
                self.color_assignment[region] = color

                # Recursively try to color the rest of the regions
                if self.solve_map_coloring(region_index + 1):
                    return True

                # If assigning color doesn't lead to a solution, backtrack
                del self.color_assignment[region]

        return False

    # Function to print the solution
    def print_solution(self):
        for region, color in self.color_assignment.items():
            print(f"{region}: {color}")

# Example usage
if __name__ == "__main__":
    # Define the map as an adjacency list (neighbors)
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['A', 'C', 'E'],
        'E': ['B', 'C', 'D']
    }

    # List of available colors
    colors = ['Red', 'Green', 'Blue']

    # Create a MapColoring object
    map_coloring = MapColoring(graph, colors)

    # Solve the problem and print the result
    if map_coloring.solve_map_coloring():
        map_coloring.print_solution()
    else:
        print("No solution exists")
