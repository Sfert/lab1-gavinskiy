import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, start=-10, end=10, num_points=500):
    
    x = np.linspace(start, end, num_points)
    y = func(x)

    plt.figure(figsize=(8, 6))
    
    plt.plot(x, y, linewidth=2, color='blue')

    plt.title("Графік функції", fontsize=14, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y = f(x)", fontsize=12)
    
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.axhline(0, color='black', linewidth=0.5, label='Вісь X')
    plt.axvline(0, color='black', linewidth=0.5, label='Вісь Y')
    plt.legend()
    plt.tight_layout()
    plt.show()
