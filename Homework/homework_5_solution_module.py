# Hauns Froehlingsdorf
# Python Programming for Beginners
# Week 5, Homework 5 part 1

# Module that will perform file parsing and writing.
# Make sure your module has good doc strings for all functions so that
# when you perform a help(homework_5_solution_module) in the python interpreter
# that you will have very informative output.
#
# HINT:  Look at all the built-in function for the string type (i.e. dir(str)).
# One of these functions will be important when looping through all_file_contents.

def AskForFileName():
    '''
    ask the user for the name of the input file
    :return:file_name
    '''

    # ask user for file
    file_name = raw_input('Please provide the name of the input file:\n')
    if len(file_name) == 0:
        print "you didn't enter anything"
        AskForFileName()
    else:
        # return the value of the letter
        print "You entered: ", file_name
        return ReadFileContents(file_name)

def ReadFileContents(file_name):
    '''
    open the file and read all the lines in the file into memory.
    :param file_name:
    :return:all_file_contents
    '''
pass

def BuildHeadList(all_file_contents ):
    '''
    loop over the variable populated in ReadFileContents and append to another list called head_list the header information from the file.
    :param all_file_contents:
    :return:all_file_contents
    '''
    # These are the lines from the top of the file to the lines that start with the word ATOM.
pass

def BuildAtomList(all_file_contents):
    '''
    loop over the variable populated in ReadFileContents and append to another list called atom_list
    :param all_file_contents:
    :return:
    '''
    # all the lines that begin with ATOM and ONLY these lines.
pass

def BuildTailList(all_file_contents ):
    '''
    loop over the variable populated in ReadFileContents and append to another list called tail_list
    :param all_file_contents:
    :return:
    '''
    # all the lines that are below those that begin with ATOM (the lines left over)
pass

def WriteNewFile():
    '''
    take the three lists created above (head_list, atom_list, tail_list) as arguments and will write these lists to an output file called output.txt
    :return:
    '''
    # should look exactly like 1JKB.pdb when finished writing
pass

# needed if file being called from commandline or run in IDLE
# this makes this object a module
if __name__=='__main__':
    # Test the functions
    AskForFileName()