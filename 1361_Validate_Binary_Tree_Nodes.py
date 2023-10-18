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
        roots = self.defineRoots(tree)
        print(self.verifLineOfMatrix(tree))
        print(self.verifRoots(tree, roots))
        result = self.verifLineOfMatrix(tree) and self.verifRoots(tree, roots)
        return result

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
    
    def defineRoots(self, tree: List[List[int]]) -> List[int]:
        roots: List[int] = []
        for nodeIndex in range(0, len(tree)):
            nodeIsRoot = True
            for nodeIndex2 in range(0, len(tree)):
                if tree[nodeIndex2][nodeIndex] != 0:
                    nodeIsRoot = False
            if nodeIsRoot == True:   
                roots.append(nodeIndex2)
        return roots
    
    def verifRoots(self, tree: List[List[int]], roots: List[int]) -> bool:
        if(len(roots) != 1): return False
        root = roots[0]
        #if(len(tree) != 1 and tree[root].count(1) == 0): return False
        for node in range(0, len(tree)):
            if tree[root][node] != 0: 
                print('ERROR')
                return False
        return True
    
    def verifLineOfMatrix(self, tree: List[List[int]]) -> bool:
        for nodeIndex, node in enumerate(tree):
            #Check that the child has two children maximum
            if node.count(1) > 2:
                return False
            #Compare each line of the matrix between them
            for nodeIndex2, node2 in enumerate(tree):
                #If the lines are the same then we do not compare them
                if nodeIndex != nodeIndex2:
                    #Check if the connexion is unidirectional
                    if node[nodeIndex2] != 0 and node2[nodeIndex] != 0:
                        return False
                    for index, value in enumerate(node):
                        #Check if the node have got a unique parent
                        if value != 0 and node2[index] != 0:
                            return False
        return True

        
assert Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1])
assert not Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1])
assert not Solution().validateBinaryTreeNodes(2, [1,0], [-1,-1])
assert not Solution().validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1])
assert not Solution().validateBinaryTreeNodes(4, [1,2,0,-1], [-1,-1,-1,-1])
