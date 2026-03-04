# COP4533 - PA2
## Programming Assignment 2: Greedy Algorithms

### Team Members
Christopher Webb - 50608994

### Requirements
Language: Python 3.x

### Build/Compilation Instructions
1. Clone the Repository
2. Run "cache.py" to test the input files 

To run the example tests: use this example command and compare the result to "tests/example1.out"

```Bash
python3 src/cache.py tests/example1.in
```

### Assumptions
#### Input Format
- The input file always contains exactly two lines. The first line contains k and m, and the second line contains the integer sequence. 
- Assumed the input format is valid as the program does not perform additional input validation besides parsing 
- Assumed k, m, and all request IDs are integers 
- k >= 1. A capacity of 0 is not handled as it would make eviction policies non-functional. 

## Written Component
### Question 1: Empirical Comparison 
| Input File | k | m  | FIFO | LRU | OPTFF |
|------------|---|----|------|-----|-------|
| File1      | 5 | 50 | 50   | 50  | 34    | |
| File2      | 4 | 50 | 25   | 26  | 13    | |
| File3      | 3 | 50 | 50   | 50  | 19    | | 

- In all of the cases seen in the files, OPTFF had the fewest cache misses. This is because it uses future knowledge when making eviction decisions, thus making it the best performing. 
- In almost each case, LRU and FIFO were tied with there being one case in which FIFO performed slightly better than LRU. This demonstrates that LRU is not universally superior to FIFO as FIFO does not consider usage patterns and for some access patterns this can outperform LRU. 

### Question 2: Bad Sequence for LRU or FIFO
For k = 3, there does exist a request sequence for which OPTFF incurss strictly fewer misses than LRU or FIFO.

For example, the sequence below displays this occurance:

```Bash
1 2 3 4 1 2 3 4 1 2 3 4

Results:
FIFO  : 12
LRU   : 12
OPTFF : 6
```

In this example with the cache capacity of 3 and a repeating cycle of 4 items, LRU and FIFO both have a 100% miss rate. With this cycle of input values, every single request is for the item that was most recently evicted in which LRU and FIFO both receive requests for the value they just evicted. However, OPTFF avoids this cycle by looking ahead and overall significantly reduces the total number of misses. 


### Question 3: Prove OPTFF is Optimal
Let OPTFF be Belady's Farthest-in-Future algorithm and A be any offline algorithm that knows the full request. The number of misses of OPTFF is no larger than that of A on any fixed sequence. 

Assume A differs from OPTFF at the first eviction decision where both have the same items in their cache. At that step OPTFF will evict the item whose next request occurs farthest in the future and A evicts a different item. 

In this instance, let x = the specific item selected for eviction by OPTFF and y = the different item selected for eviction by A. 

Since OPTFF chooses the item farthest in the future, the next time y is need must occur either before or at the same moment as the next time x is needed. 

Additionally, algorithm A will inevitably face a cache mis for y while OPTFF stilll holds y in its cache. We can therefore adjust A to create a modified strategy, A', which opts to evict x instead of y at this step. This modification ensures that A' retains y for its upcoming request, whereas the original algorithm would have suffered an additional miss to bring y back into the cache. 

By making this switch, the total number of misses is reduced or maintained because x is not needed until a point further in the future than y. By repeatedly applying this swap to every point where a strategy differs from OPTFF, we can transform any optimal offline approach into the OPTFF aproach. 

Since this transformation never increases the number of misses, it follows that OPTFF is at least as efficient as any other offline algorithm. **Therefore, OPTFF is optimal**