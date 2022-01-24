#!/usr/bin/env python
# coding: utf-8

# Question 1

# In[1]:


def twoSum(nums, target):
        lst=[]
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                #print(nums[y],"H")
                if nums[x]+nums[y]==target:
                    #print(x,y,nums[y])
                    lst.extend([x,y])
        lst=list(set(lst))
        return lst

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))


# Question 2

# In[3]:


N = int(input())

students = []
for i in range(2*N):
    students.append(input().split())
grades = {}
for j in range(0, len(students), 2):
    grades[students[j][0]] = float(students[j + 1][0])
result = []
num_to_match = sorted(set(grades.values()))[1]
for pupil in grades.keys():
    if grades[pupil] == num_to_match:
        result.append(pupil)
print('Output: ')
for k in sorted(result):
    print( k)

