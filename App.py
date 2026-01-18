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
                    # INI ADALAH MESIN UANG KAMU
    st.markdown("---")
    
    # Masukkan link Lemon Squeezy kamu di dalam tanda kutip di bawah ini:
    payment_link = "https://nikomax.lemonsqueezy.com/checkout/buy/bde6297a-8bca-4ada-9b45-8953f440835b"
    
    st.markdown(f"""
    <div style='padding: 20px; background-color: #f0f2f6; border-radius: 10px; text-align: center;'>
        <h3>🔓 Upgrade ke Versi Pro</h3>
        <p>Buka fitur penuh, tanpa batas, dan akses ke database GPT-4.</p>
        <a href='{payment_link}' style='background-color: #000000; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;'>Beli Sekarang</a>
    </div>
    """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Masukkan API Key dulu agar bisa dipakai.")
