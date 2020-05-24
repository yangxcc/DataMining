'''
python中没有二进制类型，但是可应用string（字符串类型）
来存储二进制类型的数据，因为string是以字节为单位的
'''
import struct
a=20
bytes=struct.pack('i',a)
print(bytes)
a,=struct.unpack('i',bytes)  #注意：unpack（）返回的是一个元组，如果只有一个变量，则要加上逗号
print(a)

#如果是有多个数据组成
x='hello'
y='world！'
c=20
d=45.123
bytes=struct.pack('5s6sif',x.encode('utf-8'),y.encode('utf-8'),c,d)
#5s表示占5个字符宽度的字符串，i表示整数，2i表示两个整数，f表示浮点型小数
print(bytes)