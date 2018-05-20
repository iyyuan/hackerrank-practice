#!/bin/ruby

# Note: This problem suffers from the overlapping subproblem
# A more elegant solution would include some memoization,
# perhaps through the use of a hash to remove redundant computations

# Strictly recursion only solution
def fibonacci(n)
    if n == 0
        return 0
    elsif n == 1
        return 1
    else
        return fibonacci(n-1) + fibonacci(n-2)
    end
end

n = gets.to_i
print(fibonacci(n))

