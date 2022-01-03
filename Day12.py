
import datetime
from pprint import pprint
import functools
import statistics
import pathlib
from collections import defaultdict


def main():
    begin_time = datetime.datetime.now()
    HOME = pathlib.Path(__file__).parent
    
    # Process input into cave tuples
    with open(str(HOME) + "\\Day12Data.txt", "r") as fd:
        caves = [tuple(line.rstrip().split('-')) for line in fd.readlines()]

    cave_graph = CaveGraph()
    for cave_tup in caves:
        [cave_graph.addEdge(cave_tup[i], cave_tup[1 - i]) for i in range(2)]

    cave_graph.getAllPaths("start", "end")
    pprint(cave_graph.count)

    print(datetime.datetime.now() - begin_time)

class CaveGraph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.count = 0

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def getAllPathsUtil(self, u, d, visited, path):
        if not u.isupper(): visited[u] = True
        path.append(u)

        if u == d:
            self.count += 1
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.getAllPathsUtil(i, d, visited, path)

        path.pop()
        visited[u] = False
    
    def getAllPaths(self, s, d):
        visited = defaultdict(bool)
        path = []
        self.getAllPathsUtil(s, d, visited, path)


if __name__ == '__main__':
    main()