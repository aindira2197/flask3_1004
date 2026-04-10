from flask import Flask, render_template

app = Flask(__name__)

fanlar = ["Matematika", "Fizika", "Kimyo", "Biologiya", "Tarix", "Informatika", "Geografiya"]

uzun_fan = []

for fan in fanlar:
    if len(fan) > 7:
        uzun_fan.append(fan)



@app.route('/fanlar')
def fanlar_royxati():
    return render_template('fanlar.html', uzun_fan=uzun_fan)
    



if __name__ == "__main__":
    app.run(debug=True)
