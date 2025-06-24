import pickle
import streamlit as st
import numpy as np
from xgboost import XGBRegressor


# Load trained model
w = pickle.load(open('F:\INTERSHIP\Placement\placement (1).sav', 'rb'))  # <-- updated

def predict(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = w.predict(input_array)
    return prediction[0]

def main():
    st.title("💼 Salary Prediction App")

    # Numeric inputs
    ssc_p = st.text_input("SSC Percentage").strip()
    hsc_p = st.text_input("HSC Percentage").strip()
    hsc_s = st.text_input("HSC Stream {'Commerce':0, 'Science':1, 'Arts':2}").strip()
    degree_p = st.text_input("Degree Percentage").strip()
    degree_t = st.text_input("Degree Type {'Sci&Tech':0, 'Comm&Mgmt':1, 'Others':2}").strip()
    workex = st.text_input("Work Experience {'No':0, 'Yes':1}").strip()
    etest_p = st.text_input("E-test Percentage").strip()
    specialisation = st.text_input("Specialisation {'Mkt&Fin':0, 'Mkt&HR':1}").strip()
    mba_p = st.text_input("MBA Percentage").strip()
    status = st.text_input("Status {'Placed':0, 'Not Placed':1}").strip()

    if st.button("Predict Salary"):
        try:
            input_list = [
                float(ssc_p), float(hsc_p), float(hsc_s), float(degree_p),
                float(degree_t), float(workex), float(etest_p),
                float(specialisation), float(mba_p), float(status)
            ]
            result = predict(input_list)
            st.success(f"💰 Predicted Salary: **{result}**")
        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
