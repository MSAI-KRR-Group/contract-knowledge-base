from application.config import *
from application.load_css import local_css
from application.get_git_license import get_license_name
from application.draw_graph import draw_license_graph, draw_rights_graph, draw_conditions_graph, draw_repo_graph

from knowledge_base.kb_license_query import all_terms_conditions
from knowledge_base.kb_license_query import conditions_types_all
from knowledge_base.kb_license_query import rights_types_all
from knowledge_base.kb_license_query import license_conditions
from knowledge_base.kb_license_query import license_rights
from knowledge_base.kb_license_query import repository_license
from knowledge_base.kb_license_query import repository_terms_conditions
from knowledge_base.kb_license_query import repository_rights
from knowledge_base.kb_license_query import repository_conditions
from knowledge_base.kb_license_query import warranty_type, warranty_all

from knowledge_base.kb_license_store import kb_license


def query_kb(sidebar_selection):
    # import css styles
    local_css("styles_css/style.css")
    css_red = "<span class='highlight red'>"
    css_green = "<span class='highlight green'>"
    css_blue = "<span class='highlight blue'>"
    css_orange = "<span class='highlight orange'>"
    css_end = "</span>"

    all_kb_terms_conditions = []
    all_kb_terms_conditions.extend(rights_types_all())
    all_kb_terms_conditions.extend(conditions_types_all())

    # Display a header to describe stuff contained in this funciton
    if sidebar_selection == 'I have a repository':
        st.header(f'Looking Up a License for a Repository')
    else:
        st.header(f'Looking Up: {sidebar_selection}')

    if sidebar_selection == 'Everything!':

        # enable a set of queries to get general information
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Rights', 'Conditions', 'Warranties'])
        if analysis_option == 'Rights':
            results = rights_types_all()
            for result in results:
                st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Conditions':
            results = conditions_types_all()
            for result in results:
                st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Warranties':
            results = warranty_all()
            for result in results:
                st.write(f'{css_orange}{result}{css_end}', unsafe_allow_html=True)

    elif sidebar_selection == 'I have a repository':
        # configure default value to look up a repository URL
        repo_url = st.text_input(label='Look up our repository or replace it with your own Git URL.'
                                 , value='https://github.com/MSAI-KRR-Group/contract-knowledge-base')

        # apply a recursive call to return the associated knowledge
        if repo_url:
            # query_kb(get_license_name(repo_url))
            repo_license = get_license_name(repo_url)
            st.write(f'Found a {repo_license} at {repo_url}')

            repo_url = repo_url.replace('https://','')

            search_term = 'Repository'
            check_kb = list(kb_license.query(f'isA({search_term}, repository)'))
            existing_repos = [sub[search_term] for sub in check_kb]

            if repo_url not in existing_repos:
                # kb_license.store(f'isA({repo_url}, repository)')
                kb_license.store(f'licenseOf({repo_url}, {repo_license})')
                st.write(f'Stored your repository and license as a fact in KB.')

            draw_repo_graph(repo_url, repo_license)

    else:
        # enable a set of queries that are specific to a license type
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Everything', 'Rights', 'Conditions', 'Warranties'])
        # three conditional statements based on the options listed in select box
        if analysis_option == 'Everything':
            draw_license_graph(sidebar_selection)

            all_results = []
            st.write(f'All the {css_green}Terms{css_end} and {css_blue}Conditions{css_end} of {sidebar_selection}', unsafe_allow_html=True)

            results = license_rights(sidebar_selection)
            all_results.extend(results)

            col1, col2 = st.beta_columns(2)
            col1.header('Rights')
            for result in results:
                col1.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

            results = license_conditions(sidebar_selection)
            all_results.extend(results)
            col2.header('Conditions')
            for result in results:
                col2.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

            not_terms_and_conditions = set(all_kb_terms_conditions) - set(all_results)

            if not_terms_and_conditions:

                st.write(f'The terms and conditions that are {css_red}NOT extended{css_end} by {sidebar_selection}.',
                         unsafe_allow_html=True)

                for result in not_terms_and_conditions:
                    st.write(f'{css_red}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Rights':
            draw_rights_graph(sidebar_selection)
            results = license_rights(sidebar_selection)
            for result in results:
                st.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Conditions':
            draw_conditions_graph(sidebar_selection)
            results = license_conditions(sidebar_selection)
            for result in results:
                st.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

        if analysis_option == 'Warranties':
            warranty_type(sidebar_selection)
            results = warranty_type(sidebar_selection)
            if results:
                for result in results:
                    st.write(f'{css_orange}{result}{css_end}', unsafe_allow_html=True)
            else:
                st.write(f'{css_orange}No Warranties{css_end}', unsafe_allow_html=True)

