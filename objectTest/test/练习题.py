#coding=utf-8

# import time
#
# def timer(func):
#     def warpper(*args,**kwargs):
#         stat_time = time.time()
#         func()
#         stop_time = time.time()
#         print("runnging time is %s" %(stop_time-stat_time))
#     return warpper
#
# @timer
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
# test1()

#
# class foo:
#     def __call__(self, *args,**kwargs):
#         print("call")
#
# ers = foo()
# ers()
#
# try
# except (Error1,Erro2) as e:
#
# except Exception as e:
#
# finally:
# import json
# a = json.dump()
#
# import paramiko
# import os,sys

# a = os.path.dirname(os.path.dirname(__file__))
# print(a)

#
# import socket
# server = socket.socket()
# server.bind('localhost', 3390))
# server.listen(5)
#
# while True:
#     conn, addr = server.accept()
#     data = conn.recv(1024)
#     conn.send()
# # import multiprocessing
#
# a = [1,2,3,4,5]
# a.reverse()
# for i in a:
#     print(i,end='')


class foo(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

class bar(foo):
    a = 1
test1 = bar()
test2 = bar()
print(test1.a,test2.a)

test1.a = 2
print(test1.a,test2.a)



















