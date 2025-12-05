import os

def make_range(i):
    [start, stop] = i.split('-')
    return range(int(start), int(stop) + 1)

# load input file
with open(os.path.join(__file__, "../../input")) as f:
    [rangesx, availablesx] = f.read().split('\n\n')
    ranges = [make_range(i.strip()) for i in rangesx.split('\n')]

def unify_ranges(ranges: list[range]) -> list[range]:
    ranges.sort(key=lambda r: r.start)
    merged = []
    for r in ranges:
        # the first range can stay untouched
        if not merged:
            merged.append(r)
            continue
        # get last used range
        last = merged[-1]
        # since the list is sorted by r.start: r.start >= last.start
        # so we only need to check if r starts before last ends
        if r.start < last.stop: # overlap
            if r.stop > last.stop: # if our range is not contained within last
                merged[-1] = range(last.start, r.stop) # extend last range to fit in our range
        else: # no overlap
            merged.append(r) # just add
    return merged

res = 0

# iterate over the unified ranges and add their ranges[1] up
# [1] when i say ranges here I mean the range definition in statistics, the one with: Range(X) = Max(X) - Min(X)
for r in unify_ranges(ranges):
    res += r.stop - r.start

print(res)
