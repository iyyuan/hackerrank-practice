#!/bin/ruby

def solve(arr, money)
    
    count = {}
    
    arr.each_index do |i|
        if count.key?(arr[i].to_s)
            count[arr[i].to_s] = count[arr[i].to_s] << i+1
        else
            count[arr[i].to_s] = [i+1]
        end
    end
    
    i1 = 0
    i2 = 0
    
    count.each do |key, value|
        if count.key?((money.to_i - key.to_i).to_s)
            i1 = value.first
            i2 = count[(money.to_i - key.to_i).to_s].last
            break
        end
    end
    
    puts "#{i1} #{i2}"
end

t = gets.strip.to_i
for a0 in (0..t-1)
    money = gets.strip.to_i
    n = gets.strip.to_i
    arr = gets.strip
    arr = arr.split(' ').map(&:to_i)
    solve(arr, money)
end
