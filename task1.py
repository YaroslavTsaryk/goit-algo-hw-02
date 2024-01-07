import queue
import random

#Створити чергу заявок
payment_queue = queue.Queue()

goods=["Coffee","Cake","IceCream","Burger","HappyMeal","Cheese burger","French fries"]

def generate_request():
    print("Generate requests")
    for i in range(random.randint(2,10)):
        #Створити нову заявку
        payment={random.choice(goods):random.randrange(100)}    
        #Додати заявку до черги
        print(f"Add payment: {payment}")
        payment_queue.put(payment)
    
    

def process_request():
    print("Process requests")
#     Якщо черга не пуста:
    while not payment_queue.empty():
#         Видалити заявку з черги
        payment=payment_queue.get()
#         Обробити заявку
        print(f"payment processing: {payment}")
#     Інакше:
    else:
#         Вивести повідомлення, що черга пуста
        print(f"payment queue is empty")


# Головний цикл програми:
def main():
    ch="Y"
#     Поки користувач не вийде з програми:
    while ch.lower()!="n":
#         Виконати generate_request() для створення нових заявок
        generate_request()
#         Виконати process_request() для обробки заявок
        process_request()
        ch=input("Generate more? (Y/N)")
    


if __name__ == "__main__":
    main()