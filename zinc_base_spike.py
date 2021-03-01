from zincbase import KB

### A simple case of zinc KB
print('============================== kb.1')
# https://zincbase.readthedocs.io/en/latest/README.html#installation
kb1 = KB()
kb1.store('eats(cat, cheese)')

for ans in kb1.query('eats(cat, Food)'):
    print(ans['Food'])

###


print('============================== kb.2')

### A trial run for contract KB

# 'amanda' is the license owner and grantor
# 'billy' is the the grantee / user
kb = KB()

# make a fact
kb.store('grants(@amanda, license')
kb.store('receives(@billy, license')

kb.store('isa(license, mitLicense')


###