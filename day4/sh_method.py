astr = '\thello   '
print(astr)
print(astr.strip())   # 去除两端空白字符
print(astr.lstrip()) # 去除左端空白字符
print(astr.rstrip())  # 去除右端空白字符
print('hello.tar.gz'.split('.'))

hi = 'hello world'
print(hi.title())
print(hi.upper())
print(hi.lower())
print(hi.istitle())
print('hao123'.isdigit())
print(hi.isidentifier())
print(hi.center(50))
print(hi.center(50,'#'))
print(hi.ljust(50,'#'))
print(hi.rjust(50,'#'))
print(hi.startswith('he'))
print(hi.endswith('d'))