# coding:utf-8
import pickle
from os.path import isfile
from pickle import dump,load
global PATH
PATH =r'E:\userdata.bin'

##定义user类，实例对象的userName属性存储用户名，passWord属性存储登录密码

class user:
    #实例化对象，默认是None
    def __init__(self,userName=None,passWord=None):
        self.userName=userName
        self.passWord=passWord

    #__repr__()方法定义对象打印格式
    def __repr__(self):
        return 'userName=%s    passWord=%s'%(self.userName,self.passWord)

'''
##函数showAll()
##显示当前已注册用户信息
'''
def showAll():
     global userList#全局变量usrList
     if len(userList)==0:
        print(len(userList))
        print('\t当前无注册用户')
     else:
        print('\t当前已注册用户信息如下:')
        n=0
        for x in userList:
            n+=1
            print('\t%s. '%n,x)
        input('\n\t按Enter键继续...\n')

'''
##函数logn()
##登录操作
'''
def logn():
    try:
        global userList
        userName=input('\t请输入用户名:')
        if find(userName)==-1:
             raise ValueError('用户名不存在,请注册后登录\n')
        else:
            passWord=input('\t请输入用户登录密码：')
            if logn_check(userName,passWord)==-1:
                raise ValueError('密码错误！登录失败\n')
            else:
                raise ValueError('欢迎进入系统！\n')
    except Exception as e:
        print(e)
    input('\n\t按Enter键继续...\n')

'''
##函数regist()
##注册新用户并保存至文件
'''
def regist():
    try:
        global userList
        userName=input('\t请输入用户名：')
        if userName=='':
            raise NameError('\t用户名输入无效！')
        else:
            #检查是否已存在同名的注册用户
            if find(userName)>-1:
                 raise NameError('用户名已注册，请重新添加用户！')
            else:
                passWord=input('\t请输入新用户登录密码：')
                if passWord=='':
                    raise NameError('\t登录密码输入无效！')
                else:
                    userList.append(user(userName,passWord))
                    myfile=open(PATH,'ab') 
                    #将对象保存至文件
                    dump(userList,myfile)
                    myfile.close()
                    print('\t已成功保存用户信息')
                    input('\n\t按Enter键继续......')
                  
    except Exception as e:
        print(e) 
        
        
'''
##函数find(namekey)
##查找是否存在用户名为namekey的注册用户
'''
def find(namekey):
    global userList
    #如果注册用户列表userList中存在namekey的用户，则返回位置，否则返回-1
    n=-1
    for x in userList:
        n+=1
        if x.userName==namekey:
            break
    else:
        n=-1
    return n

'''
##函数logn_check(namekey,paswordkey)
##查找是否存在用户名为namekey，密码为paswordkey的注册用户
'''
def logn_check(namekey,paswordkey):
    global userList
    #如果注册用户列表userList中存在namekey的用户且密码正确，则返回位置，否则返回-1
    n=-1
    for x in userList:
        n+=1
        if x.userName==namekey:
           if x.passWord==paswordkey:
               return n
           else:
            n=-1
    return n

##程序启动时，载入文件中的用户数据

if isfile(PATH):
    myfile=open(PATH,'rb')
    x=myfile.read(1)
    if x==b'':
        userList=list()
        myfile.close()
    else:  
        #将文件中的数据解析为一个对象
        ##由于dump函数特性，采用while True循环结合异常处理（读至文件末尾时）
        #读取文件信息至对象列表userList
        #n为计数器
        n=0
        with open(PATH,"rb") as f :
            while True:
                try:
                    if n==0:
                        userList=pickle.load(f)
                        n+=1
                    else:
                        temp=pickle.load(f)
                        userList.append(user(temp[n].userName,temp[n].passWord))
                        n+=1
                except Exception as e:
                    print(e) 
                    break
else:
    print('目标路径非文件!')

#循环显示系统操作菜单直到退出系统
while True:
    print('***用户管理系统***')
    print(' 1.显示全部用户')
    print(' 2.登录系统')
    print(' 3.注册新用户')
    print(' 4.退出系统')
    print('***User_Manage***')
    no=input('请选择对应菜单：')
    if no=='1':
        showAll()
    elif no=='2':
        logn()
    elif no=='3':
        regist()
    elif no=='4':
        print('谢谢使用，系统已退出')
        break