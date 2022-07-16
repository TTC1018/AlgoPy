from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cities = [city.lower() for city in cities]

    answer = 0
    cache = deque(maxlen=cacheSize)
    for i in range(len(cities)):
        if cities[i] not in cache:
            cache.append(cities[i])
            answer += 5
        else:
            cache.remove(cities[i])
            cache.append(cities[i])
            answer += 1

    return answer