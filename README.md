# Tugas Kelompok PAW: Landing Page Semantic HTML dari Jurnal Pilihan

Repositori ini berisi landing page berbasis **HTML5 Semantic** yang merangkum dan menganalisis jurnal ilmiah terpilih untuk mata kuliah **Pemrograman Berbasis Web (PAW)**.

---

## 📄 Informasi Jurnal Pilihan
- **Judul Artikel:** Rancang Bangun Aplikasi Chatbot pada Catering Makanan
- **Penulis:** Nugroho Aji Wicaksono, Rina Fiati
- **Afiliasi:** Program Studi Teknik Informatika, Fakultas Teknik, Universitas Muria Kudus
- **Publikasi:** *Jurnal Dialektika Informatika (Detika)*, Vol. 6, No. 1, Desember 2025, hlm. 6–11
- **DOI:** [10.24176/detika.v6i1.15814](https://doi.org/10.24176/detika.v6i1.15814)
- **Studi Kasus:** UMKM Catering Bu Sumiyati

---

## 🌟 Novelty (Kebaruan Penelitian)
1. **Pendekatan Hibrida (Hybrid Architecture):** Mengombinasikan *Rule-based system* (untuk FAQ deterministik dan alur pengisian formulir pemesanan terstruktur) dengan *Natural Language Processing (NLP)* menggunakan algoritma **Naïve Bayes** dan pembobotan kata *TF-IDF* untuk pengenalan intensi percakapan bebas pada domain spesifik UMKM katering.
2. **Integrasi Alur Pemesanan Interaktif Tanpa Aplikasi Tambahan (*Zero Installation*):** Berbasis web peramban standar dengan widget chatbot dan arsitektur siap integrasi API (seperti WhatsApp Messenger) sehingga menekan friksi adaptasi pelanggan.
3. **Efisiensi Terukur untuk Skala Usaha Mikro:** Menggunakan metodologi *Scrum*, arsitektur sistem berlapis (*layered architecture*), dan pengujian tri-faset (*Whitebox, Blackbox, UAT*) yang menghasilkan akurasi klasifikasi 87% serta waktu respon rata-rata 2,3 detik.

---

## 📂 Struktur Berkas
```text
├── index.html                     # Halaman landing page murni HTML5 Semantic
├── style.css                      # Styling minimalis, bersih, dan responsif
├── detika,+15814_page6-11.pdf     # Berkas jurnal referensi
└── README.md                      # Dokumentasi tugas & panduan repositori
```

---

## 🏷️ Penggunaan Elemen Semantic HTML5
- `<header>`: Judul landing page, metadata publikasi jurnal, dan navigasi.
- `<nav>`: Tautan navigasi internal (lompat ke section terkait).
- `<main>`: Pembungkus seluruh konten inti artikel dan analisis.
- `<section>`: Membagi konten menjadi beberapa bagian mandiri:
  - `#about`: Informasi umum, latar belakang, dan metodologi.
  - `#novelty`: Aspek kebaruan penelitian.
  - `#kekuatan`: Keunggulan teknis, metodologi, dan pengujian jurnal.
  - `#kekurangan`: Limitasi model NLU, cakupan dataset, dan evaluasi literatur.
  - `#anggota`: Tabel daftar nama dan NIM anggota kelompok.
- `<article>`: Membungkus unit bahasan mandiri di dalam setiap section.
- `<aside>`: Catatan pendukung, referensi berkas, dan panduan tugas.
- `<footer>`: Identitas penugasan, mata kuliah, dan hak cipta.

---

## 🚀 Panduan Pengumpulan & Git
1. Sesuaikan nama dan NIM seluruh anggota kelompok pada file `index.html` (bagian `<section id="anggota">`).
2. Buat repositori GitHub dengan format penamaan yang ditentukan dosen:
   ```bash
   PAW-Week2-Kelompok[no kelompok]-Kelas[alfabet]
   # Contoh: PAW-Week2-Kelompok3-KelasA
   ```
3. Lakukan inisialisasi git dan push:
   ```bash
   git init
   git add .
   git commit -m "feat: landing page semantic HTML jurnal tugas kelompok"
   git branch -M main
   git remote add origin https://github.com/[username-github]/[nama-repo].git
   git push -u origin main
   ```
4. Kumpulkan tautan repositori atau berkas sesuai instruksi di platform **MyKlass**.
