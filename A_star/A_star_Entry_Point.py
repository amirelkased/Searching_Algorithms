import Read_File
import Algorithm

if __name__ == '__main__':
    location = input("Enter File Name : ")
    # available 'graph.txt'
    graph, heuristic = Read_File.read(location)
    init = input('Welcome in A* : \nPlease enter init point : ')
    goal = input('Please enter goal point : ')
    print(Algorithm.A(graph, heuristic, init, goal))