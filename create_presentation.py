#!/usr/bin/env python3
"""
Script to generate PowerPoint presentation for PAW Tugas Kelompok:
Arsitektur Diagram, Use Case, Activity & Sequence Diagram, Class Diagram, and ERD.
Studi Kasus: UMKM Catering Bu Sumiyati (CateringBot AI)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Palette
    C_NAVY = RGBColor(15, 23, 42)          # #0F172A
    C_PRIMARY = RGBColor(30, 58, 138)       # #1E3A8A
    C_BLUE = RGBColor(2, 132, 199)          # #0284C7
    C_SKY = RGBColor(56, 189, 248)          # #38BDF8
    C_AMBER = RGBColor(245, 158, 11)        # #F59E0B
    C_EMERALD = RGBColor(16, 185, 129)      # #10B981
    C_PURPLE = RGBColor(126, 34, 206)       # #7E22CE
    C_SLATE_BG = RGBColor(248, 250, 252)    # #F8FAFC
    C_CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF
    C_CARD_BORDER = RGBColor(226, 232, 240) # #E2E8F0
    C_TEXT_MAIN = RGBColor(30, 41, 59)      # #1E293B
    C_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B
    C_TEXT_LIGHT = RGBColor(248, 250, 252)  # #F8FAFC

    TOTAL_SLIDES = 12

    def add_header(slide, tag_text, title_text, dark=False):
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_SKY if dark else C_BLUE

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_TEXT_LIGHT if dark else C_NAVY

    def add_footer(slide, current_page, dark=False):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.3))
        tf = footer_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"Pemrograman Berbasis Web (PAW) • Kelompok 3 (Kelas A) — CateringBot AI Bu Sumiyati                    Slide {current_page} dari {TOTAL_SLIDES}"
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(148, 163, 184)

    def set_slide_bg(slide, dark=False):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_NAVY if dark else C_SLATE_BG
        bg.line.fill.background()
        return bg

    # =========================================================================
    # SLIDE 1: COVER SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, dark=True)

    bar1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.9), Inches(3.6), Inches(0.35))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = RGBColor(30, 58, 138)
    bar1.line.color.rgb = C_SKY
    p_b = bar1.text_frame.paragraphs[0]
    p_b.text = "TUGAS REKAYASA PERANGKAT LUNAK & PAW"
    p_b.font.size = Pt(9.5)
    p_b.font.bold = True
    p_b.font.color.rgb = C_SKY
    p_b.alignment = PP_ALIGN.CENTER

    tbox1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(2.2))
    tf1 = tbox1.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Rancang Bangun Aplikasi Chatbot pada Catering Makanan"
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Pemodelan Diagram Sistem: Arsitektur, Use Case, Activity, Sequence, Class & ERD"
    p1_sub.font.size = Pt(17)
    p1_sub.font.bold = True
    p1_sub.font.color.rgb = C_AMBER
    p1_sub.space_before = Pt(6)

    p1_desc = tf1.add_paragraph()
    p1_desc.text = "Studi Kasus: UMKM Catering Bu Sumiyati (Jurnal Detika, Vol. 6 No. 1, Desember 2025)"
    p1_desc.font.size = Pt(13)
    p1_desc.font.color.rgb = RGBColor(203, 213, 225)
    p1_desc.space_before = Pt(6)

    # Member Cards
    members = [
        ("Ilham Fadhilah", "20200140100", "Arsitektur & Integrasi Sistem"),
        ("Danar Rohman Rozaqi", "20240140233", "Use Case & Activity Flow"),
        ("M.Ikhlasul", "20240140234", "Sequence & Class Diagram"),
        ("Anandya Arlys F", "20240140002", "Entity Relationship Diagram")
    ]
    card_w, card_h = Inches(2.7), Inches(1.8)
    for i, (name, nim, role) in enumerate(members):
        c_x = Inches(0.8) + i * (card_w + Inches(0.3))
        c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_x, Inches(4.5), card_w, card_h)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor(30, 41, 59)
        c.line.color.rgb = RGBColor(51, 65, 85)
        tf = c.text_frame
        tf.word_wrap = True
        p_n = tf.paragraphs[0]
        p_n.text = name
        p_n.font.size = Pt(13)
        p_n.font.bold = True
        p_n.font.color.rgb = RGBColor(255, 255, 255)
        p_nim = tf.add_paragraph()
        p_nim.text = f"NIM: {nim}"
        p_nim.font.size = Pt(11)
        p_nim.font.color.rgb = C_SKY
        p_nim.space_before = Pt(3)
        p_r = tf.add_paragraph()
        p_r.text = role
        p_r.font.size = Pt(9.5)
        p_r.font.color.rgb = RGBColor(148, 163, 184)
        p_r.space_before = Pt(5)

    add_footer(s1, 1, dark=True)

    # =========================================================================
    # SLIDE 2: LATAR BELAKANG & ANALISIS PERMASALAHAN
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Konteks Penelitian & Analisis Kebutuhan", "Latar Belakang Masalah & Urgensi Solusi Chatbot UMKM")

    boxes_s2 = [
        ("🔴 Permasalahan UMKM Katering", RGBColor(185, 28, 28), [
            "Tingginya beban kerja staf dalam melayani pertanyaan berulang (menu, harga, jadwal) secara manual.",
            "Waktu respon lambat saat jam sibuk berakibat hilangnya 40% calon pelanggan potensial.",
            "Pencatatan pesanan manual rentan salah input jumlah porsi, alamat, maupun tanggal acara.",
            "Pelanggan enggan mengunduh aplikasi berukuran besar hanya untuk memesan makanan sesekali."
        ]),
        ("💡 Solusi yang Diajukan (CateringBot)", C_BLUE, [
            "Aplikasi Chatbot Web 'Zero-Installation' yang diakses langsung melalui peramban web smartphone/desktop.",
            "Arsitektur Hibrida: Rule-Based untuk kepastian formulir order dan NLP Naïve Bayes untuk percakapan bebas.",
            "Otomasi Validasi: Pengecekan minimal porsi, jadwal pengantaran, dan estimasi biaya secara otomatis.",
            "Integrasi WhatsApp API Gateway untuk konfirmasi invoice instan ke dapur pengelola katering."
        ]),
        ("📊 Hasil Pengujian Teruji (Riset)", C_EMERALD, [
            "Akurasi Intent 87%: Teruji melalui Blackbox Testing & Confusion Matrix pada domain katering.",
            "Waktu Respon 2,3 Detik: Waktu olah pesan rata-rata sangat cepat memangkas antrean manual.",
            "Kenaikan Efisiensi 60%: Mempercepat siklus pemesanan makanan dari awal hingga konfirmasi.",
            "Penurunan Beban CS 40%: Staf UMKM Bu Sumiyati dapat lebih fokus pada mutu masakan dan produksi."
        ])
    ]
    for i, (title, col, pts) in enumerate(boxes_s2):
        bx = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + i * Inches(4.0), Inches(1.5), Inches(3.7), Inches(5.1))
        bx.fill.solid()
        bx.fill.fore_color.rgb = C_CARD_BG
        bx.line.color.rgb = C_CARD_BORDER
        tf = bx.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13.5)
        p_t.font.bold = True
        p_t.font.color.rgb = col
        for pt in pts:
            p_p = tf.add_paragraph()
            p_p.text = f"• {pt}"
            p_p.font.size = Pt(10.5)
            p_p.font.color.rgb = C_TEXT_MAIN
            p_p.space_before = Pt(8)

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: ARSITEKTUR DIAGRAM
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Diagram 1 • Arsitektur Perangkat Lunak", "Arsitektur Sistem 4-Lapisan (Layered Architecture)")

    # Left: Visual Diagram Image
    img_arch = "images/system-architecture.jpg"
    if os.path.exists(img_arch):
        s3.shapes.add_picture(img_arch, Inches(0.8), Inches(1.5), width=Inches(5.7), height=Inches(5.0))

    # Right: 4 Layers Breakdown Cards
    layers = [
        ("1. User Interface (UI) Layer", C_PRIMARY, "Widget Chatbot peramban web responsif (HTML5/CSS3) & Dashboard manajemen admin Bu Sumiyati."),
        ("2. Processing Layer (AI Engine)", C_BLUE, "Hybrid NLP: Naïve Bayes Classifier + TF-IDF Vectorizer untuk intent detection dan Rule-Based untuk form validation."),
        ("3. Data Layer (Penyimpanan)", C_PURPLE, "Database relasional untuk katalog menu (nasi kotak, prasmanan), basis pengetahuan (FAQ), dan transaksi pesanan."),
        ("4. Integration Layer (API Gateway)", C_EMERALD, "Jembatan API ke WhatsApp Business API dan notifikasi webhook untuk finalisasi pesanan instan ke pengelola.")
    ]
    for i, (l_title, l_col, l_desc) in enumerate(layers):
        c_y = Inches(1.5) + i * Inches(1.25)
        cd = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), c_y, Inches(5.7), Inches(1.12))
        cd.fill.solid()
        cd.fill.fore_color.rgb = C_CARD_BG
        cd.line.color.rgb = l_col
        cd.line.width = Pt(1.5)
        tf = cd.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = l_title
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = l_col
        p_d = tf.add_paragraph()
        p_d.text = l_desc
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = C_TEXT_MAIN
        p_d.space_before = Pt(3)

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: USE CASE DIAGRAM (VISUAL)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Diagram 2A • Pemodelan Fungsionalitas", "Use Case Diagram: Interaksi Aktor & Sistem Chatbot")

    img_uc = "images/use-case-diagram.jpg"
    if os.path.exists(img_uc):
        s4.shapes.add_picture(img_uc, Inches(0.8), Inches(1.5), width=Inches(6.4), height=Inches(5.0))

    # Right: Description Cards
    r_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.0))
    r_card.fill.solid()
    r_card.fill.fore_color.rgb = C_CARD_BG
    r_card.line.color.rgb = C_CARD_BORDER
    tf = r_card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Identifikasi Aktor & Batasan Sistem"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    uc_details = [
        ("Aktor 1: Pelanggan (Customer)", C_PRIMARY, "Pengguna akhir yang mengakses web tanpa login/instalasi. Melakukan konsultasi paket katering, cek tanggal acara, input formulir pesanan, dan terima invoice."),
        ("Aktor 2: Admin Katering Bu Sumiyati", C_EMERALD, "Pengelola operasional UMKM yang mengelola katalog menu, memvalidasi ketersediaan jadwal dapur, konfirmasi pembayaran, serta update template respon bot."),
        ("Fitur Utama Terpetakan:", C_BLUE, "1. Konsultasi Menu & Rekomendasi (NLP)\n2. Cek Ketersediaan Jadwal Acara\n3. Pemesanan Nasi Kotak & Prasmanan\n4. Kalkulasi Total Biaya & Diskon Porsi\n5. Penerusan Invoice via WhatsApp API\n6. Manajemen Menu & Laporan Transaksi")
    ]
    for h_txt, col, d_txt in uc_details:
        p_h = tf.add_paragraph()
        p_h.text = h_txt
        p_h.font.size = Pt(11.5)
        p_h.font.bold = True
        p_h.font.color.rgb = col
        p_h.space_before = Pt(10)
        p_d = tf.add_paragraph()
        p_d.text = d_txt
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = C_TEXT_MAIN
        p_d.space_before = Pt(2)

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: USE CASE SPESIFIKASI SKENARIO UTAMA
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Diagram 2B • Spesifikasi Fungsionalitas", "Tabel Deskripsi Skenario Use Case Utama")

    uc_table_data = [
        ("UC-01", "Konsultasi Menu & Rekomendasi", "Pelanggan", "Pelanggan mengetik pertanyaan variatif seputar rekomendasi menu katering.", "NLP Naïve Bayes mengenali intent pertanyaan dan membalas dengan rekomendasi paket."),
        ("UC-02", "Pemesanan & Reservasi Menu", "Pelanggan", "Pelanggan memilih paket (nasi kotak/prasmanan/tumpeng) dan mengisi jumlah porsi.", "Sistem memvalidasi jumlah porsi minimum dan menampilkan kalkulasi total biaya."),
        ("UC-03", "Cek Jadwal & Tanggal Acara", "Pelanggan", "Pelanggan memasukkan tanggal pelaksanaan acara hajatan / syukuran.", "Sistem memeriksa slot produksi katering pada tanggal tersebut apakah masih tersedia."),
        ("UC-04", "Dispatch Notifikasi WhatsApp", "Sistem / WA", "Data pesanan telah lengkap dan divalidasi oleh pelanggan.", "Sistem menyusun payload ringkasan pesanan dan mengirimkannya ke WhatsApp admin UMKM."),
        ("UC-05", "Konfirmasi Pesanan & Pembayaran", "Admin", "Admin menerima pesan WhatsApp berisi rincian pesanan dan bukti DP pelanggan.", "Admin mengunci jadwal di kalender dapur dan mengubah status pesanan menjadi 'Dikonfirmasi'.")
    ]

    # Create table
    tbl_shape = s5.shapes.add_table(6, 5, Inches(0.8), Inches(1.5), Inches(11.7), Inches(4.8))
    table = tbl_shape.table
    col_widths = [Inches(1.1), Inches(2.6), Inches(1.3), Inches(3.3), Inches(3.4)]
    for idx, w in enumerate(col_widths):
        table.columns[idx].width = w

    headers = ["Kode", "Nama Use Case", "Aktor", "Skenario Alur Utama", "Hasil Akhir / Post-condition"]
    for idx, text in enumerate(headers):
        cell = table.cell(0, idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(uc_table_data):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(255, 255, 255) if row_idx % 2 == 0 else RGBColor(248, 250, 252)
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_MAIN
            if col_idx in [0, 2]:
                p.alignment = PP_ALIGN.CENTER
                p.font.bold = True

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: ACTIVITY DIAGRAM
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Diagram 3A • Pemodelan Perilaku Sistem", "Activity Diagram: Alur Eksekusi Konsultasi & Pemesanan")

    # 4 Swimlane Columns
    lanes = [
        ("PELANGGAN", Inches(0.8), Inches(2.8), C_PRIMARY),
        ("CHATBOT UI", Inches(3.7), Inches(2.8), C_BLUE),
        ("PROCESSING (NLP / RULE)", Inches(6.6), Inches(2.9), C_PURPLE),
        ("ADMIN & WHATSAPP GATEWAY", Inches(9.6), Inches(2.9), C_EMERALD)
    ]
    for l_title, lx, lw, col in lanes:
        hl = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, lx, Inches(1.5), lw, Inches(0.4))
        hl.fill.solid()
        hl.fill.fore_color.rgb = col
        hl.line.fill.background()
        tf = hl.text_frame
        p = tf.paragraphs[0]
        p.text = l_title
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

        bl = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, lx, Inches(1.9), lw, Inches(4.8))
        bl.fill.solid()
        bl.fill.fore_color.rgb = C_CARD_BG
        bl.line.color.rgb = C_CARD_BORDER

    def add_act_node(text, x, y, w=Inches(2.4), h=Inches(0.65), shape=MSO_SHAPE.ROUNDED_RECTANGLE, bcol=C_BLUE):
        b = s6.shapes.add_shape(shape, x, y, w, h)
        b.fill.solid()
        b.fill.fore_color.rgb = RGBColor(241, 245, 249)
        b.line.color.rgb = bcol
        b.line.width = Pt(1.5)
        tf = b.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_MAIN
        p.alignment = PP_ALIGN.CENTER
        return b

    # Start
    st = s6.shapes.add_shape(MSO_SHAPE.OVAL, Inches(2.0), Inches(2.05), Inches(0.3), Inches(0.3))
    st.fill.solid()
    st.fill.fore_color.rgb = C_NAVY
    st.line.fill.background()

    # Steps
    add_act_node("1. Buka Web & Ketik Pertanyaan / Pesanan", Inches(1.0), Inches(2.5))
    add_act_node("2. Teruskan Input Teks ke Processing Engine", Inches(3.9), Inches(2.5))
    add_act_node("3. Tokenisasi, TF-IDF & Klasifikasi Naïve Bayes", Inches(6.8), Inches(2.5))
    add_act_node("Intent = Order?", Inches(6.8), Inches(3.3), h=Inches(0.5), shape=MSO_SHAPE.HEXAGON, bcol=C_AMBER)
    add_act_node("Ambil Jawaban FAQ dari Basis Pengetahuan", Inches(9.8), Inches(3.3))
    add_act_node("4. Tampilkan Form Pemesanan Terstruktur", Inches(3.9), Inches(4.1))
    add_act_node("5. Isi Form: Porsi, Tgl Acara & Lokasi", Inches(1.0), Inches(4.1))
    add_act_node("6. Validasi Input & Hitung Total Biaya", Inches(6.8), Inches(4.1))
    add_act_node("7. Susun Format Pesanan & Kirim via WhatsApp API", Inches(9.8), Inches(4.9))
    add_act_node("8. Admin Validasi Jadwal Dapur & Kirim Konfirmasi", Inches(9.8), Inches(5.7))
    add_act_node("9. Pelanggan Menerima Rincian Invoice di WA", Inches(1.0), Inches(5.7))

    # End
    ed1 = s6.shapes.add_shape(MSO_SHAPE.OVAL, Inches(2.0), Inches(6.45), Inches(0.3), Inches(0.3))
    ed1.fill.solid()
    ed1.fill.fore_color.rgb = C_CARD_BG
    ed1.line.color.rgb = C_NAVY
    ed2 = s6.shapes.add_shape(MSO_SHAPE.OVAL, Inches(2.04), Inches(6.49), Inches(0.22), Inches(0.22))
    ed2.fill.solid()
    ed2.fill.fore_color.rgb = C_NAVY
    ed2.line.fill.background()

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: SEQUENCE DIAGRAM (VISUAL)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Diagram 3B • Pemodelan Interaksi Objek", "Sequence Diagram: Alur Eksekusi Pemesanan Makanan Realtime")

    img_seq = "images/sequence-diagram.jpg"
    if os.path.exists(img_seq):
        s7.shapes.add_picture(img_seq, Inches(0.8), Inches(1.5), width=Inches(6.4), height=Inches(5.0))

    # Right: Narrative of message exchange
    r_seq = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.0))
    r_seq.fill.solid()
    r_seq.fill.fore_color.rgb = C_CARD_BG
    r_seq.line.color.rgb = C_CARD_BORDER
    tf = r_seq.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Penjelasan Rangkaian Interaksi Objek"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    seq_steps = [
        ("1. kirimPesan()", "Pelanggan menginput teks percakapan di antarmuka browser ChatWidget UI."),
        ("2. parseTeks()", "ChatWidget mengirimkan raw text ke DialogManager untuk normalisasi teks."),
        ("3. classifyIntent()", "DialogManager memanggil NLPClassifier (Naïve Bayes + TF-IDF) untuk mengenali maksud."),
        ("4. queryMenuHarga()", "Jika intent adalah pemesanan, sistem mengambil daftar menu & harga dari Database."),
        ("5. renderFormOrder()", "ChatWidget menampilkan formulir pemilihan porsi & tanggal acara terstruktur."),
        ("6. submitOrder()", "Pelanggan mengirim data pesanan lengkap yang sudah tervalidasi."),
        ("7. simpanPesanan()", "DialogManager menyimpan transaksi pesanan ke Database relasional."),
        ("8. sendWhatsAppAlert()", "Sistem memanggil WhatsAppGateway untuk meneruskan invoice resmi ke Admin.")
    ]
    for step_title, step_desc in seq_steps:
        p_s = tf.add_paragraph()
        p_s.text = f"{step_title}: {step_desc}"
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = C_TEXT_MAIN
        p_s.space_before = Pt(4)

    add_footer(s7, 7)

    # =========================================================================
    # SLIDE 8: CLASS DIAGRAM (VISUAL)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "Diagram 4A • Pemodelan Struktural Objek", "Class Diagram: Struktur Kelas & Relasi Berorientasi Objek")

    img_cls = "images/class-diagram.jpg"
    if os.path.exists(img_cls):
        s8.shapes.add_picture(img_cls, Inches(0.8), Inches(1.5), width=Inches(6.4), height=Inches(5.0))

    # Right: Analysis of Classes
    r_cls = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.0))
    r_cls.fill.solid()
    r_cls.fill.fore_color.rgb = C_CARD_BG
    r_cls.line.color.rgb = C_CARD_BORDER
    tf = r_cls.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Analisis Struktur Objek & Multiplicity"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    cls_insights = [
        ("Entitas Pelanggan & Pesanan", C_PRIMARY, "Pelanggan memiliki relasi 1 to 1..* dengan Pesanan (seorang pelanggan dapat membuat banyak pesanan katering)."),
        ("Komposisi Pesanan & Detail", C_AMBER, "Pesanan memiliki relasi komposisi 1 to 1..* dengan DetailPesanan (setiap pesanan terdiri dari satu atau lebih menu makanan)."),
        ("Asosiasi Menu & Kategori", C_PURPLE, "KategoriMenu mengelompokkan MenuKatering dengan relasi 1 to 1..* (contoh: Nasi Kotak, Prasmanan, Tumpeng, Snack Box)."),
        ("Integrasi Engine & Layanan WA", C_BLUE, "ChatbotEngine berasosiasi dengan WhatsAppService untuk memicu webhook notifikasi setelah pesanan berhasil divalidasi.")
    ]
    for c_title, col, c_desc in cls_insights:
        p_h = tf.add_paragraph()
        p_h.text = f"• {c_title}"
        p_h.font.size = Pt(11)
        p_h.font.bold = True
        p_h.font.color.rgb = col
        p_h.space_before = Pt(8)
        p_d = tf.add_paragraph()
        p_d.text = f"  {c_desc}"
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = C_TEXT_MAIN
        p_d.space_before = Pt(2)

    add_footer(s8, 8)

    # =========================================================================
    # SLIDE 9: CLASS DIAGRAM - RINCIAN ATRIBUT & METODE
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "Diagram 4B • Spesifikasi Kelas Sistem", "Kamus Detail Atribut & Metode Class Diagram")

    cls_table_data = [
        ("Pelanggan", "- id_pelanggan: int\n- nama: string\n- nomor_wa: string\n- alamat: string", "+ register(): bool\n+ updateProfil(): void\n+ kirimPesan(teks): void", "Mewakili entitas konsumen pemesan katering."),
        ("Pesanan", "- id_pesanan: int\n- tgl_pesanan: date\n- total_harga: decimal\n- status: string", "+ buatPesanan(): Order\n+ updateStatus(): void\n+ hitungTotal(): decimal", "Menyimpan header transaksi pemesanan makanan."),
        ("DetailPesanan", "- id_detail: int\n- kuantitas: int\n- harga_satuan: decimal\n- menu: MenuKatering", "+ getSubtotal(): decimal\n+ validasiMinPorsi(): bool", "Baris rincian item menu dan kuantitas per pesanan."),
        ("MenuKatering", "- id_menu: int\n- nama_menu: string\n- deskripsi: text\n- harga: decimal", "+ getDetailMenu(): dict\n+ updateHarga(): void\n+ cekStok(): bool", "Katalog produk makanan katering yang ditawarkan."),
        ("ChatbotEngine", "- id_chatbot: int\n- threshold: float\n- model_path: string", "+ prosesPesan(input): str\n+ classifyIntent(): str\n+ responPesan(): str", "Engine pemrosesan NLP Naïve Bayes & TF-IDF."),
        ("WhatsAppService", "- api_key: string\n- endpoint_url: string\n- status_service: enum", "+ kirimPesan(payload): bool\n+ sendOrderAlert(): void\n+ handleInbound(): void", "Gateway integrasi notifikasi ke nomor WhatsApp admin.")
    ]

    tbl_s9 = s9.shapes.add_table(7, 4, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.0))
    t9 = tbl_s9.table
    widths9 = [Inches(1.8), Inches(3.6), Inches(3.5), Inches(2.8)]
    for idx, w in enumerate(widths9):
        t9.columns[idx].width = w

    h9 = ["Nama Kelas", "Atribut (Properties)", "Metode (Operations)", "Deskripsi Tanggung Jawab"]
    for idx, text in enumerate(h9):
        cell = t9.cell(0, idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(cls_table_data):
        for col_idx, text in enumerate(row_data):
            cell = t9.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(255, 255, 255) if row_idx % 2 == 0 else RGBColor(248, 250, 252)
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(8.5)
            p.font.color.rgb = C_TEXT_MAIN
            if col_idx == 0:
                p.font.bold = True
                p.alignment = PP_ALIGN.CENTER

    add_footer(s9, 9)

    # =========================================================================
    # SLIDE 10: ENTITY RELATIONSHIP DIAGRAM (ERD) - VISUAL
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "Diagram 5A • Pemodelan Basis Data Relasional", "Entity Relationship Diagram (ERD) Skema Database Katering")

    img_erd = "images/erd-diagram.jpg"
    if os.path.exists(img_erd):
        s10.shapes.add_picture(img_erd, Inches(0.8), Inches(1.5), width=Inches(6.4), height=Inches(5.0))

    # Right: ERD Relational Insights
    r_erd = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.0))
    r_erd.fill.solid()
    r_erd.fill.fore_color.rgb = C_CARD_BG
    r_erd.line.color.rgb = C_CARD_BORDER
    tf = r_erd.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Pemodelan Relasi & Integritas Data"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    erd_relations = [
        ("PELANGGAN (1) ── (N) PESANAN", C_PRIMARY, "Setiap pelanggan dapat melakukan banyak pesanan. Foreign Key: 'id_pelanggan' di tabel PESANAN menjamin integritas riwayat transaksi pembeli."),
        ("PESANAN (1) ── (N) DETAIL_PESANAN", C_AMBER, "Satu transaksi pesanan dipecah menjadi beberapa item menu melalui tabel DETAIL_PESANAN untuk mendukung variasi menu dan porsi."),
        ("MENU_MAKANAN (1) ── (N) DETAIL_PESANAN", C_EMERALD, "Satu menu makanan dapat dipesan oleh banyak pesanan yang berbeda. Memiliki relasi Many-to-Many antara PESANAN dan MENU."),
        ("KATEGORI_MENU (1) ── (N) MENU_MAKANAN", C_PURPLE, "Kategori memudahkan pengelompokan jenis hidangan (prasmanan, tumpeng, bento/box) untuk katalog chatbot."),
        ("PELANGGAN (1) ── (N) RIWAYAT_CHAT", C_BLUE, "Mencatat setiap sesi percakapan, intent yang terdeteksi, dan respon bot untuk keperluan evaluasi model NLP berkala.")
    ]
    for r_title, col, r_desc in erd_relations:
        p_h = tf.add_paragraph()
        p_h.text = f"• {r_title}"
        p_h.font.size = Pt(10.5)
        p_h.font.bold = True
        p_h.font.color.rgb = col
        p_h.space_before = Pt(6)
        p_d = tf.add_paragraph()
        p_d.text = f"  {r_desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = C_TEXT_MAIN
        p_d.space_before = Pt(2)

    add_footer(s10, 10)

    # =========================================================================
    # SLIDE 11: ERD - SKEMA TABEL & KAMUS DATA (NORMALISASI)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11)
    add_header(s11, "Diagram 5B • Struktur Fisik Basis Data", "Kamus Data Fisik & Normalisasi Database (3NF)")

    erd_tables = [
        ("PELANGGAN", "id_pelanggan (INT - PK)", "-", "nama (VARCHAR), no_hp (VARCHAR), alamat (TEXT), email (VARCHAR)", "Master data profil konsumen pemesan."),
        ("PESANAN", "id_pesanan (INT - PK)", "id_pelanggan (FK)", "tgl_pesanan (DATE), tgl_acara (DATE), total_harga (DECIMAL), status (VARCHAR)", "Header transaksi pesanan katering."),
        ("DETAIL_PESANAN", "id_detail (INT - PK)", "id_pesanan (FK), id_menu (FK)", "quantity (INT), harga_satuan (DECIMAL), subtotal (DECIMAL)", "Tabel penghubung Many-to-Many pesanan & menu."),
        ("MENU_MAKANAN", "id_menu (INT - PK)", "id_kategori (FK)", "nama_menu (VARCHAR), deskripsi (TEXT), harga (DECIMAL), stok (INT)", "Master data hidangan dan harga katering."),
        ("KATEGORI_MENU", "id_kategori (INT - PK)", "-", "nama_kategori (VARCHAR), deskripsi (TEXT)", "Klasifikasi paket (Nasi Kotak, Prasmanan, dll)."),
        ("RIWAYAT_CHAT", "id_chat (INT - PK)", "id_pelanggan (FK)", "pesan (TEXT), respon_bot (TEXT), intent (VARCHAR), tgl_kirim (DATETIME)", "Log interaksi percakapan NLU pelanggan."),
        ("ADMIN", "id_admin (INT - PK)", "-", "nama (VARCHAR), username (VARCHAR), password_hash (VARCHAR), level (VARCHAR)", "Data otentikasi pengelola katering Bu Sumiyati.")
    ]

    tbl_s11 = s11.shapes.add_table(8, 5, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.0))
    t11 = tbl_s11.table
    widths11 = [Inches(1.8), Inches(2.2), Inches(2.0), Inches(3.7), Inches(2.0)]
    for idx, w in enumerate(widths11):
        t11.columns[idx].width = w

    h11 = ["Nama Tabel", "Primary Key (PK)", "Foreign Key (FK)", "Atribut Tambahan", "Fungsi Tabel"]
    for idx, text in enumerate(h11):
        cell = t11.cell(0, idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_PRIMARY
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    for row_idx, row_data in enumerate(erd_tables):
        for col_idx, text in enumerate(row_data):
            cell = t11.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(255, 255, 255) if row_idx % 2 == 0 else RGBColor(248, 250, 252)
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(8.5)
            p.font.color.rgb = C_TEXT_MAIN
            if col_idx in [0, 1]:
                p.font.bold = True

    add_footer(s11, 11)

    # =========================================================================
    # SLIDE 12: KESIMPULAN & TAUTAN PROYEK
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12, dark=True)
    add_header(s12, "Penutup & Rekapitulasi Penugasan", "Kesimpulan Pemodelan Sistem & Tautan Proyek", dark=True)

    # Left: Conclusion
    c_box = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.0))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    c_box.line.color.rgb = RGBColor(51, 65, 85)
    tf_c = c_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = "🎯 Kesimpulan Pemodelan Sistem"
    p_c.font.size = Pt(15)
    p_c.font.bold = True
    p_c.font.color.rgb = C_SKY

    bullets_close = [
        "Arsitektur 4-Lapisan memastikan skalabilitas dan isolasi kegagalan antar antarmuka web, pemrosesan NLP, dan gateway WhatsApp.",
        "Use Case & Activity Diagram membuktikan alur pemesanan makanan terotomasi dalam 3 langkah mudah tanpa friksi unduh aplikasi.",
        "Sequence Diagram mendokumentasikan koordinasi komponen dengan latensi rata-rata 2,3 detik dan akurasi intent 87%.",
        "Class Diagram & ERD menghasilkan arsitektur data terstruktur ternormalisasi (3NF) untuk menangani pesanan, menu, dan log chat.",
        "Sistem ini siap diimplementasikan untuk meningkatkan efisiensi operasional UMKM katering hingga 60%."
    ]
    for b in bullets_close:
        p_b = tf_c.add_paragraph()
        p_b.text = f"✔ {b}"
        p_b.font.size = Pt(10.5)
        p_b.font.color.rgb = RGBColor(226, 232, 240)
        p_b.space_before = Pt(8)

    # Right: Project Links
    l_box = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.0))
    l_box.fill.solid()
    l_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    l_box.line.color.rgb = RGBColor(51, 65, 85)
    tf_l = l_box.text_frame
    tf_l.word_wrap = True
    p_l = tf_l.paragraphs[0]
    p_l.text = "🌐 Tautan Repositori & Live Deployment"
    p_l.font.size = Pt(15)
    p_l.font.bold = True
    p_l.font.color.rgb = C_AMBER

    links_list = [
        ("Live Website (GitHub Pages):", "https://zowiedrid.github.io/PAW-Week2-Kelompok3-KelasA/"),
        ("Repositori Kode (GitHub):", "https://github.com/zowiedrid/PAW-Week2-Kelompok3-KelasA"),
        ("Landing Page Jurnal (Tugas 2):", ".../landing-jurnal.html"),
        ("Landing Page Layanan Katering:", ".../landing-layanan.html"),
        ("Jurnal Referensi (DOI):", "10.24176/detika.v6i1.15814 (Detika 2025)")
    ]
    for title, url in links_list:
        p_t = tf_l.add_paragraph()
        p_t.text = f"• {title}"
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = RGBColor(255, 255, 255)
        p_t.space_before = Pt(8)
        p_u = tf_l.add_paragraph()
        p_u.text = f"   {url}"
        p_u.font.size = Pt(9.5)
        p_u.font.color.rgb = C_SKY
        p_u.space_before = Pt(2)

    p_end = tf_l.add_paragraph()
    p_end.text = "Sekian dan terima kasih. Presentasi siap didemokan!"
    p_end.font.size = Pt(12)
    p_end.font.bold = True
    p_end.font.color.rgb = C_EMERALD
    p_end.space_before = Pt(16)
    p_end.alignment = PP_ALIGN.CENTER

    add_footer(s12, 12, dark=True)

    # Save output
    out_file = "Presentasi_Diagram_Sistem_Kelompok3.pptx"
    prs.save(out_file)
    print(f"Successfully generated {TOTAL_SLIDES}-slide presentation: {out_file}")

if __name__ == "__main__":
    build_presentation()
