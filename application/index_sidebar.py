from application.config import *
from knowledge_base.kb_license_query import license_types

def main_menu():
    pick_list_values = license_types()
    pick_list_values.insert(0, 'Everything!')
    sidebar_picklist = pick_list_values

    return st.sidebar.selectbox(label='Select Contract Type'
                                , options=sidebar_picklist
                                , key='index_main_menu')
