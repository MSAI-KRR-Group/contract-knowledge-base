from zincbase import KB

kb = KB()

# the primary owner of the project as a licensor
# and the git repo as a project
kb.store('isa(<github_username>, licensor)')
kb.store('isa(<github_repo>, project)')

# two primary types of licenses on GitHub (MIT and GNU) and two generic ones for testing
kb.store('isA(mit_license, license)')
kb.store('isA(gnu_license, license)')
kb.store('isA(merchantability_license, license)')
kb.store('isA(guarantee_license, license)')

# broadly, two types of warranties
kb.store('isA(implied_warranty, warranty)')
kb.store('isA(expressed_warranty, warranty)')

# default to a single user being the licensor, author, and copyright holder
kb.store('licenseOf(<github_repo>, mit_license)')
kb.store('authorOf(<github_repo>, <github_username>)')
kb.store('copyrightHolderOf(<github_repo>, <github_username>)')

# categories of rights per GitHub
kb.store('isA(commercial_use, right)')
kb.store('isA(modification_use, right)')
kb.store('isA(distribution_use, right)')
kb.store('isA(private_use, right)')
kb.store('isA(patent_use, right)')

# categories of conditions per GitHub
kb.store('isA(license_notice, condition)')
kb.store('isA(copyright_notice, condition)')
kb.store('isA(state_changes, condition)')
kb.store('isA(disclose_source, condition)')
kb.store('isA(same_license, condition)')

# merchantability and guarantee generically extend a type of legal warranty
kb.store('extends(merchantability_license, implied_warranty)')
kb.store('extends(merchantability_license, disclose_source)')
kb.store('extends(guarantee_license, expressed_warranty)')
kb.store('extends(guarantee_license, disclose_source)')

# mit license permissions, limitations, and conditions per GitHub
kb.store('extends(mit_license, commercial_use)')
kb.store('extends(mit_license, modification_use)')
kb.store('extends(mit_license, distribution_use)')
kb.store('extends(mit_license, private_use)')
kb.store('extends(mit_license, license_notice)')
kb.store('extends(mit_license, copyright_notice)')

# gnu license permissions, limitations, and conditions per GitHub
kb.store('extends(gnu_license, commercial_use)')
kb.store('extends(gnu_license, modification_use)')
kb.store('extends(gnu_license, distribution_use)')
kb.store('extends(gnu_license, private_use)')
kb.store('extends(gnu_license, patent_use)')
kb.store('extends(gnu_license, license_notice)')
kb.store('extends(gnu_license, copyright_notice)')
kb.store('extends(gnu_license, state_changes)')
kb.store('extends(gnu_license, disclose_source)')
kb.store('extends(gnu_license, same_license)')

# made up conditions for merchantability and garuntee license
kb.store('extends(merchantability_license, private_use)')
kb.store('extends(guarantee_license, private_use)')

# What are the things that a license can extend?
print('=== What are all the things that a given license can extend?')
print('gnu_license')
print(list(kb.query('extends(gnu_license, LicenseTermsAndConditions)')))
print('mit_license')
print(list(kb.query('extends(mit_license, LicenseTermsAndConditions)')))
print('merchantability_license')
print(list(kb.query('extends(merchantability_license, LicenseTermsAndConditions)')))
print('guarantee_license')
print(list(kb.query('extends(guarantee_license, LicenseTermsAndConditions)')))
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
# THE RULE
kb.store('extendsConditions(X, Y) :- extends(Y, X), isA(X, condition), isA(Y, license)')
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
# THE RULE
kb.store('extendsRights(X, Y) :- extends(Y, X), isA(X, right), isA(Y, license)')
print('gnu_license')
print(list(kb.query('extendsRights(Rights, gnu_license)')))
print('mit_license')
print(list(kb.query('extendsRights(Rights, mit_license)')))
print('merchantability_license')
print(list(kb.query('extendsRights(Rights, merchantability_license)')))
print('guarantee_license')
print(list(kb.query('extendsRights(Rights, guarantee_license)')))
print()


