import re

p = re.compile('[abc]')
m = p.match("a")
print(m)
m = p.match("before")
print(m)
m = p.match("dude")
print(m)
m = p.match("dad")
print(m)

p = re.compile('[abc][abc]')
m = p.match("dad")
print(m)
p = re.compile('d[abc]d1')
m = p.match("dad")
print(m)

p = re.compile('\D+')
m = p.match("hello")
m = p.search("3.Homenetwork hello")
print(m)
