
def main():
    # Process input into list of points
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day5Data.txt", "r") as fd:
        lines = fd.readlines()
    segments = []
    for line in lines:
        data = line.split(" -> ")
        for i in range(2):
            data[i] = data[i].split(',')
            for j in range(2):
                data[i][j] = int(data[i][j])
        segments += [data]
    
    
    # Consider only horizontal and vertical lines
    # segments = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], segments))
    
    # Mark lines on vents
    # Segment: [ [ x1, y1 ], [ x2, y2 ] ]
    vents = [[0] * 1000 for i in range(1000)]
    for segment in segments:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        # Matching x
        if x1 == x2:
            if y1 > y2:
                iter = range(y2, y1 + 1)
            else:
                iter = range(y1, y2 + 1)
            for i in iter:
                vents[x1][i] += 1
        # Matching y
        elif y1 == y2:
            if x1 > x2:
                iter = range(x2, x1 + 1)
            else:
                iter = range(x1, x2 + 1)
            for i in iter:
                vents[i][y1] += 1
        # Diagonal Lines
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1

            slope = (x1 - x2)/(y1 - y2)
            if slope == 1:
                ystep = 1
            else:
                ystep = -1   

            x, y = x1, y1
            comparison_tuple = (x2 + 1, y2 + ystep)
            while (x, y) != comparison_tuple:
                    print(f"x, y: {x}, {y}")
                    vents[x][y] += 1
                    x += 1
                    y += ystep
    
    # Count all dangerous spots
    count = 0
    for i in range(len(vents)):
        for j in range(len(vents[i])):
            if vents[i][j] >= 2: count += 1
    print(count)


if __name__ == '__main__':
    main()