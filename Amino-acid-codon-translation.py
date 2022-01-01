i = 0
f = 0
n = 1
aminoAcid = str()
aminoAcidl = []
base1 = ["U", "C", "A", "G"]
basel = []
base = input(str("请输入mRNA上的碱基(注:头为起始的碱基):"))
num = len(base) // 3
for s in base:
    basel.append(s)
for n in basel:
    if n in base1:
        continue
    print("碱基有误")
    quit()
while n != 0:
    for p in range(num):
        f = f + 1
        if basel[i] == "A":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                if basel[i] == "G":
                    i = i + 1
                    aminoAcid = "甲硫氨酸"
                    aminoAcidl.append(aminoAcid)
                    n = 0
                    break
                else:
                    i = i + 1
            else:
                i = i + 2
        elif basel[i] == "G":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                if basel[i] == "G":
                    i = i + 1
                    aminoAcid = "缬氨酸"
                    aminoAcidl.append(aminoAcid)
                    n = 0
                    break
                else:
                    i = i + 1
            else:
                i = i + 2
        else:
            if num == f:
                quit()
            else:
                i = i + 3
for p in range(num - f):
    if basel[i] == "U":
        i = i + 1
        if basel[i] == "U":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "苯丙氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "苯丙氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "A":
                i = i + 1
                aminoAcid = "亮氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "G":
                i = i + 1
                aminoAcid = "亮氨酸"
                aminoAcidl.append(aminoAcid)
        elif basel[i] == "C":
            i = i + 2
            aminoAcid = "丝氨酸"
            aminoAcidl.append(aminoAcid)
        elif basel[i] == "A":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "酪氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "酪氨酸"
                aminoAcidl.append(aminoAcid)
            else:
                break
        elif basel[i] == "G":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "半胱氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "半胱氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "G":
                i = i + 1
                aminoAcid = "色胺酸"
                aminoAcidl.append(aminoAcid)
            else:
                break
    elif basel[i] == "C":
        i = i + 1
        if basel[i] == "U":
            i = i + 2
            aminoAcid = "亮氨酸"
            aminoAcidl.append(aminoAcid)
        elif basel[i] == "C":
            i = i + 2
            aminoAcid = "脯氨酸"
            aminoAcidl.append(aminoAcid)
        elif basel[i] == "A":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "组氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "组氨酸"
                aminoAcidl.append(aminoAcid)
            else:
                i = i + 1
                aminoAcid = "谷氨酰胺"
                aminoAcidl.append(aminoAcid)
        elif basel[i] == "G":
            i = i + 2
            aminoAcid = "精氨酸"
            aminoAcidl.append(aminoAcid)
    elif basel[i] == "A":
        i = i + 1
        if basel[i] == "U":
            i = i + 1
            if basel[i] == "G":
                i = i + 1
                aminoAcid = "甲硫氨酸"
                aminoAcidl.append(aminoAcid)
            else:
                i = i + 1
                aminoAcid = "异亮氨酸"
                aminoAcidl.append(aminoAcid)
        elif basel[i] == "C":
            i = i + 2
            aminoAcid = "苏氨酸"
            aminoAcidl.append(aminoAcid)
        elif basel[i] == "A":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "天冬酰胺"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "天冬酰胺"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "A":
                i = i + 1
                aminoAcid = "赖氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "G":
                i = i + 1
                aminoAcid = "赖氨酸"
                aminoAcidl.append(aminoAcid)
        elif basel[i] == "G":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "丝氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "丝氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "A":
                i = i + 1
                aminoAcid = "精氨酸"
                aminoAcidl.append(aminoAcid)
    elif basel[i] == "G":
        i = i + 1
        if basel[i] == "U":
            i = i + 2
            aminoAcid = "缬氨酸"
            aminoAcidl.append(aminoAcid)
        elif basel[i] == "C":
            i = i + 2
            aminoAcid = "丙胺酸"
            aminoAcidl.append(aminoAcid)
        elif basel[i] == "A":
            i = i + 1
            if basel[i] == "U":
                i = i + 1
                aminoAcid = "天冬氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "C":
                i = i + 1
                aminoAcid = "天冬氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "A":
                i = i + 1
                aminoAcid = "谷氨酸"
                aminoAcidl.append(aminoAcid)
            elif basel[i] == "G":
                i = i + 1
                aminoAcid = "谷氨酸"
                aminoAcidl.append(aminoAcid)
        elif basel[i] == "G":
            i = i + 2
            aminoAcid = "甘氨酸"
            aminoAcidl.append(aminoAcid)
print(aminoAcidl)
