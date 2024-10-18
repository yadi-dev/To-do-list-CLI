from db import get_db_connection
from datetime import datetime


db = get_db_connection()
cursor = db.cursor()
db.commit()

def add_task():
    title = input("Masukkan judul tugas: ")
    description = input("Masukkan deskripsi tugas: ")
    due_date = input("Masukkan tanggal jatuh tempo (YYYY-MM-DD): ")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
        return
    query = "INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)"
    values = (title, description, due_date)
    cursor.execute(query, values)
    db.commit()
    print("Tugas berhasil ditambahkan!")

def view_tasks():
    query = "SELECT * FROM tasks ORDER BY due_date"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if not tasks:
        print("Tidak ada tugas.")
    else:
        for task in tasks:
            status = "Selesai" if task[4] else "Belum selesai"
            print(f"ID: {task[0]}, Judul: {task[1]}, Deskripsi: {task[2]}, Jatuh Tempo: {task[3]}, Status: {status}")

def update_task():
    task_id = input("Masukkan ID tugas yang ingin diubah: ")
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    if not cursor.fetchone():
        print("Tugas dengan ID tersebut tidak ditemukan.")
        return
    title = input("Masukkan judul baru (biarkan kosong jika tidak ingin mengubah): ")
    description = input("Masukkan deskripsi baru (biarkan kosong jika tidak ingin mengubah): ")
    due_date = input("Masukkan tanggal jatuh tempo baru (YYYY-MM-DD) (biarkan kosong jika tidak ingin mengubah): ")
    
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            return

    query = "UPDATE tasks SET "
    updates = []
    values = []
    
    if title:
        updates.append("title = %s")
        values.append(title)
    if description:
        updates.append("description = %s")
        values.append(description)
    if due_date:
        updates.append("due_date = %s")
        values.append(due_date)
    
    if not updates:
        print("Tidak ada perubahan yang dilakukan.")
        return
    query += ", ".join(updates) + " WHERE id = %s"
    values.append(task_id)
    cursor.execute(query, tuple(values))
    db.commit()
    print("Tugas berhasil diperbarui!")

def delete_task():
    task_id = input("Masukkan ID tugas yang ingin dihapus: ")
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    if not cursor.fetchone():
        print("Tugas dengan ID tersebut tidak ditemukan.")
        return
    query = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(query, (task_id,))
    db.commit()
    print("Tugas berhasil dihapus!")

def mark_task_completed():
    task_id = input("Masukkan ID tugas yang ingin ditandai selesai: ")
    cursor.execute("SELECT is_completed FROM tasks WHERE id = %s", (task_id,))
    result = cursor.fetchone()
    if not result:
        print("Tugas dengan ID tersebut tidak ditemukan.")
        return
    if result[0]:
        print("Tugas ini sudah ditandai selesai sebelumnya.")
        return

    query = "UPDATE tasks SET is_completed = TRUE WHERE id = %s"
    cursor.execute(query, (task_id,))
    db.commit()
    print("Tugas berhasil ditandai selesai!")


def print_banner():
    banner = r"""
    ████████╗ ██████╗       ██████╗  ██████╗     ██╗     ██╗███████╗████████╗
    ╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝
       ██║   ██║   ██║█████╗██║  ██║██║   ██║    ██║     ██║███████╗   ██║   
       ██║   ██║   ██║╚════╝██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   
       ██║   ╚██████╔╝      ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   
       ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝ WITH YADI-DEV
    """
    print(banner)

def print_menu():
    menu = [
        "1. Tambah Tugas",
        "2. Lihat Tugas",
        "3. Perbarui Tugas",
        "4. Hapus Tugas",
        "5. Tandai Tugas Selesai",
        "6. Keluar"
    ]
    print("\n=== Menu Utama ===")
    for item in menu:
        print(f"  {item}")

def main():
    while True:
        print_banner()
        print_menu()
        
        choice = input("Pilih menu (1-6): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
            print("Terima kasih telah menggunakan aplikasi To-Do List with yadi-dev!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
        input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
db.close()
