from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        sequence = request.form['sequence'].upper()
        scale = request.form['scale']
        summA = 0
        summT = 0
        summG = 0
        summC = 0
        summ = 0

        for letter in sequence:
            if letter == 'A':
                summA += 1
                summ += 1
            elif letter == 'T':
                summT += 1
                summ += 1
            elif letter == 'G':
                summG += 1
                summ += 1
            elif letter == 'C':
                summC += 1
                summ += 1

        if scale == '10мм':
            resA = round(summA * 100 / 19, 2)
            resT = round(summT * 100 / 26, 2)
            resG = round(summG * 100 / 20, 2)
            resC = round(summC * 100 / 22, 2)

            tetrazole = round(summ * 180 / 266, 2)
            tetrazole_percent = round(100 * tetrazole / 180, 2)

            anhydride = round(summ * 180 / 153, 2)
            anhydride_percent = round(100 * anhydride / 180, 2)

            nmi = round(summ * 180 / 165, 2)
            nmi_percent = round(100 * nmi / 180, 2)

            tca = round(summ * 450 / 106, 2)
            tca_percent = round(100 * tca / 450, 2)

            iodine = round(summ * 200 / 115, 2)
            iodine_percent = round(100 * iodine / 200, 2)

            acn = round(summ * 4000 / 130, 2)
            acn_percent = round(100 * acn / 4000, 2)

        elif scale == '1мм':
            resA = round(summA * 100 / 71, 2)
            resT = round(summT * 100 / 81, 2)
            resG = round(summG * 100 / 71, 2)
            resC = round(summC * 100 / 76, 2)
            tetrazole = round(summ * 180 / 417, 2)
            tetrazole_percent = round(100 * tetrazole / 180, 2)
            anhydride = round(summ * 180 / 621, 2)
            anhydride_percent = round(100 * anhydride / 180, 2)
            nmi = round(summ * 180 / 692, 2)
            nmi_percent = round(100 * nmi / 180, 2)
            tca = round(summ * 450 / 385, 2)
            tca_percent = round(100 * tca / 450, 2)
            iodine = round(summ * 200 / 488, 2)
            iodine_percent = round(100 * iodine / 200, 2)
            acn = round(summ * 4000 / 500, 2)
            acn_percent = round(100 * acn / 4000, 2)


        elif scale == '0.2мм':
            resA = round(summA * 100 / 107, 2)
            resT = round(summT * 100 / 124, 2)
            resG = round(summG * 100 / 107, 2)
            resC = round(summC * 100 / 104, 2)
            tetrazole = round(summ * 180 / 446, 2)
            tetrazole_percent = round(100 * tetrazole / 180, 2)
            anhydride = round(summ * 180 / 621, 2)
            anhydride_percent = round(100 * anhydride / 180, 2)
            nmi = round(summ * 180 / 692, 2)
            nmi_percent = round(100 * nmi / 180, 2)
            tca = round(summ * 450 / 385, 2)
            tca_percent = round(100 * tca / 450, 2)
            iodine = round(summ * 200 / 488, 2)
            iodine_percent = round(100 * iodine / 200, 2)
            acn = round(summ * 4000 / 500, 2)
            acn_percent = round(100 * acn / 4000, 2)


        elif scale == 'праймер':
            resA = round(summA * 100 / 71, 2)
            resT = round(summT * 100 / 81, 2)
            resG = round(summG * 100 / 71, 2)
            resC = round(summC * 100 / 76, 2)
            tetrazole = round(summ * 180 / 750, 2)
            tetrazole_percent = round(100 * tetrazole / 180, 2)
            anhydride = round(summ * 180 / 621, 2)
            anhydride_percent = round(100 * anhydride / 180, 2)
            nmi = round(summ * 180 / 692, 2)
            nmi_percent = round(100 * nmi / 180, 2)
            tca = round(summ * 450 / 385, 2)
            tca_percent = round(100 * tca / 450, 2)
            iodine = round(summ * 200 / 488, 2)
            iodine_percent = round(100 * iodine / 200, 2)
            acn = round(summ * 4000 / 570, 2)
            acn_percent = round(100 * acn / 4000, 2)

        else:
            result = {'error': 'Неправильна масштабність'}
            return render_template('index.html', result=result)


        result = {
            'A': resA, 'T': resT, 'G': resG, 'C': resC,
            'tetrazole': tetrazole, 'tetrazole_percent': tetrazole_percent,
            'anhydride': anhydride, 'anhydride_percent': anhydride_percent,
            'nmi': nmi, 'nmi_percent': nmi_percent,
            'tca': tca, 'tca_percent': tca_percent,
            'iodine': iodine, 'iodine_percent': iodine_percent,
            'acn': acn, 'acn_percent': acn_percent
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)