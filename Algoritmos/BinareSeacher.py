def binare(list, item):
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        try_ = list[mid]

        if try_ == item:
            return mid
        if try_ > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [10, 20, 200, 30, 40]

print(binare(my_list, 20))