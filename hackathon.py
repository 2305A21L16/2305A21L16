import streamlit as st

st.title("2305A21L16-PS11")


def Gen_Eff(V, CL, IL, K, Rse, Ra):
    CUL = (K * IL) ** 2 * (Rse + Ra)
    Eff = (K * V * IL - CL - CUL) / (K * V * IL) * 100 
    return Eff,CUL

st.subheader("Calculate the efficiency of DC series motor at various loads")
st.container(border=True)
V = st.number_input("Enter Voltage (V)", min_value=0.0, value=230.0)
CL = st.number_input("Enter Core Losses (CL) in Watts", min_value=0.0, value=100.0)
IL = st.number_input("Enter Full Load Current (IL) in Amps", min_value=0.0, value=15.0)
K = st.number_input("Enter Loading on Motor (K)", min_value=0.0, value=1.0)
Rse = st.number_input("Enter Series Field Resistance (Rse) in Ohms", min_value=0.0, value=0.20)
Ra = st.number_input("Enter Armature Resistance (Ra) in Ohms", min_value=0.0, value=0.10)

compute = st.button("Compute")
st.container(border=True)
if compute:
    Eff,CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)
    st.write(f"Eff = {Eff:.2f}%")
    st.write(f"CUL = {CUL:.2f} Watts")
