length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = round(length*width, 1)
perimeter = round(length*2 + width*2, 1)
print()
print(f'Rectangle summary:')
print(f'Area: {area}')
print(f'Perimeter: {perimeter}')
print(f'Diagonal: {round((length**2 + width**2)**0.5,2)}')




