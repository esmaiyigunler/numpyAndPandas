#Numpy Ornekleri


import numpy as np

# Öğrencinin sınav puanları
scores = np.array([85, 92, 78, 90, 88])

# Ortalama puan
average_score = np.mean(scores)
print("Ortalama Puan:", average_score)

# En yüksek puan
highest_score = np.max(scores)
print("En Yüksek Puan:", highest_score)

# En düşük puan
lowest_score = np.min(scores)
print("En Düşük Puan:", lowest_score)

#####################################################

import numpy as np

# Şirketin aylık satış verileri (12 ay)
monthly_sales = np.array([1200, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500])

# İlk altı ay
first_half = monthly_sales[:6]
average_first_half = np.mean(first_half)
print("İlk Altı Ay Ortalama Satış:", average_first_half)

# Son altı ay
second_half = monthly_sales[6:]
average_second_half = np.mean(second_half)
print("Son Altı Ay Ortalama Satış:", average_second_half)
###############################################################################
import numpy as np

# Rastgele günlük üretim miktarları oluşturma (30 gün)
np.random.seed(0)  # Tekrarlanabilirlik için
daily_production = np.random.randint(100, 200, size=30)

# Toplam üretim
total_production = np.sum(daily_production)
print("Toplam Üretim:", total_production)

# Ortalama günlük üretim
average_daily_production = np.mean(daily_production)
print("Ortalama Günlük Üretim:", average_daily_production)
##########################################################################

import numpy as np

# Öğrencilerin sınav notları (satır: öğrenci, sütun: sınav)
exam_scores = np.array([
    [85, 90, 88, 92],
    [78, 85, 90, 87],
    [92, 88, 82, 95],
    [80, 85, 78, 88]
])

# Her öğrencinin sınav notları için ortalamayı hesapla
average_scores = np.mean(exam_scores, axis=1)  # axis=1 satır boyunca ortalama
print("Öğrencilerin Ortalamaları:", average_scores)

# Her öğrencinin sınav notlarının ortalamadan uzaklığını hesapla
deviation_from_mean = exam_scores - average_scores[:, np.newaxis]
print("Ortalamadan Uzaklık:\n", deviation_from_mean)

##################################################################################

import numpy as np

# Laboratuvar ölçümleri (örnek: sıcaklık ve nem ölçümleri)
temperature = np.array([22.5, 23.0, 23.5, 24.0, 24.5])
humidity = np.array([50, 48, 45, 42, 40])

# Ortalama sıcaklık ve nem
avg_temperature = np.mean(temperature)
avg_humidity = np.mean(humidity)
print("Ortalama Sıcaklık:", avg_temperature)
print("Ortalama Nem:", avg_humidity)

# Sıcaklık ve nem ölçümlerinin korelasyonu
correlation = np.corrcoef(temperature, humidity)
print("Sıcaklık ve Nem Korelasyonu:\n", correlation)

#####################################################################################

import numpy as np

# Matris oluşturma
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Matris A:\n", A)

# Matris transpozu
A_transpose = A.T
print("Matris A Transpozu:\n", A_transpose)

# Matris determinantı
det_A = np.linalg.det(A)
print("Matris A Determinantı:", det_A)

# Matris tersi
A_inv = np.linalg.inv(A)
print("Matris A Tersi:\n", A_inv)
##############################################################################333


import numpy as np

# Öğrenci sınav notları
exam_scores = np.array([68, 75, 82, 60, 78, 85, 92, 55, 70, 88])

# Geçme notu
passing_score = 70

# Geçme notunu geçen öğrencilerin sayısı
passing_students = np.sum(exam_scores >= passing_score)
print("Geçme Notunu Geçen Öğrenci Sayısı:", passing_students)

# Geçme notunu geçen öğrencilerin notları
passing_scores = exam_scores[exam_scores >= passing_score]
print("Geçme Notunu Geçen Öğrencilerin Notları:", passing_scores)


