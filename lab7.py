A = [
    [19, 62, -45, -1, 84],
    [23, 54, -4, -2, 68],
    [36, 39, 96, 94, 97],
    [-3, -8, -4, -6, -22],
    [98, -5, -3, 0, 11]
]

def sort_rows_inside(matrix):
    column = len(matrix[0])
    for row in matrix:
        for i in range(column - 1):
            for j in range(column - 1 - i):
                if row[j] < row[j+1]:
                    row[j], row[j+1] = row[j+1], row[j]

def get_fi(matrix):
    result = []
    rows = len(matrix)
    column = len(matrix[0])
    
    for j in range(column):
        mul = 1
        has_elements = False
        for i in range(rows):
            if i > j: #де  i - рядок j - стовпець 
                mul *= matrix[i][j]
                has_elements = True
        
        if has_elements:
            result.append(mul)
    return result

def get_F(fi_list):
    if not fi_list: return 0
    return sum(fi_list) / len(fi_list)

sort_rows_inside(A)

print("Відсортована матриця:")
for row in A:
    print(row)

fi_values = get_fi(A)
print("Значення f_i:", fi_values)

F_value = get_F(fi_values)
print("Значення F:", F_value)

#part2
class PassengerNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class BusStop:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_passenger(self, name):
        new_passenger = PassengerNode(name)
        
        if self.head is None:
            self.head = new_passenger
            self.tail = new_passenger
        else:
            self.tail.next = new_passenger
            self.tail = new_passenger
            
        print(f" Пасажир {name} прийшов на зупинку.")

    def board_bus(self):
        if self.head is None:
            print(" Автобус приїхав, але на зупинці нікого немає.")
            return

        leaving_passenger = self.head.name
        self.head = self.head.next

        if self.head is None:
            self.tail = None
            
        print(f" Пасажир {leaving_passenger} сів у автобус.")

    def show_queue(self):
        if self.head is None:
            print(" Зупинка порожня.")
            return

        print(" Черга на зупинці: ", end="")
        current = self.head
        while current:
            print(f"[{current.name}]", end=" -> ")
            current = current.next
        print("кінець черги.")

stop = BusStop()

stop.add_passenger("Андрій")
stop.add_passenger("Олена")
stop.add_passenger("Іван")

stop.show_queue()

print("                 ")

stop.board_bus()
stop.board_bus()

stop.show_queue()

print("             " )

stop.add_passenger("Марія")
stop.show_queue()

stop.board_bus()
stop.board_bus()
stop.board_bus()
