import streamlit as st

st.title("ini halaman nabung")

with st.form("Nabung"):
    nama = st.text_input("masukkan nama:")
    nominal = st.number_input("masukan nominal nabung:")
    submit_button = st.form_submit_button("simpan")
    
    if submit_button:
        st.write(nama)
        st.session_state['Nabung'].append({
            "Nama" : nama,
            "Nominal" : nominal,
        })
        st.success("Berhasil Nabung ")
        