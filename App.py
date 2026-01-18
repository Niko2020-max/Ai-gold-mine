import streamlit as st
import openai

# --- KONFIGURASI TAMPILAN ---
st.set_page_config(page_title="AI Copywriter Pro", page_icon="💰", layout="centered")

st.title("💰 AI Copywriter Pro")
st.subheader("Buat teks jualan dalam 5 detik")

# --- INPUT USER ---
# Kita minta user memasukkan API Key mereka agar tidak perlu kita bayar biaya API
api_key = st.text_input("Masukkan OpenAI API Key Kamu:", type="password")

if api_key:
    client = openai.OpenAI(api_key=api_key)
    
    topic = st.text_area("Masukkan Produkmu:", height=100)
    tone = st.selectbox("Jenis Teks:", ["Caption Instagram", "Iklan Facebook", "Email Penawaran"])

    if st.button("Buat Sekarang ✨"):
        with st.spinner("Sedang berpikir..."):
            try:
                if tone == "Caption Instagram":
                    prompt = f"Buat caption instagram yang lucu dan menarik untuk produk: {topic}. Pakai emoji."
                elif tone == "Iklan Facebook":
                    prompt = f"Buat teks iklan facebook yang meyakinkan untuk produk: {topic}."
                else:
                    prompt = f"Buat email penawaran yang sopan untuk produk: {topic}."

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                st.success("Ini hasilnya:")
                st.write(response.choices[0].message.content)
                
                # INI TEMPAT UANG KITA MASUK NANTI
                st.markdown("---")
                st.warning("Versi Gratis: Terbatas 3x pemakaian. Upgrade ke Premium untuk Unlimited.")
                
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Masukkan API Key dulu agar bisa dipakai.")
