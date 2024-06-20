#dfs
def dfs(a,v,s,e):
  if v[e]==False:
    s.append(e)
    v[e]=True
  else:
    return
  for i in a[e]:
    dfs(a,v,s,i[1])
  print(s.pop())
  
a={1:[(1,2,0),(1,3,0)],2:[(2,1,0),(2,7,0)],3:[(3,1,0),(3,6,0),(3,5,0)],4:[(4,7,0),(4,8,0)],5:[(5,3,0),(5,7,0)],6:[(6,3,0),(6,8,0)],7:[(7,2,0),(7,5,0),(7,4,0)],8:[(8,4,0),(8,6,0),(8,6,0)]}
v={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}
s=[]#a=graph,v=visited,s=stack
for i in a:
  dfs(a,v,s,i) 





#bfs
def bfs(g,e):
  Q=[e]
  v={}
  for i in g.keys():
    v[i]=False
  v[e]=True
  while Q:
    curr=Q.pop(0)
    print(curr)
    for i in g[curr]:
      if v[i[1]]==False:
        Q.append(i[1])
        v[i[1]]=True
  
  
g={1:[(1,2,0),(1,3,0)],
   2:[(2,1,0),(2,7,0)],
   3:[(3,1,0),(3,6,0),(3,5,0)],
   4:[(4,7,0),(4,8,0)],
   5:[(5,3,0),(5,7,0)],
   6:[(6,3,0),(6,8,0)],
   7:[(7,2,0),(7,5,0),(7,4,0)],
   8:[(8,4,0),(8,6,0)]}

bfs(g,1)


#bst
class Node:
  def __init__(self,value):
    self.data=value
    self.left=None
    self.right=None
def insertbst(root,value):
  if root==None:
    return Node(value)
    
  if root.data>value:
    root.left=insertbst(root.left,value)
  elif root.data<value:
    root.right=insertbst(root.right,value)
  return root
    
  
def inorder(root):
  if root==None:
    return
  

  inorder(root.left)
  print(root.data)
  inorder(root.right)

l=[4,6,7,3,8,2,5,9,1]
root=Node(l[0])

for i in range(1,len(l)):
  insertbst(root,l[i])
inorder(root)