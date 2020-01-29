from random import random
class Symboltable:
    def __init__(self,expression):
        self.expression = expression
        self.table = []
    def createsymboltable(self):
        temp_row = [i for i in self.expression.split(' ')]
        for i in temp_row:
            row = []
            if i.isalpha():
                row.append(i)
                row.append("identifier")
            else:
                row.append(i)
                row.append("operator")
            row.append(random()*10**8)
            self.table.append(row)
    def tablebuilder(self):
        print("Symbol \t Type \t\t Location")
        for i in self.table:
            print("{} \t {} \t {:.0f}".format(i[0],i[1],i[2]))

expression = input("Enter expression split acording to space")
expr1 = Symboltable(expression)
expr1.createsymboltable()
expr1.tablebuilder()