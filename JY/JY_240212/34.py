'''
def mine(x, y, n) :
    for i in range(x-1, x+2) :
        for j in range(y-1, y+2) :
            if i>=0 and i<n and j>=0 and j<n :
                if board[i][j]==0 :
                    board[i][j]=2
answer=0
board=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
for i in range(len(board)) :
    for j in range(len(board)) :
        if board[i][j] == 1 :
            mine(i, j, len(board))
for i in range(len(board)) :
    for j in range(len(board)) :
        if board[i][j] == 0 :
            answer+=1
'''
board=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
n = len(board)
danger = set()
for i, row in enumerate(board):
    for j, x in enumerate(row):
        if not x:
            continue
        danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
print(n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger))