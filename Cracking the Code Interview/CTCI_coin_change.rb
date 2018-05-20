#!/bin/ruby

require 'json'
require 'stringio'

nm = gets.rstrip.split

n = nm[0].to_i
m = nm[1].to_i

coins = gets.rstrip.split(' ').map(&:to_i)

arr = Array.new(n+1, 0)

# base case
arr[0] = 1

coins.each do |coin|
    for i in coin..n
        arr[i] += arr[i-coin]
    end
end

puts arr.last