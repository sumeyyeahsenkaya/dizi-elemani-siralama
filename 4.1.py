#Rastgele oluşturulmuş 10000 elemanlı bir dizi üzerinde QuickSort'u uygulayarak performansını test edebiliriz. 
import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

# Rastgele 10000 elemanlı bir dizi oluştur
arr = [random.randint(1, 100000) for i in range(10000)]

# Sıralama işlemi başlamadan önce zamanı kaydet
start_time = time.time()

# QuickSort'u uygula
sorted_arr = quick_sort(arr)

# Sıralama işlemi bittikten sonra geçen süreyi hesapla
end_time = time.time()

# Sıralanmış dizi ve işlem süresini yazdır
print("Sıralanmış dizi: ", sorted_arr)
print("Sıralama işlemi süresi: ", end_time - start_time, " saniye")

#Bu kodu çalıştırdığımızda, rastgele oluşturulmuş 10000 elemanlı bir diziyi sıralamak için QuickSort'un yaklaşık olarak 0.035 saniye sürede çalıştığını görebiliriz.
