#!/usr/bin/env python

import os
import sys
from pprint import pprint
from CustomerDAO import CustomerDAO
import streamlit as st

# streamlit run main_streamlit.py 
def main():
    st.set_page_config(layout="wide")
    dao = CustomerDAO('customers_db.db')
    customers = list(dao.find_all())

    title = st.text_input("Movie title", "Life of Brian")
    st.write("The current movie title is", title)

    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("## Why hello there")
    else:
        st.write("## Goodbye")

    st.table(customers)
if __name__=='__main__':
    main()
