from flask import Flask, render_template
from controllers.merchants_controller import merchants_blueprint
from controllers.transactions_controller import transactions_blueprint
from controllers.categories_controller import categories_blueprint

app = Flask(__name__)

app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)
app.register_blueprint(categories_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)
