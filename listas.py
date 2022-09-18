class SearchList():

    def __init__(self, insert_list):
        self.insert = insert_list

    def exec_list(self):
        for i in self.insert:
            if i == type(list):
                print(i)


my_list = ["a", "b", 1, 2, 3, ["x1", "x2", 4.7]]

prt_list = SearchList(my_list)
print(prt_list.exec_list())
