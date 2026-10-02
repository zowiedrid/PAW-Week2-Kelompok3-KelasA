# Tugas Kelompok PAW: Pengembangan Homepage Responsif & Landing Page Jurnal

Repositori ini dikembangkan untuk penugasan mata kuliah **Pemrograman Berbasis Web (PAW)**, Program Studi Teknologi Informasi, Universitas Muhammadiyah Yogyakarta (UMY).

---

## 👥 Anggota Kelompok 3 (Kelas A)

| No. | Nama Mahasiswa | NIM | Peran Utama |
|:---:|:---|:---:|:---|
| 1 | **Ilham Fadhilah** | 20200140100 | Desain Homepage CSS Responsif, Media Query & Integrasi Navigasi |
| 2 | **Danar Rohman Rozaqi** | 20240140233 | Analisis Fitur Grid, Variabel `:root` & Evaluasi Kekuatan Sistem |
| 3 | **M.Ikhlasul** | 20240140234 | Penyusunan Konten Fitur Jurnal & Styling Komponen Interaktif |
| 4 | **Anandya Arlys F** | 20240140002 | Pengujian Layout Desktop & Mobile serta Aksesibilitas |

---

## 📄 Informasi Jurnal Pilihan
- **Judul Artikel:** Rancang Bangun Aplikasi Chatbot pada Catering Makanan
- **Penulis:** Nugroho Aji Wicaksono, Rina Fiati
- **Afiliasi:** Program Studi Teknik Informatika, Fakultas Teknik, Universitas Muria Kudus
- **Publikasi:** *Jurnal Dialektika Informatika (Detika)*, Vol. 6, No. 1, Desember 2025, hlm. 6–11
- **DOI:** [10.24176/detika.v6i1.15814](https://doi.org/10.24176/detika.v6i1.15814)
- **Studi Kasus:** UMKM Catering Bu Sumiyati

---

## 📂 Struktur Halaman Website Kelompok

Website kini memiliki struktur multi-halaman yang saling terhubung secara teratur:

```text
Kelompok3/
├── index.html                  # [Tugas 3] Halaman Utama (Homepage) responsif dengan CSS Grid & Hero
├── homepage.html               # Salinan alternatif / alias untuk Homepage
├── style-home.css              # [Tugas 3] Berkas CSS eksternal (:root, reset, layout grid, media queries)
├── landing-jurnal.html         # [Tugas 2] Landing Page Semantic HTML analisis jurnal ilmiah
├── landing-page.html           # Salinan kompatibilitas berkas landing page tugas sebelumnya
├── landing-layanan.html        # Landing Page Showcase Layanan & Pemesanan Catering Bu Sumiyati
├── style.css                   # Berkas CSS untuk landing page jurnal (Tugas 2)
├── images/
│   ├── hero-catering-bot.jpg   # Aset visual hero section (CateringBot AI)
│   └── system-architecture.jpg # Diagram arsitektur sistem 4-lapisan
├── detika,+15814_page6-11.pdf  # Berkas PDF jurnal referensi
└── README.md                   # Dokumentasi penugasan & panduan navigasi
```

---

## 🎯 Pemenuhan 6 Ketentuan Tugas Praktikum 3

1. **Hubungkan CSS Eksternal (`<link>`):**
   - CSS Homepage dipisahkan secara bersih di `style-home.css` dan dihubungkan pada tag `<head>` di `index.html`.
2. **CSS Variables (`:root`) & Reset Sederhana:**
   - Menyimpan variabel warna palet brand, skala spasi (`--space-*`), radius (`--radius-*`), shadow, dan font `Plus Jakarta Sans`.
   - CSS reset universal `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }` serta reset elemen media.
3. **Header / Hero Section:**
   - Header sticky dengan navbar dan dropdown navigasi multi-halaman.
   - Hero section memuat badge inovasi, judul utama (H1) bergradien, deskripsi manfaat sistem, tombol CTA (*Call-to-Action*), indikator metrik kinerja (87% akurasi, 2,3 detik respon), dan visualisasi hero.
4. **Grid Fitur (`display: grid`):**
   - 6 buah feature card interaktif:
     1. *Arsitektur Hibrida Rule-Based & NLP*
     2. *Akses Langsung Zero-Installation*
     3. *Otomasi Alur Pemesanan 3 Langkah*
     4. *Integrasi WhatsApp API Gateway*
     5. *Manajemen Menu & Kalkulasi Instan*
     6. *Kualitas Teruji Tri-Testing Scrum*
5. **Media Query (`@media`):**
   - Mengatur breakpoint responsif untuk tablet landscape (`max-width: 1024px`), tablet portrait/mobile landscape (`max-width: 768px`), dan smartphone (`max-width: 480px`).
   - Penyesuaian layout hero menjadi satu kolom, navigasi hamburger drawer, dan transisi grid menjadi 1–2 kolom tanpa *horizontal overflow*.
6. **Uji Desktop & Mobile:**
   - Seluruh halaman, tautan internal/eksternal, serta aset gambar diverifikasi dengan status HTTP 200 OK tanpa tautan rusak (*zero broken links*).
   - Dilengkapi widget simulator chatbot interaktif yang dapat diuji coba langsung di peramban web.
