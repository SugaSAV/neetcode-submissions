class Solution:
    def countSeniors(self, details: List[str]) -> int:
       srCcount = 0
       for i in details:
           if int(i[11:13]) > 60:
              srCcount += 1
       return srCcount