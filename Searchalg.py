import sys
sys.path.append('aima-python')
from search import *
import math
import time

def mhd(node):
    '''Define your manhattan-distance heuristic for the 8-puzzle here
    '''

    state = node.state
    finalState = ((state[0], state[1], state[2]),(state[3], state[4],state[5]), (state[6],state[7], state[8]))
    goal  = ((1,2,3),(4,5,6),(7,8,0))
    manhattan_distance = 0
    for i in range(3):
        for j in range(3):
            if finalState[i][j] != 0:
                value = finalState[i][j]
                goal_i = (value - 1) // 3
                goal_j = (value - 1) % 3
                manhattan_distance += abs(i - goal_i) + abs(j - goal_j)
    return manhattan_distance

    

class HW2:

    def __init__(self):
        pass

    def example_problem(self):
        #EightPuzzle example with A*
        # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        #   which represents:   1 2 3
        #                       4 5 6
        #                       7 8 _
        #

        # In this example, we'll construct a puzzle with initial state
        #               1 2 3
        #               4 5 6
        #               _ 7 8
        #
        init = (1, 2, 3, 4, 5, 6, 0, 7, 8)
        puzzle = EightPuzzle(init)
        # Checks whether the initialized configuration is solvable or not
        # this is not a required step, but my be useful in saving you from
        # impossible configurations
        print("Is the puzzle solvable from this initial state?")
        print(puzzle.check_solvability(init))

        print("A* with default heuristic")
        return astar_search(puzzle).solution()

    def problem_1a(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (0,3,6,2,5,8,1,4,7)
        puzzle = EightPuzzle(init)
        twelveAction = iterative_deepening_search(puzzle)

        return twelveAction.solution()
    
    def problem_1b(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (0,3,6,2,5,8,1,4,7)
        puzzle = EightPuzzle(init)
        astar = astar_search(puzzle).solution()
        return astar

    def problem_1c(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''
        init = (6, 0, 2, 5, 1, 3, 4, 8, 7)
        puzzle = EightPuzzle(init)
        astar = astar_search(puzzle).solution()
        return astar

    def problem_1d(self):
        '''
        Complete the mhd function (defined above class HW2)

        1. instantiate the search algorithm with the 8 puzzle problem 
        2. write code that will create a different heuristic
        3. return the solution from the A* search algorithm
        '''

        init = (6, 0, 2, 5, 1, 3, 4, 8, 7)
        puzzle = EightPuzzle(init)
        astar = astar_search(puzzle, mhd).solution()
        return astar

    def problem_2(self):
        '''
        1. find initial states with optimal solutions of lengths 15, 17, 19 and 21
        2. for each of those, for each heuristic, measure the time it takes to find a solution
        Note: It is not required that your code for this be done specifically in this 
        function. It can be elsewhere in the file if you want to structure the code differently
        The autograder will not test this code, but we will look at it by hand, so if it
        is not all in this function, leave a comment letting us know where to look.
        '''
        print("Problem 2 result: \n")
        print("| {:<10} | {:<10} |".format("default", "mhd/heuristic"))
        print("|-----------|-----------|")
        # 15: init = (1,2,3,8,4,5,6,0,7)
        # default
        start_time15 = time.time()
        init15 = (1,2,3,8,4,5,6,0,7)
        puzzle15 = EightPuzzle(init15)
        astar_search(puzzle15).solution()
        end_time15 = time.time()
        execution_time15 = end_time15 - start_time15 
        #print(f"Execution time: {execution_time15} seconds")
        #heuristic
        start_time152 = time.time()
        init152 = (1,2,3,8,4,5,6,0,7)
        puzzle152 = EightPuzzle(init152)
        astar_search(puzzle152, mhd).solution()
        end_time152 = time.time()
        execution_time152 = end_time152 - start_time152 
        #print(f"Execution time: {execution_time} seconds")
        print("| {:<10} | {:<10} |".format(f"{execution_time15}", f"{execution_time152}")+" 15")
        #17 : init = (3,6,2,0,5,8,1,4,7)
         # default
        start_time17 = time.time()
        init17 = (3,6,2,0,5,8,1,4,7)
        puzzle17 = EightPuzzle(init17)
        astar_search(puzzle17).solution()
        end_time17 = time.time()
        execution_time17 = end_time17 - start_time17 
        #print(f"Execution time: {execution_time} seconds")
        #heuristic
        start_time172 = time.time()
        init172 = (3,6,2,0,5,8,1,4,7)
        puzzle172 = EightPuzzle(init172)
        astar_search(puzzle172, mhd).solution()
        end_time172 = time.time()
        execution_time172 = end_time172 - start_time172 
        #print(f"Execution time: {execution_time} seconds")
        print("| {:<10} | {:<10} |".format(f"{execution_time17}", f"{execution_time172}")+" 17")
        # 19 : init = (3,6,2,5,8,0,1,4,7)
        start_time19 = time.time()
        init19 = (3,6,2,5,8,0,1,4,7)
        puzzle19 = EightPuzzle(init19)
        astar_search(puzzle19).solution()
        end_time19 = time.time()
        execution_time19 = end_time19 - start_time19
        #print(f"Execution time: {execution_time} seconds")
        #heuristic
        start_time192 = time.time()
        init192 = (3,6,2,5,8,0,1,4,7)
        puzzle192 = EightPuzzle(init192)
        astar_search(puzzle192, mhd).solution()
        end_time192 = time.time()
        execution_time192 = end_time192 - start_time192 
        #print(f"Execution time: {execution_time} seconds")
        print("| {:<10} | {:<10} |".format(f"{execution_time19}", f"{execution_time192}")+" 19")
        # 21: init = (6,2,5,1,3,0,4,8,7)
        start_time21 = time.time()
        init21 = (6,2,5,1,3,0,4,8,7)
        puzzle21 = EightPuzzle(init21)
        astar_search(puzzle21).solution()
        end_time21 = time.time()
        execution_time21 = end_time21 - start_time21 
        #print(f"Execution time: {execution_time} seconds")
        #heuristic
        start_time212 = time.time()
        init212 = (6,2,5,1,3,0,4,8,7)
        puzzle212 = EightPuzzle(init212)
        #astar_search(puzzle, mhd).solution()
        end_time212 = time.time()
        execution_time212 = end_time212 - start_time212
        print("| {:<10} | {:<10} |".format(f"{execution_time21}", f"{execution_time212}")+" 21")
        #print(f"Execution time: {execution_time} seconds")
        return None

    def example_problem_3(self):
        '''Use the InstrumentedProblem class to track stats about a breadth-first
        search on the Romania Map problem.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        g = InstrumentedProblem(GraphProblem('Craiova', 'Zerind', romania_map))
        result = breadth_first_graph_search(g)
        print(g)
        g2 = InstrumentedProblem(GraphProblem('Craiova', 'Zerind', romania_map))
        result2 = iterative_deepening_search(g2)
        print(g2)
        return (g.goal_tests, g2.goal_tests)

    def problem_3a(self):
        '''Use the InstrumentedProblem class to track stats about 
        different searches on the Romania Map problem.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        inst1 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map)) 
        result1 = breadth_first_graph_search(inst1)
        print(inst1)
        inst2 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result2 = depth_first_graph_search(inst2)
        print(inst2)
        inst3 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result3 = iterative_deepening_search(inst3)
        print(inst3)
        inst4 = InstrumentedProblem(GraphProblem('Timisoara', 'Pitesti', romania_map))
        result4 = recursive_best_first_search(inst4)
        print(inst4)

        return (inst1, inst2, inst3, inst4)

    def problem_3b(self):
        '''Use the InstrumentedProblem class to track stats about
        different searches on the Romania Map problem.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        inst1 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map)) 
        result1 = breadth_first_graph_search(inst1)
        print(inst1)
        inst2 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result2 = depth_first_graph_search(inst2)
        print(inst2)
        inst3 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result3 = iterative_deepening_search(inst3)
        print(inst3)
        inst4 = InstrumentedProblem(GraphProblem('Timisoara', 'Eforie', romania_map))
        result4 = recursive_best_first_search(inst4)
        print(inst4)
        return (inst1, inst2, inst3, inst4)


def main():
    
    # Create object, hw2, of datatype HW2.
    hw2 = HW2()
 
    #=======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    print('Example Problem result:')
    print('=======================')
    print(hw2.example_problem())
    

    print('Problem 1a result:')
    print('==================')
    print(hw2.problem_1a())

    print('Problem 1b result:')
    print('==================')
    print(hw2.problem_1b())


    print('Problem 1c result:')
    print('==================')
    print(hw2.problem_1c())


    print('Problem 1d result:')
    print('==================')
    print(hw2.problem_1d())
   

    print (hw2.problem_2())

    print(hw2.example_problem_3())

    print('Problem 3a result:')
    print('==================')
    print(hw2.problem_3a())

    print('Problem 3b result:')
    print('==================')
    print(hw2.problem_3b())

    
if __name__ == '__main__':
    main()
