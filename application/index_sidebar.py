from application.config import *

def main_menu():
    sidebar_picklist = ['MIT License', 'GNU GPL 3.0']
    return st.sidebar.selectbox(label='Select Contract Type'
                                , options=sidebar_picklist
                                , key='index_main_menu')