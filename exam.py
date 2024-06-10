import math

def euclideanDistance(point1, point2):
  """
  İki nokta arasindaki Öklid mesafesini hesaplar.

  Args:
    point1: İlk nokta, bir demet olarak (x1, y1).
    point2: İkinci nokta, bir demet olarak (x2, y2).

  Returns:
    İki nokta arasindaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Noktaların listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafeleri saklamak için bir liste
distances = []

# Her nokta çifti arasındaki mesafeleri hesapla
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum mesafe:", min_distance)