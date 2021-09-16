class Node:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next

    def get_data(self):
        return self.__data

    def __str__(self):
        if self.__prev__ and self.__next__:
            return "data: {}, prev: {}, next: {}".format(self.__data, self.__prev__.get_data(),
                                                         self.__next__.get_data())
        if self.__prev__ and self.__next__ is None:
            return "data: {}, prev: {}, next: {}".format(self.__data, self.__prev__.get_data(), None)
        if self.__prev__ is None and self.__next__:
            return "data: {}, prev: {}, next: {}".format(self.__data, None, self.__next__.get_data())
        if self.__prev__ is None and self.__next__ is None:
            return "data: {}, prev: {}, next: {}".format(self.__data, None, None)


class LinkedList:
    def __init__(self, first=None, last=None):
        self.__length = 0
        self.__first__ = Node(first, None, None)
        self.__last__ = Node(last, None, None)
        if first is None and last is None:
            pass
        elif first is None and last is not None:
            raise ValueError("invalid value for last")
        elif first is not None and last is None:
            self.__last__ = self.__first__
            self.__length += 1
        elif first is not None and last is not None:
            self.__first__.__next__ = self.__last__
            self.__last__.__prev__ = self.__first__
            self.__length += 2

    def __len__(self):
        return self.__length

    def __str__(self):
        if self.__first__ is None or self.__length <= 0:
            return "LinkedList[]"
        else:
            nodes = []
            current = self.__first__
            for i in range(self.__length):
                nodes.append(current.__str__())
                current = current.__next__
            result = "; ".join(nodes)
        return "LinkedList[length = {}, [{}]]".format(self.__length, result)

    def append(self, element):
        if self.__length == 0:
            tmp = Node(element)
            self.__first__ = tmp
            self.__last__ = self.__first__
        else:
            tmp = Node(element, self.__last__)
            self.__last__.__next__ = tmp
            self.__last__ = self.__last__.__next__
        self.__length += 1

    def pop(self):
        if self.__length == 0:
            raise IndexError("LinkedList is empty!")
        elif self.__length == 1:
            self.__first__ = Node(None)
            self.__last__ = self.__first__
            self.__length -= 1
        else:
            self.__last__ = self.__last__.__prev__
            self.__last__.__next__ = None
            self.__length -= 1

    def popitem(self, element):
        if self.__length == 0:
            raise KeyError("{} doesn't exist!".format(element))
        else:
            current = self.__first__
            check = 0
            for i in range(self.__length):
                if i != 0:
                    current = current.__next__
                if current.get_data() == element:
                    if i == 0:
                        if self.__length != 1:
                            self.__first__ = self.__first__.__next__
                            self.__first__.__prev__ = None
                        else:
                            self.__first__ = Node(None)
                            self.__last__ = self.__first__
                    else:
                        tmp = current
                        current = current.__prev__
                        current.__next__ = tmp.__next__
                    self.__length -= 1
                    check = 1
                    break
            if check == 0:
                raise KeyError("{} doesn't exist!".format(element))

    def clear(self):
        self.__length = 0
        self.__first__ = Node(None)
        self.__last__ = Node(None)

