import heapq

def streaming_median(nums):
    """
    Return a list of medians after each prefix of nums.
    Uses two heaps: max-heap for lower half, min-heap for upper half.
    """
    if not nums:
        return []

    low = []   # max-heap (store negatives)
    high = []  # min-heap
    result = []

    for num in nums:
        # Push to max-heap first
        heapq.heappush(low, -num)

        # Ensure all elements in low <= elements in high
        if low and high and -low[0] > high[0]:
            val = -heapq.heappop(low)
            heapq.heappush(high, val)

        # Balance the heaps
        if len(low) < len(high):
            heapq.heappush(low, -heapq.heappop(high))
        elif len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))

        # Compute median
        if len(low) > len(high):
            result.append(-low[0])
        else:
            result.append((-low[0] + high[0]) / 2.0)

    return result
