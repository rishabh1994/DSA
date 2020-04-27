import heapq
import math


def getCost(first, second):
    return math.hypot(second[0] - first[0], second[1] - first[1])


def shortest_path(M, start, goal):
    print("shortest path called")
    nodes = []
    heapq.heappush(nodes, (0, start, [start], 0))
    nodeToCost = dict()

    for i in M.intersections:
        nodeToCost[i] = math.inf

    nodeToCost[start] = 0

    if start == goal:
        return [start]

    finalPath = []

    while nodes:

        node = heapq.heappop(nodes)
        currentNode = node[1]
        currentPath = node[2]
        actualNodeToNodeCost = node[3]

        if currentNode == goal:
            break

        for neighbour in M.roads[currentNode]:

            costToReachNeighbour = getCost(M.intersections[currentPath[len(currentPath) - 1]],
                                           M.intersections[neighbour])
            approximateCostToGoal = getCost(M.intersections[goal], M.intersections[neighbour])
            totalCost = actualNodeToNodeCost + costToReachNeighbour + approximateCostToGoal
            existingCost = nodeToCost[neighbour]

            if existingCost > totalCost:

                newList = currentPath.copy()
                newList.append(neighbour)
                heapq.heappush(nodes, (totalCost, neighbour, newList, actualNodeToNodeCost + costToReachNeighbour))
                nodeToCost[neighbour] = totalCost

                if neighbour == goal:
                    finalPath = newList

    return finalPath
