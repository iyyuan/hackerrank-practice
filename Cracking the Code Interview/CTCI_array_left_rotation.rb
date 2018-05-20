#!/bin/ruby

require 'json'
require 'stringio'

nk = gets.rstrip.split

n = nk[0].to_i
k = nk[1].to_i

a = gets.rstrip.split(' ').map(&:to_i)
b = []

# A left rotation by 4 means that for every index
# the value should be the value at (index+4)%size of array
n.times do |i|
    b[i] = a[(i+k) % n]
end

puts b.join(" ")
