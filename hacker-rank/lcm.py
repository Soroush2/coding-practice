numbers_list=[int(input("Enter a number: ")) for _ in range(2)]
number_max=max(numbers_list)
gcd=0
for divisor in range(1,number_max):
    if numbers_list[0]%divisor==0 and numbers_list[1]%divisor==0:
        gcd=divisor
lcm=abs(numbers_list[0]*numbers_list[1])//gcd
number1_multipliers=[numbers_list[0]*i for i in range(1,numbers_list[0])]
number2_multipliers=[numbers_list[1]*i for i in range(1,numbers_list[1])]
lcm=min([i for i in number1_multipliers if i in number2_multipliers])
custom_list=[]
print(f"The Greates Common Divisor is {gcd} and The Least Common Multiplier is {lcm}")
    
