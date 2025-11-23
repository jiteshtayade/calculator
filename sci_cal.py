import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Scientific Calculator")

# Inputs
num1 = st.number_input("Value A", value=0.0)
num2 = st.number_input("Value B (used only for some operations)", value=0.0)

operation = st.selectbox(
    "Operation",
    [
        "Add", "Subtract", "Multiply", "Divide", "Modulo", "Power",
        "Square Root (A)", "Square Root (B)",
        "Factorial (A)", "Factorial (B)",
        "Sin(A)", "Cos(A)", "Tan(A)",
        "Log (base e)", "Log10"
    ]
)

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                st.error("Division by zero.")
                st.stop()
            result = num1 / num2
        elif operation == "Modulo":
            result = num1 % num2
        elif operation == "Power":
            result = num1 ** num2
        elif operation == "Square Root (A)":
            if num1 < 0:
                st.error("sqrt() of negative number is invalid.")
                st.stop()
            result = math.sqrt(num1)
        elif operation == "Square Root (B)":
            if num2 < 0:
                st.error("sqrt() of negative number is invalid.")
                st.stop()
            result = math.sqrt(num2)
        elif operation == "Factorial (A)":
            if num1 < 0 or int(num1) != num1:
                st.error("Factorial requires a non-negative integer.")
                st.stop()
            result = math.factorial(int(num1))
        elif operation == "Factorial (B)":
            if num2 < 0 or int(num2) != num2:
                st.error("Factorial requires a non-negative integer.")
                st.stop()
            result = math.factorial(int(num2))
        elif operation == "Sin(A)":
            result = math.sin(num1)
        elif operation == "Cos(A)":
            result = math.cos(num1)
        elif operation == "Tan(A)":
            result = math.tan(num1)
        elif operation == "Log (base e)":
            if num1 <= 0:
                st.error("Log undefined for <= 0.")
                st.stop()
            result = math.log(num1)
        elif operation == "Log10":
            if num1 <= 0:
                st.error("Log10 undefined for <= 0.")
                st.stop()
            result = math.log10(num1)
        else:
            st.error("Invalid operation.")
            st.stop()

        st.success(f"Result = {result}")

    except Exception as e:
        st.error(f"Error: {e}")
