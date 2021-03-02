from application.config import *
from knowledge_base.kb_license_query import all_terms_conditions

def query_kb(sidebar_selection):
    if sidebar_selection == 'MIT License':
        st.header('The MIT License')
        analysis_option = st.selectbox('What do you want to know?', ['Everything', 'Rights', 'Conditions'])

        if analysis_option == 'Everything':
            st.write(f'All the Terms and Conditions of {sidebar_selection}')
            results = all_terms_conditions('mit_license')
            for result in results:
                st.button(result)
        # TODO: configure results and options for each query type from kb_license_query
        if analysis_option == 'Rights':
            st.write('return all Rights')
        if analysis_option == 'Conditions':
            st.write('return all Conditions')

    if sidebar_selection == 'GNU GPL 3.0':
        st.header('GNU GPL 3.0 License')
        analysis_option = st.selectbox('What do you want to know?', ['Everything', 'Rights', 'Conditions'])

        if analysis_option == 'Everything':
            st.write(f'All the Terms and Conditions of {sidebar_selection}')
            results = all_terms_conditions('gnu_license')
            for result in results:
                st.button(result)
        if analysis_option == 'Rights':
            st.write('return all Rights')
        if analysis_option == 'Conditions':
            st.write('return all Conditions')