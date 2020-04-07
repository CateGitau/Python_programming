l = [2, 3, 5, 8, 11, 12, 18]

search_for = 11

slice_start = 0
slice_end = len(l) - 1

found = False

while slice_start <= slice_end and not found:
    mid = (slice_start + slice_end)// 2
    if l[mid] == search_for:
        found = True
    else:
        if search_for > l[mid]:
            slice_start = mid + 1
        else:
            slice_end = mid - 1

print(mid)