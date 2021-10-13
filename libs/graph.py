import matplotlib.pyplot as plt
import numpy as np

def graph2d(function):
    x = np.linspace(-5,5,100)

    try:
        y = eval(function)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.plot(x,y, 'r')

        plt.show()


    except:

        y = eval("np."+function)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.plot(x,y, 'r')

        plt.show()


def graph3d(function):

    try:
        def f(x, y):
            return eval(function)

        x = np.linspace(-6, 6, 30)
        y = np.linspace(-6, 6, 30)

        X, Y = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

    except:
        def f(x, y):
            return eval("np."+function)

            x = np.linspace(-6, 6, 30)
            y = np.linspace(-6, 6, 30)

            X, Y = np.meshgrid(x, y)
            Z = f(X, Y)

            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='viridis', edgecolor='none')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            plt.show()


