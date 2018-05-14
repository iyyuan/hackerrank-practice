#!/bin/ruby

$dist = []
n = gets.to_i

n.times do
    temp = gets.split(" ").map(&:to_i) 
    num_nodes = temp[0]
    num_edges = temp[1]
    
    edges = {}
    dist = Array.new(num_nodes+1, -1)
    
    # Construct adjacency data structure
    num_edges.times do
        edge = gets.split(" ").map(&:to_i)
        
        # For an undirected graph, we must add
        # edges from both sides
        if edges.key?(edge[0])
            edges[edge[0]] << edge[1]
        else
            edges[edge[0]] = [edge[1]]
        end
        
        if edges.key?(edge[1])
            edges[edge[1]] << edge[0]
        else
            edges[edge[1]] = [edge[0]]
        end
    end
    
    start_node = gets.to_i
    
    seen = [start_node]
    queue = [start_node]
    dist[start_node] = 0
    
    # Standard BFS loop
    while !queue.empty?
        # Equivalent to Queue.poll()
        current = queue.shift

        # Iterate through all neighbours
        if edges.key?(current)
            edges[current].each do |val|
                
                # Only if we haven't seen the neighbour yet
                if !seen.include?(val)
                    # Add neighbour to the to-visit queue
                    # Add neighbour to the visited list
                    # Update the distance
                    queue << val
                    seen << val
                    dist[val] = dist[current] + 6
                end
            end
        end
    end
    
    output_str = ""
    
    dist.each_index do |i|
        if i != start_node and i > 0
            output_str += dist[i].to_s + " "
        end
    end
    
    puts output_str[0..-1]
end