# 根据要求，将代码注释改为中文

class SequenceString:
    def __init__(self, initial_string=""):
        self.string = initial_string  # 初始化字符串

    def copy(self, src):
        self.string = src.string  # 复制操作：将一个字符串的内容复制到另一个字符串
        return self.string

    def compare(self, src):
        return self.string == src.string  # 比较操作：比较两个字符串是否相等


# 根据实验步骤创建顺序串对象
stringSrc = SequenceString("Array")  # 创建顺序串 stringSrc 并初始化为 "Array"
stringDst = SequenceString("GeneralizedList")  # 创建顺序串 stringDst 并初始化为 "GeneralizedList"

# 执行复制操作并打印结果
copy_result = stringDst.copy(stringSrc)
print(f"复制结果: {copy_result}")

# 验证复制操作的正确性
print("复制正确:", stringDst.string == stringSrc.string)

# 执行比较操作并打印结果
compare_result = stringDst.compare(stringSrc)
print(f"比较结果: {compare_result}")

# 验证比较操作的正确性，因为 stringDst 已从 stringSrc 复制，所以应该相等
print("比较正确:", compare_result == True)
