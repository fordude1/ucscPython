# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 5, Homework 5 part 2

#  determine the differences between two files after first writing a new file
# that is exactly the same as the input file.
# This program will be importing homework_5_solution_module.py

# import our solution module
import homework_5_solution_module as h5sm

# going to use itertools to save some code
import itertools

def Run():
    '''
    Call functions from homework_5_solution_module for this program
    :return:
    '''
    file_name = h5sm.AskForFileName()
    all_file_contents = h5sm.ReadFileContents(file_name)
    head_list = h5sm.BuildHeadList(all_file_contents)
    atom_list = h5sm.BuildAtomList(all_file_contents)
    tail_list = h5sm.BuildTailList(all_file_contents)
    h5sm.WriteNewFile(head_list, atom_list, tail_list)
    file_2 = 'output.txt'
    file_difference = DifferenceTwoFiles(file_name, file_2)


def DifferenceTwoFiles(file_1, file_2):
    '''
    take in the name of two files as parameters
    :return:diff_list
    '''

    # This function will open both files reading in all lines into two separate variables
    # and compare the two to determine if the files are different.
    # This function will accomplish this by looping over the elements of the
    # first variable and checking if the second variable contains the same line
    # in the same order.  If there is a difference, then the element that is
    # different should be appended to a list call diff_list.
    # This list should then be counted for the number of differences and that number output.


    # no need to specify read as that is the default
    file1 = open(file_1)
    file2 = open(file_2)

    # initialize our list
    diff_list = []

    # initialize our counter
    diff_count = 0

    with open(file_1):
        with open(file_2):
            for i, (line1, line2) in enumerate(itertools.izip_longest(file1, file2)):
                if line1 != line2:

                    #show me the difference
                    print line2
                    # append to the diff_list
                    diff_list.append(line1)

                    # if there are differences, increase the count
                    diff_count += 1

    # print out the difference count
    print "The diff count is:", diff_count
    #return diff_list

# Start the program
Run()