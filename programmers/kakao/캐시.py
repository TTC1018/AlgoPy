from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cities = [city.lower() for city in cities]

    answer = 0
    cache = set()
    order = deque()
    for i in range(len(cities)):
        if cities[i] not in cache:
            if len(order) == cacheSize:
                cache.remove(order.popleft())  # 캐시 꽉 차면 LRU
            cache.add(cities[i])
            order.append(cities[i])
            answer += 5
        else:
            order.remove(cities[i])
            order.append(cities[i])
            answer += 1

    return answerㅋ