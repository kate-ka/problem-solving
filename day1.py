with open('day1.txt', 'r') as f:
    count = 0
    lines = f.read()
    i = 1
    done = False
    for item in lines:

        if item == '(':
            count += 1
        if item == ')':

            count -= 1
        if done is False and count==-1:

            # print the position of a character when Santa enters the basement
            print(i)
            done = True
        i += 1

    print(count)


    # print (count) # 138



