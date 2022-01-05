# 1991번

import sys
input = sys.stdin.readline

def preorder(item):
    if item != ".":
        print(item, end = "")
        a, b = tree[item]
        preorder(a)
        preorder(b)

def inorder(item):
    if item != ".":
        a, b = tree[item]
        inorder(a)
        print(item, end = "")
        inorder(b)

def postorder(item):
    if item != ".":
        a, b = tree[item]
        postorder(a)
        postorder(b)
        print(item, end = "")

tree = dict()
for i in range(int(input())):
    temp = input().rstrip().split()
    tree[temp[0]] = [temp[1], temp[2]]

preorder("A")
print()
inorder("A")
print()
postorder("A")

