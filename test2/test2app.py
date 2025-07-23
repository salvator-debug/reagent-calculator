from flask import Flask, render_template, request

app = Flask(__name__, template_folder='test2templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    mode = request.form.get('mode', 'mode1')  # За замовчуванням — режим 1
    results = []
    total = {'A':0,'T':0,'G':0,'C':0,
            'tetrazole': 0, 'anhydride': 0, 'nmi': 0,
            'tca': 0, 'iodine': 0, 'acn': 0, 'summmolarweight':0,
            'tetrazole_percent':0,'anhydride_percent':0,
            'nmi_percent':0,'tca_percent':0,
            'iodine_percent':0,'acn_percent':0
             }

    if request.method == 'POST' and mode == 'mode1':
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
                    resA = round(summA * 100 / 214, 2)
                    resT = round(summT * 100 / 248, 2)
                    resG = round(summG * 100 / 214, 2)
                    resC = round(summC * 100 / 208, 2)
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
                    continue

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

    return render_template('testindex.html', mode=mode, results=results, total=total)


if __name__ == '__main__':
    app.run(debug=True)