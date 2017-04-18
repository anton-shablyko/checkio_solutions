class Friends:
    def __init__(self, connections):
        self.connections = [sorted(i) for i in connections]
        print(self.connections)

    def add(self, connection):
        connection = sorted(connection)
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        connection = sorted(connection)
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return {i[x] for i in self.connections for x in range(len(i))}

    def connected(self, name):
        result = []
        for i in self.connections:
            if name in i:
                i.remove(name)
                result.append(i[0])
        return set(result)


x = Friends([{"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"},  {"c", "d"}])
x.add({"c", "d"})
x.add({"c", "d"})
#x.remove({"c", "d"})
x.names()
x.connected("a")

#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
#     digit_friends = Friends([{"1", "2"}, {"3", "1"}])
#     assert letter_friends.add({"c", "d"}) is True, "Add"
#     assert letter_friends.add({"c", "d"}) is False, "Add again"
#     assert letter_friends.remove({"c", "d"}) is True, "Remove"
#     assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
#     assert letter_friends.names() == {"a", "b", "c"}, "Names"
#     assert letter_friends.connected("d") == set(), "Non connected name"
#     assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
