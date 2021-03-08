# this area is just for debugging etc
# scrips are called by app from application
from knowledge_base.kb_license_query import all_terms_conditions
from knowledge_base.kb_license_store import *

if __name__ == '__main__':

    # print(kb_license.name)
    all_nodes = kb_license.nodes()
    all_edges = kb_license.edges()

    # kb_license.plot()
    # kb_license.attr('mit_license', {'comment': "A permissive type of copyleft license."})
    # kb_license.node('mit_license').comment = "The MIT License is a permissive type of copyleft license."
    # print(kb_license.node('mit_license').attrs)
    license_type = 'merchantability_license'
    search_term = 'Warranty'
    results = list(kb_license.query(f'extendsWarranties({search_term}, {license_type})'))
    result =  [sub[search_term] for sub in results]

    print(result)

