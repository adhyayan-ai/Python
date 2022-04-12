nums = []
total = 0
while True:
    prompt = input('Enter your number here or say "add" to stop and add the numbers: ')
    if prompt == "add":
        for i in nums:
            total += i
        print("The sum is", total)
        break
    else:
        nums.append(int(prompt))