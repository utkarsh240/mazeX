from pyMaze import maze,COLOR,agent
m = maze(50,50)
m.CreateMaze(theme=COLOR.light)

a=agent(m,filled=True, footprints=True, color=COLOR.yellow) # arrow
# print(a.x)
# print(a.y)
# print(a.position)
# a.position = (5,6)
# a.position = (6,6)
# a.position = (7,6)
# a.position = (5,9)

m.tracePath({a:m.path}, delay=50)
m.run()