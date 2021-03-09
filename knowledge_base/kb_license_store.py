# STORE queries HERE

from knowledge_base.config import *

def license_mt():
    kb = KB()
    kb.name = 'contract_companion'

    # the primary owner of the project as a licensor
    # and the git repo as a project
    kb.store(f'{isA}(<github_username>, licensor)')
    kb.store(f'{isA}(<github_repo>, repository)')

    # two primary types of licenses on GitHub (MIT and GNU) and two generic ones for testing
    kb.store(f'{isA}({mit_license}, license)')
    kb.store(f'{isA}({gnu_license}, license)')
    kb.store(f'{isA}({merchantability_license}, license)')
    kb.store(f'{isA}({guarantee_license}, license)')

    # broadly, two types of warranties
    kb.store(f'{isA}({implied_warranty}, {warranty})')
    kb.store(f'{isA}({expressed_warranty}, {warranty})')

    # default to a single user being the licensor, author, and copyright holder
    kb.store(f'{licenseOf}(<github_repo>, {mit_license})')
    kb.store(f'{authorOf}(<github_repo>, <github_username>)')
    kb.store(f'{copyrightHolderOf}(<github_repo>, <github_username>)')

    # categories of rights per GitHub
    kb.store(f'{isA}({commercial_use}, {right})')
    kb.store(f'{isA}({modification_use}, {right})')
    kb.store(f'{isA}({distribution_use}, {right})')
    kb.store(f'{isA}({private_use}, {right})')
    kb.store(f'{isA}({patent_use}, {right})')

    # categories of conditions per GitHub
    kb.store(f'{isA}({license_notice}, {condition})')
    kb.store(f'{isA}({copyright_notice}, {condition})')
    kb.store(f'{isA}({state_changes}, {condition})')
    kb.store(f'{isA}({disclose_source}, {condition})')
    kb.store(f'{isA}({same_license}, {condition})')

    # merchantability and guarantee generically extend a type of legal warranty
    kb.store(f'{extends}({merchantability_license}, {implied_warranty})')
    kb.store(f'{extends}({merchantability_license}, {disclose_source})')
    kb.store(f'{extends}({guarantee_license}, {expressed_warranty})')
    kb.store(f'{extends}({guarantee_license}, {disclose_source})')

    # mit license permissions, limitations, and conditions per GitHub
    kb.store(f'{extends}({mit_license}, {commercial_use})')
    kb.store(f'{extends}({mit_license}, {modification_use})')
    kb.store(f'{extends}({mit_license}, {distribution_use})')
    kb.store(f'{extends}({mit_license}, {private_use})')
    kb.store(f'{extends}({mit_license}, {license_notice})')
    kb.store(f'{extends}({mit_license}, {copyright_notice})')

    # gnu license permissions, limitations, and conditions per GitHub
    kb.store(f'{extends}({gnu_license}, {commercial_use})')
    kb.store(f'{extends}({gnu_license}, {modification_use})')
    kb.store(f'{extends}({gnu_license}, {distribution_use})')
    kb.store(f'{extends}({gnu_license}, {private_use})')
    kb.store(f'{extends}({gnu_license}, {patent_use})')
    kb.store(f'{extends}({gnu_license}, {license_notice})')
    kb.store(f'{extends}({gnu_license}, {copyright_notice})')
    kb.store(f'{extends}({gnu_license}, {state_changes})')
    kb.store(f'{extends}({gnu_license}, {disclose_source})')
    kb.store(f'{extends}({gnu_license}, {same_license})')

    # made up conditions for merchantability and guarantee license
    kb.store(f'{extends}({merchantability_license}, {private_use})')
    kb.store(f'{extends}({guarantee_license}, {private_use})')

    # What conditions (ONLY) are extended by a license?
    # THE RULE
    kb.store(f'{extendsConditions}(X, Y) :- {extends}(Y, X), {isA}(X, {condition}), {isA}(Y, license)')

    # What permissions (ONLY) are extended by a license?
    # THE RULE
    kb.store(f'{extendsRights}(X, Y) :- {extends}(Y, X), {isA}(X, {right}), {isA}(Y, license)')

    # What are ALL the terms and conditions a repository's license?
    # THE RULE
    kb.store(f'{repositoryTermsConditions}(X, Z) :- {licenseOf}(X, Y), {extends}(Y, Z), {isA}(Y, license)')

    # What rights (ONLY) are extended by a repository?
    # THE RULE
    kb.store(f'{repositoryRights}(X, Z) :- {licenseOf}(X, Y), {extendsRights}(Z, Y)')

    # What conditions (ONLY) are extended by a repository?
    # THE RULE
    kb.store(f'{repositoryConditions}(X, Z) :- {licenseOf}(X, Y), {extendsConditions}(Z, Y)')


    # What warranties does a license extend?
    # THE RULE
    kb.store(f'{extendsWarranties}(X, Y) :- {extends}(Y, X), {isA}(X, {warranty}), {isA}(Y, license)')

    #TODO Implement Goals
    ### this section is for linking users to goals to contracts
    ## Describe goals that people have with regards to contracts
    kb.store(f'({goal})')
    # add new goals to a list and allow KB to apply them in a loop
    mit_goals = ['short', 'easy_to_understand', 'permissive', 're_releasable', 'enable_as_dependency_in_other_projects', 'popular', 'no_warranty']
    for a_goal in mit_goals:
        kb.store(f'{isA}({a_goal}{goal})')
        kb.store(f'{supportsGoal}({mit_license}{a_goal})')

    gnu_goals = ['do_not_enable_use_in_closed_software', 'strong_copyleft', 'no_warranty']
    for a_goal in gnu_goals:
        kb.store(f'{isA}({a_goal}{goal})')
        kb.store(f'{supportsGoal}({gnu_license}{a_goal})')

    merchantability_goals = ['extend_warranty', 'implied_warranty']
    for a_goal in merchantability_goals:
        kb.store(f'{isA}({a_goal}{goal})')
        kb.store(f'{supportsGoal}({merchantability_license}{a_goal})')

    guarantee_goals = ['extend_warranty', 'expressed_warranty']
    for a_goal in guarantee_goals:
        kb.store(f'{isA}({a_goal}{goal})')
        kb.store(f'{supportsGoal}({guarantee_license}{a_goal})')
    ### this section is for linking users to goals to contracts

    # add comments about facts in the KB
    kb.node(mit_license).comment = "The MIT License is a permissive type of copyleft license, it permits reuse within proprietary software so long as all copies of the software include a copy of the license."
    kb.node(gnu_license).comment = "The GNU GPL License is a classic type of copyleft license, it allows for reuse but requires that all derivative works maintain similar licensing terms."
    kb.node(merchantability_license).comment = "Merchantability is a fictitious license type that extends a type of warranty known as implied warranty."
    kb.node(guarantee_license).comment = "Guarantee is a fictitious license type that extends a type of warranty known as expressed warranty."
    kb.node(right).comment = "A claim recognized and delimited by law for the purpose of securing it - Websters."
    kb.node(commercial_use).comment = "Commercial use describes any activity in which you use a product or service for financial gain."
    kb.node(goal).comment = r'''A copyright holder's expectation of a contract or a users's expectation of a contract. Broadly, a time-bound expectation expressed in one or more objectives that is measurable and has a definitive end-result, from thelawdictionary.'''

    return kb