# 1 bubble sorting
sayuran = ["Bayam", "Jagung", "Kangkung", "Tomat", "Cabai"]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

bubble_sort(sayuran)
print(sayuran)
# 2 selection sorting
def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        
        data[i], data[min_index] = data[min_index], data[i]

    return data

minuman = ["susu", "Kopi", "pop ice", "capucino", "es teh"]

print("Data sebelum diurutkan:", minuman)
hasil = selection_sort(minuman)
print("Data setelah diurutkan:", hasil)
# 3 insertion sorting
makanan = ["sate", "bakso", "nasi goreng", "ayam geprek", "mie ayam"]

for i in range(1, len(makanan)):
    key = makanan[i]
    j = i - 1

    while j >= 0 and makanan[j] > key:
        makanan[j + 1] = makanan[j]
        j -= 1

    makanan[j + 1] = key

print("Hasil pengurutan:", makanan)


