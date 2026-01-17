import streamlit as st
import pandas as pd

# Tetapan Halaman
st.set_page_config(page_title="Dashboard Maklumat Pelajar", layout="wide", page_icon="🎓")

# URL Google Sheet
DATA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRDjXlAepJEOgEoAZD2_ab-xed3AU6LyLkY-ixEqlRx3h2CT224Jd7ww4e0qC9-WQ/pub?output=csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(DATA_URL, dtype=str)
        df.columns = df.columns.str.strip()
        df = df.fillna("-")
        return df
    except Exception as e:
        st.error(f"Ralat: {e}")
        return None

def main():
    st.title("🎓 Sistem Maklumat Pelajar")
    st.markdown("---")

    df = load_data()

    if df is not None:
        st.sidebar.header("🔐 Carian Pelajar")
        ic_input = st.sidebar.text_input("Masukkan No. IC (Tanpa Sengkang)", max_chars=12)
        search_btn = st.sidebar.button("Semak")
        
        if search_btn:
            if ic_input:
                pelajar = df[df['NO. IC'] == ic_input]
                if not pelajar.empty:
                    data = pelajar.iloc[0]
                    st.success(f"Rekod Ditemui: {data.get('NAMA', '-')}")
                    
                    tab1, tab2, tab3 = st.tabs(["Peribadi", "Sekolah", "Ibu Bapa"])
                    
                    with tab1:
                        st.subheader("Maklumat Peribadi")
                        c1, c2 = st.columns(2)
                        c1.text_input("Nama", data.get('NAMA', '-'), disabled=True)
                        c2.text_input("No. IC", data.get('NO. IC', '-'), disabled=True)
                        c1.text_input("Tarikh Lahir", data.get('TARIKH LAHIR', '-'), disabled=True)
                        c2.text_input("Jantina", data.get('JANTINA', '-'), disabled=True)

                    with tab2:
                        st.subheader("Maklumat Sekolah")
                        c1, c2 = st.columns(2)
                        c1.text_input("Kelas", data.get('NAMA KELAS', '-'), disabled=True)
                        c2.text_input("Tarikh Masuk", data.get('TARIKH MASUK SEKOLAH', '-'), disabled=True)

                    with tab3:
                        st.subheader("Maklumat Penjaga")
                        st.text_input("Nama Penjaga 1", data.get('PENJAGA 1', '-'), disabled=True)
                        st.text_input("No. Tel Penjaga 1", data.get('NO. TEL. BIMBIT PENJAGA 1', '-'), disabled=True)
                        st.divider()
                        st.text_input("Nama Penjaga 2", data.get('PENJAGA 2', '-'), disabled=True)
                        st.text_input("No. Tel Penjaga 2", data.get('NO. TEL. BIMBIT PENJAGA 2', '-'), disabled=True)
                else:
                    st.error("Tiada rekod dijumpai.")
            else:
                st.warning("Sila masukkan No. IC.")
        else:
            st.info("Sila masukkan No. IC di bahagian kiri (sidebar) untuk mula.")

if __name__ == "__main__":
    main()
