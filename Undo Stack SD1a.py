undo_stack = []

undo_stack.append("Menambahkan mahasiswa Atna")
undo_stack.append("Mengubah data Dimas")
undo_stack.append("Menghapus data Tio")

print("\nStack Undo:", undo_stack)

aksi_dibatalkan = undo_stack.pop()

print("Aksi yang di-undo:", aksi_dibatalkan)
print("Stack setelah undo:", undo_stack)