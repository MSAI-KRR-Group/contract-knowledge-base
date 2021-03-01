from zincbase import KB


# https://zincbase.readthedocs.io/en/latest/README.html#installation
# try a working knowledge base - simple case
kb = KB()
kb.store('eats(cat, cheese)')

for ans in kb.query('eats(cat, Food)'):
    print(ans['Food'])