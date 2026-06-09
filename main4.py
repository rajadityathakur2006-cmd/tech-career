from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am narendarmodi bot!"

if __name__ == "__main__":
    app.run(debug=True)



import math


bot_name='narendarmodi'
print(f'hello i am {bot_name}:how may i assist you sir?')
while True:
    user_input: str = input('you: ').lower()

    if user_input in ['hello','hey', 'hi']:
          print(f'{bot_name}:hey their,how may i assist you today')    
    if user_input =='hello':
         print(f'{bot_name}:hey there,how are you sir')
    elif user_input == 'how are you':
            print(f'{bot_name}:i am doing good,what about you sir')
    elif user_input in ['bye','goodbye','have a great day']:
                print(f'{bot_name}:goodbye,have a great day sir')
    elif user_input in ['+', 'add', 'sum', 'addition', 'square', 'multiplication', 'division', 'subtraction', 'division', 'square root']:
           print(f"{bot_name}:what numbers you want to {user_input}?")
           try:
            num1 = float(input('first number: '))
            num2 = float(input('second number: '))
            print(f'{bot_name}: the sum of {num1} and {num2} is {num1 + num2}')
           except ValueError:
            print(f'{bot_name}:please enter valid numbers')
           if user_input in ['+','add','sum','addition']:
            try:
                num1: float = float(input('first number: '))
                num2: float= float(input('second number: '))
                print(f'{bot_name}:{num1 + num2}')
                print (f'the sum of two number {num1} and {num2} is sum of {num1 + num2}')
            except ValueError:
                print(f'{bot_name}:please enter valid numbers')
            else:
             print(f'{bot_name}:sorry,i did not understand that,plesae try again...') 
             if user_input in ['-', 'subtract', 'subtraction']:
              print(f'{bot_name}:{num1 - num2}')
    elif user_input in ['*', 'multiply', 'multiplication']:
            print(f'{bot_name}:{num1 * num2}')
    elif user_input in ['/', 'divide', 'division']:
            if num2 != 0:
                print(f'{bot_name}:{num1 / num2}')
            else:
                print(f'{bot_name}:please enter a non-zero second number')
    elif user_input in ['square']:
            print(f'{bot_name}:{num1 ** 2}')
    elif user_input in ['square root']:
            print(f'{bot_name}:{math.sqrt(num1)}')
    else:
          print(f'{bot_name}:i didnt get,what you want to say')
