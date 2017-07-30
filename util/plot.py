import matplotlib.pyplot as plt
import numpy as np


def aplot():
    """
    plot axis
    :return:
    """
    X = np.linspace(-np.pi, np.pi)
    S = np.sin(X)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', 0, r'$\pi/2$', r'$\pi$'])
    plt.yticks([-1, 0, 1],
               [r'$-1$', r'$0$', r'$1$'])

    plt.plot(X, S, label='sin')
    plt.legend(loc='upper left', frameon=False)

    t = np.pi/2
    plt.plot([t, t], [0, np.sin(t)])
    plt.scatter([t, ], [np.sin(t), ], 50)
    plt.annotate(r'$sin(\frac{\pi}{2})=1$',
                 xy=(t, np.sin(t/2)),
                 xytext=(-20, +50),
                 textcoords='offset points',
                 )

    plt.show()


def asubplot():
    x = np.linspace(-np.pi, np.pi)
    y = np.sin(x)

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey='all')
    ax1.plot(x, y)
    ax2.scatter(x, y)

    fig2, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
    axes[1, 0].plot(x, y)
    axes[1, 1].scatter(x, y)

    plt.show()

if __name__ == '__main__':
    # aplot()
    asubplot()
