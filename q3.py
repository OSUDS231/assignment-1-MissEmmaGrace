seconds = int(input("Please enter a number of seconds to convert into hours, minutes, seconds: "))
hour = seconds//(60*60)
minute = (seconds%(60*60))//60
second = (seconds%(60*60))%60
print(f'{seconds} seconds = {hour} hours, {minute} minutes, {second} seconds')

