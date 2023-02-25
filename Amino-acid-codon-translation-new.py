key_codon_dict = {'UUU': '苯丙氨酸', 'UUC': '苯丙氨酸', 'UUA': '亮氨酸', 'UUG': '亮氨酸',
                   'UCU': '丝氨酸', 'UCC': '丝氨酸', 'UCA': '丝氨酸', 'UCG': '丝氨酸',
                   'UAU': '苏氨酸', 'UAC': '苏氨酸', 'UAA': '终止密码子', 'UAG': '终止密码子',
                   'UGU': '半胱氨酸', 'UGC': '半胱氨酸', 'UGA': '终止密码子', 'UGG': '色氨酸',
                   'CUU': '亮氨酸', 'CUC': '亮氨酸', 'CUA': '亮氨酸', 'CUG': '亮氨酸',
                   'CCU': '脯氨酸', 'CCC': '脯氨酸', 'CCA': '脯氨酸', 'CCG': '脯氨酸',
                   'CAU': '组氨酸', 'CAC': '组氨酸', 'CAA': '甘氨酸', 'CAG': '甘氨酸',
                   'CGU': '精氨酸', 'CGC': '精氨酸', 'CGA': '精氨酸', 'CGG': '精氨酸',
                   'AUU': '异亮氨酸', 'AUC': '异亮氨酸', 'AUA': '异亮氨酸', 'AUG': '甲硫氨酸(起始密码子)',
                   'ACU': '苏氨酸', 'ACC': '苏氨酸', 'ACA': '苏氨酸', 'ACG': '苏氨酸',
                   'AAU': '天冬酰胺', 'AAC': '天冬酰胺', 'AAA': '赖氨酸', 'AAG': '赖氨酸',
                   'AGU': '丝氨酸', 'AGC': '丝氨酸', 'AGA': '精氨酸', 'AGG': '精氨酸',
                   'GUU': '缬氨酸', 'GUC': '缬氨酸', 'GUA': '缬氨酸', 'GUG': '缬氨酸(起始密码子)',
                   'GCU': '丙氨酸', 'GCC': '丙氨酸', 'GCA': '丙氨酸', 'GCG': '丙氨酸',
                   'GAU': '天冬酰胺', 'GAC': '天冬酰胺', 'GAA': '谷氨酸', 'GAG': '谷氨酸',
                   'GGU': '甘氨酸', 'GGC': '甘氨酸', 'GGA': '甘氨酸', 'GGG': '甘氨酸'}

# 用户输入区域
base = input("请输入mRNA上的碱基:")

# 获取字符串总长，并未循环次数做准备
base_length = len(base) // 3

bool_key_start = False
cycles_counts = 0
start_step = 0
step = 0
# 获取字符串切片起始数
for i in range(base_length):
    cycles_counts += 1
    
    # 以字符串中3个元素为一组进行截取
    pre_base = base[(0 + step): (3 + step)]
    
    compare_base = key_codon_dict[pre_base]
    
    if compare_base == key_codon_dict["AUG"] :
        start_step = step
        bool_key_start = True
        break
    elif compare_base == key_codon_dict["GUG"] :
        start_step = step
        bool_key_start = True
        break
    else:
        step += 3

# 判断mRNA链中是否有起始密码子
if bool_key_start == False:
    print("该氨基酸链可能无法形成")
    quit()

bool_key_end = False

# 获取字符串切片末尾数
end_step = 0
for i in range((base_length - cycles_counts)):
    
    # 以字符串中3个元素为一组进行截取
    pre_base = base[(0 + step): (3 + step)]
    
    
    compare_base = key_codon_dict[pre_base]
    
    if compare_base == key_codon_dict["UAA"] :
        end_step = step
        bool_key_end = True
        break
    elif compare_base == key_codon_dict["UAG"] :
        end_step = step
        break
    elif compare_base == key_codon_dict["UGA"] :
        end_step = step
        bool_key_end = True
        break
    else:
        step += 3
        end_step = step
        
# 判断密码子中是否有密码子        
if bool_key_end == False:
    print("该密码子中不含终止密码子")


# 最终处理
final_end_step = end_step + 3
final_cycles_counts = (final_end_step - start_step) // 3
step_ = 0

for i in range(final_cycles_counts):
    
    pre_base = base[(start_step + step_): ((start_step + 3) + step_)]
    step_ += 3
    print (key_codon_dict[pre_base], end=" ")