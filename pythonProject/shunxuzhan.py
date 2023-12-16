class SequenceStack:
    def __init__(self, maxsize):
        self.max = maxsize
        self.elem = [None] * self.max
        self.top = 0
        self.base = 0

    def is_empty(self):
        return self.top == self.base

    def push(self, elem):
        if self.top - self.base == self.max:
            raise Exception("The stack is full!")
        self.elem[self.top] = elem
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        self.top -= 1
        return self.elem[self.top]

    def get_top(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        return self.elem[self.top - 1]

    def get_length(self):
        return self.top - self.base

    def traverse(self):
        for i in range(self.top):
            print(self.elem[i], end=" ")
        print()


if __name__ == '__main__':
    elements = [1, 3, 5]  # 定义要入栈的元素
    s = SequenceStack(len(elements))  # 初始化栈

    print("Is the stack empty? ", s.is_empty())

    for elem in elements:
        s.push(elem)  # 元素入栈

    print("Stack elements: ", end="")
    s.traverse()  # 遍历栈内所有元素

    print("Top element of the stack: ", s.get_top())  # 获取栈顶元素
    print("Length of the stack: ", s.get_length())  # 获取栈的长度

    while not s.is_empty():
        e = s.pop()  # 弹栈
        print(f"After popping, top element is: {e}, Stack now: ", end="")
        s.traverse()  # 输出每次弹栈后，栈内剩余的元素

    print("Is the stack empty? ", s.is_empty())
