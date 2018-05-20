#!/bin/ruby
    
mem = {
    0 => 1,
    1 => 1,
    2 => 2
}

s = gets.strip.to_i

for a0 in (0..s-1)
    n = gets.strip.to_i
    
    (n+1).times do |i|
        if !mem.key?(i)
            mem[i] = mem[i-3] + mem[i-2] + mem[i-1]
        end
    end
    
    puts mem[n]
end
