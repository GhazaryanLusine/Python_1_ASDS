from Productcheck import check

        
def buy(product,num,price):
        if check(product,num)==True:
             return(f"You bought {product} and spent {num*price}")
        else:
             return("Sorry! We are out of this product") 

def main():
    print(buy("pen",45,2))

if __name__=="__main__":
    main()



    