class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def offer(self, elmt):
        self.queue.append(elmt)
        print(f"Added to queue > {elmt}")

    def poll(self):
        if self.queue != []:
            self.queue.sort()
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
            

pq = PriorityQueue()
pq.offer(10)
pq.offer(12)
pq.offer(8)
pq.offer(25)

while(not pq.isEmpty()):
    pq.poll()





