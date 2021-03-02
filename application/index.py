from application.config import *
from application.index_sidebar import main_menu
from application.index_main_queries import query_kb


class Application():
    def __init__(self):
        # the text that displays in the tab at the very top of the page
        st.set_page_config(page_title='Contract Companion')

    def run_app(self):
        # primary app call will run everything contained in frame()
        self.frame()

    def frame(self):
        # place main components of page here, add more as necessary
        self.title()
        self.body()
        self.footer()

    def title(self):
        # execute st calls for title section
        st.title('A Contract Companion')

    def body(self):
        # execute st calls for body section
        # a header for this section
        st.markdown("<h3 style='text-align: center; color: black;font-family:courier;'> Your Contract, Your Knowledge </h3>", unsafe_allow_html=True)

        # makes a sidebar selection in index
        sidebar_selection = main_menu()

        # if there is a selection, run a query based on the selected value
        if sidebar_selection:
            # call the helper function
            query_kb(sidebar_selection)


    def footer(self):
        # make st calls for footer section here
        st.markdown(
            '<i style="font-size:11px">Version Alpha\nPowered by [Zincbase](https://github.com/tomgrek/zincbase)</i>',
            unsafe_allow_html=True)
        st.markdown(
            '<i style="font-size:11px">&copy All Rights Reserved [The Project Group](https://github.com/MSAI-KRR-Group)</i>',
            unsafe_allow_html=True)
        st.markdown(
            '<p style="font-size:11px">The information provided by this app (the “Site”) is for general informational purposes only. All information on the Site is provided in good faith, however we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability or completeness of any information on the Site.</p>',
            unsafe_allow_html=True
        )
