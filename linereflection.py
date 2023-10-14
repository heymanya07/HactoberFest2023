def isReflected(points):
    if not points:
        return True

    points_set = set(map(tuple, points))  # Convert the points to a set of tuples for faster lookup

    # Calculate the average x-coordinate
    avg_x = sum(x for x, _ in points) / len(points)

    for x, y in points:
        # Check if the reflected point is in the set
        if (2 * avg_x - x, y) not in points_set:
            return False

    return True

# Example usage:
points = [[1, 1], [-1, 1]]
result = isReflected(points)
print(result)  # Output will be True
