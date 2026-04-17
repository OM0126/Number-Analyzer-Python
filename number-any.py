while True:
    
    print("-------__________number analyzer____-----")
    print("1. analyze a number")
    print("2. exit")

    choice = input("enter your choice:")

    if choice == "1":
        
        num = int(input("enter a number:"))

        dig  = 0 
        sum = 0
        even_count = 0 
        odd_count = 0
        largest = 0
        smallest = 9
        rev = 0

        temp = num ## we are using temp to keep our orgginal number safe.

        while temp > 0:

            last = temp  % 10 ## see we will use % this ure to get the last digit

            dig += 1

            sum = sum + last

            if last % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            
            if last > largest:
                largest = last
            
            if last < smallest:
                smallest = last

            rev = rev * 10 + last
            
            temp = temp // 10 ## we are using // this to remove the last digit

            
        print("Digits:", dig)
        print("Sum:", sum)
        print("Even:", even_count)
        print("Odd:", odd_count)
        print("Largest digit:", largest)
        print("smallest digit:", smallest)
        print("reverse of the digits:", rev)

        break

    elif choice == "2":
        print("exiting")
        break
   
    else:
        print("invalid choice,try again")