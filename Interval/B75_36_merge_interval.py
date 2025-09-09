# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         newnode=intervals[0]
#         res=[]
#         count=0
#         intervals.sort(key=lambda x: x[0])
#         print(intervals)

#         for i in range(1,len(intervals)):
#             if intervals[i][1]<newnode[0]:
#                 res.append(intervals[i])
#             elif intervals[i][1]<=newnode[1] and intervals[i][0]>=newnode[0]:   
#                 newnode=newnode 
#             elif intervals[i][0]>newnode[1]:
#                 res.append(newnode)    
#                 newnode=intervals[i]
#             elif intervals[i][0]<=newnode[1] and intervals[i][1]<=newnode[0]:
#                 newnode[0]=min(newnode[0],intervals[i][0])
#                 newnode[1]=max(newnode[1],intervals[i][1])
#                 count=i
#             elif intervals[i][0]<=newnode[1] and intervals[i][1]>=newnode[0]:
#                 newnode[0]=min(newnode[0],intervals[i][0])
#                 newnode[1]=max(newnode[1],intervals[i][1])
#                 print("ye chala")
#                 count=i    
#             elif intervals[i][0]<=newnode[1] and intervals[i][1]<=newnode[1]:
#                 newnode[0]=min(newnode[0],intervals[i][0])
#                 newnode[1]=max(newnode[1],intervals[i][1])
#                 count=i    
#             elif intervals[i][0]<=newnode[1] and intervals[i][1]>=newnode[1]:
#                 newnode[0]=min(newnode[0],intervals[i][0])
#                 newnode[1]=max(newnode[1],intervals[i][1])
#                 count=i
#         # if count==len(intervals)-1:
#         print(count)
#         res.append(newnode)     
#         return res       


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            # If current interval overlaps with last in res
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res
