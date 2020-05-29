from generate import main
from flask import Flask, send_file, url_for, render_template, redirect
from form import makeCrossword
from uuid import uuid1
from random import shuffle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = makeCrossword()
    if form.validate_on_submit():
        pic_id = uuid1().hex
        words = form.words.data.upper().split()
        shuffle(words)
        structure = f'structure{form.structure.data}'
        if main(f'data/{structure}.txt', words, f'static/{pic_id}.png'):
            return render_template('crossword.html', id=pic_id)
        else:
            return render_template('crossword.html', message="No Solution, try using one of the sample words list!")
    return render_template('main.html', form=form)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
