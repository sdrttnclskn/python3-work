>>> x = [1,2,3,4]
>>> x
[1, 2, 3, 4]
>>> maaslar =[1000,30000,4000,7000,76000]
>>> maaslar
[1000, 30000, 4000, 7000, 76000]
>>> maaslar[3]
7000
>>> maaslar[-3]
4000
>>> maaslar[2:]
[4000, 7000, 76000]
>>> maaslar.append(1000)
>>> maaslar
[1000, 30000, 4000, 7000, 76000, 1000]
>>> maaslar + x
[1000, 30000, 4000, 7000, 76000, 1000, 1, 2, 3, 4]
>>> maalar = maaslar + x
>>> maaslar
[1000, 30000, 4000, 7000, 76000, 1000]
>>> maaslar + x
[1000, 30000, 4000, 7000, 76000, 1000, 1, 2, 3, 4]
>>> _
[1000, 30000, 4000, 7000, 76000, 1000, 1, 2, 3, 4]
>>> maaslar.append(7**3)
>>> maaslar
[1000, 30000, 4000, 7000, 76000, 1000, 343]
>>> ll = [maaslar,x]
>>> len(ll)
2
>>> ll
[[1000, 30000, 4000, 7000, 76000, 1000, 343], [1, 2, 3, 4]]
>>> ll[1]
[1, 2, 3, 4]
>>> ll[0]
[1000, 30000, 4000, 7000, 76000, 1000, 343]
>>> ll[0][1]
30000
>>> ll[1][2]
3
>>> maaslar.append(11)
>>> ll
[[1000, 30000, 4000, 7000, 76000, 1000, 343, 11], [1, 2, 3, 4]]
>>> 
