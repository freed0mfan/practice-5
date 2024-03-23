stations = input('N K M: ')
N = int(stations.split(' ')[0])
K = int(stations.split(' ')[1])
M = int(stations.split(' ')[2])

if K < M:
    if M - K - 1 < N - M + K - 1:
        print(M - K - 1)
    else:
        print(N - M + K - 1)
else:
    if K - M - 1 < N - K + M - 1:
        print(K - M - 1)
    else:
        print(N - K + M - 1)
