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
# 2. PAUTAN DATA (CSV BARU)
# ---------------------------------------------------------------------
DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSPy_LGvgSNp1hmoCe9l-ZZzLRfF1gw2doIQHblIrhVazrzEZ5bO7hrszMUjNlE2oRqoGaz_BFWqe9K/pub?output=csv"

# ---------------------------------------------------------------------
# 3. FUNGSI MEMUAT TURUN DATA
# ---------------------------------------------------------------------
@st.cache_data
def load_data():
    try:
        # Baca CSV dan pastikan semua data dibaca sebagai text (string)
        df = pd.read_csv(DATA_URL, dtype=str)
        # Buang jarak kosong pada nama tajuk (header)
        df.columns = df.columns.str.strip()
        # Gantikan kotak kosong dengan tanda '-'
        df = df.fillna("-")
        return df
    except Exception as e:
        st.error(f"Gagal memuat turun data. Ralat: {e}")
        return None

# ---------------------------------------------------------------------
# 4. PAPARAN UTAMA (MAIN)
# ---------------------------------------------------------------------
def main():
    st.title("🎓 Sistem Maklumat Pelajar")
    st.write("Sila masukkan No. Kad Pengenalan untuk carian.")
    st.markdown("---")

    # Muat data di belakang tabir
    df = load_data()

    if df is not None:
        # --- SIDEBAR (KIRI) UNTUK CARIAN ---
        st.sidebar.header("🔐 Carian")
        st.sidebar.info("Masukkan No. IC tanpa sengkang (contoh: 090101010001)")
        
        ic_input = st.sidebar.text_input("NO. IC PELAJAR", max_chars=12)
        search_btn = st.sidebar.button("🔍 Semak Maklumat")

        # --- LOGIK BILA BUTANG DITEKAN ---
        if search_btn:
            if ic_input:
                # Cari pelajar dalam database
                # Pastikan ejaan 'NO. IC' sama sebiji dengan dalam Excel/CSV
                pelajar = df[df['NO. IC'] == ic_input]

                if not pelajar.empty:
                    # Ambil data pertama yang jumpa
                    data = pelajar.iloc[0]
                    
                    st.success(f"✅ Rekod Dijumpai: **{data.get('NAMA', 'Tiada Nama')}**")
                    
                    # Gunakan TABS untuk susun maklumat supaya kemas
                    tab1, tab2, tab3 = st.tabs(["👤 Peribadi", "🏫 Sekolah", "👪 Penjaga"])

                    # TAB 1: MAKLUMAT PERIBADI
                    with tab1:
                        st.subheader("Butiran Diri")
                        c1, c2 = st.columns(2)
                        c1.text_input("Nama Penuh", data.get('NAMA', '-'), disabled=True)
                        c2.text_input("No. Kad Pengenalan", data.get('NO. IC', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("Tarikh Lahir", data.get('TARIKH LAHIR', '-'), disabled=True)
                        c2.text_input("Jantina", data.get('JANTINA', '-'), disabled=True)
                        
                        c1, c2 = st.columns(2)
                        c1.text_input("Kaum", data.get('KAUM', '-'), disabled=True)
                        c2.text_input("Agama", data.get('AGAMA', '-'), disabled=True)

                        st.text_area("Alamat Rumah", data.get('ALAMAT', '-'), disabled=True)

                    # TAB 2: MAKLUMAT SEKOLAH
                    with tab2:
                        st.subheader("Butiran Kelas")
                        c1, c2 = st.columns(2)
                        c1.text_input("Nama Kelas", data.get('NAMA KELAS', '-'), disabled=True)
                        c2.text_input("Jenis Kelas", data.get('JENIS KELAS', '-'), disabled=True)
                        
                        st.subheader("Tarikh")
                        c1, c2 = st.columns(2)
                        c1.text_input("Tarikh Masuk Sekolah", data.get('TARIKH MASUK SEKOLAH', '-'), disabled=True)
                        c2.text_input("Tarikh Masuk Kelas", data.get('TARIKH MASUK KELAS', '-'), disabled=True)

                    # TAB 3: MAKLUMAT PENJAGA
                    with tab3:
                        st.subheader("Penjaga 1 (Utama)")
                        c1, c2 = st.columns(2)
                        c1.text_input("Nama Penjaga 1", data.get('PENJAGA 1', '-'), disabled=True)
                        c2.text_input("No. Tel Penjaga 1", data.get('NO. TEL. BIMBIT PENJAGA 1', '-'), disabled=True)
                        c1.text_input("Pekerjaan Penjaga 1", data.get('PEKERJAAN PENJAGA 1', '-'), disabled=True)
                        c2.text_input("Pendapatan Penjaga 1", data.get('PENDAPATAN PENJAGA 1', '-'), disabled=True)

                        st.markdown("---")
                        
                        st.subheader("Penjaga 2")
                        c1, c2 = st.columns(2)
                        c1.text_input("Nama Penjaga 2", data.get('PENJAGA 2', '-'), disabled=True)
                        c2.text_input("No. Tel Penjaga 2", data.get('NO. TEL. BIMBIT PENJAGA 2', '-'), disabled=True)

                else:
                    st.error(f"❌ Tiada rekod dijumpai untuk No. IC: {ic_input}")
            else:
                st.warning("⚠️ Sila masukkan No. IC terlebih dahulu.")
        
        else:
            # Paparan bila belum tekan butang search
            st.info("👈 Sila gunakan menu di sebelah kiri untuk membuat carian.")

if __name__ == "__main__":
    main()
