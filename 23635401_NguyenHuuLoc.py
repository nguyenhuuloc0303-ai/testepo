# Bài tập về nhà Linked Lists
# Câu 1: Tạo một ngăn xếp (stack) bằng cấu trúc danh sách liên kêt đơn (singly linked list)
# - Phần đầu của danh sách liên kết được dùng để biểu diễn phần tử trên cùng của ngăn xếp.

#------------- Lớp danh sách liên kết đơn cho ngăn xếp LinkedStack -------------
class LinkedStack:
    ''' Triển khai ngăn xếp LIFO sử dụng danh sách liên kết đơn '''

    #--------- Lớp riêng _Node gồm phần tử và liên kết đến nút kế tiếp ---------
    class _Node:
        ''' Node riêng tư để lưu trữ một nút liên kết đơn'''

        def __init__(self, element, next):       # Khởi tạo node
            self._element = element              # Trỏ tới phần tử
            self._next = next                    # Trỏ tới nút kế tiếp
  
    #------------------- Các phương thức của stack -----------------------------

    def __init__(self):
        ''' Khởi tạo một ngăn xếp (stack) rỗng gồm _head và _size'''

        self._head = None
        self._size = 0


    def __len__(self):
        ''' Trả về số phần tử trong ngăn xếp '''

        return self._size


    def is_empty(self):
        ''' Trả vè True  nếu ngăn xếp rỗng '''

        return self._size == 0


    def top(self):
        ''' 
        Trả về (nhưng không xóa) phần tử ở trên cùng (top) của ngăn xếp.
        Trả về None nếu ngăn xếp rỗng
        '''

        if self.is_empty():
            raise IndexError('Stack is emty')
        return self._head._element

    def push(self, e):
        ''' Thêm phần tử e vào đầu ngăn xếp '''
        
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        '''
        Xóa và trả về phần tử ở đầu ngăn xếp
        Trả về None nếu ngăn xếp rỗng
        '''
        
        if self.is_empty():
            raise IndexError('Stack is Empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def __str__(self):
        ''' Trả về chuỗi thể hệ ngăn xếp '''

        arr = ''
        start = self._head
        for i in range(self._size):
            arr += str(start._element) + ', '
            start = start._next

        return '<' + arr + ']'

stack = LinkedStack()
print("Ban đầu, stack rỗng:", stack.is_empty())
    
print("Đẩy các phần tử 10, 20, 30 vào stack")
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack hiện tại:", stack)
    
print("Phần tử trên cùng của stack:", stack.top())
    
print("Lấy phần tử khỏi stack:", stack.pop())
print("Stack sau khi pop:", stack)
    
print("Độ dài của stack:", len(stack))
    
print("Xóa hết phần tử trong stack")
stack.pop()
stack.pop()
    
print("Stack có rỗng không?", stack.is_empty())
    
try:
    print("Thử pop khi stack rỗng")
    stack.pop()
except IndexError as e:
    print("Lỗi bắt được:", e)       

#########################################################################
# Câu 2: Tạo một hàng đợi (queue) sử dụng cấu trúc liên kết đơn (Singly linked list)
# - Các phần tử được thêm vào cuối hàng đợi
# - Các phần tử được xóa khỏi đầu hàng đợi

#------------ Tạo lớp danh sách liên kết đơn cho hàng đợi LinkedQueue ----------
class LinkedQueue:
    ''' Triển khai Queue FIFO sử dụng danh sách liên kết đơn '''

    #--------- Lớp riêng _Node gồm phần tử và liên kết đến nút kế tiếp ---------
    class _Node:
        ''' Node lưu trữ danh sách liên kết đơn '''

        def __init__(self, element, next):         # Khởi tạo node
            ''' Khởi tạo một node gồm phần tử element và next trỏ tới phần tử tiếp theo '''
            
            self._element = element
            self._next = next
  
    # ------------------------Các phương thức-----------------------------------

    def __init__(self):
        ''' Khởi tạo một hàng đợi rỗng gồm _head, _tail, _size '''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        ''' Trả về số phần tử trong hàng đợi'''
        return self._size
    

    def is_empty(self):
        ''' Trả về True nếu hàng đợi đang rỗng'''
        return self._size == 0

    def first(self):
        '''Trả về (nhưng không xóa bỏ) phần tử đầu tiên ở đầu hàng đợi
        Trả về None nếu hàng đợi rỗng'''

        if self.is_empty():
            raise IndexError('Queue is Empty')
        
        return self._head._element
  
    def dequeue(self):
        ''' 
        Xóa và trả về phần tử đầu tiên ở đầu hàng đợi (FIFO)
        Trả về None nếu hàng đợi đang trống'''

        if self.is_empty():
            raise IndexError('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
        

    def enqueue(self, e):
        ''' Thêm một phần tử vào phía cuối của hàng đợi'''

        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        

    def __str__(self):
        '''Trả về chuỗi biểu diễn hàng đợi'''
        arr = ''
        start = self._head
        for i in range(self._size):
            arr += str(start._element) + ', '
            start = start._next
        return '<' + arr + '<'

print('\n')
queue = LinkedQueue()
print("Thêm các phần tử 10, 20, 30 vào queue")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue hiện tại:", queue)

print("Phần tử đầu tiên trong queue:", queue.first())

print("Lấy phần tử khỏi queue:", queue.dequeue())
print("Queue sau khi dequeue:", queue)

print("Độ dài của queue:", len(queue))

print("Xóa hết phần tử trong queue")
queue.dequeue()
queue.dequeue()

print("Queue có rỗng không?", queue.is_empty())

try:
    print("Thử dequeue khi queue rỗng")
    queue.dequeue()
except IndexError as e:
    print("Lỗi bắt được:", e) 

####################
# Câu 3: Danh sách liên kết đôi
# - Mỗi nút duy trì tham chiếu đến nút tiếp theo và nút trước đó.
# - Các nút header và trailer được thêm vào để đơn giản hóa các hoạt động.
# - Có thể chèn và xóa tại bất kỳ vị trí quỹ đạo nào với thời gian O(1).

class _DoublyLinkedBase:
    ''' Lớp cơ sở cung cấp danh sách liên kết đôi'''

    #-----------------------------------------------------------------
    class _Node:
        ''' Node lưu trữ danh sách liên kết đôi '''
    
        def __init__(self, element, prev, next):  # Khởi tạo node
          self._element = element                 # Phần tử được lưu trữ
          self._prev = prev                       # Trỏ tới node trước
          self._next = next                       # Trỏ tới node sau
    #-------------------------------------------------------------------
    def __init__(self): 
        '''Khởi tạo danh sách rỗng''' 
        self._header = self._Node(None, None, None) 
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer        # trailer sau header
        self._trailer._prev = self._header        # header trước trailer
        self._size = 0                            # số phần tử

    def __len__(self): 
        '''Trả về số phần tử trong danh sách''' 
        return self._size

    def is_empty(self): 
        '''Trả về True nếu danh sách rỗng'''
        return self._size == 0
        
    def _insert_between(self, e, predecessor, successor):
        '''Thêm phần tử e vào giữa hai node đã tồn tại
        Trả về node mới tạo'''

        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

               
    def _delete_node(self, node): 
        '''Xóa một node trong danh sách
        Trả về phần tử vừa xóa'''

        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


print('\n')       
dll = _DoublyLinkedBase()

print("Ban đầu, danh sách rỗng:", dll.is_empty())
print("Số phần tử ban đầu:", len(dll))

first_node = dll._insert_between(10, dll._header, dll._trailer)
print("Sau khi thêm 10:", len(dll))

second_node = dll._insert_between(20, first_node, dll._trailer)
print("Sau khi thêm 20:", len(dll))

third_node = dll._insert_between(30, second_node, dll._trailer)
print("Sau khi thêm 30:", len(dll))


dll._delete_node(second_node)
print("Sau khi xóa 20:", len(dll))

dll._delete_node(first_node)
print("Sau khi xóa 10:", len(dll))

dll._delete_node(third_node)
print("Sau khi xóa 30:", len(dll))

print("Danh sách có rỗng không?", dll.is_empty())