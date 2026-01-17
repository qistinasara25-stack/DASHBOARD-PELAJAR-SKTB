import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------
# 1. TETAPAN HALAMAN
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard Maklumat Pelajar",
    layout="wide",
    page_icon="🎓"
)

# ---------------------------------------------------------------------
# 2. PAUTAN DATA
# ---------------------------------------------------------------------
# Link CSV yang anda berikan tadi
DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSPy_LGvgSNp1hmoCe9l-ZZzLRfF1gw2doIQHblIrhVazrzEZ5bO7hrszMUjNlE2oRqoGaz_BFWqe9K/pub?output=csv"

# ---------------------------------------------------------------------
# 3. FUNGSI MEMUAT TURUN DATA
# ---------------------------------------------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(DATA_URL, dtype=str)
        # Bersihkan nama tajuk (buang jarak kosong di tepi)
        df.columns = df.columns.str.strip()
        # Isi tempat kosong dengan tanda '-'
        df = df.fillna("-")
        return df
    except Exception as e:
        st.error(f"Masalah memuat turun data: {e}")
        return None

# ---------------------------------------------------------------------
# 4. PAPARAN UTAMA
# ---------------------------------------------------------------------
def main():
    st.title("🎓 Sistem Maklumat Pelajar")
    st.markdown("---")

    df = load_data()

    if df is not None:
        # --- SIDEBAR: CARIAN ---
        st.sidebar.header("🔐 Carian Pelajar")
        st.sidebar.info("Masukkan No. Kad Pengenalan Pelajar")
        
        # Ruang input IC
        ic_input = st.sidebar.text_input("NO. KAD PENGENALAN (Tanpa -)", max_chars=12)
        search_btn = st.sidebar.button("🔍 Cari")

        # --- PROSES CARIAN ---
        if search_btn:
            if ic_input:
                # Cari pelajar berdasarkan NO. IC
                pelajar = df[df['NO. IC'] == ic_input]

                if not pelajar.empty:
                    data = pelajar.iloc[0] # Ambil data baris pertama
                    
                    st.success(f"✅ Rekod Ditemui: **{data.get('NAMA', '')}**")
                    
                    # Kita pecahkan kepada 5 Tab supaya kemas & semua info muat
                    t1, t2, t3, t4, t5 = st.tabs([
                        "👤 Profil Murid", 
                        "🏫 Persekolahan", 
                        "👨 Ayah / Penjaga 1", 
                        "👩 Ibu / Penjaga 2", 
                        "🏠 Alamat"
                    ])

                    # --- TAB 1: PROFIL MURID ---
                    with t1:
                        st.subheader("Maklumat Peribadi")
                        c1, c2 = st.columns(2)
                        c1.text_input("1. Nama Penuh", data.get('NAMA', '-'), disabled=True)
                        c2.text_input("No. Kad Pengenalan", data.get('NO. IC', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("2. Tarikh Lahir", data.get('TARIKH LAHIR', '-'), disabled=True)
                        c2.text_input("7. Jantina", data.get('JANTINA', '-'), disabled=True)
                        
                        c1, c2, c3 = st.columns(3)
                        c1.text_input("8. Kaum", data.get('KAUM', '-'), disabled=True)
                        c2.text_input("9. Agama", data.get('AGAMA', '-'), disabled=True)
                        c3.text_input("10. Warganegara", data.get('WARGANEGARA', '-'), disabled=True)
                        
                        st.text_input("11. Status Yatim", data.get('STATUS YATIM', '-'), disabled=True)

                    # --- TAB 2: PERSEKOLAHAN ---
                    with t2:
                        st.subheader("Maklumat Kelas & Sekolah")
                        c1, c2 = st.columns(2)
                        c1.text_input("5. Nama Kelas", data.get('NAMA KELAS', '-'), disabled=True)
                        c2.text_input("6. Jenis Kelas", data.get('JENIS KELAS', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("3. Tarikh Masuk Sekolah", data.get('TARIKH MASUK SEKOLAH', '-'), disabled=True)
                        c2.text_input("4. Tarikh Masuk Kelas", data.get('TARIKH MASUK KELAS', '-'), disabled=True)

                    # --- TAB 3: PENJAGA 1 ---
                    with t3:
                        st.subheader("Maklumat Penjaga 1 (Utama)")
                        st.text_input("12. Nama Penjaga 1", data.get('PENJAGA 1', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("13. No. KP Penjaga 1", data.get('NO. PENGENALAN PENJAGA 1', '-'), disabled=True)
                        c2.text_input("14. Hubungan", data.get('HUBUNGAN PENJAGA 1', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("19. No. Tel Penjaga 1", data.get('NO. TEL. BIMBIT PENJAGA 1', '-'), disabled=True)
                        c2.text_input("20. Bil. Tanggungan", data.get('TANGGUNGAN', '-'), disabled=True)
                        
                        st.markdown("##### Pekerjaan")
                        c1, c2 = st.columns(2)
                        c1.text_input("15. Pekerjaan", data.get('PEKERJAAN PENJAGA 1', '-'), disabled=True)
                        c2.text_input("16. Status Kerja", data.get('STATUS KERJA PENJAGA 1', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("17. Nama Majikan", data.get('NAMA MAJIKAN PENJAGA 1', '-'), disabled=True)
                        c2.text_input("18. Pendapatan (RM)", data.get('PENDAPATAN PENJAGA 1', '-'), disabled=True)

                    # --- TAB 4: PENJAGA 2 ---
                    with t4:
                        st.subheader("Maklumat Penjaga 2")
                        st.text_input("21. Nama Penjaga 2", data.get('PENJAGA 2', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("22. No. KP Penjaga 2", data.get('NO. PENGENALAN PENJAGA 2', '-'), disabled=True)
                        c2.text_input("23. Hubungan", data.get('HUBUNGAN PENJAGA 2', '-'), disabled=True)
                        
                        st.text_input("28. No. Tel Penjaga 2", data.get('NO. TEL. BIMBIT PENJAGA 2', '-'), disabled=True)
                        
                        st.markdown("##### Pekerjaan")
                        c1, c2 = st.columns(2)
                        c1.text_input("24. Pekerjaan", data.get('PEKERJAAN PENJAGA 2', '-'), disabled=True)
                        c2.text_input("25. Status Kerja", data.get('STATUS KERJA PENJAGA 2', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("26. Nama Majikan", data.get('NAMA MAJIKAN PENJAGA 2', '-'), disabled=True)
                        c2.text_input("27. Pendapatan (RM)", data.get('PENDAPATAN PENJAGA 2', '-'), disabled=True)

                    # --- TAB 5: ALAMAT ---
                    with t5:
                        st.subheader("Lokasi Tempat Tinggal")
                        st.text_area("29. Alamat Rumah", data.get('ALAMAT', '-'), height=100, disabled=True)
                        
                        c1, c2, c3 = st.columns(3)
                        c1.text_input("30. Poskod", data.get('POSKOD', '-'), disabled=True)
                        c2.text_input("31. Daerah", data.get('DAERAH', '-'), disabled=True)
                        c3.text_input("32. Negeri", data.get('NEGERI', '-'), disabled=True)

                else:
                    st.error(f"❌ Maaf, tiada rekod dijumpai untuk No. IC: {ic_input}")
            else:
                st.warning("⚠️ Sila masukkan No. IC Pelajar.")
        else:
            st.info("👈 Sila masukkan No. IC di menu sebelah kiri.")

if __name__ == "__main__":
    main()
