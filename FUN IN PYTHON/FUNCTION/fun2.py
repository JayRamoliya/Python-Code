# default argument
# two parameter totaly require

def greeet(name='jay',msg='good'):
    print('hello ',name,', ',msg)

# greeet('monica','good morning')
# greeet()


# arbitrary argument
def gret(*name):
    for i in name:
        # print('hello ',name)
        print('hello ',i)

gret('jay','sneh','manav')


