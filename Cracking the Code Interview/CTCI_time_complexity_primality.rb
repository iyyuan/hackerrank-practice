#!/bin/ruby

p = gets.strip.to_i
for a0 in (0..p-1)
    n = gets.strip.to_i
    
    is_prime = true
    
    # 1 is not a prime number
    if n <= 1
        puts "Not prime"
        next
    else
        for i in (2..Integer.sqrt(n))
           if n % i == 0
              is_prime = false
              break
           end
        end
    end
    
    if is_prime
        puts "Prime"
    else
        puts "Not prime"
    end
end