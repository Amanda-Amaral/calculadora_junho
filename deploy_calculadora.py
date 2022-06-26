import streamlit as st
import numpy as np
import pickle
import pandas as pd
from catboost import CatBoostRegressor

@st.cache()

def loader(model_path="./model.cbm"):
    model_input = pd.read_csv(data_path)       
    model = CatBoostRegressor()
    model.load_model("./model.cbm")
    return model

model = loader()

def main():
    st.title("Calculadora de Aluguél")
    st.subheader("Barra da Tijuca - RJ")

    quartos =st.slider("Número de quartos",min_value=1,max_value=5,value=1)
    area = st.number_input("Área", min_value=22, max_value=436, step=4,value =70)
    pred = st.button("Predict")
  
    novo_imovel=pd.DataFrame([[area,quartos]],columns=['Area','Numero de Quartos'],)
    if pred:
        st.dataframe(novo_imovel)
        prediction = model.predict(novo_imovel)[0]
        
        st.write(f"Preço previsto: R$ {prediction: ,.2f}")
        
if __name__=='__main__':
    main()