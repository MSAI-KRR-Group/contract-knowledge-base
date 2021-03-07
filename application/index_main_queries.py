from application.config import *
from application.load_css import local_css
from application.get_git_license import get_license_name

from knowledge_base.kb_license_query import all_terms_conditions
from knowledge_base.kb_license_query import conditions_types_all
from knowledge_base.kb_license_query import rights_types_all
from knowledge_base.kb_license_query import license_conditions
from knowledge_base.kb_license_query import license_rights
from knowledge_base.kb_license_query import repository_license
from knowledge_base.kb_license_query import repository_terms_conditions
from knowledge_base.kb_license_query import repository_rights
from knowledge_base.kb_license_query import repository_conditions


def query_kb(sidebar_selection):
    # import css styles
    local_css("styles_css/style.css")
    css_red = "<span class='highlight red'>"
    css_green = "<span class='highlight green'>"
    css_blue = "<span class='highlight blue'>"
    css_end = "</span>"

    all_kb_terms_conditions = []
    all_kb_terms_conditions.extend(rights_types_all())
    all_kb_terms_conditions.extend(conditions_types_all())

    # Display a header to describe stuff contained in this funciton
    if sidebar_selection == 'I have a repository':
        st.header(f'Looking Up a License for a Repository')
    else:
        st.header(f'Found {sidebar_selection}')

    if sidebar_selection == 'Everything!':
        # enable a set of queries to get general information
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Rights', 'Conditions'])
        if analysis_option == 'Rights':
            results = rights_types_all()
            for result in results:
                st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)
        if analysis_option == 'Conditions':
            results = conditions_types_all()
            for result in results:
                st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

    elif sidebar_selection == 'I have a repository':
        # configure default value to look up a repository URL
        repo_url = st.text_input(label='Look up our repository or replace it with your own Git URL.'
                                 , value='https://github.com/MSAI-KRR-Group/contract-knowledge-base')

        # apply a recursive call to return the associated knowledge
        if repo_url:
            query_kb(get_license_name(repo_url))

    else:
        # enable a set of queries that are specific to a license type
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Everything', 'Rights', 'Conditions'])
        # three conditional statements based on the options listed in select box
        if analysis_option == 'Everything':
            all_results = []
            st.write(f'All the {css_green}Terms{css_end} and {css_blue}Conditions{css_end} of {sidebar_selection}', unsafe_allow_html=True)
            results = license_rights(sidebar_selection)
            all_results.extend(results)
            for result in results:
                st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

            results = license_conditions(sidebar_selection)
            all_results.extend(results)
            for result in results:
                st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

            not_terms_and_conditions = set(all_kb_terms_conditions) - set(all_results)

            if not_terms_and_conditions:

                st.write(f'The terms and conditions that are {css_red}NOT extended{css_end} by {sidebar_selection}.',
                         unsafe_allow_html=True)

                for result in not_terms_and_conditions:
                    st.write(f'{css_red}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Rights':
            results = license_rights(sidebar_selection)
            for result in results:
                st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Conditions':
            results = license_conditions(sidebar_selection)
            for result in results:
                st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

