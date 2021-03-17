from src.application.config import *
from src.application.load_css import local_css
from src.application.get_git_license import get_license_name
from src.application.draw_graph import draw_license_graph, draw_rights_graph, draw_conditions_graph, draw_repo_graph

from src.knowledge_base.kb_license_query import license_types
from src.knowledge_base.kb_license_query import conditions_types_all
from src.knowledge_base.kb_license_query import rights_types_all
from src.knowledge_base.kb_license_query import license_conditions
from src.knowledge_base.kb_license_query import license_rights
from src.knowledge_base.kb_license_query import repository_license
from src.knowledge_base.kb_license_query import repository_terms_conditions
from src.knowledge_base.kb_license_query import repository_rights
from src.knowledge_base.kb_license_query import repository_conditions
from src.knowledge_base.kb_license_query import warranty_type, warranty_all
from src.knowledge_base.kb_license_query import get_comment
from src.knowledge_base.kb_license_store import license_mt


def query_kb(sidebar_selection):
    # import microtheory
    kb_license = license_mt()
    css_folder = os.sep.join(['src', 'styles_css'])
    css_filename = 'style.css'
    css_file = os.sep.join([css_folder, css_filename])
    # import css styles
    local_css(css_file)
    # store css highlights as string objects
    css_red = "<span class='highlight red'>"
    css_green = "<span class='highlight green'>"
    css_blue = "<span class='highlight blue'>"
    css_orange = "<span class='highlight orange'>"
    css_gray = "<span class='highlight gray'>"
    css_end = "</span>"

    # get a full account of all possible information types for negative inference
    all_kb_terms_conditions = []
    all_kb_terms_conditions.extend(rights_types_all())
    all_kb_terms_conditions.extend(conditions_types_all())
    all_kb_terms_conditions.extend(warranty_all())

    if sidebar_selection == 'I have a repository':
        st.header(f'Looking Up a License for a Repository')
    else:
        st.header(f'Looking Up: {sidebar_selection}')

    # look up all data about everything
    if sidebar_selection == 'Everything!':

        # subset of things to query under everything
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Licenses', 'Rights', 'Conditions', 'Warranties'])
        # query and return results
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
        if analysis_option == 'Licenses':
            results = license_types()
            # special case - return comments for each and break into cols
            col1, col2 = st.beta_columns(2)
            for result in results:
                col1.write(f'{css_gray}{result}{css_end}', unsafe_allow_html=True)
                comment = get_comment(result)
                col2.markdown(
                    f'<p style="font-size:12px">{comment}</p>',
                    unsafe_allow_html=True
                )
    # if selected, enable URL input
    elif sidebar_selection == 'I have a repository':
        # configure default value to look up a repository URL
        repo_url = st.text_input(label='Look up our repository or replace it with your own Git URL.'
                                 , value='https://github.com/MSAI-KRR-Group/contract-knowledge-base')


        if repo_url:
            # parse URL response for git license
            repo_license = get_license_name(repo_url)
            # only runs if a supported license is returned or the URL is valid
            if repo_license != 'Unsupported':
                st.write(f'Found a {repo_license} at {repo_url}')
                # drop unnecessary string from URL (causes issues in KB)
                repo_url = repo_url.replace('https://','')
                # check if the repo is known, if not, add it to the KB
                search_term = 'Repository'
                check_kb = list(kb_license.query(f'isA({search_term}, repository)'))
                existing_repos = [sub[search_term] for sub in check_kb]
                if repo_url not in existing_repos:
                    kb_license.store(f'licenseOf({repo_url}, {repo_license})')
                    st.write(f'Stored your repository and license as a fact in KB.')
                # render a graph of the given selection
                draw_repo_graph(repo_url, repo_license)
                # init an empty container to track cumulative results
                all_results = []
                st.write(
                    f'All the {css_green}Terms{css_end}, {css_blue}Conditions{css_end}, and {css_orange}Warranties{css_end} of {repo_url}',
                    unsafe_allow_html=True)

                results = license_rights(repo_license)
                all_results.extend(results)

                col1, col2, col3 = st.beta_columns(3)
                col1.header('Rights')
                for result in results:
                    col1.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

                results = license_conditions(repo_license)
                all_results.extend(results)
                col2.header('Conditions')
                for result in results:
                    col2.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

                results = warranty_type(repo_license)
                all_results.extend(results)
                col3.header('Warranties')
                if results:
                    for result in results:
                        col3.write(f'{css_orange}{result}{css_end}', unsafe_allow_html=True)
                else:
                    col3.write(f'{css_orange}None{css_end}', unsafe_allow_html=True)

            else:
                st.write(f'The target URL is {repo_license}, try again.')

    else:
        ## the else condition is assumed to be when a specific type of license is being selected
        # enable a set of queries that are specific to a license type
        analysis_option = st.selectbox(label='What do you want to know?'
                                       , options=['Everything', 'Rights', 'Conditions', 'Warranties'])
        # three conditional statements based on the options listed in select box
        if analysis_option == 'Everything':
            draw_license_graph(sidebar_selection)

            all_results = []
            st.write(f'All the {css_green}Terms{css_end}, {css_blue}Conditions{css_end}, and {css_orange}Warranties{css_end} of {sidebar_selection}', unsafe_allow_html=True)

            results = license_rights(sidebar_selection)
            all_results.extend(results)

            col1, col2, col3= st.beta_columns(3)
            col1.header('Rights')
            for result in results:
                col1.write(f'{css_green}{result}{css_end}', unsafe_allow_html=True)

            results = license_conditions(sidebar_selection)
            all_results.extend(results)
            col2.header('Conditions')
            for result in results:
                col2.write(f'{css_blue}{result}{css_end}', unsafe_allow_html=True)

            results = warranty_type(sidebar_selection)
            all_results.extend(results)
            col3.header('Warranties')
            for result in results:
                col3.write(f'{css_orange}{result}{css_end}', unsafe_allow_html=True)

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

