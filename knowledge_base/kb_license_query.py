# Make queries HERE
from knowledge_base.config import *
from knowledge_base.kb_license_store import license_mt

def all_terms_conditions(license_type):
    kb_license = license_mt()
    # return all terms and conditions of a license
    search_term = 'TermsAndConditions'
    results = list(kb_license.query(f'{extends}({license_type}, {search_term})'))
    return [sub[search_term] for sub in results]

    # examples of how this works
    # What are ALL the terms and conditions a license?
    # print('=== What are all the terms and conditions that a license-type can extend?')
    # print('gnu_license')
    # print(list(kb_license.query('extends(gnu_license, TermsAndConditions)')))
    # print(list(kb_license.query('extends(mit_license, TermsAndConditions)')))
    # print(list(kb_license.query('extends(merchantability_license, TermsAndConditions)')))
    # print(list(kb_license.query('extends(guarantee_license, TermsAndConditions)')))
    # print()

#TODO, finish building the app to call of the rest of these queries
def conditions_types_all():
    kb_license = license_mt()
    # return all types of conditions in the kb
    search_term = 'Condition'
    results = list(kb_license.query(f'{isA}({search_term}, {condition})'))
    return [sub[search_term] for sub in results]

    # examples of how this works
    # What are the conditions of a license?
    # print('=== What are all the possible types of license conditions?')
    # print(list(kb_license.query('isA(Condition, condition)')))
    # print()

def rights_types_all():
    kb_license = license_mt()
    # return all types of rights in the kb
    search_term = 'Right'
    results = list(kb_license.query(f'{isA}({search_term}, {right})'))
    return [sub[search_term] for sub in results]

    # examples of how this works
    # What are the rights of a license?
    # print('=== What are all the possible rights of a license?')
    # print(list(kb_license.query('isA(Right, right)')))
    # print()

def license_types():
    kb_license = license_mt()
    # return all types of licenses in the KB
    search_term = 'License'
    results = list(kb_license.query(f'{isA}({search_term}, license)'))
    return [sub[search_term] for sub in results]

    # examples of how this works
    # What types of licenses are available?
    # print('=== What types of licenses are available?')
    # print(list(kb_license.query('isA(License, license)')))
    # print()

def license_conditions(license_type):
    kb_license = license_mt()
    # return the all the conditions of a license
    search_term = 'Conditions'
    results = list(kb_license.query(f'{extendsConditions}({search_term}, {license_type})'))
    return [sub[search_term] for sub in results]

    # examples of how this works
    # What conditions (ONLY) are extended by a license?
    # print('=== What conditions (ONLY) are extended by a license?')
    # print('gnu_license')
    # print(list(kb_license.query('extendsConditions(Conditions, gnu_license)')))
    # print('mit_license')
    # print(list(kb_license.query('extendsConditions(Conditions, mit_license)')))
    # print('merchantability_license')
    # print(list(kb_license.query('extendsConditions(Conditions, merchantability_license)')))
    # print('guarantee_license')
    # print(list(kb_license.query('extendsConditions(Conditions, guarantee_license)')))
    # print()

def license_rights(license_type):
    kb_license = license_mt()
    # return the all the rights of a license
    search_term = 'Rights'
    results = list(kb_license.query(f'{extendsRights}({search_term}, {license_type})'))
    return [sub[search_term] for sub in results]

    # examples of how this works
    # What permissions (ONLY) are extended by a license?
    # print('=== What rights (ONLY) are extended by a license?')
    # print('gnu_license')
    # print(list(kb_license.query('extendsRights(Rights, gnu_license)')))
    # print('mit_license')
    # print(list(kb_license.query('extendsRights(Rights, mit_license)')))
    # print('merchantability_license')
    # print(list(kb_license.query('extendsRights(Rights, merchantability_license)')))
    # print('guarantee_license')
    # print(list(kb_license.query('extendsRights(Rights, guarantee_license)')))
    # print()

#TODO: How to implement a workflow of queries based on repository? Can we link back to actual repo?
def repository_license(repo_name='<github_repo>'):
    kb_license = license_mt()
    search_term = 'License'
    results = list(kb_license.query(f'{licenseOf}({repo_name}, {search_term})'))
    return [sub[search_term] for sub in results]

    # example of how this works
    # What is the license of a repository?
    # print('=== What is the license of a repository?')
    # print(list(kb_license.query(f'licenseOf(<github_repo>, License)')))
    # print()

def repository_terms_conditions(repo_name='<github_repo>'):
    kb_license = license_mt()
    search_term = 'TermsAndConditions'
    results = list(kb_license.query(f'{repositoryTermsConditions}({repo_name}, {search_term})'))
    return [sub[search_term] for sub in results]

    # example of how this works
    # What are ALL the terms and conditions a repository's license?
    # print('=== What are the terms and conditions a repository\'s license?')
    # print(list(kb_license.query('repositoryTermsConditions(<github_repo>, TermsAndConditions)')))
    # print()

def repository_rights(repo_name='<github_repo>'):
    kb_license = license_mt()
    search_term = 'RepositoryRights'
    results = list(kb_license.query(f'{repositoryRights}({repo_name}, {search_term})'))
    return [sub[search_term] for sub in results]

    # example of how this works
    # What rights (ONLY) are extended by a repository?
    # print('=== What rights (ONLY) are extended by a repository?')
    # print(list(kb_license.query('repositoryRights(<github_repo>, RepositoryRights)')))
    # print()

def repository_conditions(repo_name='<github_repo>'):
    kb_license = license_mt()
    search_term = 'RepositoryConditions'
    results = list(kb_license.query(f'{repositoryConditions}({repo_name}, {search_term})'))
    return [sub[search_term] for sub in results]

    # example of how this works
    # What conditions (ONLY) are extended by a repository?
    # print('=== What conditions (ONLY) are extended by a repository?')
    # print(list(kb_license.query('repositoryConditions(<github_repo>, RepositoryConditions)')))
    # print()

def warranty_type(license_type):
    kb_license = license_mt()
    # return all terms and conditions of a license
    search_term = 'Warranty'
    results = list(kb_license.query(f'{extendsWarranties}({search_term}, {license_type})'))
    return [sub[search_term] for sub in results]

def warranty_all():
    kb_license = license_mt()
    # return all types of conditions in the kb
    search_term = 'Warranty'
    results = list(kb_license.query(f'{isA}({search_term}, {warranty})'))
    return [sub[search_term] for sub in results]

def get_comment(x):
    kb_license = license_mt()
    return kb_license.node(x).comment
