from __future__ import annotations


class Employee:
    def __init__(self, name: str):
        self._head: Employee = None
        self._is_head: bool = False
        self.name: str = name

    @property
    def head(self) -> Employee:
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @property
    def is_head(self) -> bool:
        return self._is_head

    @is_head.setter
    def is_head(self, is_head):
        self._is_head = is_head


    # def is_head(self, employee: Employee) -> bool:
    #     return employee.is_head


def set_head(master: Employee, slave: Employee) -> bool:
    if not slave or not master:
        return False
    slave.head = master
    master.is_head = True
    return True


if __name__ == "__main__":
    head_employee = Employee("He")
    slave_employee = Employee("Sl")
    if set_head(head_employee, slave_employee):
        print(slave_employee.head.name, "- head of", slave_employee.name)
        print("Is", head_employee.name, "head?", head_employee.is_head)
        print("Is", slave_employee.name, "head?", slave_employee.is_head)
    else:
        print("He or Sl not employee(")
