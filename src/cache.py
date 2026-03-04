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

def optff(k, requests): 
    cache = []
    misses = 0
    m = len(requests)

    for i in range(m):
        item = requests[i]

        if item in cache:
            continue # Cache hit 
        
        # Miss
        misses += 1
        if len(cache) < k: 
            cache.append(item)

        else:
            farthest = -1
            victim = None

            for entry in cache: 
                next_use = -1 

                for j in range(i + 1, m):
                    if requests[j] == entry:
                        next_use = j
                        break
                if next_use == -1:
                    victim = entry
                    break

                if next_use > farthest:
                    farthest = next_use
                    victim = entry

            cache.remove(victim)
            cache.append(item)

    return misses

def main():
    if len(sys.argv) != 2: 
        print("Usage: python cache.py <input_file>")
        return
    
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        first_line = f.readline().strip().split()
        k = int(first_line[0]) # capacity of the cache
        m = int(first_line[1]) # sequence of requests
        requests = list(map(int, f.readline().strip().split()))

    print(f"FIFO  : {fifo(k, requests)}")
    print(f"LRU   : {lru(k, requests)}")
    print(f"OPTFF : {optff(k, requests)}")


if __name__ == "__main__":    
    main()