ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(abs(az - cx), cy // ay, abs(ax - cz))
