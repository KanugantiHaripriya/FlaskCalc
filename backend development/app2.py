from flask import Flask,render_template,request

app2=Flask(__name__)

@app2.route('/',methods=['GET'])
def homepage():
    return 'you are in homepage'

@app2.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app2.route('/index',methods=['GET'])
def index2():
    return render_template('index.html')

#to receive the form data
@app2.route('/login-form',methods=['POST'])
def login_form_data():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return {'response':int(num1)+int(num2)}
#-----------------------------------------------------------------------------------------
@app2.route('/add',methods=['GET'])
def addition():
    return render_template('add.html')

@app2.route('/addition-form',methods=['POST'])
def addition_form():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    return [int(num1)+int(num2)]


@app2.route('/sub',methods=['GET'])
def substraction():
    return render_template('sub.html')

@app2.route('/substraction-form',methods=['POST'])
def substraction_form():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    return [int(num1)-int(num2)]



@app2.route('/mul',methods=['GET'])
def multiplication():
    return render_template('mul.html')
@app2.route('/multiplication-form',methods=['POST'])
def multiplication_form():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    return [int(num1)*int(num2)]


@app2.route('/div',methods=['GET'])
def division():
    return render_template('div.html')
@app2.route('/division-form',methods=['POST'])
def division_form():
    num1 = request.form['a_value']
    num2 = request.form['b_value']
    return [int(num1)//int(num2)]
app2.run()    

#---------------------------------------------------------------------------------------------