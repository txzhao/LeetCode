class Solution(object):
    def fizzBuzz(self, n):
        # Write a program that outputs the string representation of numbers from 1 to n.
        # for multiples of three, output “Fizz” instead of the number; for multiples of five output “Buzz”. 
        # For numbers which are multiples of both three and five output “FizzBuzz”.
        # type n: int
        # rtype: List[str]
        
        outs = []
        
        for i in range(n):
            out = ""
            if (i + 1)%3 == 0:
                out += "Fizz"
            if (i + 1)%5 == 0:
                out += "Buzz"
            if (i + 1)%3 != 0 and (i + 1)%5 != 0:
                out += str(i + 1)
            outs.append(out)
        
        return(outs)
