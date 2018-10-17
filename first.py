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
def calculate(root):
  if root.left :
    calculate(root.left)
    if root.data == '+' :
      root.data = str(int(root.left.data) + int(root.right.data))
      return root.data
    elif root.data == '-':
      root.data = str(int(root.left.data) - int(root.right.data))
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
sign_list = []
int_list = []
strin = "3-14+61+7"
i = int(0)
j = int(0)
root = Tree()

j = i
sign = strin[i]
while(i < len(strin)):
  if strin[i] == '+' or strin[i] == '-' or strin[i] == '/' or strin[i] == '*':
    sign_list.append(strin[i])
    int_list.append(strin[j:i])
    j = i + 1
  i=i+1

int_list.append(strin[j:i])
root.data = int_list[0]

for i in range(0, len(sign_list)):
  root = insrt(root, sign_list[i], int(int_list[i + 1]))

print(calculate(root))
