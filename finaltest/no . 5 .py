# Dictionary merek handphone
handphone = {
    "vivo": [8 , 258],
    "oppo": [8 , 128],
    "advan": [4 , 128],
    "iphone": [12 , 512],
    "samsung": [6 , 128],
    "axioo": [4 , 32]
}

print("Data Merek handphone:")
for m, ram in handphone.items():
    print(f"- {m} : {ram}")

merek = input("\nMasukkan merek handphone yang ingin dicari: ")

if merek in handphone:
    print(f"barang tersedi")
    print(f"ram + penyimpanan: {handphone[merek]}")
else:
    print(f"barang tidak tersedia .")
