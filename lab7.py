def sort_rows_inside(matrix):
    if not matrix:
        return
    
    columns = len(matrix[0])
    for row in matrix:
        for i in range(columns - 1):
            for j in range(columns - 1 - i):
                if row[j] < row[j+1]:
                    row[j], row[j+1] = row[j+1], row[j]

def get_fi(matrix):
    result = []
    rows = len(matrix)
    if not rows:
        return result
    
    columns = len(matrix[0])
    
    for j in range(columns):
        multiply = 1
        has_elements = False
        for i in range(rows):
            if i > j:
                multiply *= matrix[i][j]
                has_elements = True
        
        if has_elements:
            result.append(multiply)
            
    return result

def get_f_avg(fi_list):
    if not fi_list:
        return 0
    return sum(fi_list) / len(fi_list)

###########################

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

    def board_bus(self):
        if self.head is None:
            return None

        leaving_passenger_name = self.head.name
        self.head = self.head.next

        if self.head is None:
            self.tail = None
            
        return leaving_passenger_name

    def show_queue(self):
        queue_list = []
        current = self.head
        while current:
            queue_list.append(current.name)
            current = current.next
        return queue_list

if __name__ == "__main__":
    a = [
        [19, 62, -45, -1, 84],
        [23, 54, -4, -2, 68],
        [36, 39, 96, 94, 97],
        [-3, -8, -4, -6, -22],
        [98, -5, -3, 0, 11]
    ]

    sort_rows_inside(a)
    fi_values = get_fi(a)
    f_value = get_f_avg(fi_values)

    stop = BusStop()

    stop.add_passenger("Андрій")
    stop.add_passenger("Олена")
    stop.add_passenger("Іван")

    queue_before_board = stop.show_queue()

    stop.board_bus()
    stop.board_bus()

    queue_after_two_board = stop.show_queue()

    stop.add_passenger("Марія")

    queue_after_maria = stop.show_queue()

    stop.board_bus()
    stop.board_bus()
    stop.board_bus()

    queue_final = stop.show_queue()
