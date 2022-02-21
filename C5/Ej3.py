s1 ='{0}, {1}, {2}'.format('a', 'b', 'c')
print(s1)
# 'a, b, c'
s2 ='{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
print(s2)
# 'a, b, c'
s3 ='{2}, {1}, {0}'.format('a', 'b', 'c')
print(s3)
# 'c, b, a'
s4 ='{2}, {1}, {0}'.format(*'abc')     
print(s4)
# 'c, b, a'
s5 ='{0}{1}{0}'.format('abra', 'cad')   
print(s5)
# 'abracadabra'