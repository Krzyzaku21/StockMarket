# %%
class Process:
    def __init__(self, obj_id, obj_order, obj_type, obj_price, obj_quantity):
        self.obj_id = obj_id
        self.obj_order = obj_order
        self.obj_type = obj_type
        self.obj_price = obj_price
        self.obj_quantity = obj_quantity

    def __repr__(self):
        return f'Process({self.obj_id}, {self.obj_type}, {self.obj_price}, {self.obj_quantity})'


class Run(Process):
    def __init__(self):
        self.process = Process
        self.bill = []
        self.coins = 0

    def sums(self, element):
        communicate = ''
        if element.obj_order == 'Buy':
            self.coins -= element.obj_quantity * element.obj_price
        else:
            self.coins += element.obj_quantity * element.obj_price
        if self.coins < 0:
            communicate = 'lose'
        else:
            communicate = 'earn'
        print(f'You {element.obj_order}: {element.obj_quantity} apples and {communicate} {self.coins}')

    def check_type(self, element):
        if element.obj_type == 'Add':
            self.bill.append(element)
        elif element.obj_type == 'Remove':
            for e in self.bill:
                if element.obj_id in e.obj_id:
                    self.bill.remove(e)
        print(f'{element.obj_type}: {element} to: ', self.bill)
        return self.bill


# %%
ID = [
    {'001': ['Buy', 'Add', 20.0, 100]},
    {'002': ['Sell', 'Add', 25.0, 200]},
    {'003': ['Buy', 'Add', 23.0, 50]},
    {'004': ['Buy', 'Add', 23.0, 70]},
    {'003': ['Buy', 'Remove', 23.0, 50]},
    {'005': ['Sell', 'Add', 28, 100]}
]

if __name__ == '__main__':
    run = Run()
    for id_elem in ID:
        for key, values in id_elem.items():
            elem = Process(key, *values)
            run.check_type(elem)
    print()
    print(run.bill)
    print()
    for proc in run.bill:
        run.sums(proc)

# %%
