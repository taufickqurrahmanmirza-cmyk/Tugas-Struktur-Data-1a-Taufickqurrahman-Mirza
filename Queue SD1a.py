from collections import deque

antrean = deque()

antrean.append("Atna")
antrean.append("Dimas")
antrean.append("Tio")

print("\nAntrean:", antrean)

mahasiswa_diproses = antrean.popleft()

print("Mahasiswa yang diproses:", mahasiswa_diproses)
print("Antrean setelah diproses:", antrean)

