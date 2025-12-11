# 1 Binary search
sayur = ["Bayam", "Kangkung", "Wortel", "Kentang", "Buncis", "Brokoli"]
harga = [5000, 6000, 8000, 10000, 12000, 14000]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

index = binary_search(harga, 5000)
print("Ditemukan:", sayur[index], "Dengan harga:", harga[index])
# 2 interpolation
sayur = ["Bayam", "Kangkung", "Wortel", "Kentang", "Buncis", "Brokoli"]
harga = [5000, 6000, 8000, 10000, 12000, 14000]

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

index = interpolation_search(harga, 10000)
print("Ditemukan:", sayur[index], "Dengan harga:", harga[index])
