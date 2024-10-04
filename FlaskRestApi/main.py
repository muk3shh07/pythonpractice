from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrng(n):
        
   order = len(str(n))
   sum = 0
   num = n

   while(n!=0):
    digit = n % 10
    sum = sum + digit ** order
    n = n // 10

   if(sum == num):
    print(f"{num} is Armstrong number")
    result={
           "Number" : num,
           "Armstrong" : True,
           "Server IP" : "122.234.213.53"

           
        }
     

   else:
    print(f"{num} is not a armstrong number")
   result={
           "Number" : num,
           "Armstrong" : True,
           "Server IP" : "122.234.213.53"

           
        }
   
   return jsonify(result)


if __name__== "__main__":
    app.run(debug=True)

