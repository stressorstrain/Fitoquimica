import csv
from pylab import *
import os


def get_image(date, ars, h2, he):

    if he:
        plt.clf()
        plt.plot(date, he, marker='o', markerfacecolor="black", markersize=10, color='green', linewidth=8, label="Helio")
        plt.xlabel("Data de Verificacao")
        plt.ylabel("Kpa")
        plt.xticks(date, rotation='45')
        plt.yticks(np.arange(0, 180, step=10))
        leg = plt.legend(loc='upper left', frameon=False)
        plt.subplots_adjust(bottom=0.15)
        return plt
    else:
        plt.clf()
        print(ars)
        plt.plot(date, ars, marker='o', markerfacecolor="blue", markersize=10, color='skyblue', linewidth=8, label="Ar Sintetico")
        plt.plot(date, h2, marker='o', markerfacecolor="white", markersize=10, color='red', linewidth=8, label="Hidrogenio")
        plt.xlabel("Data de Verificacao")
        plt.ylabel("Kgf/c3")
        plt.xticks(date, rotation='45')
        plt.yticks(np.arange(0, 20000, step=1000))
        leg = plt.legend(loc='upper left', frameon=False)
        plt.subplots_adjust(bottom=0.15)
        return plt


def start(info):
    crom_dir = str(os.path.abspath(__file__).split('gas.py')[0])
    with open(crom_dir+"gas_data.txt", "a") as csvfile:
        csvfile.write("\n" + info)
        csvfile.close()

    with open(crom_dir+"gas_data.txt", "r") as csvfiler:
        plots = csv.reader(csvfiler, delimiter='\t')
        date = []
        ars = []
        h2 = []
        he = []
        path1 = crom_dir+'static/cromatografia/images/doubplot.png'
        path2 = crom_dir+'static/cromatografia/images/heplot.png'

        for row in plots:
            print(row)
            row[0] = re.sub('/2018', '', row[0])
            date.append(row[0])
            ars.append(int(row[1]))
            h2.append(int(row[2]))
            he.append(int(row[3]))
            #labels.append(row)
            #x.append(int(row[1]))
            #y.append(int(row[2]))
        if os.path.isfile(path1):
            os.remove(path1)  # Opt.: os.system("rm "+strFile)
        if os.path.isfile(path2):
            os.remove(path2)
        x = get_image(date, ars, h2, None)
        plt.savefig(path1)
        ars.clear(), h2.clear()

        y = get_image(date, None, None, he)
        savefig(path2)
        ars.clear(), h2.clear(), he.clear()
        plt.show()

        return True

