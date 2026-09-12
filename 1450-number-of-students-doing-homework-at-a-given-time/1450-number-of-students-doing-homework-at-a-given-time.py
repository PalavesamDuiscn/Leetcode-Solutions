class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        count=0
        for i,j  in zip(startTime,endTime):
            for i in range(i,j+1):
                if i==queryTime:
                    count+=1
                    break
        return count
        