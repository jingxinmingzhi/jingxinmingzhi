import io
a = io.StringIO('aghgh')
a.seek(1)
a.write('b')
print(a.getvalue())
