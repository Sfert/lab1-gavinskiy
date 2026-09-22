import numpy as np  
import matplotlib.pyplot as plt 

def f(x):

    return x**2 + 2*x + 1

x = np.linspace(-5, 5, 100) 
y = f(x)

plt.figure(figsize=(8, 6))

plt.plot(
    x, 
    y, 
    label='f(x) = x² + 2x + 1',
    color='blue', 
    linewidth=2 
)


plt.title('Графік квадратичної функції f(x) = x² + 2x + 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()

min_x = -1
min_y = f(min_x)
plt.scatter(min_x, min_y, color='red', s=50, zorder=5)
plt.axvline(x=min_x, color='red', linestyle='--', alpha=0.5)
plt.axhline(y=min_y, color='red', linestyle='--', alpha=0.5)


plt.xlim(-5, 5)
plt.ylim(0, 36)

plt.tight_layout()
plt.show()

print(f"Мінімум функції знаходиться в точці: ({min_x}, {min_y})")
print(f"Значення функції в точці x = 0: {f(0)}")
print(f"Значення функції в точці x = 2: {f(2)}")
