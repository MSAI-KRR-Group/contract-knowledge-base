from application.config import *
from application.load_css import local_css

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
        st.header(f'Looking up your repository, {sidebar_selection}')
    else:
        st.header(f'Looking up {sidebar_selection}')

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
        temp_default_repo_name = '<github_repo>'

        repo_name = st.text_input(label='What is the repository name?'
                                  ,value=temp_default_repo_name)

        results = repository_license(repo_name)

        for result in results:
            # looping through results but really only expectig one license per repository
            st.write(f'The license for {repo_name} is {result}')

        if repo_name:
            analysis_option = st.selectbox(label=f'What do you want to know about {repo_name}?'
                                           , options=['Everything', 'Rights', 'Conditions'])

            if analysis_option == 'Everything':

                all_results = []
                st.write(f'All the {css_green}Terms{css_end} and {css_blue}Conditions{css_end} extended by {repo_name}', unsafe_allow_html=True)
                results = repository_rights(repo_name)
                all_results.extend(results)
                for result in results:
                    st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

                results = repository_conditions(repo_name)
                all_results.extend(results)
                for result in results:
                    st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

                st.write(f'The terms and conditions that are {css_red}NOT extended{css_end} by {repo_name}.',
                         unsafe_allow_html=True)

                not_terms_and_conditions = set(all_kb_terms_conditions) - set(all_results)

                for result in not_terms_and_conditions:
                    st.write(f'{css_red}{result}{css_end}', unsafe_allow_html=True)

            if analysis_option == 'Rights':
                results = repository_rights(repo_name)
                for result in results:
                    st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

            if analysis_option == 'Conditions':
                results = repository_conditions(repo_name)
                for result in results:
                    st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

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

