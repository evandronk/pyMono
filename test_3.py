import csv
import mono_pso as pso
import numpy as np
import mono_iso as isotherms
import matplotlib.pyplot as plt
import openpyxl

error = 30
temperaturas = []
temperaturas.append('298K CP350')
temperaturas.append('298K MBM750')
temperaturas.append('298K SP550')

relative = False
modelo = 'multisite'
nome = modelo
if relative:
    nome = nome + '_relative'

#param_min_max = [[1, 100], [1, 100]]#Langmuir
param_min_max = [[1, 5], [1, 100], [1, 2]]#Sips & Multisite & Toth & GAB
#param_min_max = [[5, 10000], [1, 10000]]#BET



for temperatura in temperaturas:
    if modelo == 'langmuir':
        objF = isotherms.langmuir
        qF = isotherms.__langmuir_q__
    elif modelo == 'sips':
        objF = isotherms.sips
        qF = isotherms.__sips_q__
    elif modelo == 'bet':
        objF = isotherms.bet
        qF = isotherms.__bet_q__
    elif modelo == 'multisite':
        objF = isotherms.multisite_langmuir
        qF = isotherms.__langmuir_multi_q__
    elif modelo == 'gab':
        objF = isotherms.gab
        qF = isotherms.__gab_q__
    elif modelo == 'toth':
        objF = isotherms.toth
        qF = isotherms.__toth_q__

    file_path = str(temperatura) + '.csv'

    column1_data = []
    column2_data = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for column in csv_reader:
            try:
                if column[0].split(",")[0] == 'pressure':
                    column1_data.append(float(column[1].split(",")[0]))
                if column[0].split(",")[0] == 'adsorption':
                    column2_data.append(float(column[1].split(",")[0]))
            except:
                pass

    print(column1_data)
    print(column2_data)
    maximo = 1+np.max(column2_data)


    initial_error = 10
    print("Limit error: " + str(error))


    def restriction(lista):
        if objF == isotherms.langmuir:
            return lista[0][0] > 0 and lista[0][1] > 0
        if objF == isotherms.bet:
            return lista[0][0] > 0 and lista[0][1] > 0
        if objF == isotherms.sips:
            return lista[0][0] > 0 and lista[0][1] > 0 and lista[0][2] > 0
        if objF == isotherms.toth:
            return lista[0][0] > 0 and lista[0][1] > 0 and lista[0][2] > 0
        if objF == isotherms.gab:
            return lista[0][0] > 0 and lista[0][1] > 0 and lista[0][2] > 0
        if objF == isotherms.multisite_langmuir:
            return lista[0][0] > 0 and lista[0][1] > 0 and lista[0][2] > 0


    result = [[-1, -2], [-1, -2], [-1, -2], [-1, -2], ]

    while initial_error > error or not restriction(result):

        result = pso.pso(column1_data, column2_data, objF, 200, 200,
                         param_min_max=[param_min_max], comp_n=1, relative=relative)
        q_sim = []
        print(result)

        for pressure in column1_data:
            q_sim.append(qF(pressure, result[0]))

        plt.scatter(column1_data, column2_data)
        plt.scatter(column1_data, q_sim)
        plt.show()

        if result[1] < error and restriction(result):


            wb = openpyxl.Workbook()
            ws = wb.active
            error_abs_column = []
            relative_error_column = []
            quadratic_error_column = []
            for i in range(0, len(column2_data)):
                error_abs_column.append(abs(column2_data[i]-q_sim[i]))
                relative_error_column.append(abs(column2_data[i]-q_sim[i])/column2_data[i])
                quadratic_error_column.append(abs(column2_data[i]-q_sim[i])**2)


            error_abs_mean = np.mean(error_abs_column)
            relative_error_mean = np.mean(relative_error_column)
            quadratic_error_mean = np.mean(quadratic_error_column)
            std_error_abs = np.std(error_abs_column)
            std_relative_error = np.std(relative_error_column)
            std_quadratic_error = np.std(quadratic_error_column)
            #Médias
            error_abs_column.append('Média')
            error_abs_column.append(error_abs_mean)
            relative_error_column.append('Média')
            relative_error_column.append(relative_error_mean)
            quadratic_error_column.append('Média')
            quadratic_error_column.append(quadratic_error_mean)

            #Desvios
            error_abs_column.append('Desvio')
            error_abs_column.append(std_error_abs)
            relative_error_column.append('Desvio')
            relative_error_column.append(std_relative_error)
            quadratic_error_column.append('Desvio')
            quadratic_error_column.append(std_quadratic_error)

            #Nomes das colunas
            column1_data.insert(0, "Pressure")
            column2_data.insert(0, "q_exp")
            q_sim.insert(0, "q_sim")
            error_abs_column.insert(0, 'Abs Error')
            relative_error_column.insert(0, 'Relative Error %')
            quadratic_error_column.insert(0, 'Quadratic Error')

            #Parâmetros
            column1_data.append('-')
            column1_data.append('-')
            column1_data.append('-')
            column1_data.append('Parâmetros')
            for resultado in result[0]:
                column1_data.append(resultado)

            lst = [column1_data, column2_data, q_sim, error_abs_column, relative_error_column, quadratic_error_column]
            for r, row in enumerate(lst, start=1):
                for c, value in enumerate(row, start=1):
                    ws.cell(row=c, column=r).value = value
            wb.save("resultado " + nome + temperatura + ' ' + str(round(result[1], 2)) + ".xlsx")
        initial_error = result[1]
