import string
import math

alphabets = ["#"] + list(string.ascii_uppercase)

text = input("\n\nEnter a text: ").strip().upper()
text = text.replace(" ","")

key = input("Enter a Key: ").strip().upper()
key = key.replace(" ", "")
key2 = key

choice = int(input("\nChoose a Option: \n\t 1.Encrypt \n \t 2.Decrypt \n\n\t => "))

length_of_text = len(text)
length_of_key = len(key)

if length_of_text > length_of_key:
    different = length_of_text - length_of_key
    for i in range(math.ceil(different/length_of_key)):
        key+=key2

text_num = []
key_num = []

for i in text:
    text_num.append(alphabets.index(i))
for i in key:
    key_num.append(alphabets.index(i))

if choice == 1:
    sum_num = [text_num[i]+key_num[i] for i in range(length_of_text)]

    for i in range(length_of_text):
        if sum_num[i] > 26:
            sum_num[i] = sum_num[i]%26
    
    cipher = "".join(alphabets[i] for i in sum_num)
    print("Cipher Text :  "+cipher)

elif choice == 2:
    sub_num = [text_num[i]-key_num[i] for i in range(length_of_text)]
    for i in range(length_of_text):
        if sub_num[i] <= 0:
            sub_num[i] = 26 + sub_num[i]

    plain = "".join(alphabets[i] for i in sub_num)
    print("Plain Text :  " + plain)

else:
    print(" \t\t Wrong Choice ! ! ! ")