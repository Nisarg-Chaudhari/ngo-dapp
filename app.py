from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/donation', methods=['GET','POST'])
def donation():
    if request.method == 'POST':
        form = request.form
        donation_amount = form['donation-amount']
        print(f"Donation of {donation_amount} was succesfull")
        return redirect('/')
    return render_template('donation.html')

@app.route('/ngo', methods=['GET','POST'])
def ngo():
    if request.method == 'POST':
        form = request.form
        ngo_addr = form['ngo-addr']
        print(f"Your address {ngo_addr} is added.")
        return redirect('/')
    return render_template('ngo.html')


if __name__ == '__main__':
    app.run(debug=True)