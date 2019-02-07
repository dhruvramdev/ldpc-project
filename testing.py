import pandas as pd
article_read = pd.read_csv('zoo.csv',delimiter = ',')

def decimalToBinary(num,k_prec):
    binary=""
    integral = int(num)
    fractional = num-integral
    intLength = 0
    while(integral):
        intLength+=1
        remainder=integral%2
        binary+=str(remainder)
        integral=integral/2
    if(intLength<6):
        while(intLength<6):
            intLength+=1
            binary+="0"
    binary=binary[ : : -1]
    binary+='.'
    while(k_prec):
        fractional*=2
        fract_bit = int(fractional)
        if(fract_bit==1):
            fractional-=fract_bit
            binary+='1'
        else:
            binary+='0'
        k_prec-=1
    return binary

def binaryToDecimal(binary,length):
    i=0
    intDecimal=0
    fracDecimal=0.0
    intLength=0
    while(binary[intLength]!='.'):
        intLength+=1
    point=intLength
    intLength-=1
    while(binary[i]!='.'):
        if(binary[i]=='1'):
            intDecimal+=pow(2,intLength)
        intLength-=1
        i+=1
    i=1
    point+=1
    while(point<length):
        if(binary[point]=='1'):
            fracDecimal+=1.0/pow(2,i)
        point+=1
        i+=1
    finalDecimal = float(intDecimal) + float(fracDecimal)
    return round(finalDecimal,4)

def compressBinary(binary):
    i=0
    compressBin = ""
    while(i<6):
        if(i%2 == 0):
            if((binary[i] == '0' and binary[i+1] == '0') or (binary[i] == '1' and binary[i+1] == '1')):
                compressBin+="0"
            else:
                compressBin+="1"
        i+=1
    compressBin+="."
    i=0
    while(i<16):
        if(i%2 == 0):
            if((binary[i+8] == '0' and binary[i+7] == '0') or (binary[i+8] == '1' and binary[i+7] == '1')):
                compressBin+="0"
            else:
                compressBin+="1"
        i+=1
    return compressBin

print compressBinary(decimalToBinary(26.2257,16))
print binaryToDecimal(decimalToBinary(26.2257,16),23)
print "\n\n"
i=0
for i in range(0,20):
   print "\n"
   print binaryToDecimal(decimalToBinary(article_read.temperature[i],16),23)
   print article_read.temperature[i]
