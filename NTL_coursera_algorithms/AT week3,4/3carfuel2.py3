distance_between_cities = int(input())
full_tank = int(input())
n = int(input())
stations = list(map(int, input().split()))
x = []
current = 0
stops = 0
stations.append(distance_between_cities)

for i in range(1,n+1):
    if stations[i]-stations[i-1]>full_tank:
        print(-1)
        exit()

for i in range(n+1):
    if current==distance_between_cities:
        break
    if stations[i] <= full_tank+current:
        x.append(stations[i])
    else:
        current = max(x)
        stops += 1
        x = []
        x.append(stations[i])


print(stops)
