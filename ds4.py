def datastructure():
    ds_input = input('Enter:\n 1 for Stack,\n 2 for Queue,\n 3 for Tree, \n 4 to exit.\nYour Input - ')
    def ds_sel():
        if ds_input == 1:
            print('Congratulations you\'ve selected Stack Data Structure.')
            s = []

            def stack():
                i = 0
                x = int(input(
                    'Menu For Stack:\n1 to push\n2 to pop\n3 to check if stack is empty\n4  to exit\n5 to print stack \nYour Input - '))
                if x == 1:
                    k = int(input('Enter the number of elements you want to include in stack - '))
                    while i <= k - 1:
                        z = input('Enter the number you want to push in stack - ')
                        s.append(z)
                        i += 1
                    print(f'The stack is {s}')
                    stack()
                elif x == 2:
                    print(f'The stack is {s}')

                    def pop():
                        j = int(input('Enter the index of element you want to pop out - '))
                        k = int(j - 1)
                        if k < len(s):
                            print('The element you pop out is ' + s.pop(k))
                            print(s)
                        else:
                            print('Enter element which is inside the index of stack -')
                            pass

                    if len(s):
                        pop()
                    else:
                        pass
                    stack()
                elif x == 3:
                    if len(s):
                        print('The stack is not empty')
                    else:
                        print('The stack is empty')
                    stack()
                elif x == 4:
                    datastructure()
                elif x == 5:
                    print(s)
                    stack()
                elif ((x>5)or(x<1)):
                    print("Invalid entry.")
                    stack()
            stack()
        elif ds_input == 2:
            print('Congratulations you\'ve selected Queue Data Structure.')
            q = []

            def queue():
                i = 0
                x = int(input('Menu For Queue:\n1 to push\n2 to pop\n3 to check if queue is empty\n4  to exit\n5 to print queue \nYour Input - '))
                if x == 1:
                    k = int(input('Enter the number of elements you want to include in queue - '))
                    while i <= k - 1:
                        z = input('Enter the number you want to push in queue -')
                        q.append(z)
                        i += 1
                    print(f'The queue is {q}')
                    queue()
                elif x == 2:
                    print(f'The queue is {q}')

                    def pop():
                        j = int(input('Enter the index of element you want to pop out.'))
                        k = int(j - 1)
                        if k < len(q):
                            print('The element you pop out is ' + q.pop(k))
                            print(q)
                        else:
                            print('Enter element which is inside the index of queue.')
                            pass

                    if len(q):
                        pop()
                    else:
                        pass
                    queue()
                elif x == 3:
                    if len(q):
                        print('The queue is not empty')
                    else:
                        print('The queue is empty')
                    queue()
                elif x == 4:
                    datastructure()
                elif x == 5:
                    print(q)
                    queue()
                elif ((x>5)or(x<1)):
                    print("Invalid entry.")
                    queue()
            queue()
        elif ds_input == 3:
            print('Congratulations you\'ve selected Tree Data Structure.')
            d = {}
            def tree():
                x = int(input('Menu For Tree:\n1 to enter nodes\n2 to pop\n3 to check if tree is empty\n4  to exit\n5 to print tree \nYour Input - '))
                if x == 1:
                    p_node = input('Enter a parent node.')
                    a = input('Enter left child node.')
                    b = input('Enter right child node.')
                    c_node = [a, b]
                    d.update({p_node: c_node})
                    print(d)
                    tree()
                elif x == 2:
                    print(d)
                    j = input('Enter the Parent node which you want to pop.')
                    d.pop(j)
                    print(d)
                    tree()
                elif x == 3:
                    if len(d):
                        print('The tree is not empty')
                    else:
                        print('The tree is empty')
                    tree()
                elif x == 4:
                    datastructure()
                elif x == 5:
                    print(d)
                    tree()
                elif ((x>5)or(x<1)):
                    print("Invalid entry.")
                    tree()
            tree()
        elif ds_input == 4:
            pass
    try:
        ds_input = int(ds_input)
        if (ds_input >= 1)and(ds_input <= 4):
            ds_sel()
        elif ((ds_input <= 0) or (ds_input >= 4)):
            def inv():
                print('Invalid entry.')
                ds_input = int(input('Enter:\n 1 for Stack,\n 2 for Queue,\n 3 for Tree, \n 4 to exit.\n'))

                if ((ds_input >= 1) and (ds_input <= 4)):
                    ds_sel()
                else:
                    inv()
            inv()
    except:
        print('Invalid Entry. Only Integers are allowed.')
        datastructure()
datastructure()