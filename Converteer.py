weight = int(input('ENTER YOUR WEIGHT: '))
unit = input("ENTER THE UNIT (L)/(K): ")

if unit.upper() == "L":
    weightConverted = weight * 0.45
    print(f'YOUR WEIGHT INKGS IS: {weightConverted}')

elif unit.upper() == "K":
    weightConverted = weight / 0.45
    print(f'YOUR WEIGHT IN LLB IS: {weightConverted}')
    
else:
    print("ENTER THE RIGHT LETTER!!! ")
 