import streamlit as st
import google.generativeai as genai

# إعدادات واجهة Pioneer Tech
st.set_page_config(page_title="Pioneer Tech AI", page_icon="🚀")
st.title("Pioneer Tech - Digital Solutions")
st.write("Bienvenue dans votre assistant intelligent.")

# إدخال الـ API Key (بش نحطوه في إعدادات المنصة مش في الكود للأمان)
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
  
    # أستعمل الموديل هذا حصراً لأنه الأكثر استقراراً في النسخة المجانية
model = genai.GenerativeModel('gemini-1.5-flash')
    if st.button("إرسال"):
        response = model.generate_content(user_input)
        st.markdown(f"**Pioneer AI:** {response.text}")
else:

    st.warning("الرجاء إدخال API Key من Google AI Studio للبدء.")
