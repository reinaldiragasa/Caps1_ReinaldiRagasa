# Main Data Structure
list_alat_pemboran = [
    ['Drill Bit', 80, 0.3, 0, 156, 12000, 'PDC', 5],
    ['Drill Collar', 500, 9.14, 57, 171, 5000, '4145H', 20],
    ['Drill Pipe', 200, 9.3, 108, 127, 1500, 'S135', 300],
    ['Stabilizer', 300, 1.5, 57, 171, 4000, '4145H/S135', 4],
    ['Reamer', 500, 1.8, 64, 216, 20000, 'Alloy/TC', 2],
    ['Top Drive', 10000, 2.5, 76, 584, 600000, '4130', 1],
    ['Mud Motor', 500, 3, 57, 171, 30000, '4145H', 3],
    ['Swivel', 1000, 1.2, 76, 330, 40000, '4140', 1],
    ['Accelerator', 300, 1.8, 51, 165, 8000, '4140', 2],
    ['Rotary Table', 3000, 0.6, 0, 445, 150000, 'Cast/Alloy', 1],
    ['MWD', 250, 3, 57, 171, 250000, '316SS', 3],
]

# Authentication Variables
registered_users = {}
first_time_user = True

# Utility Functions
def validate_email(email):
    """Check if email meets requirements"""
    if not email.endswith("@gmail.com"):
        return False, "Email harus diakhiri dengan @gmail.com"
    
    prefix = email.split("@")[0]
    if not prefix.isalnum():
        return False, "Email hanya boleh mengandung huruf dan angka sebelum @gmail.com"
    
    return True, "Email valid"

def check_password(password):
    """Check if password meets requirements"""
    if len(password) <= 6:
        return False, "Password harus lebih dari 6 karakter"
    
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    
    if not (has_letter and has_number):
        return False, "Password harus mengandung huruf dan angka"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    
    if not (has_upper and has_lower):
        return False, "Password harus mengandung huruf besar dan kecil"
    
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return False, "Password tidak boleh mengandung karakter berulang secara berurutan"
    
    return True, "Password valid"

def bubble_sort(data, column_index, reverse=False):
    """Implement bubble sort for sorting data"""
    n = len(data)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (data[j][column_index] > data[j+1][column_index]) if not reverse else (data[j][column_index] < data[j+1][column_index]):
                data[j], data[j+1] = data[j+1], data[j]
    return data

def find_extreme(data, column_index, find_max=False):
    """Find min or max value using bubble sort approach"""
    if not data:
        return None
    
    extreme_value = data[0][column_index]
    extreme_items = [data[0]]
    
    for item in data[1:]:
        current_value = item[column_index]
        if (find_max and current_value > extreme_value) or (not find_max and current_value < extreme_value):
            extreme_value = current_value
            extreme_items = [item]
        elif current_value == extreme_value:
            extreme_items.append(item)
    
    return extreme_value, extreme_items

def print_table(data, column_index=None, attribute_name=None, unit=None, extreme_type=None):
    """Print table with various options: sorting or extreme values (min/max)"""
    if not data:
        print("Tidak ada data untuk ditampilkan")
        return
    
    if extreme_type:
        extreme_value = data[0][column_index]
    
    print("=" * 142)
    print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
    print("=" * 142)
    
    for idx, item in enumerate(data, start=1):
        print(f"| {idx:<3} | {item[0]:<12} | {item[1]:<12} | {item[2]:<12} | {item[3]:<10} | {item[4]:<10} | {item[5]:<15} | {item[6]:<25} | {item[7]:<15} |")
    
    print("=" * 142)
    
    if extreme_type:
        print(f"\n{attribute_name} {'minimum' if extreme_type == 'min' else 'maksimum'} adalah {extreme_value} {unit}.")
        print(f"\n{attribute_name} {'minimum' if extreme_type == 'min' else 'maksimum'} terdapat di alat pemboran berikut dengan {attribute_name.lower()} sebesar {extreme_value} {unit}:")
        for item in data:
            print(f"- {item[0]} dengan {attribute_name.lower()} sebesar {item[column_index]} {unit}")

def daftar_alat_pemboran():
    """Display all drilling equipment in table format"""
    print("\nDaftar Alat Pemboran:")
    print("=" * 142)
    print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
    print("=" * 142)
    for idx, alat_pemboran in enumerate(list_alat_pemboran, start=1):
        print(f"| {idx:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
    print("=" * 142)

# Authentication Functions
def register():
    """Handle user registration"""
    print("\n=== REGISTER ===")
    while True:
        email = input("Masukkan email: ").strip()
        is_valid, message = validate_email(email)
        
        if not is_valid:
            print(f"Email tidak valid: {message}")
            continue
            
        if email in registered_users:
            print("\nEmail sudah terdaftar.")
            while True:
                kembali = input("Kembali ke menu awal? (y/n): ").lower().strip()
                if kembali == 'y':
                    return False  
                elif kembali == 'n':
                    break  
                else:
                    print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
            continue
            
        break
    
    while True:
        password = input(''' 
Syarat password:
1. Mengandung lebih dari 6 karakter
2. Mengandung karakter alphabet dan numerik
3. Mengandung huruf kapital dan huruf kecil
4. Karakter yang sama tidak berurutan
                         
Masukkan password: ''').strip()
        
        is_valid, message = check_password(password)
        
        if not is_valid:
            print(f"Password tidak valid: {message}")
            continue
            
        break
    
    registered_users[email] = password
    print("\nRegistrasi berhasil! Silakan login untuk menggunakan program.")
    return True

def login():
    """Handle user login"""
    global first_time_user
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        print("\n=== LOGIN ===")
        email = input("Masukkan email: ").strip()
        
        # Check if email is registered
        if email not in registered_users:
            print("\nEmail belum terdaftar. Silahkan registrasi terlebih dahulu.")
            
            # Reset first_time_user flag since we've now checked for registered users
            first_time_user = False
            
            while True:
                kembali = input("Kembali ke menu awal? (y/n): ").lower().strip()
                if kembali == 'y':
                    return False  
                elif kembali == 'n':
                    break  
                else:
                    print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
            continue
            
        password = input("Masukkan password: ").strip()
        
        if registered_users[email] != password:
            print("\nPassword salah!")
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Percobaan tersisa: {remaining}")
            continue
            
        print("\nLogin berhasil!")
        return True
    
    print("\nAnda telah melebihi batas percobaan login. Program akan keluar.")
    return False

def auth_menu():
    """Display authentication menu"""
    while True:
        print("\n=== SELAMAT DATANG ===")
        print("1. Register")
        print("2. Login")
        
        choice = input("Pilihan Anda: ").strip()
        
        if choice == '1':
            if register():
                return True
        elif choice == '2':
            if login():
                return True
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

# Equipment Display Functions
def display_all_then_filter():
    """Display all equipment then filter"""
    if not list_alat_pemboran:  
        print("Data alat pemboran tidak ada.") 
        return
    
    print("=" * 142)
    print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
    print("=" * 142)

    for idx, alat_pemboran in enumerate(list_alat_pemboran, start=1):
        print(f"| {idx:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
    
    print("=" * 142)

def all_alat_pemboran():
    """Display all drilling equipment"""
    if not list_alat_pemboran:  
        print("Data alat pemboran tidak ada.")
        return
    
    display_all_then_filter()

def spesifik_alat_pemboran():
    """Display specific equipment by name"""
    print("Masukkan nama alat pemboran yang ingin ditampilkan:")
    selected_name = input().strip() 
    
    found = False
    for alat_pemboran in list_alat_pemboran:
        if selected_name.lower() in alat_pemboran[0].lower(): 
            if not found:  
                print("=" * 142)
                print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
                print("=" * 142)
            found = True
            print(f"| {list_alat_pemboran.index(alat_pemboran) + 1:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
    
    if not found:
        print("Alat pemboran yang dicari tidak ditemukan!")
    else:
        print("=" * 142)

def spesifik_material_grade(material_grade):
    """Display equipment by material grade"""
    ditemukan = False
    for alat_pemboran in list_alat_pemboran:
        if alat_pemboran[6].lower() == material_grade.lower():  
            if not ditemukan:
                print("=" * 142)
                print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
                print("=" * 142)
                ditemukan = True
            print(f"| {list_alat_pemboran.index(alat_pemboran) + 1:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
    
    if not ditemukan:
        print(f"Tidak ada alat pemboran di material grade '{material_grade}'.")
    else:
        print("="*142)

def handle_sort_or_extreme(choice):
    """Handle sorting or finding extreme values"""
    attr_map = {
        '1': (1, "Weight (kg)", "Berat", "kg"),
        '2': (2, "Length (m)", "Panjang", "m"),
        '3': (3, "ID (mm)", "ID", "mm"),
        '4': (4, "OD (mm)", "OD", "mm"),
        '5': (5, "Price (USD)", "Harga", "USD"),
        '6': (7, "Stock", "Stock", "buah"),
        '7': (None, "Kembali", None, None)
    }
    
    while True:
        print('''Pilih atribut yang ingin diurutkan:
    1. Weight (kg)
    2. Length (m)
    3. ID (mm)
    4. OD (mm)
    5. Price (USD)
    6. Stock
    7. Kembali ke menu Sort Alat Pemboran''')
    
        attribute_choice = input(f"Masukkan angka atribut yang ingin di{'urutkan' if choice in ('2','3') else 'cari nilai'} {'min' if choice in ('2','4') else 'max'} nya (1-7): ").strip()
        
        if attribute_choice == '7':
            print("Kembali ke menu Sub Menu.")
            return
        
        if attribute_choice not in attr_map:
            print("Input tidak valid. Harap masukkan angka 1-7.")
            continue
        
        col_idx, col_name, attr_name, unit = attr_map[attribute_choice]
        
        if choice == '2':
            print(f"Menampilkan tabel alat pemboran dari {attr_name.lower()} terendah ke tertinggi:")
            sorted_data = bubble_sort(list_alat_pemboran.copy(), col_idx)
            print_table(sorted_data)
        elif choice == '3':
            print(f"Menampilkan tabel alat pemboran dari {attr_name.lower()} tertinggi ke terendah:")
            sorted_data = bubble_sort(list_alat_pemboran.copy(), col_idx, reverse=True)
            print_table(sorted_data)
        elif choice == '4':
            print(f"Menampilkan {attr_name.lower()} minimal:")
            extreme_value, extreme_items = find_extreme(list_alat_pemboran, col_idx)
            print_table(extreme_items, col_idx, attr_name, unit, "min")
        elif choice == '5':
            print(f"Menampilkan {attr_name.lower()} maksimal:")
            extreme_value, extreme_items = find_extreme(list_alat_pemboran, col_idx, find_max=True)
            print_table(extreme_items, col_idx, attr_name, unit, "max")
        
        break  

def show_all_alat_pemboran():
    """Display all equipment with sorting/filtering options"""
    while True:
        print('''
        Sub Menu:
        1. Menampilkan semua alat pemboran
        2. Menampilkan data dari min ke max 
        3. Menampilkan data dari max ke min 
        4. Menampilkan data minimum
        5. Menampilkan data maksimum
        6. Menampilkan data spesifik alat pemboran
        7. Menampilkan data berdasarkan material grade
        8. Kembali ke main menu
        ''')
        
        sub_choice = input("Masukkan pilihan dari Sort Alat Pemboran: ").strip()
        
        if sub_choice == '1':
            print("Menampilkan semua alat pemboran:")
            all_alat_pemboran()  
        elif sub_choice in ('2', '3', '4', '5'):
            handle_sort_or_extreme(sub_choice)
        elif sub_choice == '6':
            display_all_then_filter()
            spesifik_alat_pemboran()
        elif sub_choice == '7':
            material_grade = input("Masukkan material grade yang dicari: ").strip()
            print(f"Menampilkan data alat pemboran berdasarkan material grade: {material_grade}")
            spesifik_material_grade(material_grade)
        elif sub_choice == '8':
            print("Kembali ke main menu.")
            return
        else:
            print("Input tidak valid")

# CRUD Operations
def add_alat_pemboran():
    """Add new drilling equipment"""
    while True:
        print('''
        1. Menambah Alat Pemboran
        2. Kembali ke Main Menu
        ''')
        pilihan = input("Masukkan pilihan Anda: ").strip()

        if pilihan == '1':
            print("\nData Alat Pemboran Sebelum Penambahan:")
            daftar_alat_pemboran()

            nama_alat_pemboran = input('Masukkan Nama Alat Pemboran: ').strip()

            for alat_pemboran in list_alat_pemboran:
                if alat_pemboran[0].lower() == nama_alat_pemboran.lower():
                    print("Error: Data ini telah ada!\n")
                    break
            else:  
                while True:
                    try:
                        berat = int(input('Masukkan berat (kg): '))
                        if berat <= 0:
                            print("Berat harus lebih besar dari 0!")
                            continue
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                while True:
                    try:
                        panjang = int(input('Masukkan panjang (m): '))
                        if panjang <= 0:
                            print("Panjang harus lebih besar dari 0!")
                            continue
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                while True:
                    try:
                        ID = int(input('Masukkan ID (mm): '))
                        if ID < 0:  
                            print("ID tidak boleh negatif!")
                            continue
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                while True: 
                    try:
                        OD = int(input('Masukkan OD (mm): '))
                        if OD <= 0:
                            print("OD harus lebih besar dari 0!")
                            continue
                        if OD <= ID and ID != 0: 
                            print("Error. OD tidak bisa lebih kecil dari atau sama dengan ID (kecuali ID=0). Masukkan nilai yang valid!")
                            continue
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                while True:
                    try:
                        harga = int(input('Masukkan harga (USD): '))
                        if harga <= 0:
                            print("Harga harus lebih besar dari 0!")
                            continue
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                material_grade = input('Masukkan material grade: ').strip()

                while True:
                    try:
                        stock = int(input('Masukkan stock: '))
                        if stock < 0:
                            print("Stock tidak boleh negatif!")
                            continue
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                print("\nData yang akan disimpan:")
                print(f"Equipment: {nama_alat_pemboran}")
                print(f"Weight (kg): {berat}")
                print(f"Length (m): {panjang}")
                print(f"ID (mm): {ID}")
                print(f"OD (mm): {OD}")
                print(f"Price (USD): {harga}")
                print(f"Material grade: {material_grade}")
                print(f"Stock: {stock}")

                while True:
                    simpan = input("Apakah Anda ingin menyimpan data ini? (y/n): ").lower().strip()
                    if simpan == 'y':
                        list_alat_pemboran.append([nama_alat_pemboran, berat, panjang, ID, OD, harga, material_grade, stock])
                        print(f'\nAlat pemboran {nama_alat_pemboran} berhasil ditambahkan dan disimpan!')
                        
                        print("\nData Alat Pemboran Setelah Penambahan:")
                        daftar_alat_pemboran()
                        break
                    elif simpan == 'n':
                        print('Data tidak disimpan. Kembali ke menu utama.\n')
                        break
                    else:
                        print("Input tidak valid! Masukkan 'y' atau 'n'.")

        elif pilihan == '2':
            print("Kembali ke main menu...\n")
            break
        else:
            print("Pilihan tidak valid. Harap pilih 1 atau 2.\n")

def delete_alat_pemboran():
    """Delete drilling equipment"""
    while True:
        print(''' 
            Menu Penghapusan Alat Pemboran:
            1. Menghapus Alat Pemboran
            2. Kembali ke Main Menu
        ''')
        pilihan = input("Masukkan pilihan Anda (1/2): ").strip()
        
        if pilihan == '1':
            print("=" * 142)
            print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
            print("=" * 142)
    
            for idx, alat_pemboran in enumerate(list_alat_pemboran, start=1):
                print(f"| {idx:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
    
            print("=" * 142)

            nama_alat_pemboran = input("Masukkan nama alat pemboran yang ingin dihapus: ").strip()

            found = False
            for i, alat_pemboran in enumerate(list_alat_pemboran):
                if alat_pemboran[0].lower() == nama_alat_pemboran.lower():
                    found = True

                    print("\nAlat pemboran yang ingin Anda hapus adalah:")
                    print("=" * 142)
                    print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
                    print("=" * 142)
                    print(f"| {i+1:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
                    print("=" * 142)
                    
                    while True:
                        validasi = input("Hapus data? (y/n): ").lower().strip()
                        if validasi == 'y':
                            print(f"Alat pemboran {alat_pemboran[0]} berhasil dihapus.")
                            del list_alat_pemboran[i]
                            break
                        elif validasi == 'n':
                            print("Data batal dihapus.")
                            break
                        else:
                            print("Input tidak valid! Masukkan 'y' atau 'n'.")
                            continue
                    
                    break 

            if not found:
                print("Data tidak ditemukan. Anda akan kembali ke menu penghapusan.")
                continue
                
        elif pilihan == '2':
            return 
        else:
            print("Input tidak valid! Masukkan angka 1 atau 2.")

def update_alat_pemboran():
    """Update drilling equipment information"""
    while True:
        print("\n1. Mengupdate Alat Pemboran per Kolom")
        print("2. Mengupdate Semua Kolom Alat Pemboran")
        print("3. Kembali ke Main Menu")
        pilihan_awal = input("Masukkan pilihan (1/2/3): ").strip()

        if pilihan_awal == '1':
            print("\nDaftar Alat Pemboran:")
            print("=" * 142)
            print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
            print("=" * 142)
    
            for idx, alat_pemboran in enumerate(list_alat_pemboran, start=1):
                print(f"| {idx:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
    
            print("=" * 142)

            nama_alat_pemboran = input("Masukkan nama alat pemboran yang mau diupdate: ").lower().strip()

            alat_pemboran_ditemukan = False
            for i, alat_pemboran in enumerate(list_alat_pemboran):
                if alat_pemboran[0].lower() == nama_alat_pemboran.lower():  
                    alat_pemboran_ditemukan = True
                    nomor_alat_pemboran = i

                    print("\nAlat pemboran yang Dipilih:")
                    print("=" * 142)
                    print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
                    print("=" * 142)
                    print(f"| {i+1:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
                    print("=" * 142)
                    break
            
            if not alat_pemboran_ditemukan:
                print("Error: Nama alat pemboran tidak ditemukan.")
                continue 

            while True:
                validasi = input("Lanjutkan update? (y/n): ").lower().strip()
                if validasi in ['y', 'n']:
                    break
                print("Input tidak valid! Harap masukkan 'y' atau 'n'.")

            if validasi == 'n':
                print("Kembali ke menu update.")
                continue  

            data_awal = list_alat_pemboran[nomor_alat_pemboran][:]

            while True:
                print("\nPilih kolom yang ingin diupdate:")
                print("1. Weight (kg)")
                print("2. Length (m)")
                print("3. ID (mm)")
                print("4. OD (mm)")
                print("5. Price (USD)")
                print("6. Material grade")
                print("7. Stock")
                print("8. Kembali ke menu update")
                
                pilihan = input("Masukkan nomor pilihan (1-8): ").strip()
                
                if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > 8:
                    print("Input tidak valid! Harap masukkan angka antara 1-8.")
                    continue
                
                pilihan = int(pilihan)

                if pilihan == 1:
                    while True:
                        try:
                            berat = int(input('Masukkan berat baru (kg): '))
                            if berat <= 0:
                                print("Berat harus lebih besar dari 0!")
                                continue
                            list_alat_pemboran[nomor_alat_pemboran][1] = berat
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk berat.")
                
                elif pilihan == 2:
                    while True:
                        try:
                            panjang = int(input('Masukkan panjang baru (m): '))
                            if panjang <= 0:
                                print("Panjang harus lebih besar dari 0!")
                                continue
                            list_alat_pemboran[nomor_alat_pemboran][2] = panjang
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk panjang.")
                
                elif pilihan == 3:
                    while True:
                        try:
                            ID = int(input('Masukkan ID baru (mm): '))
                            if ID < 0:
                                print("ID tidak boleh negatif!")
                                continue
                            if ID >= list_alat_pemboran[nomor_alat_pemboran][4]:
                                print("Error: ID tidak bisa lebih besar dari atau sama dengan OD. Masukkan nilai yang valid!")
                                continue
                            list_alat_pemboran[nomor_alat_pemboran][3] = ID
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk ID.")
                
                elif pilihan == 4:
                    while True:
                        try:
                            OD = int(input('Masukkan OD baru (mm): '))
                            if OD <= 0:
                                print("OD harus lebih besar dari 0!")
                                continue
                            if OD <= list_alat_pemboran[nomor_alat_pemboran][3]:
                                print("Error: OD tidak bisa lebih kecil dari atau sama dengan ID. Masukkan nilai yang valid!")
                                continue
                            list_alat_pemboran[nomor_alat_pemboran][4] = OD
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk OD.")
                
                elif pilihan == 5:
                    while True:
                        try:
                            harga = int(input('Masukkan harga baru (USD): '))
                            if harga <= 0:
                                print("Harga harus lebih besar dari 0!")
                                continue
                            list_alat_pemboran[nomor_alat_pemboran][5] = harga
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk harga.")
                
                elif pilihan == 6:
                    material_grade = input('Masukkan material grade baru: ').strip()
                    list_alat_pemboran[nomor_alat_pemboran][6] = material_grade
                
                elif pilihan == 7:
                    while True:
                        try:
                            stock = int(input('Masukkan stock baru: '))
                            if stock < 0:
                                print("Stock tidak boleh negatif!")
                                continue
                            list_alat_pemboran[nomor_alat_pemboran][7] = stock
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk stock.")

                elif pilihan == 8:
                    print("Kembali ke menu update alat pemboran.")
                    break

                while True:
                    lanjut_update = input("Lanjutkan update kolom lain? (y/n): ").lower().strip()
                    if lanjut_update in ['y', 'n']:
                        break
                    print("Input tidak valid! Harap masukkan 'y' atau 'n'.")

                if lanjut_update == 'n':
                    break

            print("\nData Alat Pemboran Setelah Update:")
            daftar_alat_pemboran()

        elif pilihan_awal == '2':
            daftar_alat_pemboran()

            nama_alat_pemboran = input("Masukkan nama alat pemboran yang mau diupdate: ").strip()

            alat_pemboran_ditemukan = False
            for i, alat_pemboran in enumerate(list_alat_pemboran):
                if alat_pemboran[0].lower() == nama_alat_pemboran.lower(): 
                    alat_pemboran_ditemukan = True
                    nomor_alat_pemboran = i

                    print("\nAlat pemboran yang Dipilih:")
                    print("=" * 142)
                    print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
                    print("=" * 142)
                    print(f"| {i+1:<3} | {alat_pemboran[0]:<12} | {alat_pemboran[1]:<12} | {alat_pemboran[2]:<12} | {alat_pemboran[3]:<10} | {alat_pemboran[4]:<10} | {alat_pemboran[5]:<15} | {alat_pemboran[6]:<25} | {alat_pemboran[7]:<15} |")
                    print("=" * 142)

                    while True:
                        lanjutkan = input("Lanjutkan update (y/n): ").lower().strip()
                        if lanjutkan in ['y', 'n']:
                            break
                        print("Input tidak valid! Harap masukkan 'y' atau 'n'.")

                    if lanjutkan == 'n':
                        break

                    print("\nMasukkan data baru:")
                    while True:
                        try:
                            berat = int(input('Weight (kg): '))
                            if berat <= 0:
                                print("Berat harus lebih besar dari 0!")
                                continue
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    
                    while True:
                        try:    
                            panjang = int(input('Length (m): '))
                            if panjang <= 0:
                                print("Panjang harus lebih besar dari 0!")
                                continue
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    
                    while True:
                        try:   
                            ID = int(input('ID (mm): '))
                            if ID < 0:
                                print("ID tidak boleh negatif!")
                                continue
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    
                    while True:
                        try:
                            OD = int(input('OD (mm): '))
                            if OD <= 0:
                                print("OD harus lebih besar dari 0!")
                                continue
                            if OD <= ID:
                                print("Error: OD tidak bisa lebih kecil dari atau sama dengan ID. Masukkan nilai yang valid!")
                                continue
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                         
                    while True:
                        try:
                            harga = int(input('Harga (USD): '))
                            if harga <= 0:
                                print("Harga harus lebih besar dari 0!")
                                continue
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    
                    material_grade = input("Material Grade Baru: ").strip()  
                    
                    while True:
                        try:       
                            stock = int(input('Stock: ')).strip()  
                            if stock < 0:
                                print("Stock tidak boleh negatif!")
                                continue
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                        
                    while True:
                        simpan_data = input("Update data (y/n): ").lower().strip()
                        if simpan_data in ['y', 'n']:
                            break
                        print("Input tidak valid! Harap masukkan 'y' atau 'n'.")

                    if simpan_data == 'n':
                        print("Update dibatalkan.")
                        break

                    list_alat_pemboran[nomor_alat_pemboran][1] = berat
                    list_alat_pemboran[nomor_alat_pemboran][2] = panjang
                    list_alat_pemboran[nomor_alat_pemboran][3] = ID
                    list_alat_pemboran[nomor_alat_pemboran][4] = OD
                    list_alat_pemboran[nomor_alat_pemboran][5] = harga
                    list_alat_pemboran[nomor_alat_pemboran][6] = material_grade
                    list_alat_pemboran[nomor_alat_pemboran][7] = stock

                    print("\nData berhasil diupdate!")
                    print("\nData Alat Pemboran Setelah Update:")
                    daftar_alat_pemboran()
                    break

            if not alat_pemboran_ditemukan:
                print(f"Alat pemboran dengan nama '{nama_alat_pemboran}' tidak ditemukan.")

        elif pilihan_awal == '3':
            print("Kembali ke main menu.")
            break

        else:
            print("Pilihan tidak valid! Harap pilih antara 1, 2, atau 3.")

# Purchase Function
def buy_alat_pemboran():
    """Handle equipment purchase"""
    while True:
        print('''
        Sub Menu Pembelian:
        1. Membeli Alat Pemboran
        2. Kembali ke Main Menu
        ''')
        sub_choice = input("Masukkan pilihan Anda (1/2): ").strip()
        
        if sub_choice == '1':
            print("\nDaftar Alat Pemboran Tersedia:")
            print("=" * 142)
            print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
            print("=" * 142)
            for idx, alat in enumerate(list_alat_pemboran, start=1):
                stock_status = "OUT OF STOCK" if alat[7] == 0 else alat[7]
                print(f"| {idx:<3} | {alat[0]:<12} | {alat[1]:<12} | {alat[2]:<12} | {alat[3]:<10} | {alat[4]:<10} | {alat[5]:<15} | {alat[6]:<25} | {stock_status:>15} |")
            print("=" * 142)
            
            nama_alat = input("\nMasukkan nama alat pemboran yang ingin dibeli: ").strip()
            
            found = False
            selected_alat = None
            alat_index = -1
            
            for i, alat in enumerate(list_alat_pemboran):
                if nama_alat.lower() == alat[0].lower():
                    found = True
                    selected_alat = alat
                    alat_index = i
                    break
            
            if not found:
                print("Error: Nama alat pemboran tidak ditemukan.")
                continue

            if selected_alat[7] == 0:
                print(f"\nStock {selected_alat[0]} yang tersedia saat ini tidak ada. Mohon pilih alat pemboran yang lain.")
                continue

            print("\nAlat Pemboran yang Dipilih:")
            print("=" * 142)
            print(f"| {'No':<3} | {'Equipment':<12} | {'Weight (kg)':<12} | {'Length (m)':<12} | {'ID (mm)':<10} | {'OD (mm)':<10} | {'Price (USD)':<15} | {'Material grade':<25} | {'Stock':<15} |")
            print("=" * 142)
            print(f"| {1:<3} | {selected_alat[0]:<12} | {selected_alat[1]:<12} | {selected_alat[2]:<12} | {selected_alat[3]:<10} | {selected_alat[4]:<10} | {selected_alat[5]:<15} | {selected_alat[6]:<25} | {selected_alat[7]:<15} |")
            print("=" * 142)
            
            while True:
                confirm = input(f"Beli alat pemboran {selected_alat[0]}? (y/n): ").lower().strip()
                if confirm == 'n':
                    print("Pembelian dibatalkan.")
                    break
                elif confirm == 'y':
                    while True:
                        try:
                            quantity = int(input(f"Masukkan jumlah yang ingin dibeli (stock tersedia: {selected_alat[7]}): "))
                            if quantity <= 0:
                                print("Jumlah harus lebih dari 0!")
                                continue
                            if quantity > selected_alat[7]:
                                print(f"Jumlah yang dibeli melebihi stock. Saat ini stock yang tersedia: {selected_alat[7]}")
                                continue
                            break
                        except ValueError:
                            print("Input tidak valid! Mohon masukkan angka.")
                    
                    total_price = selected_alat[5] * quantity
                    print(f"\nTotal harga untuk {quantity} {selected_alat[0]}: ${total_price}")
                    
                    while True:
                        try:
                            payment = int(input("Masukkan jumlah uang (USD): "))
                            if payment < 0:
                                print("Jumlah uang tidak boleh negatif!")
                                continue
                            break
                        except ValueError:
                            print("Input tidak valid! Mohon masukkan angka.")
                    
                    if payment == total_price:
                        print("\nTerima kasih! Silahkan datang lagi.")
                        list_alat_pemboran[alat_index][7] -= quantity
                        break
                    elif payment > total_price:
                        change = payment - total_price
                        print(f"\nTerima kasih! Ini kembalian Anda: ${change}. Silahkan datang lagi.")
                        list_alat_pemboran[alat_index][7] -= quantity
                        break
                    else:
                        shortage = total_price - payment
                        print(f"\nMaaf, uang Anda kurang ${shortage}.")
                        break
                    
                else:
                    print("Input tidak valid! Harap masukkan 'y' atau 'n'.")
                    continue
                
                break   
        
        elif sub_choice == '2':
            print("Kembali ke main menu.")
            return
        else:
            print("Pilihan tidak valid! Harap pilih antara 1 atau 2.")

# Main Menu
def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n=== MENU UTAMA ===")
        pilihanMenu = input(''' 
                            Selamat Datang di Tempat Analisa Pemboran
                            List Menu:
                            1. Menampilkan Data Alat Pemboran
                            2. Menambah Alat Pemboran
                            3. Menghapus Alat Pemboran
                            4. Mengupdate Alat Pemboran
                            5. Membeli Alat Pemboran
                            6. Exit program
                            Masukkan angka Menu yang ingin dijalankan: 
        ''').strip()

        if pilihanMenu == '1': 
            show_all_alat_pemboran()
        elif pilihanMenu == '2': 
            add_alat_pemboran()     
        elif pilihanMenu == '3': 
            delete_alat_pemboran()
        elif pilihanMenu == '4':
            update_alat_pemboran()
        elif pilihanMenu == '5':
            buy_alat_pemboran()
        elif pilihanMenu == '6':
            print('Keluar dari Program !!!') 
            break
        else:
            print("\nPilihan tidak valid! Harap masukkan angka 1-6.")

# Main Program
def main():
    """Main program entry point"""
    while True:
        if auth_menu():  
            main_menu()  
        
        while True:
            choice = input("\nApakah Anda ingin keluar dari program? (y/n): ").lower().strip()
            if choice == 'y':
                print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
                return
            elif choice == 'n':
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    main()