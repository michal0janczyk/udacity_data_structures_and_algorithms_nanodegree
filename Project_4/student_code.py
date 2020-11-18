# #!/usr/bin/env python3


from math import sqrt
from heapq import heappush, heappop, heapify
# from map_data import Map10, Map40


class Node:
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.element == other.element

    def __str__(self):
        return str(self.element) + " " + str(self.priority)


def heuristic(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def update_priority(distance, x1, y1, x2, y2):
    return distance + heuristic(x1, y1, x2, y2) * 10


def next_move(prev_node, start, goal):
    current = goal
    path = []
    while current != start and goal < start:
        path.append(current)
        try:
            current = prev_node[current]
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")
    path.append(start)
    path.reverse()
    return path


def shortest_path(map, start, goal):
    open_node = []
    node_priority = {}
    visited_node = {}

    root = Node(start, 0)
    visited_node[start] = None
    node_priority[start] = 0

    heapify(open_node)
    heappush(open_node, root)

    while open_node:
        current_node = heappop(open_node)
        for next_child in map.roads[current_node.element]:
            current_coords = map.intersections[current_node.element]
            x_pos = current_coords[0]
            y_pos = current_coords[1]
            next_node = map.intersections[next_child]
            x_pos_child = next_node[0]
            y_pos_child = next_node[1]
            new_priority = update_priority(
                node_priority[current_node.element],
                x_pos,
                y_pos,
                x_pos_child,
                y_pos_child,
            )
            if next_child not in node_priority.keys():
                node_priority[next_child] = new_priority
                goal_node = map.intersections[goal]
                x_pos_goal = goal_node[0]
                y_pos_goal = goal_node[1]
                priority = update_priority(
                    new_priority, x_pos_goal, y_pos_goal, x_pos_child,
                    y_pos_child)
                next_node = Node(next_child, priority)
                heappush(open_node, next_node)
                visited_node[next_child] = current_node.element
    return next_move(visited_node, start, goal)
