import os
import sys , os
global aminoAcid
global basel
global base2
aminoAcid = []
judge1 = ["A","U","G"]
judge2 = ["G","U","G"]
base1 = ["U", "C", "A", "G"]
base2 = []
basel = []



def write():
    global f
    f = -1
    global base
    base = input(str("请输入mRNA上的碱基(注:头为起始的碱基):"))

    # 将元素加入basel列表中
    for s in base:
        basel.append(s)

    # 判断输入碱基是否符合要求
    for n in basel:
        if n in base1:
            continue
        print("碱基有误")

        # 获取PYTHON的位置
        python = sys.executable

        # sys.argv用来获得此文件的位置
        # os.execl用来向命令行输出指令
        # 此方法于网络寻得，理解并不深
        os.execl(python,python,*sys.argv)
    
    global num 
    num = (len(base) // 3) - 1
    global numOrigin
    numOrigin = len(base) // 3



def remove_list():
    del basel[0]
    del basel[0]
    del basel[0]


def judgeOrigin():
# 判断是否为起始密码子
    for i in range(numOrigin):
        global f
        f = f + 1
        base2.append(basel[0])
        base2.append(basel[1])
        base2.append(basel[2])
        if base2 == judge1:
            aminoAcid.append("甲硫氨酸")
            remove_list()
            break
        elif base2 == judge2:
            aminoAcid.append("颉氨酸")
            remove_list()
            break
        else:
            if f == num:
                print("无法形成氨基酸")
                python = sys.executable
                os.execl(python,python,*sys.argv)
            else:
                remove_list()
                base2.clear()

def mainFunction():
# 遍历列表以达到程序目的
    for p in range(num - f):
        if basel[0] == "U":
            if basel[1] == "U":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("苯丙氨酸")
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("苯丙氨酸")
                elif basel[2] == "A":
                    remove_list()
                    aminoAcid.append("亮氨酸")
                elif basel[2] == "G":
                    remove_list()
                    aminoAcid.append("亮氨酸")
                 
            elif basel[1] == "C":
                remove_list()
                aminoAcid.append("丝氨酸")
             
            elif basel[1] == "A":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("酪氨酸")
                 
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("酪氨酸")
                 
                else:
                    break
            elif basel[1] == "G":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("半胱氨酸")
                 
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("半胱氨酸")
                 
                elif basel[2] == "G":
                    remove_list()
                    aminoAcid.append("色胺酸")
                 
                else:
                    break
        elif basel[0] == "C":
            if basel[1] == "U":
                remove_list()
                aminoAcid.append("亮氨酸")
             
            elif basel[1] == "C":
                remove_list()
                aminoAcid.append("脯氨酸")
             
            elif basel[1] == "A":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("组氨酸")
                 
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("组氨酸")
                 
                else:
                    remove_list()
                    aminoAcid.append("氨酰胺")
                 
            elif basel[1] == "G":
                remove_list()
                aminoAcid.append("精氨酸")
             
        elif basel[0] == "A":
            if basel[1] == "U":
                if basel[2] == "G":
                    remove_list()
                    aminoAcid.append("甲硫氨酸")

                else:
                    remove_list()
                    aminoAcid.append("异亮氨酸")
                 
            elif basel[1] == "C":
                remove_list()
                aminoAcid.append("苏氨酸")
             
            elif basel[1] == "A":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("天冬酰胺")
                 
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("天冬酰胺")
                 
                elif basel[2] == "A":
                    remove_list()
                    aminoAcid.append("赖氨酸")
                 
                elif basel[2] == "G":
                    remove_list()
                    aminoAcid.append("赖氨酸")
                 
            elif basel[1] == "G":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("丝氨酸")
                
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("丝氨酸")
                
                elif basel[2] == "A":
                    remove_list()
                    aminoAcid.append("精氨酸")
                
        elif basel[0] == "G":
            if basel[1] == "U":
                remove_list()
                aminoAcid.append("缬氨酸")
            
            elif basel[1] == "C":
                remove_list()
                aminoAcid.append("丙胺酸")
            
            elif basel[1] == "A":
                if basel[2] == "U":
                    remove_list()
                    aminoAcid.append("天冬氨酸")
                
                elif basel[2] == "C":
                    remove_list()
                    aminoAcid.append("天冬氨酸")
                
                elif basel[2] == "A":
                    remove_list()
                    aminoAcid.append("谷氨酸")
                
                elif basel[2] == "G":
                    remove_list()
                    aminoAcid.append("谷氨酸")
                
            elif basel[1] == "G":
                remove_list()
                aminoAcid.append("甘氨酸")



judgeStart = "y"
while judgeStart == "y":
    aminoAcid.clear()
    basel.clear()
    base2.clear()
    judgeStart == "n"
    write()
    judgeOrigin()
    mainFunction()
    print(aminoAcid)
    judgeStart = input("是否再次执行程序(y/n)")
    if judgeStart == "y":
        judgeStart = "y"
    else:
        break