#!/bin/ruby

require 'json'
require 'stringio'

mn = gets.rstrip.split
m = mn[0].to_i
n = mn[1].to_i

magazine = gets.rstrip.split(' ').map(&:to_s)
ransom = gets.rstrip.split(' ').map(&:to_s)

dict = {}

magazine.each do |str|
    if dict.key?(str)
        dict[str] = dict[str] + 1
    else
        dict[str] = 1
    end
end

ransom.each do |str|
    if dict.key?(str)
        dict[str] = dict[str] - 1
    else
        dict[str] = -1
    end
end

valid = true

dict.each do |key, value|
    if value < 0
        valid = false
    end
end

if valid
    puts "Yes"
else
    puts "No"
end
