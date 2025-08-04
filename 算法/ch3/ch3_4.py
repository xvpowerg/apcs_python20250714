class Queue():
    def __init__(self):
        self.my_queue = []

    def enqueue(self,data):
        self.my_queue.append(data)
    def dequeue(self):
        return self.my_queue.pop(0)
    def size(self):
        return len(self.my_queue)
    def isEmpy(self):
        return self.size() == 0
    
queue = Queue()

queue.enqueue("Ken")
queue.enqueue("Vivin")
queue.enqueue("Lindy")
while queue.size():
    print(queue.dequeue())

