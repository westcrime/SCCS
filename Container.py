class Container:

    _cont = dict()
    _curr_user = None
    
    def add_user(self, name: str):
        for i in self._cont:
            if i == name:
                return
        self._cont[name] = set()

    def change_user(self, name: str):
        for i in self._cont:
            if i == name:
                self._curr_user = name
        

    def add(self, *objs):
        if self._curr_user != None:
            for i in objs:
                self._cont[self._curr_user].add(i)

    def find(self, *objs):
        if self._curr_user != None:
            for obj in objs:
                if obj in self._cont[self._curr_user]:
                    continue
                else:
                    print("No such elements")
            print(objs)

    def remove(self, obj):
        if self._curr_user != None:
            for i in self._cont[self._curr_user]:
                if obj == i:
                    self._cont[self._curr_user].remove(obj)
                    return

    def print(self):
        if self._curr_user != None:
            print(self._cont)

cont = Container()

cont.add_user("dima")
cont.add_user("sasha")
cont.change_user("dima")
cont.add(3)
cont.add(4)
cont.add(5)
cont.print()
cont.change_user("sasha")
cont.add(6)
cont.print()
cont.change_user("dima")
cont.remove(4)
cont.print()
cont.find(3, 5)