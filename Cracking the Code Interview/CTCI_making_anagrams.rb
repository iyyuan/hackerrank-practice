#!/bin/ruby

a = gets.strip
b = gets.strip

count = {}
numOps = 0

a.each_char do |c|
    if count.key?(c)
        count[c] = count[c] + 1 
    else
        count[c] = 1
    end
end

b.each_char do |c|
   if count.key?(c)
        count[c] = count[c] - 1 
    else
        count[c] = -1
    end
end

count.each do |key, value|
    if value != 0
       numOps += value.abs 
    end
end

puts numOps
