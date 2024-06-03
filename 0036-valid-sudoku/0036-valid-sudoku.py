class Solution(object):
    def isValidSudoku(self, board):
        # 初始化了三个列表来跟踪每一行、每一列和每个3x3子格中的数字：
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    # 计算它所属的3x3子格的索引 box_index
                    box_index = (i // 3) * 3 + (j // 3)
                    # 检验在行、列、3*3中是否有重复
                    if num in rows[i] or num in columns[j] or num in box[box_index]:
                        return False
                    rows[i].append(num)
                    columns[j].append(num)
                    box[box_index].append(num)

        return True
        