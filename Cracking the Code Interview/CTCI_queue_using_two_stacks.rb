# Enter your code here. Read input from STDIN. Print output to STDOUT

$s1 = [] #Push stack
$s2 = [] #Pop/peek stack

def enqueue(val)
    $s1 << val
end

def dequeue()
    # If the pop stack is empty, add
    # everything from the push stack
    # to the pop stack
    if $s2.empty?
        $s1.length.times do
            $s2 << $s1.pop
        end
    end
    # Pop the last element
    $s2.pop
end

def peek()
    # If the pop stack is empty, add
    # everything from the push stack
    # to the pop stack
    if $s2.empty?
        $s1.length.times do
            $s2 << $s1.pop
        end
    end
    # Return the last element
    return $s2.last
end

n = gets.to_i

n.times do
    input = gets.split(" ").map(&:to_i)
    op = input[0]
    val = input[1]

    if op == 1
        enqueue(val)
    elsif op == 2
        dequeue()
    elsif op == 3
        puts peek()
    end
end
