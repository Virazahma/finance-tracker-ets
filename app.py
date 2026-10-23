from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Transaksi Bulanan (Mulai dari Maret 2026 - 5 Bulan Lebih)
transaksi_list = [
    {"tanggal": "2026-03-10", "keterangan": "Gaji Maret", "jenis": "masuk", "jumlah": 4500000},
    {"tanggal": "2026-03-15", "keterangan": "Bayar Kos Maret", "jenis": "keluar", "jumlah": 1200000},
    {"tanggal": "2026-04-12", "keterangan": "Gaji April", "jenis": "masuk", "jumlah": 4800000},
    {"tanggal": "2026-04-20", "keterangan": "Belanja Lebaran", "jenis": "keluar", "jumlah": 1500000},
    {"tanggal": "2026-05-10", "keterangan": "Gaji Mei", "jenis": "masuk", "jumlah": 5000000},
    {"tanggal": "2026-05-18", "keterangan": "Service Motor", "jenis": "keluar", "jumlah": 350000},
    {"tanggal": "2026-06-12", "keterangan": "Gaji Juni", "jenis": "masuk", "jumlah": 5000000},
    {"tanggal": "2026-06-25", "keterangan": "Liburan Singkat", "jenis": "keluar", "jumlah": 800000},
    {"tanggal": "2026-07-10", "keterangan": "Gaji Juli", "jenis": "masuk", "jumlah": 5500000},
    {"tanggal": "2026-07-15", "keterangan": "Beli Buku Kuliah", "jenis": "keluar", "jumlah": 250000}
]

@app.route('/')
def home():
    total_masuk = sum(t['jumlah'] for t in transaksi_list if t['jenis'] == 'masuk')
    total_keluar = sum(t['jumlah'] for t in transaksi_list if t['jenis'] == 'keluar')
    saldo_akhir = total_masuk - total_keluar
    
    return render_template('index.html', masuk=total_masuk, keluar=total_keluar, saldo=saldo_akhir, data=transaksi_list)

@app.route('/transaksi')
def transaksi():
    return render_template('simple.html', data_transaksi=transaksi_list)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        tanggal = request.form.get('tanggal')
        keterangan = request.form.get('keterangan')
        jumlah = int(request.form.get('jumlah'))
        jenis = request.form.get('jenis')
        
        transaksi_list.insert(0, {
            "tanggal": tanggal,
            "keterangan": keterangan,
            "jenis": jenis,
            "jumlah": jumlah
        })
        return redirect(url_for('transaksi'))
        
    return render_template('tambah.html')

@app.route('/profil')
def profil():
    return render_template('profile.html')

@app.route('/pengaturan')
def pengaturan():
    return render_template('pengaturan.html')

if __name__ == '__main__':
    app.run(debug=True)