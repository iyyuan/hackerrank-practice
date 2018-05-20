#!/bin/ruby

brackets = {
    "}" => "{",
    "]" => "[",
    ")" => "("
}

t = gets.strip.to_i
for a0 in (0..t-1)
    expression = gets.strip
    stack = []
    balanced = true
    
    expression.each_char do |c|
        if ["[", "(", "{"].include?(c)
            stack << c 
        end
        
        if ["]", ")", "}"].include?(c)
           if stack.last == brackets[c]
               stack.pop
           else
               balanced = false
           end
        end
    end
    
    if !stack.empty?
        puts "NO"
    else
        if balanced
            puts "YES"
        else
            puts "NO"
        end    
    end
end


