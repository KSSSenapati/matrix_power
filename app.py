import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

st.set_page_config(layout='wide')
st.markdown("<h1 style='text-align: center; color: #A48153;'>Topic - To Compute The Result Of A Matrix Raised To A Power</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'>NAME - K SANTANU SEKHAR SENAPATI</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>ROLL No. - 118EE0577</h4>", unsafe_allow_html=True)

st.write('\n')
st.write('\n')

st.write("[Algorithm Explanation](https://drive.google.com/file/d/1Aa3380X81jKVnD5iUn-JuPpvWvUa_jH0/view?usp=sharing)")

import numpy as np

def matrix_power(A, k):

    for column in A.columns:
        A[column] = A[column].astype(int)
    A = A.values
    
    return np.linalg.matrix_power(A, k)

st.write('\n\n\n\n')
st.write('Give dimension of the matrix')
n = st.number_input('n value :', min_value=1, value=1)

st.write('Give input for the power')
k = st.number_input('k value :', min_value=1, value=1)
if st.checkbox('Feed Input Matrix'):
    st.text('* While entering the values press tab to go to the next input field and press enter after giving the inputs')
    st.text('* If you want to change the dimension of the input matrix then uncheck the checkbox before changing the input dimension')
    st.text('* The page may take some time to load the grid for providing input to the matrix, kindly wait')
    
    input_dataframe = pd.DataFrame(
        '',
        index=[i for i in range(n)],
        columns=['column-'+str(i+1) for i in range(n)]
    )


    resp = AgGrid(
            input_dataframe, 
        editable=True,
        sortable=False,
        filter=False,
        resizable=False,
        defaultWidth=5,
        fit_columns_on_grid_load=True,
        key='input_frame')
    
    st.write('Given Input Matrix')
    st.write(resp['data'].values)

    if st.button('Calculate Result'):
        ans = matrix_power(resp['data'], k)
        
        st.write('Output Matrix', ans)


        
