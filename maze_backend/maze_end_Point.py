"""
We can find the farthest point in a maze to be the end point from start(0,0) 
by the dijkstra's algorithm.
The function find_end will return the end point using the function make_step

"""

def make_step(mazelist,k,m,max_cord):

  """A function that places the value of all neighbouring
     co-ordinate to be the distance from start, in a demo
     temporary list(here it's 'm').
  """

  chk = False
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        if i>0 and m[i-1][j] == 0 and mazelist[i-1][j] == 0:
          m[i-1][j] = k + 1
          chk = True
          max_cord = (i-1,j)
        if j>0 and m[i][j-1] == 0 and mazelist[i][j-1] == 0:
          m[i][j-1] = k + 1
          chk = True
          max_cord = (i,j-1)
        if i<len(m)-1 and m[i+1][j] == 0 and mazelist[i+1][j] == 0:
          m[i+1][j] = k + 1
          chk = True
          max_cord = (i+1,j)
        if j<len(m[i])-1 and m[i][j+1] == 0 and mazelist[i][j+1] == 0:
           m[i][j+1] = k + 1
           chk = True
           max_cord = (i,j+1)
  
  if chk == True: return True, max_cord
  else: return (False, max_cord)


def find_end(mazelist):

    """
    This function finds the farthest co-ordinate from start,
    which is 0,0 to make that co-ordinate to be the destination.

    """

    start = 0,0
    m = []
    for i in range(len(mazelist)):
        m.append([])
        for j in range(len(mazelist[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1
    
    k = 0
    chk, max_cord = True, 0
    while chk == True:
        k += 1
        chk, max_cord = make_step(mazelist,k,m,max_cord)

    mazelist[max_cord[0]][max_cord[1]] = 3

    return mazelist
