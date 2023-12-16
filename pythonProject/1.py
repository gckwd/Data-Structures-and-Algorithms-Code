class SequenceList:
    def __init__(self, max_size):
        """初始化顺序表"""
        self.max_size = max_size
        self.data = [None] * max_size
        self.length = 0

    def is_empty(self):
        """判断顺序表是否为空"""
        return self.length == 0

    def is_full(self):
        """判断顺序表是否已满"""
        return self.length == self.max_size

    def insert(self, value):
        """在顺序表尾部插入元素"""
        if self.is_full():
            raise ValueError("顺序表已满，无法插入元素")
        self.data[self.length] = value
        self.length += 1

    def get_length(self):
        """获取顺序表的长度"""
        return self.length

    def find_element(self, value):
        """在顺序表中查找元素"""
        for i in range(self.length):
            if self.data[i] == value:
                return i
        return -1

    def insert_after(self, value_to_insert, after_value):
        """在指定元素之后插入新元素"""
        index = self.find_element(after_value)
        if index == -1:
            raise ValueError(f"未找到值为{after_value}的元素，无法插入")
        self.insert_at_index(index + 1, value_to_insert)

    def insert_at_index(self, index, value):
        """在指定索引位置插入元素"""
        if self.is_full():
            raise ValueError("顺序表已满，无法插入元素")
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.length += 1

    def delete_element(self, value):
        """删除指定元素"""
        index = self.find_element(value)
        if index == -1:
            raise ValueError(f"未找到值为{value}的元素，无法删除")
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.length -= 1

    def display(self):
        """打印顺序表中的所有元素"""
        for i in range(self.length):
            print(self.data[i], end=' ')
        print()

    def destroy(self):
        """销毁顺序表"""
        self.length = 0
        self.data = [None] * self.max_size
