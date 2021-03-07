# this area is just for debugging etc
# scrips are called by app from application
from knowledge_base.kb_license_query import all_terms_conditions
from knowledge_base.kb_license_store import *

if __name__ == '__main__':

    # print(kb_license.name)
    all_nodes = kb_license.nodes()
    all_edges = kb_license.edges()

    kb_license.plot()

