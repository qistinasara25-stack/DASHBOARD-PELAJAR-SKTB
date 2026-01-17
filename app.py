st.text_input("Jenis Kelas", data.get('JENIS KELAS', '-'), disabled=True)
                        with col2:
                            st.text_input("Tarikh Masuk Sekolah", data.get('TARIKH MASUK SEKOLAH', '-'), disabled=True)
                            st.text_input("Tarikh Masuk Kelas", data.get('TARIKH MASUK KELAS', '-'), disabled=True)
                        
                        st.metric(label="Bilangan Tanggungan", value=data.get('TANGGUNGAN', '0'))

                    # TAB 3: IBU BAPA / PENJAGA
                    with tab3:
                        st.subheader("Maklumat Penjaga 1")
                        c1, c2, c3, c4 = st.columns(4)
                        c1.text_input("Nama Penjaga 1", data.get('PENJAGA 1', '-'), disabled=True)
                        c2.text_input("Hubungan (1)", data.get('HUBUNGAN PENJAGA 1', '-'), disabled=True)
                        c3.text_input("Pekerjaan (1)", data.get('PEKERJAAN PENJAGA 1', '-'), disabled=True)
                        c4.text_input("No. Tel (1)", data.get('NO. TEL. BIMBIT PENJAGA 1', '-'), disabled=True)

                        st.markdown("---")
                        st.subheader("Maklumat Penjaga 2")
                        c1, c2, c3, c4 = st.columns(4)
                        c1.text_input("Nama Penjaga 2", data.get('PENJAGA 2', '-'), disabled=True)
                        c2.text_input("Hubungan (2)", data.get('HUBUNGAN PENJAGA 2', '-'), disabled=True)
                        c3.text_input("Pekerjaan (2)", data.get('PEKERJAAN PENJAGA 2', '-'), disabled=True)
                        c4.text_input("No. Tel (2)", data.get('NO. TEL. BIMBIT PENJAGA 2', '-'), disabled=True)

                    # TAB 4: ALAMAT
                    with tab4:
                        st.subheader("Lokasi Tempat Tinggal")
                        st.text_area("Alamat Penuh", data.get('ALAMAT', '-'), disabled=True)
                        
                        c1, c2, c3, c4 = st.columns(4)
                        c1.text_input("Poskod", data.get('POSKOD', '-'), disabled=True)
                        c2.text_input("Bandar", data.get('BANDAR', '-'), disabled=True)
                        c3.text_input("Daerah", data.get('DAERAH', '-'), disabled=True)
                        c4.text_input("Negeri", data.get('NEGERI', '-'), disabled=True)

                else:
                    st.error("❌ Tiada rekod dijumpai. Sila pastikan NO. IC dimasukkan dengan betul.")
            else:
                st.warning("⚠️ Sila masukkan NO. IC terlebih dahulu.")
        
        else:
            # Paparan awal sebelum user login
            st.info("👋 Selamat Datang. Sila masukkan No. Kad Pengenalan di sebelah kiri untuk melihat maklumat pelajar.")
            st.markdown("""
            Panduan Pengguna:
            1. Masukkan No. IC pada ruang di *sidebar* (kiri).
            2. Tekan butang 'Semak Maklumat'.
            3. Maklumat akan dipaparkan jika rekod wujud dalam pangkalan data.
            """)

if name == "main":
    main()
