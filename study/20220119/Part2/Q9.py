a = dict()

a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' error
a[250] = 'python'

print(a)