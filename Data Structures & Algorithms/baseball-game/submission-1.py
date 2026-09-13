class Solution:
    def calPoints(self, operations: List[str]) -> int:
        k=0
        array=[]
        for i in range(len(operations)):
            if operations[i] == "+":
               array.append(array[k-2] + array[k-1])
               k+=1

            elif operations[i] == "D":
                array.append( 2* array[k-1])
                k+=1
            elif operations[i] == "C":
                array.pop(k-1)
                k=k-1
            else: 
                array.append( int(operations[i]))
                k=k+1

        return(sum(array)) 

        