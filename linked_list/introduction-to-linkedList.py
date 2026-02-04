'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        # code here
        print(arr[0],end=" ")
        for i in range(1,len(arr)):
            print("->",arr[i],end=" ")
        
        
