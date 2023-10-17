from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        try:
            if n != len(leftChild) or n != len(rightChild):
                raise ValueError("The size of tree is not egual with leftChild size or/and rightChild size")
        except ValueError as e:
            print(e)
            return False
        tree = self.createEmptyTreeMatrix(n)
        tree = self.fillTreeMatrix(tree, leftChild)
        tree = self.fillTreeMatrix(tree, rightChild)
        for nodeIndex, node in enumerate(tree):
            for nodeIndex2, node2 in enumerate(tree):
                if nodeIndex != nodeIndex2:
                    if node.count(1) > 2:
                        return False
                    if node[nodeIndex2] != 0 and node2[nodeIndex]:
                        return False
                    for index, value in enumerate(node):
                        if value != 0 and node2[index] != 0:
                            return False
        return True

    def createEmptyTreeMatrix(self, n: int) -> List[List[int]]:
        emptyTree: List[List[int]] = []
        for column in range(0, n):
            emptyTree.append([])
            for line in range(0, n):
                emptyTree[column].append(0)
        return emptyTree
    
    def fillTreeMatrix(self, tree: List[List[int]], children: List[int]) -> List[List[int]]:
        for nodeIndex, childConnexion in enumerate(children):
            if childConnexion != -1:
                tree[nodeIndex][childConnexion] = 1
        return tree
        
assert Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1])
assert not Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1])
assert not Solution().validateBinaryTreeNodes(2, [1,0], [-1,-1])
assert not Solution().validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1])
