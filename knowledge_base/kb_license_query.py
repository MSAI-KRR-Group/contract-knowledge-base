from knowledge_base.kb_license_store import *

# What are ALL the terms and conditions a license?

def all_terms_conditions(license_type):
        search_term = 'TermsAndConditions'
        results = list(kb_license.query(f'extends({license_type}, {search_term})'))
        return [sub[search_term] for sub in results]

    # if license_type == 'GNU GPL 3.0':
    #     selection = 'gnu_license'

    # print('=== What are all the terms and conditions that a license-type can extend?')
    # print('gnu_license')
    #
    # print(list(kb_license.query('extends(gnu_license, TermsAndConditions)')))
    # print(list(kb_license.query('extends(mit_license, TermsAndConditions)')))
    # print(list(kb_license.query('extends(merchantability_license, TermsAndConditions)')))
    # print(list(kb_license.query('extends(guarantee_license, TermsAndConditions)')))
    # print()

def conditions_types_all():
    # What are the conditions of a license?
    print('=== What are all the possible types of license conditions?')
    print(list(kb_license.query('isA(Condition, condition)')))
    print()

def rights_types_all():
    # What are the rights of a license?
    print('=== What are all the possible rights of a license?')
    print(list(kb_license.query('isA(Right, right)')))
    print()

def license_types():
    # What types of licenses are available?
    print('=== What types of licenses are available?')
    print(list(kb_license.query('isA(License, license)')))
    print()

def license_conditions():
    # What conditions (ONLY) are extended by a license?
    print('=== What conditions (ONLY) are extended by a license?')
    print('gnu_license')
    print(list(kb_license.query('extendsConditions(Conditions, gnu_license)')))
    print('mit_license')
    print(list(kb_license.query('extendsConditions(Conditions, mit_license)')))
    print('merchantability_license')
    print(list(kb_license.query('extendsConditions(Conditions, merchantability_license)')))
    print('guarantee_license')
    print(list(kb_license.query('extendsConditions(Conditions, guarantee_license)')))
    print()

def license_permissions():
    # What permissions (ONLY) are extended by a license?
    print('=== What rights (ONLY) are extended by a license?')
    print('gnu_license')
    print(list(kb_license.query('extendsRights(Rights, gnu_license)')))
    print('mit_license')
    print(list(kb_license.query('extendsRights(Rights, mit_license)')))
    print('merchantability_license')
    print(list(kb_license.query('extendsRights(Rights, merchantability_license)')))
    print('guarantee_license')
    print(list(kb_license.query('extendsRights(Rights, guarantee_license)')))
    print()

def repository_license():
    # What is the license of a repository?
    print('=== What is the license of a repository?')
    print(list(kb_license.query('licenseOf(<github_repo>, License)')))
    print()

def repository_terms_conditions():
    # What are ALL the terms and conditions a repository's license?
    print('=== What are the terms and conditions a repository\'s license?')
    print(list(kb_license.query('repositoryTermsConditions(<github_repo>, TermsAndConditions)')))
    print()

def repository_rights():
    # What rights (ONLY) are extended by a repository?
    print('=== What rights (ONLY) are extended by a repository?')
    print(list(kb_license.query('repositoryRights(<github_repo>, RepositoryRights)')))
    print()

def repository_conditions():
    # What conditions (ONLY) are extended by a repository?
    print('=== What conditions (ONLY) are extended by a repository?')
    print(list(kb_license.query('repositoryConditions(<github_repo>, RepositoryConditions)')))
    print()

