import threading

balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


# def run_thread(n):
#     for i in range(10000):
#         change_it(n)

lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# import threading
# import time
#
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)
# 进程
# import os
# import random
# import time
# from multiprocessing import Process, Queue
#
#
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入：
#     pw.start()
#     # 启动子进程pr,读取：
#     pr.start()
#     # 等待pw结束
#     pw.join()
#     # pr进程离是死循环，无法等待其结束，只能强行终止
#     pr.terminate()
# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
#                       stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode())
# print('Exit code:', p.returncode)

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# import os
# import random
# import time
# from multiprocessing import Pool
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subProcesses done...')
#     p.close()
#     p.join()
#     print('All subProcesses done.')

# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# import json
#
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def __str__(self):
#         return "name:"+self.name+"age:"+str(self.age)+"score:"+str(self.score)


# s = Student('ryan', 27, 99)
#
#
# # print(json.dumps(s))
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#
#     }


# print(json.dumps(s, default=student2dict))


# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
#
# json_str = '{"age":20,"score":90,"name":"Bob"}'
# print(json.loads(json_str, object_hook=dict2student))
# d = dict(name = 'Bob',age = 19,score = 98)
# j = json.dumps(d)
# print(j)

# import pickle
#
# d = dict(name='bob', age=20, score=88)
# pickle.dumps(d)
#
# f = open('C:/Users/Ryan/Desktop/config.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('C:/Users/Ryan/Desktop/config.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)

# import os
# l = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(l)

# import os
# s = os.path.splitext('C:/Users/Ryan/Desktop/config.txt')
# print(s)

# import os
# print(os.name)

# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue().decode('utf-8'))

# from io import StringIO
# f = StringIO('hello!\nHi\n')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


# from io import StringIO
# f = StringIO()
# f.write('hello tao shi yi\n')
# f.write('hello tao shi yi')
# print(f.getvalue())

# with open('C:/Users/Ryan/Desktop/config.txt', 'a') as f:
#     f.write('Hello...\n')

# f = open('C:/Users/Ryan/Desktop/config.txt', 'a')
# f.write('Hello...\n')
# f.close()

# with open('C:/Users/Ryan/Desktop/config.txt', 'r') as f:
#     count = 0
#     while count < 3:
#         print(f.readline())
#         count = count+1

# f = open('C:/Users/Ryan/Desktop/config.txt', 'r')
# txt = f.read()
# f.close()
# print(txt)


# try:
#     f = open('C:/Users/Ryan/Desktop/config.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#
# lisa = Student("lisa", 99)
# ryan = Student("ryan", 66)
#
# print(lisa.get_grade())
# print(ryan.get_grade())
#
# lisa.age = 31
# print(ryan.age)

# def triangles():
#     t = []
#     while True:
#         for i in range(len(t) - 1):
#             t[i] = t[i] + t[i + 1]
#         t.insert(0, 1)
#         yield t[:]
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
#
#
# move(3, 'A', 'B', 'C')
#
#
# # def fact(n):
# #     return fact_iter(n, 1)
# #
# #
# # def fact_iter(num, product):
# #     if num == 1:
# #         return product
# #     return fact_iter(num - 1, num * product)
# #
# #
# def fu(x):
#     return x * x
#
#
# r = map(fu, [1, 2, 3, 4, 5])
# list(r)

# print(fact(5))

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(100))
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x > 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs('a'))


# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# l = [1, 2, 3, 4]
# print(max(l))

# age = 6
# print('your age is', age)
# if age > 18:
#     print("adult")
# elif age > 6:
#     print('teenager')
# else:
#     print('kid')
# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# height = 1.8
# weight = 75
# bim = weight / (height * height)
# print(bim)
# if bim < 18.5:
#     print('guoqing')
# elif bim < 25:
#     print('zhengchang')
# elif bim < 28:
#     print('guozhong')
# elif bim < 32:
#     print('feipang')
# else:
#     print('yanzhongfeipang')

# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum += x
# print(sum)

# sum = 0
# for x in list(range(101)):
#     sum += x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum += n
#     n -= 2
# print(sum)
