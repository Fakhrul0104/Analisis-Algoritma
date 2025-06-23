import math

# Fungsi menghitung jarak Euclidean antara dua titik
def hitung_jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Brute force untuk kasus dasar
def brute_force(P):
    min_jarak = float('inf')
    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            jarak = hitung_jarak(P[i], P[j])
            if jarak < min_jarak:
                min_jarak = jarak
    return min_jarak

# Menghitung jarak terkecil dalam strip
def jarak_di_strip(strip, d):
    min_jarak = d
    n = len(strip)
    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            jarak = hitung_jarak(strip[i], strip[j])
            if jarak < min_jarak:
                min_jarak = jarak
    return min_jarak

# Fungsi rekursif utama
def closest_pair_rec(Px, Py):
    n = len(Px)
    
    if n <= 3:
        return brute_force(Px)
    
    mid = n // 2
    midpoint = Px[mid]
    
    Qx = Px[:mid]
    Rx = Px[mid:]
    
    Qy = list()
    Ry = list()
    
    for point in Py:
        if point[0] <= midpoint[0]:
            Qy.append(point)
        else:
            Ry.append(point)
    
    d_left = closest_pair_rec(Qx, Qy)
    d_right = closest_pair_rec(Rx, Ry)
    d = min(d_left, d_right)
    
    strip = [p for p in Py if abs(p[0] - midpoint[0]) < d]
    
    return min(d, jarak_di_strip(strip, d))

# Fungsi utama
def closest_pair(P):
    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda x: x[1])
    return closest_pair_rec(Px, Py)

# Contoh penggunaan
if __name__ == "__main__":
    titik = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    hasil = closest_pair(titik)
    print(f"Jarak terdekat adalah: {hasil}")
