import streamlit as st
import google.generativeai as genai

# إعدادات واجهة Pioneer Tech
st.set_page_config(page_title="Pioneer Tech AI", page_icon="🚀")
st.title("Pioneer Tech - Digital Solutions")
st.write("Bienvenue dans votre assistant intelligent.")

# إدخال الـ API Key من الجانب
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استعملنا 1.5-flash حصراً لأنه الموديل المفعّل في مشروعك الآن
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_input("كيفاش نجموا نعاونوا مشروعك اليوم؟")
        
        if st.button("إرسال"):
            if user_input:
                response = model.generate_content(user_input)
                st.markdown(f"**Pioneer AI:** {response.text}")
            else:
                st.warning("الرجاء كتابة سؤالك.")
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")
else:
    st.warning("الرجاء إدخال API Key من Google AI Studio.")
