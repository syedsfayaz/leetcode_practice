# Problem Name is &&& Best Average Grade &&& PLEASE DO NOT REMOVE THIS LINE.

"""
  Instructions:

  Given a list of student test scores, find the best average grade.
  Each student may have more than one test score in the list.

  Complete the bestAverageGrade function in the editor below.
  It has one parameter, scores, which is an array of student test scores.
  Each element in the array is a two-element array of the form [student name, test score]
  e.g. [ "Bobby", "87" ].
  Test scores may be positive or negative integers.

  If you end up with an average grade that is not an integer, you should
  use a floor function to return the largest integer less than or equal to the average.
  Return 0 for an empty input.

  Example:

  Input:
  [ [ "Bobby", "87" ],
    [ "Charles", "100" ],
    [ "Eric", "64" ],
    [ "Charles", "22" ] ].


    dict = {'Bobby': 87,"Charles":122,"Eric":64}
    dict_count = {'Bobby': 1,"Charles":2,"Eric":1}


  Expected output: 87
  Explanation: The average scores are 87, 61, and 64 for Bobby, Charles, and Eric,
  respectively. 87 is the highest.
"""

""" Find the best average grade. """


'''[["Bobby", "87"],
           ["Charles", "100"],
           ["Eric", "64"],
           ["Charles", "22"]]'''
def bestAverageGrade(scores):
    if len(scores) == 1:
        return (int(scores[0][1]))
    elif len(scores) == 0:
        return None
    employee = {}
    employee_sal = {}
    for values in scores:
        if values[0] not in employee:
            employee_sal[values[0]] = 1
            employee[values[0]] = int(values[1])
        else:
            employee_sal[values[0]] += 1
            employee[values[0]] += int(values[1])
    result = []
    for value, sal in employee.items():
        employee[value] = sal / employee_sal[value]
        result.append(employee[value])
    return max(result)




def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """

    # TODO: implement more test cases
    # tc1 = [["Bobby", "87"],
    #        ["Charles", "100"],
    #        ["Eric", "64"],
    #        ["Charles", "22"]];
    #return bestAverageGrade(tc1) == 87

    # tc1 = [["Bobby", "87"],
    #        ["Eric", "87"],
    #        ["Charles", "87"]];
    #
    # return bestAverageGrade(tc1) == 87
    # tc1 = [["Bobby", "87"]];
    #
    # return bestAverageGrade(tc1) == 87
    # tc1 = [["Bobby", "100"], ["Bobby", "100"]];
    #
    # return bestAverageGrade(tc1) == 100
    tc1 = [];

    return bestAverageGrade(tc1) == None


if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n");
    else:
        print("Tests fail\n");
