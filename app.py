from flask import Flask, render_template # type: ignore

app = Flask(__name__)

# Dummy data
companies = [
    {
        'name': 'Tech Corp',
        'location': 'New York',
        'description': 'A tech company that builds web apps.',
        'employees_count': 150
    },
    {
        'name': 'Green Solutions',
        'location': 'San Francisco',
        'description': 'Environmental consultancy and services.',
        'employees_count': 80
    },
    {
        'name': 'EduSmart',
        'location': 'Chicago',
        'description': 'Online learning platform for schools.',
        'employees_count': 200
    },
    {
        'name': 'HealthPlus',
        'location': 'Boston',
        'description': 'Innovative health tech solutions and medical devices.',
        'employees_count': 120
    }
]

@app.route('/companies')
def show_companies():
    return render_template('companies.html', companies=companies)

if __name__ == '__main__':
    app.run(debug=True)
