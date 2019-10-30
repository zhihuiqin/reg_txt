import re  
#文本所在TXT文件  
file = './txt/ck.txt'   
time1 = 'File Name='  
siappid1='Version='  
userid1='Size='
IsPE1 ='IsPE='
MD51 = 'MD5='
cc='/>'
aa='<'
f = open(file,'r')  
buff = f.read()  
pat = re.compile(time1+'(.*?)'+IsPE1)  
pat1 = re.compile(IsPE1+'(.*?)'+siappid1)  
pat2 = re.compile(siappid1+'(.*?)'+userid1)
pat3 = re.compile(aa+'(.*?)'+cc)
result6=pat3.findall(buff)
part4=re.compile(userid1+'(.*?)'+MD51)
part5=re.compile(MD51+'(.*?)'+cc)
x = open("./txt/logfx01.txt", 'w')  
x.write("===========================开始数据================================="+"\n")  
x.write("\t"+"File Name"+"\t"+"IsPE"+"\t"+"Version"+"\t"+"Size"+"\t"+"MD5"+"\n")
for i in range(0,len(result6)): 
    result=pat.findall(result6[i])
   # print(result)
    result1=pat1.findall(result6[i])  
    result2=pat2.findall(result6[i])
   # print(result2)
    result3=part4.findall(result6[i])
    result4=part5.findall(result6[i])
    if len(result)==0:  
        result.append("空")  
    if len(result1)==0:  
        result1.append("空")  
    if len(result2)==0:  
        result2.append("空")
    if len(result4)==0:  
        result4.append("空")
    x.write(result[0]+"\t"+result1[0]+"\t"+result2[0]+"\t"+result3[0]+"\t"+result4[0]+"\n")  
x.write("===========================结束数据================================="+"\n")      
print("执行完毕!生成文件logfx01.txt")  
x.close()