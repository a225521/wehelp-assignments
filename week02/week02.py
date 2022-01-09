# 1.函式與流程控制: 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
def calculate(min,max):
    sum=0
    for x in range(min,max+1):
        sum=sum+x
    print(sum)
calculate(1,3)
calculate(4,8)

# 2. Python 字典與列表: 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。

def avg(data):
    length=data["count"]
    sum=0
    for n in data["employees"]:
        sum=sum+n["salary"]
    print(sum/length)
avg({
"count":3,
"employees":[
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
})

#3. 演算法
def maxProduct(nums):
    if len(nums)>=2:
        result=nums[0]*nums[1]
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            temp=nums[i]*nums[j]
            if result<temp:
                result=temp  
    print(result)
   
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])

#4. 英文版演算法
def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
result=twoSum([2, 11, 7, 15], 9)
print(result)