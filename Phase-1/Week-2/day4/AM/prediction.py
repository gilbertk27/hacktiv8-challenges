import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# load all files
with open('list_cat_cols.txt', 'r') as file_1:
  list_cat_col = json.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
  list_num_col = json.load(file_2)

with open('model_encoder.pkl', 'rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('model_scaler.pkl', 'rb') as file_4:
  model_scaler = pickle.load(file_4)

with open('model_lin_reg.pkl', 'rb') as file_5:
  model_lin_reg = pickle.load(file_5)

def app():
    with st.form('from_fifa_2022'):
        # field 
        name = st.text_input('Name', value='')
        age = st.number_input('Age', min_value=16, max_value=60, 
                            value=25, step=1, help='Ini adalah usia pemain')
        height = st.slider('Height', 100, 250, 170)
        weight = st.number_input('weight', 50, 150, 70)
        price = st.number_input('Price', value=0)
        
        st.markdown('----')
        attacking_work_rate  = st.selectbox('Attacking Work Rate', 
                                            ('Low', 'Medium', 'High'),
                                            index= 1)
        
        defensive_work_rate = st.selectbox('Defensive Work Rate', 
                                            ('Low', 'Medium', 'High'),
                                            index= 1)
        
        pace_total = st.number_input('Pace', min_value=0, max_value=100, 
                                    value=50)
        shooting_total = st.number_input('Shooting', min_value=0, max_value=100, 
                                    value=50)
        passing_total = st.number_input('Passing', min_value=0, max_value=100, 
                                    value=50)
        dribbling_total = st.number_input('Dribbling', min_value=0, max_value=100, 
                                    value=50)
        defending_total = st.number_input('Defending', min_value=0, max_value=100, 
                                    value=50)
        physicality = st.number_input('Physicality', min_value=0, max_value=100, 
                                    value=50)
        
        #submit buttion
        submitted = st.form_submit_button('Predict')

    #Inference
    data_inf = {
        'Name' : name,
        'Age' : age,
        'Height' : height,
        'Weight' : weight,
        'Price' : price,
        'AttackingWorkRate' : attacking_work_rate,
        'DefensiveWorkRate' : defensive_work_rate,
        'PaceTotal' : pace_total,
        'ShootingTotal': shooting_total,
        'PassingTotal' : passing_total,
        'DribblingTotal' : dribbling_total,
        'DefendingTotal' : defending_total,
        'PhysicalityTotal': physicality,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    # logic ketika user submit
    if submitted:
        #split between numerical and categorical columns
        data_inf_num = data_inf[list_num_col]
        data_inf_cat = data_inf[list_cat_col]
        
        # scaling and encoding
        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis = 1)

        #predict using linear reg model

        y_pred_inf = model_lin_reg.predict(data_inf_final)
        
        st.write('## Predicted Rating: ', str(int(y_pred_inf)))

if __name__ == '__main__':
    app()