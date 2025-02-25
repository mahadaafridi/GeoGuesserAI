from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Home Page')

@app.route('/test.html')
def test():
    return render_template('test.html', the_title='Test')

if __name__ == '__main__':
    app.run(debug=True) 
    
