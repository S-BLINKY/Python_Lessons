def pascal_triangle(n):
    triangle = []
    
    for i in range(n):
        row = [1]  # every row starts with 1
        
        # middle elements = sum of two elements above
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
                
        if i > 0: # every row except first ends with 1
            row.append(1)
            
        triangle.append(row)
    return triangle

# to print result
n = int(input("Enter number of rows: "))
triangle = pascal_triangle(n)

for row in triangle:
    print(" " * (n - len(row)), end="") #for pyramid shape
    print(" ".join(map(str, row)))
            