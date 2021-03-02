from application.config import *
from knowledge_base.kb_license_query import all_terms_conditions
from knowledge_base.kb_license_query import conditions_types_all
from knowledge_base.kb_license_query import rights_types_all

def query_kb(sidebar_selection):
    # Display a header to describe stuff contained in this funciton
    st.header(f'The {sidebar_selection} License')

    # embed the question as the label of the select box
    analysis_option = st.selectbox(label='What do you want to know?'
                                 , options=['Everything', 'Rights', 'Conditions'])

    # configure the query term (needs work)
    #TODO: make this scalable for many types of licenses
    license_to_query = 'mit_license' if sidebar_selection == 'MIT' else 'gnu_license' if sidebar_selection == 'GNU GPL 3.0' else ''

    # three conditional statements based on the options listed in select box
    if analysis_option == 'Everything':
        st.write(f'All the Terms and Conditions of {sidebar_selection}')
        results = all_terms_conditions(license_to_query)
        for result in results:
            st.button(result)
    if analysis_option == 'Rights':
        results = rights_types_all()
        for result in results:
            st.button(result)
    if analysis_option == 'Conditions':
        results = conditions_types_all()
        for result in results:
            st.button(result)
