class GFG :

    class Node :
        data = 0
        prev = None
        next = None

        @staticmethod
        def getnode( data) :
            newNode = GFG.Node()
            newNode.data = data
            newNode.prev = None
            newNode.next = None
            return newNode

    class Deque :
        front = None
        rear = None
        Size = 0
        def __init__(self) :
            self.front = None
            self.rear = None
            self.Size = 0

        def isEmpty(self) :
            return (self.front == None)

        def size(self) :
            return self.Size

        def insertFront(self, data) :
            newNode = GFG.Node.getnode(data)

            if (newNode == None) :
                print("OverFlow\n", end ="")
            else :

                if (self.front == None) :
                    self.rear = newNode
                    self.front = newNode
                else :
                    newNode.next = self.front
                    self.front.prev = newNode
                    self.front = newNode

                self.Size += 1

        def insertRear(self, data) :
            newNode = GFG.Node.getnode(data)

            if (newNode == None) :
                print("OverFlow\n", end ="")
            else :

                if (self.rear == None) :
                    self.front = newNode
                    self.rear = newNode
                else :
                    newNode.prev = self.rear
                    self.rear.next = newNode
                    self.rear = newNode
                self.Size += 1
                
        def deleteFront(self) :

            if (self.isEmpty()) :
                print("UnderFlow\n", end ="")
            else :
                temp = self.front
                self.front = self.front.next

                if (self.front == None) :
                    self.rear = None
                else :
                    self.front.prev = None

                self.Size -= 1

        def deleteRear(self) :

            if (self.isEmpty()) :
                print("UnderFlow\n", end ="")
            else :
                temp = self.rear
                self.rear = self.rear.prev

                if (self.rear == None) :
                    self.front = None
                else :
                    self.rear.next = None

                self.Size -= 1

        def getFront(self) :

            if (self.isEmpty()) :
                return -1
            return self.front.data

        def getRear(self) :

            if (self.isEmpty()) :
                return -1
            return self.rear.data
        
        def erase(self) :
            self.rear = None
            while (self.front != None) :
                temp = self.front
                self.front = self.front.next
            self.Size = 0

    @staticmethod
    def main( args) :
        dq = GFG.Deque()
        print("Insert element \'5\' at rear end\n", end ="")
        dq.insertRear(5)
        print("Insert element \'10\' at rear end\n", end ="")
        dq.insertRear(10)
        print("Rear end element: " + str(dq.getRear()) + "\n", end ="")
        dq.deleteRear()
        print("After deleting rear element new rear" + " is: " + str(dq.getRear()) + "\n", end ="")
        print("Inserting element \'15\' at front end \n", end ="")
        dq.insertFront(15)
        print("Front end element: " + str(dq.getFront()) + "\n", end ="")
        print("Number of elements in Deque: " + str(dq.size()) + "\n", end ="")
        dq.deleteFront()
        print("After deleting front element new " + "front is: " + str(dq.getFront()) + "\n", end ="")

if __name__=="__main__":
    GFG.main([])
