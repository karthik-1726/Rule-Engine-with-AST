from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import rules

# Initialize the Flask application
app = Flask(__name__, static_folder="templates/static")

# MySQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/rules_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning

# Initialize the database
db = SQLAlchemy(app)

# Create a Rule model
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

def create_database():
    """Create the database if it doesn't exist."""
    connection = mysql.connector.connect(user='root', password='', host='localhost')
    cursor = connection.cursor()
    
    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS rules_database")
    connection.commit()
    
    # Close the connection
    cursor.close()
    connection.close()

@app.route('/')
def index():
    return render_template('html/index.html') 

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json.get('rule_string')
    if not rule_string:  # Check if rule_string is empty or None
        return jsonify({"error": "Rule string is required"}), 400
    ast = rules.create_rule(rule_string)

    # Convert the AST Node to a dictionary for JSON serialization
    return jsonify(ast.to_dict()), 200  # Ensure we call to_dict() here


@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rules = request.json.get('rules')
    if not rules or not all(rules):  # Check if rules is empty or contains empty values
        return jsonify({"error": "At least one rule is required"}), 400
    combined_ast = rules.combine_rules(rules)
    return jsonify(combined_ast), 200

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    data = request.json.get('data')
    ast = request.json.get('ast')
    if not data or not ast:  # Check if data or ast is missing
        return jsonify({"error": "Both data and AST are required"}), 400
    result = rules.evaluate_rule(ast, data)
    return jsonify(result), 200


if __name__ == '__main__':
    create_database()  # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
