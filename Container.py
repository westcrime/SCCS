import os, re


class Container:

    _cont = dict()
    _curr_user = None
    
    def add_user(self, name: str):
        for i in self._cont:
            if i == name:
                return
        self._cont[name] = set()
        self._curr_user = name

    def grep(self, filter:str):
        try:
            got_item = False
            for element in self._cont[self._curr_user]:
                if re.match(filter,element):
                    print(f"founded: {element}")
                    got_item = True
            
            if not got_item:
                print("No matches found")
        except re.error:
            print("Incorrect regex input")

    def change_user(self, name: str):
        if self._curr_user != None:
            if input("Save current container (y/n)?: ") == 'y':
                self.save()

        self._curr_user = name

        if not self._curr_user in self._cont.keys():
            self._cont[self._curr_user]=set()

        print(f"Switched to {self._curr_user}")

        if input("Load the container (y/n)?: ") == 'y':
            self.load() 
        

    def save(self):
        with open (f"{self._curr_user}.txt",'w') as file:
            for element in self._cont[self._curr_user]:
                file.write(str(element) + ' ')
        print(f"Data saved to {self._curr_user}.txt")


    def load(self):
        if not os.path.exists(f"{self._curr_user}.txt"):
            print("No such file in directory.")
            return

        with open (f"{self._curr_user}.txt",'r') as file:
            for element in file.readline().split():
                self._cont[self._curr_user].add(element)
        print(f"Container for user {self._curr_user} loaded")     


    def add(self, *objs):
        if self._curr_user != None:
            for i in objs:
                self._cont[self._curr_user].add(i)

    def find(self, *objs):
        if self._curr_user != None:
            for obj in objs:
                if obj in self._cont[self._curr_user]:
                    print(f"founded: {obj}")
                    continue

    def remove(self, obj):
        if self._curr_user != None:
            for i in self._cont[self._curr_user]:
                if obj == i:
                    self._cont[self._curr_user].remove(obj)
                    return
            print("No such element!")

    def print(self):
        if self._curr_user != None:
            print(self._cont[self._curr_user])


def main():
    _cont = Container()

    print("enter your username to make possible to load your last container")
    name = input()
    _cont.add_user(name)
    _cont.load()

    menu_str = "What do you want to do?\n1. Add element\n2. Remove\n3. Find key\n4. Print list\n5. Grep\n6. Save\n7. Load\n8. Switch user\n9. Exit"
        
    while True:
        print(menu_str)
        decision = input()

        if decision == "1":
            print("Enter element to add")
            _cont.add(input())
        elif decision == "2":
            print("Enter element to remove")
            _cont.remove(input())
        elif decision == "3":
            print("Enter element to find")
            _cont.find(input())
        elif decision == "4":
            print("Printing")
            _cont.print()
        elif decision == "5":
            print("Enter regex to match")
            _cont.grep(input())
        elif decision == "6":
            print("Saving")
            _cont.save()
        elif decision == "7":
            print("Load")
            _cont.load()
        elif decision == "8":
            print("Enter the name of user to switch on")
            _cont.change_user(input())
        elif decision == "9":
            print("Exiting\n")
            break

if __name__ == "__main__":
    main()