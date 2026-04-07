class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix[0]), len(matrix)
        mat = []
        for i in range(ROWS):
            ls = []
            for j in range(COLS):
                ls.append(matrix[j][i])
            mat.append(ls)
        return mat