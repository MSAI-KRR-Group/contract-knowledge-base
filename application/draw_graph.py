from application.config import *
import graphviz as graphviz
from graphviz import Source
from knowledge_base.kb_license_store import *
from knowledge_base.kb_license_query import *

def draw_license_graph(x):

    G = graphviz.Digraph()

    G.edge(x, 'license', label='isA')

    all_tc = all_terms_conditions(x)
    rights = license_rights(x)
    conditions = license_conditions(x)

    G.edge(x, 'conditions', label='extendsConditions')
    G.edge(x, 'rights', label='extendsRights')

    st.write('The Current Knowledge Graph')

    st.graphviz_chart(G)

def draw_rights_graph(x):

    G = graphviz.Digraph()

    G.edge(x, 'license', label='isA')

    rights = license_rights(x)

    G.edge(x, 'rights', label='extendsRights')

    for i in rights:
        G.edge('rights', i, label='extends')

    st.write('The Current Knowledge Graph')

    st.graphviz_chart(G)

def draw_conditions_graph(x):

    G = graphviz.Digraph()

    G.edge(x, 'license', label='isA')

    conditions = license_conditions(x)

    G.edge(x, 'conditions', label='extendsConditions')

    for i in conditions:
        G.edge('conditions', i, label='extends')

    st.write('The Current Knowledge Graph')

    st.graphviz_chart(G)


def draw_repo_graph(repo, license):
    G = graphviz.Digraph()

    G.edge(repo, 'repository', label='isA')
    G.edge(license, repo, label='licenseOf')
    G.edge(license, 'conditions', label='extendsConditions')
    G.edge(license, 'rights', label='extendsRights')
    G.edge(repo, 'conditions', label='repositoryConditions')
    G.edge(repo, 'rights', label='repositoryRights')

    st.write('The Current Knowledge Graph')

    st.graphviz_chart(G)
