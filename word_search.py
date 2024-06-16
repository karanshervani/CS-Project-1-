
'''
File: word_search.py
Author: Karan Kumar 
Course: CSC 120, Spring 2024
Purpose: This program reads a grid of letters and a word list from files, then
    searches for words in the grid. Words can be found horizontally, 
    vertically or diagonally in the grid and must be present in the word list.
'''
def get_word_list():
    """
    This function converts the txt file to a list of words
    and also makes the grid aswell.
    Args:
        None
    Returns:
        grid: A 2D list of words containing the data
        w: A list containing the words given in the txt file 
        to which we have to check from. 
    """
    w_list = input()
    g_list = input()

    w_file = open(w_list, 'r')
    g_file = open(g_list, 'r')
    
    w = []
    grid = []

    for word in w_file:
        word = word.strip('\n')
        w.append(word)

    for i in g_file:
        grid.append(i.split())

    w_file.close()
    g_file.close()

    return grid, w
    
def occurs_in(sub_string, word_list):
    """
    This function checks wether the word exists in the word list.
    Args:
        sub_string: The list containing all the words found in the grid
        word_list: TA list containing the words given in the txt file 
        to which we have to check from.
    Returns:
            Value: True or False depending on the result
    """
    # Check if sub_string is in word_list
    value = sub_string in (word.lower() for word in word_list)
    return value

def horizontal_search(grid, word_list, possible_words):
    """
    This function checks wether the word exists in the word list in
      horizontal direction.
    Args:
        grid: A 2D list of words containing the data
        word_list: TA list containing the words given in the txt file
        to which we have to check from.
        possible_words: An empty list
    Returns:
         possible_words: A list of all the words found.
    """
    for lines in grid:
        for i in range(len(lines)):
            for j in range(i+3, len(lines)+1):
                row_string = "".join(lines[i:j])
                reverse_row_string = "".join(lines[::-1][i:j])
                if occurs_in(row_string, word_list):
                    possible_words.append(row_string)

                if occurs_in(reverse_row_string, word_list):
                    possible_words.append(reverse_row_string)

def vertical_search(grid, word_list, possible_words):
    """
    This function checks wether the word exists in the word list in
    vertical direction.
    Args:
        grid: A 2D list of words containing the data
        word_list: TA list containing the words given in the txt file
        to which we have to check from.
        possible_words: An empty list
    Returns:
         possible_words: A list of all the words found.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            column = [lines[j] for lines in grid]
            reverse_column = column[::-1]

            for k in range(i+3, len(column)+1):
                column_string = "".join(column[i:k])
                reverse_column_string = "".join(reverse_column[i:k])

                if occurs_in(column_string, word_list):
                    possible_words.append(column_string)

                if occurs_in(reverse_column_string, word_list):
                    possible_words.append(reverse_column_string)

def diagonal_search(grid, word_list, possible_words):
    """
    This function checks wether the word exists in the word list in 
    diagnol direction.
    Args:
        grid: A 2D list of words containing the data
        word_list: TA list containing the words given in the txt file
        to which we have to check from.
        possible_words: An empty list
    Returns:
         possible_words: A list of all the words found.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            diagonal = []
            a = i
            b = j
            while a < len(grid) and b < len(grid):
                diagonal.append(grid[a][b])
                a += 1
                b += 1
                
            for k in range(len(diagonal) - 2):
                for l in range(k+3, len(diagonal)+1):
                    diagonal_string = "".join(diagonal[k:l])

                    if occurs_in(diagonal_string, word_list):
                        possible_words.append(diagonal_string)

def main():
    '''
    This function executes the program and give us the desired output.
    '''
    gd, rtl = get_word_list()
    ltr = []

    horizontal_search(gd, rtl, ltr)
    vertical_search(gd, rtl, ltr)
    diagonal_search(gd, rtl, ltr)

    possible_words_list = sorted(set(ltr))

    for word in possible_words_list:
        print(word)

main()