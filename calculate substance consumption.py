

sequence = input('введіть послідовність: ')


while True:
    umova = input('ввведіть масштабність(праймер,[40нм],0.2мм,1мм,10мм):')
    if umova == '10мм':
        summA = 0
        summT = 0
        summG = 0
        summC = 0
        summ = 0
        for letter in sequence:
                summ= summ +1
                if letter == 'A':
                    summA = summA + 1
                elif letter == 'T':
                    summT = summT + 1
                elif letter == 'G':
                    summG = summG + 1
                elif letter == 'C':
                    summC = summC + 1
                else:
                    print('немає такої букви')
        # print('A:',summA)AGAAATCTCGATTCCACAAAATGGATCCAGA
        # print('T:',summT)
        # print('G:',summG)
        # print('C:',summC)
        print(summ)
        print('витрачено А:',round(summA * 100 / 19, 2), '%')
        print('витрачено T:',round(summT * 100 / 26, 2), '%')
        print('витрачено G:',round(summG * 100 / 20, 2), '%')
        print('витрачено C:',round(summC * 100 / 22, 2), '%')
        print('витрачено тетразолу[180мл]:',round(summ * 180/266, 2),'мл або',round(100*round(summ*180/266,2)/180, 2),'%')
        print('витрачено кислотного ангідриту[180мл]:',round(summ * 180 / 153, 2),'мл або',round( 100* round(summ * 180/153, 2)/180,2),'%')
        print('витрачено NMI[180мл]:', round(summ * 180 / 165, 2), 'мл або',round( 100* round(summ * 180/165, 2)/180,2),'%')
        print('витрачено TCA[450мл]:', round(summ * 450 / 106, 2), 'мл або',round( 100* round(summ * 450/106, 2)/450,2),'%')
        print('витрачено iodine[200мл]:', round(summ * 200 / 115, 2),   'мл або', round( 100* round(summ * 200/115, 2)/200,2),'%')
        print('витрачено ацетонітрилу[4л]:', round(summ * 4000 / 130, 2),'мл або',round( 100* round(summ * 4000/130, 2)/4000,2),'%')
        break

    elif umova == '1мм':
            summA = 0
            summT = 0
            summG = 0
            summC = 0
            summ = 0

            for letter in sequence:
                    summ = summ + 1
                    if letter == 'A':
                        summA = summA + 1
                    elif letter == 'T':
                        summT = summT + 1
                    elif letter == 'G':
                        summG = summG + 1
                    elif letter == 'C':
                        summC = summC + 1
                    else:
                        print('немає такої букви')
            # print('A:',summA)
            # print('T:',summT)
            # print('G:',summG)
            # print('C:',summC)
            print('витрачено А:',round(summA * 100 / 71, 2), '%')
            print('витрачено T:',round(summT * 100 / 81, 2), '%')
            print('витрачено G:',round(summG * 100 / 71, 2), '%')
            print('витрачено C:',round(summC * 100 / 76, 2), '%')
            print('витрачено тетразолу[180мл]:', round(summ * 180 / 417, 2), 'мл або',
                  round(100 * round(summ * 180 / 417, 2) / 180, 2), '%')
            print('витрачено кислотного ангідриту[180мл]:', round(summ * 180 / 621, 2), 'мл або',
                  round(100 * round(summ * 180 / 621, 2) / 180, 2), '%')
            print('витрачено NMI[180мл]:', round(summ * 180 / 692, 2), 'мл або',
                  round(100 * round(summ * 180 / 692, 2) / 180, 2), '%')
            print('витрачено TCA[450мл]:', round(summ * 450 / 385, 2), 'мл або',
                  round(100 * round(summ * 450 / 385, 2) / 450, 2), '%')
            print('витрачено iodine[200мл]:', round(summ * 200 / 488, 2), 'мл або',
                  round(100 * round(summ * 200 / 488, 2) / 200, 2), '%')
            print('витрачено ацетонітрилу[4л]:', round(summ * 4000 / 500, 2), 'мл або',
                  round(100 * round(summ * 4000 / 500, 2) / 4000, 2), '%')
            break


    elif umova == '0.2мм':
        summA = 0
        summT = 0
        summG = 0
        summC = 0
        summ = 0
        for letter in sequence:
                summ=summ+1
                if letter == 'A':
                    summA = summA + 1
                elif letter == 'T':
                    summT = summT + 1
                elif letter == 'G':
                    summG = summG + 1
                elif letter == 'C':
                    summC = summC + 1
                else:
                    print('немає такої букви')
        # print('A:',summA)
        # print('T:',summT)
        # print('G:',summG)
        # print('C:',summC)
        print('витрачено А:',round(summA * 100 / 107, 2), '%')
        print('витрачено T:',round(summT * 100 / 124, 2), '%')
        print('витрачено G:',round(summG * 100 / 107, 2), '%')
        print('витрачено C:',round(summC * 100 / 104, 2), '%')
        print('витрачено тетразолу[180мл]:', round(summ * 180 / 446, 2), 'мл або',
              round(100 * round(summ * 180 / 446, 2) / 180, 2), '%')
        print('витрачено кислотного ангідриту[180мл]:', round(summ * 180 / 621, 2), 'мл або',
              round(100 * round(summ * 180 / 621, 2) / 180, 2), '%')
        print('витрачено NMI[180мл]:', round(summ * 180 / 692, 2), 'мл або',
              round(100 * round(summ * 180 / 692, 2) / 180, 2), '%')
        print('витрачено TCA[450мл]:', round(summ * 450 / 385, 2), 'мл або',
              round(100 * round(summ * 450 / 385, 2) / 450, 2), '%')
        print('витрачено iodine[200мл]:', round(summ * 200 / 488, 2), 'мл або',
              round(100 * round(summ * 200 / 488, 2) / 200, 2), '%')
        print('витрачено ацетонітрилу[4л]:', round(summ * 4000 / 500, 2), 'мл або',
              round(100 * round(summ * 4000 / 500, 2) / 4000, 2), '%')
        break
    elif umova == 'праймер':
        summA = 0
        summT = 0
        summG = 0
        summC = 0
        summ = 0

        for letter in sequence:
            summ = summ + 1
            if letter == 'A':
                summA = summA + 1
            elif letter == 'T':
                summT = summT + 1
            elif letter == 'G':
                summG = summG + 1
            elif letter == 'C':
                summC = summC + 1
            else:
                print('немає такої букви')
        # print('A:',summA)
        # print('T:',summT)
        # print('G:',summG)
        # print('C:',summC)
        print('витрачено А:', round(summA * 100 / 71, 2), '<%')
        print('витрачено T:', round(summT * 100 / 81, 2), '<%')
        print('витрачено G:', round(summG * 100 / 71, 2), '<%')
        print('витрачено C:', round(summC * 100 / 76, 2), '<%')
        print('витрачено тетразолу[180мл]:', round(summ * 180 / 750, 2), 'мл або',
              round(100 * round(summ * 180 / 750, 2) / 180, 2), '%')
        print('витрачено кислотного ангідриту[180мл]:', round(summ * 180 / 621, 2), 'мл або',
              round(100 * round(summ * 180 / 621, 2) / 180, 2), '%')
        print('витрачено NMI[180мл]:', round(summ * 180 / 692, 2), 'мл або',
              round(100 * round(summ * 180 / 692, 2) / 180, 2), '%')
        print('витрачено TCA[450мл]:', round(summ * 450 / 385, 2), 'мл або',
              round(100 * round(summ * 450 / 385, 2) / 450, 2), '%')
        print('витрачено iodine[200мл]:', round(summ * 200 / 488, 2), 'мл або',
              round(100 * round(summ * 200 / 488, 2) / 200, 2), '%')
        print('витрачено ацетонітрилу[4л]:', round(summ * 4000 / 570, 2), 'мл або',
              round(100 * round(summ * 4000 / 570, 2) / 4000, 2), '%')
        break
else:
    print('введіть правильну розмірність')

