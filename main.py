import numpy as np
import matplotlib.pyplot as plt
import time, operator,csv
from matplotlib.animation import FuncAnimation, PillowWriter

def f1():
    t_start = time.perf_counter()
    sp1 = np.random.randint(1, 10**4, size=10**6)
    sp2 = np.random.randint(1, 10**4, size=10**6)
    sp_ans=list(map(operator.mul, sp1, sp2))
    all_time0 = time.perf_counter() - t_start

    t_start = time.perf_counter()
    ar1 = np.array(sp1)
    ar2 = np.array(sp2)
    ar_ans=np.multiply(ar1, ar2)
    all_time = time.perf_counter() - t_start
    print('Время перемножения обычных списков:',all_time0)  # Убедились, что NumPy быстрее
    print('Время перемножения массивов NumPy:',all_time)

def file():
    with open('data2.csv', 'r') as f:
        f = list(csv.reader(f, delimiter=','))
        column = np.array([])
        del f[0]
        for row in f:
            column = np.append(column, float(row[1]))
    return column

def f2():
    y = file()

    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(12, 6))
    fig.set(facecolor='floralwhite')
    fig.suptitle(f'Cреднеквадратичное отклонение: {np.std(y)}',fontsize = 20, color = 'green',fontstyle = 'italic')

    ax[0].hist(y, 16)
    ax[0].set(facecolor = 'white',
       title = 'Гистограмма',
       xlabel = 'индексы',
       ylabel = 'Значения')
    ax[0].grid()

    ax[1].hist(y, 16,density=True)
    ax[1].set(facecolor='white',
              title='Нормализованная гистограмма',
              xlabel='индексы',
              ylabel='Значения')
    ax[1].grid()

    plt.show()

# x∈(-5;5); y∈(-5;5); z=sin(x^y)
def f3():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    z = np.sin(np.sign(x) * (np.abs(x)**y))

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(projection='3d')
    ax.set(xlabel='Ox',ylabel='Oy',zlabel='Oz',title='График функции: x∈(-5;5); y∈(-5;5); z=sin(x^y)')
    ax.plot(x, y, z)

    plt.show()

def dop():
    fig, ax = plt.subplots()
    x, y = [], []
    ln, = ax.plot([], [])

    def init():
        ax.set_xlim(0, 10)
        ax.set_ylim(-1, 1)
        return ln,

    def update(frame):
        x.append(frame)
        y.append(np.sin(frame))
        ln.set_data(x, y)
        return ln,

    ani = FuncAnimation(fig, func=update, frames=np.linspace(0, 10),
                        init_func=init)
    writer = PillowWriter(fps=40)
    ani.save("dop.gif", writer=writer)

f1()
f3()
f2()
dop()
