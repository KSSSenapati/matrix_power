import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

st.set_page_config(layout='wide')
st.markdown("<h1 style='text-align: center; color: #A48153;'>Topic - To Compute The Result of a Matrix Raised to a Power</h1>", unsafe_allow_html=True)

#st.markdown("<div><div style='text-align: left;'><h4>A</h4></div><div style='text-align: right;'><h4>B</h4></div></div>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>NAME-KANCHADA SANTANU SEKHAR SENAPATI      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ROLL NO-118EE0577</h4>", unsafe_allow_html=True)
# st.subheader("NAME-KANCHADA SANTANU SEKHAR SENAPATI")
# st.subheader("ROLL NO-118EE0577")

st.write('\n')
st.write('\n')

#st.write("[More information about the topic](https://docs.google.com/presentation/d/1XQXzOV60eLvaQh0XRO-vuG3Zg1sIwR3SVBhkpjCa7rs/edit?usp=sharing)")

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

    if st.button('Calculate Power of the matrix'):
        ans = matrix_power(resp['data'], k)
        
        st.write('Output Matrix', ans)

        
