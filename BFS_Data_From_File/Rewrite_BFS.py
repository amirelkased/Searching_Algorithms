import Read_Graph
import BFS_Algorithm

if __name__ == '__main__':
    file = input('Welcome in BFS Algo :\nPlease enter file name : ')
    # file name is graph.txt
    graph_represent = Read_Graph.fileName(file)
    init = input('Enter init state : ')
    print('The path is : ', BFS_Algorithm.bfs(graph_represent, init))
