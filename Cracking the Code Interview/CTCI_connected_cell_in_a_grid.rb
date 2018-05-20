#!/bin/ruby

n = gets.strip.to_i
m = gets.strip.to_i
grid = Array.new(n)
for grid_i in (0..n-1)
    grid_t = gets.strip
    grid[grid_i] = grid_t.split(' ').map(&:to_i)
end

# Global visited nxm array
$visited = Array.new(n)
for grid_i in (0..n-1)
    $visited[grid_i] = Array.new(m, false)
end

# Global list of directions
$directions = [
    # clockwise from 12 o'clock
    [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]
]

# Global counter for easier manipulation
$count = 0

def dfs(n, m, x, y, grid)
    # If we have visited this cell, exit
    if $visited[x][y] == true
        return
    end
    
    # If the cell is a 0, mark it as visited and exit
    if grid[x][y] == 0
        $visited[x][y] = true
        return
    end
    
    # Mark the cell as visited
    # Increment the global counter
    $visited[x][y] = true
    $count += 1
    
    $directions.each do |dir|
        tempX = x + dir[0]
        tempY = y + dir[1]
        
        # Check that the following are met:
        # 1. The adjacent x,y are within the boundaries of the grid
        # 2. The adjacent cell has not been visited
        # 3. The adjacent cell is a 1
        if tempX >= 0 and tempX < n and tempY >= 0 and tempY < m and !$visited[tempX][tempY] and grid[tempX][tempY] == 1
            dfs(n, m, tempX, tempY, grid)
        end
    end
end

max_count = 0
for x in (0..n-1)
    for y in (0..m-1)
        $count = 0
        dfs(n, m, x, y, grid)
        
        if $count > max_count
            max_count = $count
        end
    end
end

puts max_count
