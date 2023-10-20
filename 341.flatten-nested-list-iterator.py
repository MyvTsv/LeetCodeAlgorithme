from typing import List


class NestedInteger:
    def __init__(self, isInteger):
        self.value = None
        self.list = []
        self.isInteger = isInteger

    def setValue(self, v):
        if self.isInteger:
            self.value = v
        else:
            raise ValueError("Exception")

    def addValue(self, nest):
        if nest is not None and not self.isInteger:
            self.list.append(nest)

    def addInteger(self, v):
        if not self.isInteger:
            n = NestedInteger(True)
            n.setValue(v)
            self.list.append(n)
        else:
            raise ValueError("Exception")

    def addList(self):
        if not self.isInteger:
            n = NestedInteger(False)
            self.list.append(n)

    def isInteger(self) -> bool:
        return self.isInteger

    def getInteger(self):
        return self.value

    def getList(self):
        return self.list

    def __str__(self):
        string = ""
        if self.isInteger:
            return string + str(self.value)
        elif len(self.list) == 0:
            return string + '[]'
        else:
            string += '['
            for i in range(0, len(self.list) - 1):
                string += self.list[i].__str__() + ','
            lastIndex = len(self.list) - 1
            string += self.list[lastIndex].__str__() + ']'
            return string

    def __getitem__(self, index):
        if not self.isInteger:
            return self.list[index]

    def __len__(self):
        if not self.isInteger:
            return len(self.list)


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):

        def mergeArray(nestedList: List[NestedInteger]) -> List[int]:
            if len(nestedList) == 1 and nestedList[0].getInteger() != None:
                return [nestedList[0].getInteger()]
            array: List[NestedInteger] = []
            for i in nestedList:
                if i.isInteger and i.getInteger() != None:
                    array += mergeArray([i])
                else:
                    array += mergeArray(i.getList())
            return array
        self.mergeNestedList = mergeArray(nestedList)
        self.currentPosition = 0

    def next(self) -> int:
        value = self.mergeNestedList[self.currentPosition]
        self.currentPosition += 1
        return value

    def hasNext(self) -> bool:
        return 0 <= self.currentPosition + 1 <= len(self.mergeNestedList)


list = NestedInteger(False)
list2 = NestedInteger(False)

list.addList()
list.getList()[0].addInteger(1)
list.getList()[0].addInteger(1)
list.addInteger(2)
list.addList()
list.getList()[2].addInteger(1)
list.getList()[2].addInteger(1)

i, v = NestedIterator(list), []
while i.hasNext():
    v.append(i.next())
assert v == [1, 1, 2, 1, 1]

list2.addInteger(1)
list2.addList()
list2.getList()[1].addInteger(4)
list2.getList()[1].addList()
list2.getList()[1].getList()[1].addInteger(6)

i, v = NestedIterator(list2), []
while i.hasNext():
    v.append(i.next())
assert v == [1, 4, 6]
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
