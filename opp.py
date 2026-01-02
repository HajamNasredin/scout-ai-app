import streamlit as st
import google.generativeai as genai

# إعدادات Pioneer Tech
st.set_page_config(page_title="Pioneer Tech AI", page_icon="🚀")
st.title("Pioneer Tech - Digital Solutions")
st.write("Bienvenue dans votre assistant intelligent.")

# إدخال الـ API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # التغيير الجذري هنا: استعمال flash بدل pro
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_input("كيفاش نجموا نعاونوا مشروعك اليوم؟")
        
        if st.button("إرسال"):
            if user_input:
                # سطر 19: طلب المحتوى
                response = model.generate_content(user_input)
                st.success("تمت الإجابة بنجاح!")
                st.markdown(f"**Pioneer AI:** {response.text}")
            else:
                st.warning("أكتب حاجة قبل ما تبعث.")
    except Exception as e:
        st.error(f"خطأ تقني: {e}")
else:
    st.info("الرجاء إدخال الـ API Key في القائمة الجانبية.")
