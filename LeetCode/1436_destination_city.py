"""You are given the array paths, where paths[i] = [cityAi, cityBi]
 means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, 
there will be exactly one destination city.
"""
import collections
paths = [["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],
["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],
["TtnllZpKKg","OAxMijOZgW"]]

def destCity(paths):
    d = collections.defaultdict(str)
    for path in paths:
        src = path[0]
        dst = path[1]
        d[src] = dst
    for k, v in d.items():
        print(d)
        if v not in d:
            return v


print(destCity(paths))

            
