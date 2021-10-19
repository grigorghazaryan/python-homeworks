# 10. Write a program that takes a list of ten prices and ten products, 
# applies an 11% discount to each of the prices displays the output like below.

fruits = [ "Apple 🍏", "Orange 🍊", "Pear 🍐" ] 
prices = [ 3, 4, 5 ] 

for fruit, price in zip(fruits, prices):
    print(f"{fruit} $ {price - (price * 11 / 100)}")