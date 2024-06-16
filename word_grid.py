'''
File: word_grid.py
Author: Karan Kumar 
Course: CSC 120, Spring 2024
Purpose: This program processes a wordgrid file and generates random numbers.
   It then converts random numbers into random letters and prints the output.
   It also allows the user to generzte the grid size and random seed. After
   specifying the grid size and random seed, it stores the value in a 2D list.
   Finally, it converts the 2D lists into a grid where each sublist is printed
   in different rows making a grid of size n*n.
'''
import random
def init():
    '''
    Argument:
            No Arguments given as stated in the problem.
    Returns:
            The grid size.
    '''
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    '''
    Argument:
            grid size.
    Returns:
            2D list of alphabets.
    '''
    grid = []
    for i in range(grid_size):
        nlist = []
        for j in range(grid_size):
            w = random.randint(0,25)  # Generates random number
            dict = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'
                    ,10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',         
                    18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}  
            # Convert numbers into letters
            nlist.append(dict[w])
        grid.append(nlist)
    return grid


def print_grid(grid):
    '''
    Argument:
            2D list of alphabets.
    '''
    for i in grid:
        print(','.join(i))  # Converts 2D list of letters into grid of letters.

def main():
    '''
    Main function executes the program and generate a random grid of letters 
    of specified given size.
    '''
    size=init()
    grid=make_grid(size)
    print_grid(grid)

main()