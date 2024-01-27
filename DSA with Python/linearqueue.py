class linearQueue:
    def __init__(self,max):
        self.size=max
        self.ar=[None]*max
        self.front=self.rear=-1
    def enqueue(self,item):
        if(self.rear==self.size-1):
            print("Queue is full")
        elif(self.front==-1):
            self.front=self.rear=0
            self.ar[self.rear]=item
        else:
            self.rear=self.rear+1
            self.ar[self.rear]=item
    def dequeue(self):
        if(self.front==-1):
            print("queue is empty")
        elif(self.front==self.rear):
            x=self.ar[self.front]
            self.front=self.rear=-1
            return x
        else:
            x=self.ar[self.front]
            self.front=self.front+1
            return x
    def display(self):
        if (self.front==-1):
            print("Queue is empty!")
        print("elements of the queue are :")
        for i in range(self.front,self.rear+1):
            print(self.ar[i],end=" ")
if __name__=="__main__":
    obj=linearQueue(10)
    obj.display()
    obj.enqueue(11)
    obj.display()
    obj.enqueue(22)
    obj.display()
    r=obj.dequeue()
    print("deleted element is:",r)
    
