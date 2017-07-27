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
        return file_name

def ReadFileContents(file_name):
    '''
    open the file and read all the lines in the file into memory.
    :param file_name:
    :return:all_file_contents
    '''

    #open and read all lines
    in_file = open(file_name)
    all_file_contents = in_file.readlines()

    return all_file_contents

def BuildHeadList(all_file_contents):
    '''
    loop over the variable populated in ReadFileContents and append to another list called head_list
    the header information from the file.
    :param all_file_contents:
    :return:head_list
    '''

    # initialize our list
    head_list = []

    # use enumerated list to get line numbers in original file
    for counter1,line in enumerate(all_file_contents):

        # get line numbers up to ATOM and assign to line_number
        if line.startswith("ATOM"):
            line_number = counter1
            # no need to go any further
            break

    # use enumerated list to create our first list up to line_number
    for counter2,line in enumerate(all_file_contents):
        if counter2 < line_number:
            head_list.append(line)

    # test
    #print head_list



def BuildAtomList(all_file_contents):
    '''
    loop over the variable populated in ReadFileContents and append to another list called atom_list
    :param all_file_contents:
    :return:atom_list
    '''
    # all the lines that begin with ATOM and ONLY these lines.

    # initialize our list
    atom_list = []

    # for loop to get all lines that start with ATOM
    for line in all_file_contents:
        if line.startswith("ATOM"):
            atom_list.append(line)

    # return our new list
    print atom_list
    #return atom_list




def BuildTailList(all_file_contents ):
    '''
    loop over the variable populated in ReadFileContents and append to another list called tail_list
    :param all_file_contents:
    :return:tail_list
    '''
    # all the lines that are below those that begin with ATOM (the lines left over)
    print "TailList"
    print all_file_contents

def WriteNewFile():
    '''
    take the three lists created above (head_list, atom_list, tail_list)
    as arguments and will write these lists to an output file called output.txt
    :return:
    '''
    # should look exactly like 1JKB.pdb when finished writing
pass

# needed if file being called from commandline or run in IDLE
# this makes this object a module
if __name__=='__main__':

    # Test the functions
    file_name = AskForFileName()
    all_file_contents = ReadFileContents(file_name)
    #head_list = BuildHeadList(all_file_contents)
    atom_list = BuildAtomList(all_file_contents)