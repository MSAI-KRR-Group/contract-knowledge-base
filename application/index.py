from application.config import *
from application.index_sidebar import main_menu
from knowledge_base.kb_license_query import all_terms_conditions
class Application():
    def __init__(self):
        st.set_page_config(page_title='Contract Companion')

    def run_app(self):
        self.frame()

    def frame(self):
        self.title()
        self.body()
        self.footer()

    def title(self):
        st.title('A Contract Companion')

    def body(self):
        st.markdown("<h3 style='text-align: center; color: black;font-family:courier;'> Your Contract, Your Knowledge </h3>", unsafe_allow_html=True)
        sidebar_selection = main_menu()

        if sidebar_selection == 'MIT License':
            st.header('The MIT License')
            analysis_option = st.selectbox('What do you want to know?', ['Everything', 'Rights', 'Conditions'])

            if analysis_option == 'Everything':
                st.write(f'All the Terms and Conditions of {sidebar_selection}')
                results = all_terms_conditions('mit_license')
                for result in results:
                    st.button(result)
            #TODO: configure results and options for each query type from kb_license_query
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


    def footer(self):
        st.markdown(
            '<i style="font-size:11px">Version Alpha</i>',
            unsafe_allow_html=True)

        st.markdown(
            '<i style="font-size:11px">&copy All Rights Reserved [The Project Group](https://github.com/MSAI-KRR-Group)</i>',
            unsafe_allow_html=True)
        st.markdown(
            '<p style="font-size:11px">The information provided by this app (the “Site”) is for general informational purposes only. All information on the Site is provided in good faith, however we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability or completeness of any information on the Site.</p>',
            unsafe_allow_html=True
        )
