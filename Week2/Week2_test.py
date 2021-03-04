# 第一題 

def calculate(min, max):
    s = 0
    for  i  in range(min,max+1):
        s += i
    print("最後印出" , s)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

 
# 第二題
def avg(data):
    s = data["count"]
    y = 0
    for i in range(s):
        y += data["employees"][i]["salary"]
    x = y // s
    print(f"公司員工平均薪資{x}元")
    


avg({"count":3,"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


# 第三題  
def maxProduct(nums):
    w = []
    for i in  range(0, len(nums)):
        for j in range(0, len(nums)):
                if i != j :
                    mul = nums[i] * nums[j]
                    w.append(mul)
                    # print(mul)
            
    print(max(w))


 
            


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值
maxProduct([-20, -20, 5, 2, 1])


# 第四題
def twoSum(nums, target):
    for i in nums:
        for j in range(target+1):
           if i + j is target:
               z = nums.index(i)
               y = nums.index(j)
               return [z,y]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


# 第五題
def maxZeros(nums):
    a = 0
    f = []
    for i in nums:
        if i == 0:
           a += 1
           f.append(a)  
        elif i  == 1 :
            f.append(a)
            a = 0
            
                
    print(max(f))

  
# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([1, 1, 1, 1, 0]) # 得到 1
maxZeros([1, 1, 1, 1, 0, 1, 0, 1, 1]) # 得到 1
