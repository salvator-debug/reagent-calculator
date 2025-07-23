from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    mode = request.args.get('mode', 'mode1')  # отримуємо режим з query параметра, за замовчуванням mode1
    results = []
    total = {'A': 0, 'T': 0, 'G': 0, 'C': 0,
             'tetrazole': 0, 'anhydride': 0, 'nmi': 0,
             'tca': 0, 'iodine': 0, 'acn': 0, 'summmolarweight': 0,
             'tetrazole_percent': 0, 'anhydride_percent': 0,
             'nmi_percent': 0, 'tca_percent': 0,
             'iodine_percent': 0, 'acn_percent': 0
             }

    if mode == 'mode1':
        if request.method == 'POST':
            scale = request.form.get('scale')

            for i in range(1, 5):
                if request.form.get(f'use_seq{i}') == 'on':
                    sequence = request.form.get(f'sequence{i}', '').upper()
                    summA = sequence.count('A')
                    summT = sequence.count('T')
                    summG = sequence.count('G')
                    summC = sequence.count('C')
                    summmolarweight = round(313.209 * summA + 304.196 * summT + 329.208 * summG + 289.184 * summC, 2)
                    summ = summA + summT + summG + summC

                    if summ == 0:
                        continue

                    # Тут твоя логіка розрахунку reagents залежно від scale
                    # Я спростив для прикладу (просто передам відсотки):
                    resA = round(summA * 100 / summ, 2)
                    resT = round(summT * 100 / summ, 2)
                    resG = round(summG * 100 / summ, 2)
                    resC = round(summC * 100 / summ, 2)

                    # Припустимо, що reagents – просто кратні суми:
                    tetrazole = summ * 10
                    anhydride = summ * 5
                    nmi = summ * 7
                    tca = summ * 9
                    iodine = summ * 4
                    acn = summ * 12

                    # Проценти — приблизні
                    tetrazole_percent = 100
                    anhydride_percent = 100
                    nmi_percent = 100
                    tca_percent = 100
                    iodine_percent = 100
                    acn_percent = 100

                    results.append({
                        'seq_num': i, 'sequence': sequence,
                        'A': resA, 'T': resT, 'G': resG, 'C': resC,
                        'tetrazole': tetrazole, 'tetrazole_percent': tetrazole_percent,
                        'anhydride': anhydride, 'anhydride_percent': anhydride_percent,
                        'nmi': nmi, 'nmi_percent': nmi_percent,
                        'tca': tca, 'tca_percent': tca_percent,
                        'iodine': iodine, 'iodine_percent': iodine_percent,
                        'acn': acn, 'acn_percent': acn_percent,
                        'summmolarweight': summmolarweight
                    })

            for r in results:
                total['A'] += r['A']
                total['T'] += r['T']
                total['G'] += r['G']
                total['C'] += r['C']
                total['tetrazole'] += r['tetrazole']
                total['tetrazole_percent'] += r['tetrazole_percent']
                total['anhydride'] += r['anhydride']
                total['anhydride_percent'] += r['anhydride_percent']
                total['nmi'] += r['nmi']
                total['nmi_percent'] += r['nmi_percent']
                total['tca'] += r['tca']
                total['tca_percent'] += r['tca_percent']
                total['iodine'] += r['iodine']
                total['iodine_percent'] += r['iodine_percent']
                total['acn'] += r['acn']
                total['acn_percent'] += r['acn_percent']
                total['summmolarweight'] += r['summmolarweight']

            for k in total:
                total[k] = round(total[k], 2)

        return render_template('index.html', results=results, total=total, mode=mode)

    elif mode == 'mode2':
        # Поки що пустий режим 2
        return render_template('mode2.html', mode=mode)


if __name__ == '__main__':
    app.run(debug=True)