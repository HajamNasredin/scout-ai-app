import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Pioneer Tech AI", page_icon="🚀")
st.title("Pioneer Tech - Digital Solutions")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استعملنا gemini-pro لأنه الأكثر توافقاً مع جميع مفاتيح الـ API
        model = genai.GenerativeModel('gemini-pro')
        
        user_input = st.text_input("كيفاش نجموا نعاونوا مشروعك اليوم؟")
        
        if st.button("إرسال"):
            if user_input:
                response = model.generate_content(user_input)
                st.markdown(f"**Pioneer AI:** {response.text}")
            else:
                st.warning("أكتب سؤالك الأول.")
    except Exception as e:
        # إظهار الخطأ بشكل مهني
        st.error(f"تنبيه تقني: {e}")
else:
    st.info("الرجاء إدخال الـ API Key الخاص بـ Pioneer Tech.")
