from application.config import *
from knowledge_base.kb_license_query import all_terms_conditions
from knowledge_base.kb_license_query import conditions_types_all
from knowledge_base.kb_license_query import rights_types_all
from knowledge_base.kb_license_query import license_conditions
from knowledge_base.kb_license_query import license_rights

def query_kb(sidebar_selection):
    # Display a header to describe stuff contained in this funciton
    st.header(f'Looking up {sidebar_selection}')

    if sidebar_selection == 'Everything!':
        # enable a set of queries to get general information
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Rights', 'Conditions'])
        if analysis_option == 'Rights':
            results = rights_types_all()
            for result in results:
                st.button(result)
        if analysis_option == 'Conditions':
            results = conditions_types_all()
            for result in results:
                st.button(result)

    else:
        # enable a set of queries that are specific to a license type
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Everything', 'Rights', 'Conditions'])
        # three conditional statements based on the options listed in select box
        if analysis_option == 'Everything':
            st.write(f'All the Terms and Conditions of {sidebar_selection}')
            results = all_terms_conditions(sidebar_selection)
            for result in results:
                st.button(result)

        if analysis_option == 'Rights':
            results = license_rights(sidebar_selection)
            for result in results:
                st.button(result)

        if analysis_option == 'Conditions':
            results = license_conditions(sidebar_selection)
            for result in results:
                st.button(result)

