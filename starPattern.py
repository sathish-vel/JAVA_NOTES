#............................1.SQUARE STAR PATTERN$#..........................
def square_Pattern(num):         
    print("SQUARE STAR PATTERN:")
    for i in range(num):
        for j in range(num):
            print("*",end=" ")
        print()    

#............................2.HOLLOW SQUARE STAR PATTERN$#..........................
def Hollow_Square_Pattern(num):
    print("HOLLOW SQUARE STAR PATTERN:")
    for i in range(1,num+1):
        for j in range(1,num+1):
            if (i==1 or j==1 or i==num or j==num):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()            
#............................3.HOLLOW SQUARE STAR PATTERN WITH DIAGONAL$#..........................
def Hollow_Square_Pattern_With_Diagonal(num):
    print("HOLLOW SQUARE STAR PATTERN WITH DIAGONAL:")
    for i in range(1,num+1):
        for j in range(1,num+1):
            if(i==1 or j==1 or i==num or j==num or j==(num-i+1) or i==j):
                   print("*",end=" ")
            else:
                print(" ",end=" ")
        print()            
#.........................4.right_triangle_star_pattern.......................
def right_triangle_star_pattern(num):
    print("Right_triangle_star_pattern")            
    for i in range(1,num+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()      
#...............5.Hollow_right_triangle_star_pattern........................
def Hollow_right_triangle_star_pattern(num):
    print("Hollow_right_triangle_star_pattern")            
    for i in range(1,num+1):
            for j in range(1,i+1):
                if(j==1 or i==num or i==j):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")    
            print()     
#......................6.inverted_right_triangle_star_pattern..................            
def inverted_right_triangle_star_pattern(num):
    print("inverted_right_triangle_star_pattern:")
    for i in range(num, 0,-1):
        for j in range(i):
            print("*",end=" ")
        print()    
#.......................7.hollow_mirror_inverted_right_triangle_star_pattern................
def hollow_mirror_inverted_right_triangle_star_pattern(num):
    print("mirror_inverted_right_triangle_star_pattern:")
    for i in range(num):
        for j in range(num):
            if (i==num-1 or j==num-1 or i+j==num-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()             
#.............8.mirror_inverted_right_triangle_star_pattern....................
def mirror_inverted_right_triangle_star_pattern(num):
    print("mirror_inverted_right_triangle_star_pattern:")
    for i in range(num):
        print(" "*i +"*"*(num-i))
             
#.................9.mirror_right_triangle_star_pattern.......................
def mirror_right_triangle_star_pattern(num):
    print("mirror_right_triangle_star_pattern:")
    for i in range(1,num+1):
        print(" "*(num-i) +"*"*i)
#...............10.mirror_right_triangle_star_pattern_own....................
def mirror_right_triangle_star_pattern_own(num):
    print("mirror_right_triangle_star_pattern(OWN METHOD):") 
    for i in range(num):
        for j in range(num-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
#.............11.X_star_pattern.........................
def X_star_pattern(num): 
    print("X_star_pattern:")
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i==j or j==num-i+1:
                print("*",end="")
            else:
                print(" ",end="")
        print()         
#....................12.pyramid_star_pattern.........................
def pyramid_star_pattern(num):
    print("Pyramid_star_pattern (short method):")
    for i in range(1,num+1):
            print(" "*(num-i)+"*"*(2*i-1))
#...................pyramid_star_pattern_own......................
def pyramid_star_pattern_own(num):
    print("Pyramid_star_pattern (OWN method):")
    for i in range(num):
        for j in range(num-i-1):
            print("  ",end="")
        for j in range(2*i-1):
            print(" *",end="") 
        print()     
def inverted_pyramid_star_pattern_own(num):#////////////////
    print("inverted_Pyramid_star_pattern (OWN method):")
    for i in range(num):
        for j in range(i):
            print("  ",end="")
        for j in range(2*(num-i)-1):
            print(" *",end="") 
        print()           
#............#$$$$$$$$$$$$$$$$................
num=int(input("enter the Rows : "))
square_Pattern(num)
Hollow_Square_Pattern(num)
Hollow_Square_Pattern_With_Diagonal(num)
right_triangle_star_pattern(num)
Hollow_right_triangle_star_pattern(num)
inverted_right_triangle_star_pattern(num)
hollow_mirror_inverted_right_triangle_star_pattern(num)
mirror_inverted_right_triangle_star_pattern(num)
mirror_right_triangle_star_pattern(num)
mirror_right_triangle_star_pattern_own(num)
X_star_pattern(num)
pyramid_star_pattern(num)
pyramid_star_pattern_own(num)
inverted_pyramid_star_pattern_own(num)