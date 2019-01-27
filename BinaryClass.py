#Binary class written by Cambrea Earley
#This class creates a binary string and implements &,|,~,^
#bit operations are supported between Binary class instances

class Binary:
    #declares and initiallizes the binary string as a list
    #the most significant bit is at index 0 of the list
    def __init__(self,x):
        self.stringInput = x
        self.binString =[int(i) for i in x]

    #used as a private helper function to this class
    #argument: b1 a binary string represented as a list
    #argument: b2 a binary string represented as a list
    #cond: a function to compare bits, returns boolean
    #returns the string result of the operation 
    def iterateComp(self,b1,b2,cond):
        temp = [None]*4
        for x in range(4):
            if cond(b1[x],b2[x]):
                temp[x] = 1
            else:
                temp[x] = 0
        return temp
    
    #argument bin2 represents another instance of the binary class
    #And will return the result of the and(&) bit operator applied to self
    #and bin2
    #returns Binary class instance
    def And(self,bin2):
        temp = [None]*4
        b1 = self.binString
        b2 = bin2.binString
        andfn = lambda x,y : ((x == y) and (x == 1))
        
        #compare and store anded values in temp
        temp = self.iterateComp(b1,b2,andfn)
                
        #create and return instance of bin class
        return Binary(temp)
    
    #argument bin2 represents another instance of the binary class
    #Or will return the result of the or(|) bit operator applied to self
    #and bin2
    #returns Binary class instance
    def Or(self,bin2):
        temp = [None]*4
        b1 = self.binString
        b2 = bin2.binString

       #compare and store or'ed values in temp
        temp = self.iterateComp(b1,b2,(lambda x,y : (x == 1) or (y==1)))
                
        #create and return instance of bin class
        return Binary(temp)

    #Not will create a Binary class instance with the result
    #of applying the not(~) operator to the binary string
    #returns Binary class instance
    def Not(self):
        temp = [None]*4
        for x in range(4):
            if(self.binString[x] == 1):
                temp[x] = 0
            else:
                temp[x] = 1

        return Binary(temp)
 
    #argument bin2 represents another instance of the binary class
    #Xor will return the result of the xor(^) bit operator applied to self
    #and bin2
    #returns Binary class instance
    def Xor(self,bin2):
        temp = [None]*4
        b1 = self.binString
        b2 = bin2.binString

        #compare and store xor'ed values in temp
        temp = self.iterateComp(b1,b2,
             (lambda x,y : ((x == 1) and (y==0)) or ((x == 0) and (y == 1))))
                
        #create and return instance of bin class
        return Binary(temp)

    

        
        
        
        
            
    

        
        
        
        
