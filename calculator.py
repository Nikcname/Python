class Tree(object):
  def __init__(self):
    self.left = None
    self.right = None
    self.data = None
    self.parent = None

#####################################
def printTree(root):
  if(root):
     printTree(root.left)
     print(root.data)
     printTree(root.right)

#####################################
def isinteger(var):
  try:
    float(var)
    return True
  except ValueError:
    return False


#####################################
def calculate(root):
  if root.left :
    calculate(root.left)
    if root.data == '+' :
      root.data = str(float(root.left.data) + float(root.right.data))
      return root.data
    elif root.data == '-':
      root.data = str(float(root.left.data) - float(root.right.data))
      return root.data
  return root.data

#####################################
def insrt(root, data, value):
  tmp = Tree()
  root.parent = tmp
  tmp.left = root
  tmp.data = data
  tmp.right = Tree()
  tmp.right.data = value
  tmp.right.parent = tmp
  return tmp

#####################################
def changeDtoO(root):
  if root.left:
    changeDtoO(root.left)
    if root.data == '/':
      if isinteger(root.left.data) == True:
        root.data = str(float(root.left.data) / float(root.right.data))
        root.left=None
        root.right=None
      elif isinteger(root.left.data) == False and root.parent:
        root.left.right.data = str(float(root.left.right.data) / float(root.right.data))
        root.left.parent = root.parent
        root.parent.left = root.left
      elif isinteger(root.left.data) == False and root.parent == None:
        root.left.right.data = str(float(root.left.right.data) / float(root.right.data))
        root.left.parent = None
        root = root.left
  return root

#####################################
def changeMtoO(root):
  if root.left:
    changeMtoO(root.left)
    if root.data == '*':
      if isinteger(root.left.data) == True:
        root.data = str(float(root.left.data) * float(root.right.data))
        root.left=None
        root.right=None
      elif isinteger(root.left.data) == False and root.parent:
        root.left.right.data = str(float(root.left.right.data) * float(root.right.data))
        root.left.parent = root.parent
        root.parent.left = root.left
      elif isinteger(root.left.data) == False and root.parent == None:
        root.left.right.data = str(float(root.left.right.data) * float(root.right.data))
        root.left.parent = None
        root = root.left
  return root
#####################################
sign_list = []
int_list = []
strin = input()
i = int(0)
j = int(0)
root = Tree()

j = i
if strin[i] == '-' or strin[i] == '+':
  i=i+1
while(i < len(strin)):
  if strin[i] == '+' or strin[i] == '-' or strin[i] == '/' or strin[i] == '*':
    sign_list.append(strin[i])
    int_list.append(strin[j:i])
    j = i + 1
  i=i+1
int_list.append(strin[j:i])

root.data = int_list[0]

for i in range(0, len(sign_list)):
  root = insrt(root, sign_list[i], float(int_list[i + 1]))

#printTree(root)

root = changeMtoO(root)
root = changeDtoO(root)

print(calculate(root))
