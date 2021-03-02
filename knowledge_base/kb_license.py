from zincbase import KB

kb = KB()

# the primary owner of the project as a licensor
# and the git repo as a project
kb.store('isa(<github_username>, licensor)')
kb.store('isa(<github_repo>, repository)')

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

# made up conditions for merchantability and guarantee license
kb.store('extends(merchantability_license, private_use)')
kb.store('extends(guarantee_license, private_use)')

# What conditions (ONLY) are extended by a license?
# THE RULE
kb.store('extendsConditions(X, Y) :- extends(Y, X), isA(X, condition), isA(Y, license)')

# What permissions (ONLY) are extended by a license?
# THE RULE
kb.store('extendsRights(X, Y) :- extends(Y, X), isA(X, right), isA(Y, license)')

# What are ALL the terms and conditions a repository's license?
# THE RULE
kb.store('repositoryTermsConditions(X, Z) :- licenseOf(X, Y), extends(Y, Z), isA(Y, license)')

# What rights (ONLY) are extended by a repository?
# THE RULE
kb.store('repositoryRights(X, Z) :- licenseOf(X, Y), extendsRights(Z, Y)')

# What conditions (ONLY) are extended by a repository?
# THE RULE
kb.store('repositoryConditions(X, Z) :- licenseOf(X, Y), extendsConditions(Z, Y)')

