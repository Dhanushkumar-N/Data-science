from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Load the dataset from the CSV file
dataset = []

with open('Flipkart_Mobiles.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        dataset.append(row)

# Define a function to filter the dataset based on conditions
def filter_dataset(memory, storage, rating):
    filtered_data = []

    for item in dataset:
        if (memory == 'All' or item['Memory'] == memory) \
           and (storage == 'All' or item['Storage'] == storage) \
           and (rating == 'All' or float(item['Rating']) >= float(rating)):
            filtered_data.append(item)

    return filtered_data

@app.route('/', methods=['GET', 'POST'])
def index():
    memory = request.form.get('memory', 'All')
    storage = request.form.get('storage', 'All')
    rating = request.form.get('rating', 'All')

    filtered_data = filter_dataset(memory, storage, rating)

    return render_template('index.html', data=filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
