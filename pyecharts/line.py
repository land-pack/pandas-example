from pyecharts import Line

attr = ['jack', 'car', 'dog', 'cat', 'socket', 'git']

v1 = [ 5, 20, 36, 10, 10, 20]
v2 = [ 14, 10, 26, 20, 40, 10]

line = Line('Line Demo')

line.add('User A', attr, v1, mark_point=['average'])
line.add('User B', attr, v2, mark_point=['average', "max"], is_smooth=True)


line.show_config()
line.render()
