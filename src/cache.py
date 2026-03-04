import sys

def fifo(k, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache: 
            continue # Indicates a cache hit

        misses += 1
        if len(cache) == k:
            cache.pop(0)

        cache.append(request)

    return misses

def lru(k, requests):
    cache = []
    usage_map = {}
    misses = 0
    for i in range (len(requests)):
        item = requests[i]

        if item in cache:
            usage_map[item] = i # Update last access index 
        else:
            misses += 1
            if len(cache) >= k: 
                oldest = float('inf')
                victim = None
                
                for entry in cache:
                    if usage_map[entry] < oldest:
                        oldest = usage_map[entry]
                        victim = entry
                
                cache.remove(victim)
            
            cache.append(item)
            usage_map[item] = i

    return misses

