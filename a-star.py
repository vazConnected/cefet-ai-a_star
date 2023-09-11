import math

class Node():
    def __init__(self, parent, position: tuple[int, int]):
        if parent is not None and not isinstance(parent, Node):
            raise ValueError("Parent must be a Node.")
        else:
            self.parent = parent

        if isinstance(position, tuple) and len(position) == 2 and all(isinstance(x, int) for x in position):
            self.position: tuple[int, int] = position
        else:
            raise ValueError("Invalid position. It must be a tuple of two integers.")
        
        self.distanceToReachTheGoal: int = 0 # (g) Distância para atingir o objetivo
        self.heuristic: int = 0 # (h): Heuristica 
        self.totalCost: int = 0 # (f): f = g + h
    
    def __eq__(self, object):
        if not isinstance(object, Node):
            return False
        else:
            return self.position == object.position
    
    def __hash__(self):
        return self.position.__hash__()
    
    def getNeighbours(self, board: list[list[str]]) -> set[tuple[int, int]]:
        neighbours: set[tuple[int, int]] = set()

        row: int = self.position[0]
        column: int = self.position[1] 

        # Acima
        if (row > 0) and (board[row - 1][column] != "1"):
            neighbours.add( (row - 1, column) )

        # Abaixo
        if (row < len(board) - 1) and board[row + 1][column] != "1":
            neighbours.add( (row + 1, column) )

        # Direita
        if (column < (len(board[row]) - 1)) and board[row][column + 1] != "1":
            neighbours.add( (row, column + 1) )

        # Esquerda
        if column > 0 and board[row][column - 1] != "1":
            neighbours.add( (row, column - 1) )

        return neighbours


def main() -> None:
    board: list[list[str]] = getBoard()
    origin: tuple[int, int] = getOrigin(board)
    destination: tuple[int, int] = getDestination(board)

    bestPath: list[tuple[int, int]] = aStar(board, origin, destination)

    print(f"Path from {origin} to {destination}:\n\t{formatOutput(bestPath, origin, destination)}")

def aStar(board: list[list[str]], origin: tuple[int, int], destination: tuple[int, int]) -> list[tuple[int, int]]:
    visited: list[Node] = [] # posicoes fechadas
    active: list[Node] = [] # posicoes abertas para exploracao

    active.append(Node(None, origin))

    while len(active) > 0:
        currentPosition: Node = active[0]
        currentIndex: int = 0

        # obter currentPosition (posicao atual)
        for index in range(len(active)):
            if active[index].totalCost < currentPosition.totalCost:
                currentPosition = active[index]
                currentIndex = index
        
        # Mover posicao atual de active (posicoes ativas para busca) para visited (posicoes ja visitadas)
        visited.append( active.pop(currentIndex) )

        # Checa se destination (destino) foi atengido 
        if currentPosition.position == destination:
            path: list[tuple[int, int]] = []
            tempCurrentNode: Node = currentPosition

            while tempCurrentNode is not None:
                path.append(tempCurrentNode.position)
                tempCurrentNode = tempCurrentNode.parent
            
            path.reverse()
            return path
        
        # Obter neighbours validos (vizinhos)
        neighbourTuples: set[tuple[int, int]] = currentPosition.getNeighbours(board) - set( map(lambda x: x.position, visited ) )
        
        for neighbour in neighbourTuples:
            currentNeighbourNode: Node = Node(currentPosition, neighbour)

            # Definir valores para distanceToReachTheGoal (g = distancia para atingir o objetivo) (g),
            # heuristic (h = heuristica) and totalCost (f = custo total)
            currentNeighbourNode.distanceToReachTheGoal = currentPosition.distanceToReachTheGoal + 1
            currentNeighbourNode.heuristic = heuristic(origin, destination)
            currentNeighbourNode.totalCost = currentNeighbourNode.distanceToReachTheGoal + currentNeighbourNode.heuristic

            if currentNeighbourNode not in set(active):
                active.append(currentNeighbourNode)

def heuristic(origin: tuple[int, int], destination: tuple[int, int]) -> float:
    # return abs(origin[0] - destination[0]) + abs(origin[1] - destination[1]) # Distancia de Manhattan
    return math.sqrt( math.pow( (origin[0] - destination[0]), 2)+ math.pow( (origin[1] - destination[1]), 2 ) ) # Distancia Euclidiana

def getOrigin(board: list[list[str]]) -> tuple[int, int]:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "s":
                return (i, j)
    
    return None

def getDestination(board: list[list[str]]) -> tuple[int, int]:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "e":
                return (i, j)
    
    return None

def formatOutput(path: list[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]) -> str:
    if path == None or len(path) == 0:
        return "No path found"

    output: str = ""

    for index in range(len(path)):
        currentStep: tuple[int, int] = path[index]

        if currentStep == start:
            output += "origin -> "
        elif currentStep == end:
            output += "destination."
        else:
            output += str("(") + str(currentStep[0]) + str(", ") + str(currentStep[1]) + str(")") + str(" -> ")

    return output

def getBoard() -> list[list[str]]:
    file: file = open("board.txt", "r")
    lines: str = file.read().splitlines()

    board: list[list[str]] = []
    for line in lines:
        board.append(line.split(" "))

    return board

if __name__ == '__main__':
    main()