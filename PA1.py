# Determine whether the inputs are valid
def valid_input(color_array, start_node, target_color):
    if color_array is None or len(color_array) == 0:
        print("Please input a valid color array!")
        return False
    
    i, j = start_node
    num_rows = len(color_array)
    num_cols = len(color_array[0])

    if i < 0 or j < 0 or i >= num_rows or j >= num_cols:
        print("Please input a valid start node!")
        return False
    
    if target_color not in ['R', 'G', 'B', 'Y', 'W', 'G', 'X']:
        print("Please input a valid target color!")
        return False
    
    return True

# pait the color array by resursion   
def paint_fill(color_array, start_node, target_color, replace_color):
    rows, cols = len(color_array), len(color_array[0])
    modified_cells = []

    def valid_pos(i, j):
        return 0 <= i < rows and 0 <= j < cols and color_array[i][j] == target_color
    
    def paint(i, j):
        if valid_pos(i, j):
            color_array[i][j] = replace_color 
            modified_cells.append((i, j))
            paint(i, j - 1)
            paint(i, j + 1)
            paint(i - 1, j)
            paint(i + 1, j)
            
    i, j = start_node
    paint(i, j)

    print("List of cell locations modified:")
    for i in range(rows):
        for cell in modified_cells:
            if cell[0] == i:
                print(f"({cell[0]}, {cell[1]})", end=", ")
        print('\n')
    print("Number of cells modified:", len(modified_cells))

# read the array from the txt file
def read_txt(filename):
    color_array = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split(',')
            color_array.append(line)
    return color_array

def main():
    file1 = "testcase1.txt"
    file2 = "testcase2.txt"
    start_node1 = (0, 0)
    target_color = 'B'
    replace_color = 'Y'
    color_array1 = read_txt(file1)
    if valid_input(color_array1, start_node1, target_color):
        paint_fill(color_array1, start_node1, target_color, replace_color)

    print('\n')
    color_array2 = read_txt(file2)
    start_node2 = (0, 2)
    if valid_input(color_array2, start_node2, target_color):
        paint_fill(color_array2, start_node2, target_color, replace_color)

if __name__ == '__main__':
    main()