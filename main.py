from knowledge_base.kb_license import *

# What are ALL the terms and conditions a license?
print('=== What are all the terms and conditions that a license-type can extend?')
print('gnu_license')
print(list(kb.query('extends(gnu_license, TermsAndConditions)')))
print('mit_license')
print(list(kb.query('extends(mit_license, TermsAndConditions)')))
print('merchantability_license')
print(list(kb.query('extends(merchantability_license, TermsAndConditions)')))
print('guarantee_license')
print(list(kb.query('extends(guarantee_license, TermsAndConditions)')))
print()

# What are the conditions of a license?
print('=== What are all the possible types of license conditions?')
print(list(kb.query('isA(Condition, condition)')))
print()

# What are the rights of a license?
print('=== What are all the possible rights of a license?')
print(list(kb.query('isA(Right, right)')))
print()

# What types of licenses are available?
print('=== What types of licenses are available?')
print(list(kb.query('isA(License, license)')))
print()

# What conditions (ONLY) are extended by a license?
print('=== What conditions (ONLY) are extended by a license?')
print('gnu_license')
print(list(kb.query('extendsConditions(Conditions, gnu_license)')))
print('mit_license')
print(list(kb.query('extendsConditions(Conditions, mit_license)')))
print('merchantability_license')
print(list(kb.query('extendsConditions(Conditions, merchantability_license)')))
print('guarantee_license')
print(list(kb.query('extendsConditions(Conditions, guarantee_license)')))
print()

# What permissions (ONLY) are extended by a license?
print('=== What rights (ONLY) are extended by a license?')
print('gnu_license')
print(list(kb.query('extendsRights(Rights, gnu_license)')))
print('mit_license')
print(list(kb.query('extendsRights(Rights, mit_license)')))
print('merchantability_license')
print(list(kb.query('extendsRights(Rights, merchantability_license)')))
print('guarantee_license')
print(list(kb.query('extendsRights(Rights, guarantee_license)')))
print()

# What is the license of a repository?
print('=== What is the license of a repository?')
print(list(kb.query('licenseOf(<github_repo>, License)')))
print()

# What are ALL the terms and conditions a repository's license?
print('=== What are the terms and conditions a repository\'s license?')
print(list(kb.query('repositoryTermsConditions(<github_repo>, TermsAndConditions)')))
print()

# What rights (ONLY) are extended by a repository?
print('=== What rights (ONLY) are extended by a repository?')
print(list(kb.query('repositoryRights(<github_repo>, RepositoryRights)')))
print()

# What conditions (ONLY) are extended by a repository?
print('=== What conditions (ONLY) are extended by a repository?')
print(list(kb.query('repositoryConditions(<github_repo>, RepositoryConditions)')))
print()

