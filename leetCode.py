# menghitung baris ke sn
start = int(input("Start :"))
end = int(input("End :"))
step = int(input("Beda :"))
hasil = start
p = [str(start)]
n = 0
while start != end:
    start = start + step
    hasil += start
    p.append(f"+ {start}")
print("Barisan", " ".join(p))
print("Hasil:", hasil)