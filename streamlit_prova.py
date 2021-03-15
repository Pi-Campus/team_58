# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:08:21 2021

@author: sasha
"""

import streamlit as st
import numpy as np
import pandas as pd



st.title('NLP Query')


query = st.text_input('Query input')

result = 'data result BLABLABLA'



if query:
    st.text('Result')
    st.write(f'the result of {query} is:')

    df = np.random.rand(50,2)
    df = pd.DataFrame(df)
    st.dataframe(df.head())
    
    
    st.area_chart(df)