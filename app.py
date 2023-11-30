from flask import Flask, request, render_template
from database import Person, getResults

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def read_form():
    data = request.form.get
    vote = Person(data('name'), data('car'))
    vote.save()

    results = getResults()
    print(results)

    return render_template('result.html',
                           fronxVotes=results['Fronx'],
                           gvVotes=results['GrandVitara'],
                           ertigaVotes=results['Ertiga'],
                           totalVotes=results['Total'])


app.run()
