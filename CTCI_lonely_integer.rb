#!/bin/ruby

n = gets.strip.to_i
a = gets.strip
a = a.split(' ').map(&:to_i)

value = 0

a.each do |val|
   value ^= val 
end

puts value