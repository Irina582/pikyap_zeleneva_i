class HardDisk:
    def __init__(self, id, name, capacity, price, computer_id):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.price = price
        self.computer_id = computer_id

    def __repr__(self):
        return f"HardDisk(id={self.id}, name='{self.name}')"


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Computer(id={self.id}, name='{self.name}')"


class HardDiskComputer:
    def __init__(self, computer_id, hard_disk_id):
        self.computer_id = computer_id
        self.hard_disk_id = hard_disk_id

    def __repr__(self):
        return f"HardDiskComputer(computer_id={self.computer_id}, hard_disk_id={self.hard_disk_id})"