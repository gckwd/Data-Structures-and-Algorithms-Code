
class SequenceQueue:
    def __init__(self, capacity=5):
        self.queue = []  # 初始化队列为空列表
        self.capacity = capacity  # 设置队列的容量

    def is_empty(self):
        return len(self.queue) == 0  # 判断队列是否为空

    def is_full(self):
        return len(self.queue) == self.capacity  # 判断队列是否已满

    def enqueue(self, item):
        if self.is_full():
            return False  # 如果队列已满，返回False表示无法入队
        self.queue.append(item)  # 在队列末尾添加新元素
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("从空队列中出队")  # 如果队列为空，则抛出异常
        return self.queue.pop(0)  # 移除队列头部元素并返回

    def front(self):
        if self.is_empty():
            raise IndexError("获取空队列的队头元素")  # 如果队列为空，则抛出异常
        return self.queue[0]  # 返回队列头部元素但不移除

    def size(self):
        return len(self.queue)  # 返回队列中元素的数量

    def traverse(self):
        return self.queue.copy()  # 复制队列中的所有元素以便遍历


# 创建一个顺序队列实例
seq_queue = SequenceQueue()

# 检查队列是否为空并打印结果
print("队列是否为空：", seq_queue.is_empty())

# 试图将一系列奇数元素入队直到队列满，然后打印相关信息
for i in range(1, 20, 2):  # 尝试入队一些奇数
    success = seq_queue.enqueue(i)
    if not success:
        print(f"无法入队元素 {i}：队列已满")
        break

# 遍历队列并打印所有元素
print("入队元素后的队列：", seq_queue.traverse())

# 获取队头元素并打印
if not seq_queue.is_empty():
    print("队头元素：", seq_queue.front())

# 获取队列的大小并打印
print("队列的大小：", seq_queue.size())

# 出队一个元素并打印被移除的元素
print("出队元素：", seq_queue.dequeue())

# 在出队一个元素后尝试入队一个新元素，并打印操作结果及队列的最终状态
success = seq_queue.enqueue(11)
print("在出队一个元素后尝试入队元素 11：", "成功" if success else "失败")
print("最终队列状态：", seq_queue.traverse())
