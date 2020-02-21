def tabla():
     
        for i in range (1,10):
            n = 10
            num = 1
            print(" ")
            while num <= n:
                z = num * i
                print("{} x {} = {}".format(i, num, z))
                num = num + z
tabla()
