'''
Build the most efficient airports/roads
Each city must be able to access one airport

Can be improved with better union/find
'''
from Kruskals import kruskals


def least_cost_for_airports_and_roads(airport_cost, n_cities, roads):
    minimum_roads, parents = kruskals(range(1, n_cities + 1), roads)
    road_cost = sum(road[2] for road in minimum_roads)
    num_sections = len([node for node in parents if node == parents[node]])
    return road_cost + num_sections * airport_cost


assert least_cost_for_airports_and_roads(100, 4, [[1, 2, 10], [4, 3, 12], [4, 1, 41], [2, 3, 23]]) == 145
assert least_cost_for_airports_and_roads(1000, 5, [[1, 2, 20], [4, 5, 40], [3, 2, 30]]) == 2090
