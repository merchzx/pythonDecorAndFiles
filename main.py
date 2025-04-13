# def toMuch_calls(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         if count <= 5:
#             return func(*args, **kwargs)
#         else:
#             print(f"Функция func_name вызвана слишком много раз!")
#             return
#
#     return wrapper
#
#
# @toMuch_calls
# def printHello():
#     print("Hello")
#
#
# printHello()
# printHello()
# printHello()
# printHello()
# printHello()
# printHello()


# import time
# from time import sleep
#
#
# def time_it(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         res = end-start
#         print(f"Time of func = {res:.4f}")
#         return result
#     return wrapper
#
# @time_it
# def slow_function():
#     time.sleep(2)
#
# slow_function()

#
# f = input("Input name of file pls: ")
# wordToFind = input("Type word to finding: ")
#
# try:
#     with open(f, 'r', encoding='utf-8') as f:
#         t = f.read()
#         w = t.split()
#         count = w.count(wordToFind)
#         print(f"word '{wordToFind}' =  {count} times.")
# except FileNotFoundError:
#     print("STUPID NIGGA.")
# except Exception as e:
#     print("Error nigga:", e)

f = input("Input name of file pls: ")
wordToFind = input("Type word to finding: ")

try:
    with open('text.txt', 'r', encoding='utf-8') as i:
        l = i.readlines()
        l = [s.strip() for s in l]
        l.sort()

    with open('sorted.txt', 'w', encoding='utf-8') as o:
        for s in l:
            o.write(s + '\n')

    print("File is done sorted.txt")
except FileNotFoundError:
    print("No file nigga")
except Exception as e:
    print("Error:", e)




