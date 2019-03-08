"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
"""



import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pylab
from figure import Figure
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox

def addButtonClicked(event):
        spir.spin(radiobuttons_color.value_selected)
        ax.clear()
        ax.plot(spir.x, spir.y, spir.z)
        pylab.draw()
        print("spiiiin!")


def textSubmited(text):
        spir.deg = int(text)


def main():
        mpl.rcParams['legend.fontsize'] = 10
        global fig, ax
        fig, ax = pylab.subplots()
        ax = fig.gca(projection='3d')
        theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
        z = np.linspace(-2, 2, 100)
        r = z**2 + 1
        x = r * np.sin(theta)
        y = r * np.cos(theta)
        global spir
        spir = Figure(x, y, z)

                # Оставим снизу от графика место для виджетов
        fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

        # !!! Создадим ось для кнопки
        axes_button_add = pylab.axes([0.7, 0.05, 0.25, 0.075])

        # !!! Создадим кнопку
        button_add = Button(axes_button_add, 'Вращать!')
        button_add.on_clicked(addButtonClicked)

                # !!! Создание осей для переключателей
        axes_radiobuttons = pylab.axes([0.05, 0.05, 0.2, 0.2])

        # !!! Создание переключателя
        global radiobuttons_color
        radiobuttons_color = RadioButtons(axes_radiobuttons,
                                        ['X', 'Y', 'Z'])


        axbox = pylab.axes([0.85, 0.15, 0.1, 0.1])
        text_box = TextBox(axbox, 'Введите угол в градусах')
        text_box.on_submit(textSubmited)




        ax.plot(x, y, z, label='parametric curve')
        ax.legend()

        pylab.show()



if __name__ == "__main__":
        main()


