from application.config import *
from knowledge_base.kb_license_query import license_types

def main_menu():
    # populate the list of possible licenses from the kb
    pick_list_values = license_types()
    # hard code an option to pick everything as default state
    pick_list_values.insert(0, 'Everything!')
    pick_list_values.append('I have a repository')
    # convenience object
    sidebar_picklist = pick_list_values
    # return the select box with options as st object
    return st.sidebar.selectbox(label='Select Contract Type'
                                , options=sidebar_picklist
                                , key='index_main_menu')
