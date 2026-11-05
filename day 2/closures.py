def discount_calculator(discount, price):


    def calculate_discount(price):
        discounted_price = price - (price * discount / 100)
        
        return{
            'original_price': price,
            'discounted_price': discounted_price
        }
        

    return calculate_discount

student_discount = discount_calculator(10,100)
print(student_discount(100))
festival_discount = discount_calculator(20, 200)
print(festival_discount(200))
premium_discount = discount_calculator(30, 300)
print(premium_discount(300))