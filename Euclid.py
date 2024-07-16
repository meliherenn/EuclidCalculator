import math


points = []


n = int(input("How many points will you enter? "))

for i in range(n):
    x = float(input(f"Enter the x coordinate of point {i+1}: "))
    y = float(input(f"Enter the y coordinate of point {i+1}: "))
    points.append((x, y))


def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))


if distances:
    min_distance = min(distances)
    print("Minimum Euclidean distance:", min_distance)
else:
    print("No distances to calculate.")
