class Queue:
    def __init__(self):
        self.queue = []
    
    def offer(self, elmt):
        self.queue.append(elmt)
        print(f"Added to queue > {elmt}")

    def poll(self):
        if self.stack != []:
            print(f"Removed from queue > {self.queue[0]} ")
            self.queue.remove(self.queue[0])
        else:
            print("Queue is empty")

    def peek(self):
        print(f"Head is > {self.queue[0]}")

    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False

q = Queue()
q.offer(20)
q.offer(90)
q.offer(34)
q.poll()
q.peek()
