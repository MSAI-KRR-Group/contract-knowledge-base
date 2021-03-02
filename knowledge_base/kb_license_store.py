from knowledge_base.config import kb_license

# the primary owner of the project as a licensor
# and the git repo as a project
kb_license.store('isa(<github_username>, licensor)')
kb_license.store('isa(<github_repo>, repository)')

# two primary types of licenses on GitHub (MIT and GNU) and two generic ones for testing
kb_license.store('isA(mit_license, license)')
kb_license.store('isA(gnu_license, license)')
kb_license.store('isA(merchantability_license, license)')
kb_license.store('isA(guarantee_license, license)')

# broadly, two types of warranties
kb_license.store('isA(implied_warranty, warranty)')
kb_license.store('isA(expressed_warranty, warranty)')

# default to a single user being the licensor, author, and copyright holder
kb_license.store('licenseOf(<github_repo>, mit_license)')
kb_license.store('authorOf(<github_repo>, <github_username>)')
kb_license.store('copyrightHolderOf(<github_repo>, <github_username>)')

# categories of rights per GitHub
kb_license.store('isA(commercial_use, right)')
kb_license.store('isA(modification_use, right)')
kb_license.store('isA(distribution_use, right)')
kb_license.store('isA(private_use, right)')
kb_license.store('isA(patent_use, right)')

# categories of conditions per GitHub
kb_license.store('isA(license_notice, condition)')
kb_license.store('isA(copyright_notice, condition)')
kb_license.store('isA(state_changes, condition)')
kb_license.store('isA(disclose_source, condition)')
kb_license.store('isA(same_license, condition)')

# merchantability and guarantee generically extend a type of legal warranty
kb_license.store('extends(merchantability_license, implied_warranty)')
kb_license.store('extends(merchantability_license, disclose_source)')
kb_license.store('extends(guarantee_license, expressed_warranty)')
kb_license.store('extends(guarantee_license, disclose_source)')

# mit license permissions, limitations, and conditions per GitHub
kb_license.store('extends(mit_license, commercial_use)')
kb_license.store('extends(mit_license, modification_use)')
kb_license.store('extends(mit_license, distribution_use)')
kb_license.store('extends(mit_license, private_use)')
kb_license.store('extends(mit_license, license_notice)')
kb_license.store('extends(mit_license, copyright_notice)')

# gnu license permissions, limitations, and conditions per GitHub
kb_license.store('extends(gnu_license, commercial_use)')
kb_license.store('extends(gnu_license, modification_use)')
kb_license.store('extends(gnu_license, distribution_use)')
kb_license.store('extends(gnu_license, private_use)')
kb_license.store('extends(gnu_license, patent_use)')
kb_license.store('extends(gnu_license, license_notice)')
kb_license.store('extends(gnu_license, copyright_notice)')
kb_license.store('extends(gnu_license, state_changes)')
kb_license.store('extends(gnu_license, disclose_source)')
kb_license.store('extends(gnu_license, same_license)')

# made up conditions for merchantability and guarantee license
kb_license.store('extends(merchantability_license, private_use)')
kb_license.store('extends(guarantee_license, private_use)')

# What conditions (ONLY) are extended by a license?
# THE RULE
kb_license.store('extendsConditions(X, Y) :- extends(Y, X), isA(X, condition), isA(Y, license)')

# What permissions (ONLY) are extended by a license?
# THE RULE
kb_license.store('extendsRights(X, Y) :- extends(Y, X), isA(X, right), isA(Y, license)')

# What are ALL the terms and conditions a repository's license?
# THE RULE
kb_license.store('repositoryTermsConditions(X, Z) :- licenseOf(X, Y), extends(Y, Z), isA(Y, license)')

# What rights (ONLY) are extended by a repository?
# THE RULE
kb_license.store('repositoryRights(X, Z) :- licenseOf(X, Y), extendsRights(Z, Y)')

# What conditions (ONLY) are extended by a repository?
# THE RULE
kb_license.store('repositoryConditions(X, Z) :- licenseOf(X, Y), extendsConditions(Z, Y)')

