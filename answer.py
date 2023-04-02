#!/usr/bin/python

"""
Python Core object Types
"""

def number():
"""
    This is to review numbers and basic operations.
    """
# Write the value 4 to the power of 5 and assign it to variable x.
inta = 4**5
    x =a
# Write the value x divided by 3 and assign it to variable y.
    b=x%3
    y = b

    return x,y

def strings():
    """
    This is to review numbers and strings and basic operations.
    """

    # Assign a string "stevens" to a variable stevens.

    a = "stevens"
    print(a)

    # Repeat variable stevens 7 times and assign it to variable stevens_7.

    stevens_7 = a 
    print(a*7)

    # What is the length of stevens_7?

    length=len(a)
    print(length)

    # Concatenate variable stevens with string " is great" and assign it to variable great.

    b ="is great"
    z = a+b
    print(z)

    # Replace "great" with "good" in variable great and assign it to a new variable good.

    b = "is great"

b = b.replace("great", "good")

print(b)

    return stevens, stevens_7, length, great, good


def list_1D():
    """
    This is to review basic operations with lists.
    """
    s = " hoboken,is,awesome,i,like,it "
    s = ''.join("hoboken,is,awesome,i,like,it".split())
    print(s)
  
    #Remove whitespace characters on both side and assign it to a new variable hoboken.

    hoboken = ''.join("hoboken,is,awesome,i,like,it".split())
    print(hoboken)

    # Split variable hoboken on a delimiter(comma) into a list of substrings and assign it to a new variable hoboken_list.

    hoboken= hoboken_list

    # Get the first item in the hoboken_list and assign it to a new variable hoboken_first_item.

    hoboken_first_item =

    ####
    l=[2,3,4,1,5,6,9,10,15,12,13,-2,-6,0,0]
    l.sort()
    print(l)

    # Inplace sort list l (use .sort() ).



    # Get the 4th to 10th item in sorted list l and assign them to a new list new_l.
import itemgetter

    new_l =(l[4]),(l[10])
    print(new_l)

    return hoboken,hoboken_list, hoboken_first_item, l, new_l



def list_3D ( ) :
    # Create a 3 x 3 matrix A as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]

     A = [[1,4,5],
          [6,10,11],
          [12,17,38]]
 

    # Collect the items in the last column of matrix A using list comprehension and assign it to a new variable last_column.

    last_column = A[2],A[5],A[8]

    # Get the item at the last row and last column of A.

    a =A[6],A[7],A[8]

    # Get the item at row 2 and column 1 of A.

    b = A[3]


    return A,last_column, a, b


def dictionary():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   "fruit" => "apple"
    #   "quantity" => 18
    #   "color" => "red"
    fruit_dict ={'fruit':'apple','quantity':18,'color':'red'}
    
    # Get the item in dictionary fruit_dict that the key "fruit" maps to.

    f = fruit_dict('fruit')

    # Increase the value that key "quantity" map to by 1.


    return fruit_dict, f
def dictionary_nested():
    # Create a nested dictionary Grace where:
    #   "name" => {"first_name" => "Grace", "last_name" => "Hopper"} (a dictionary)
    #   "jobs" => ["scientist", "engineer"] (a list)
    #   "age" => 85

    Grace ={"first_name"="grace","last_name"="hopper","jobs"=["scientist,engineer"],"age"=85}

    # Get the value of key "last_name" from the subdictionary of key "name" in dictionary Grace. (aka."Hopper")

    last_name = 

    # Add "programmer" to the list that key "jobs" maps to.



    # Get the third item in the list that key "job" maps to. (the item  you recently added)
    
    job =



    return Grace,last_name, job



number()
strings()
list_1D()
list_2D()
dictionary()
dictionary_nested()
