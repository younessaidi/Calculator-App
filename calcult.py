import streamlit as st #streamlit run calcult.py

st.title("🧮 Calculator App")
num1 = st.number_input("🔢 Enter first number: ")
num2 = st.number_input("🔢 Enter second number: ")
opert = st.selectbox("👉 Choose operation:", ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"])

hi = st.button("🎯 Calculate")
if hi:
    st.markdown("*dont forget to see more about me* [Younes](https://github.com/younessaidi)")
    if opert == "✖️ Multiply":
        result = num1 * num2
        st.success(f"✅ Result: {result}")

    elif opert == "➗ Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {result}")
        else:
            st.error("⚠️ Cannot divide by zero 🚫")

    elif opert == "➕ Add":
        result = num1 + num2
        st.success(f"✅ Result: {result}")

    elif opert == "➖ Subtract":
        result = num1 - num2
        st.success(f"✅ Result: {result}")

    else :
        st.write("is wrong")
st.markdown("**Thanks for see my project** [Younes](https://github.com/younessaidi)") #Younes </>
