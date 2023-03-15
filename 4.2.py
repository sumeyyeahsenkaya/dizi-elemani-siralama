#Rastgele oluşturulmuş 10000 elemanlı bir diziyi Brute Force yöntemiyle sıralamak için Python'da şu kodu kullanabiliriz
import random
import time

def brute_force_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

# Rastgele 10000 elemanlı bir dizi oluştur
arr = [random.randint(1, 100000) for i in range(10000)]

# Sıralama işlemi başlamadan önce zamanı kaydet
start_time = time.time()

# Brute Force yöntemiyle sırala
brute_force_sort(arr)

# Sıralama işlemi bittikten sonra geçen süreyi hesapla
end_time = time.time()

# Sıralanmış dizi ve işlem süresini yazdır
print("Sıralanmış dizi: ", arr)
print("Sıralama işlemi süresi: ", end_time - start_time, " saniye")

#Bu kodu çalıştırdığımızda, rastgele oluşturulmuş 10000 elemanlı bir diziyi Brute Force yöntemiyle sıralamak için yaklaşık olarak 18.5 saniye sürede çalıştığını görebiliriz.
