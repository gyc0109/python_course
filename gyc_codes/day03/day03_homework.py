# 1. 判断下列逻辑语句的True,False
# 
#    ```python
#    1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
#	 False or True or False and True and True or True
#    False or True or False or True
#    True
#
#    not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
#	 False and True or False and True and True or False
# 	 False or False or False
# 	 False
#    
#    ```
# 
# 2. 求出下列逻辑语句的值。
# 
#    ```python
#    8 or 3 and 4 or 2 and 0 or 9 and 7
#	 8 or 4 or 0 or 7
# 	 8	    
#    
#    0 or 2 and 3 and 4 or 6 and 0 or 3
# 	 0 or 4 or 0 or 3
# 	 4
#
#    ```
# 
# 3. 下列结果是什么？
# 
#    ```python
#    6 or 2 > 1 6
#    3 or 2 > 1 3
#    0 or 5 < 4 False
#    5 < 4 or 3 3
#    2 > 1 or 6 True
#    3 and 2 > 1 True
#    0 and 3 > 1 0
#    2 > 1 and 3 3
#    3 > 1 and 0 0
#    3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2 2
#    ```
# 
# 4. 实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）。
# 
# total = 0
# user = "gyc"
# password = 123456
# 
# while total < 3:
# 	input_user = input("Please input username: ")
# 	input_password = int(input("Please input password: "))
# 	
# 	if input_user == user and input_password == password:
# 		print("login success")
# 		break
# 	else:
# 		print("login error")
# 		total += 1
# 
# 
# 5. 猜年龄游戏 
#    要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。
# age = 20
# total = 0
# 
# while total < 3:
# 	user_age = int(input("Please input your want age: "))
# 
# 	if user_age == age:
# 		print("Yes! You success")
# 		break
# 	else:
# 		print("NO! You error")
# 		total += 1
# 		continue
# 
# 6. 猜年龄游戏升级版
#    要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
age = 20
total = 0

while total < 3:
	user_age = int(input("Please input your want age: "))

	if user_age == age:
		print("Yes! You success")
		break
	else:
		print("NO! You error")
		total += 1
		if total == 3:
			choose = input("You want continue: (yes/no)")
			if choose == "yes":
				total = 0
			else:
				total = 3	 
				print("game over")
		continue
