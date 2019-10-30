#_*_coding:utf-8_*_
import re  
#文本所在TXT文件  
file = './txt/ckj.txt'   
time1 = 'File Name='  
siappid1='Version='  
userid1='Size='
cc='/>'
f = open(file,'r')  
buff = f.read()  
pat = re.compile(time1+'(.*?)'+siappid1)  #.*?指匹配中间任意个字符，离最后一个标志一个或2个字符
pat1 = re.compile(siappid1+'(.*?)'+userid1)  
pat2 = re.compile(userid1+'(.*?)'+cc)  
x = open("./txt/logfx.txt", 'w')  
x.write("===========================开始数据================================="+"\n")  
x.write("\t"+"File Name"+"\t"+"Version"+"\t\t"+"Size"+"\n")
result=pat.findall(buff)
print(result)
result1=pat1.findall(buff)  
result2=pat2.findall(buff)
print(result2)
if len(result)==0:  
    result.append("空")  
if len(result1)==0:  
    result1.append("空")  
if len(result2)==0:  
    result2.append("空")  
x.write(result[0]+"\t"+result1[0]+"\t"+result2[0]+"\n") #读写不能直接操作列表，但可以是列表中的一个元素
x.write("===========================结束数据================================="+"\n")      
print("执行完毕!生成文件logfx.txt")  
x.close()