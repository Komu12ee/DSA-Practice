class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alphadict={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        

        # print(alphadict)
        # for i in range(len(strs))
        # if i in check:
        #     i+=1
        #     continue
        # else:
        #     strng=strs[i]
        #     while strng:
        #         if strs[]    
        # alphadict = {key: 0 for key in alphadict}
        # print(alphadict)

        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())


        
     