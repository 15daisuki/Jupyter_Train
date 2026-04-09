%matplotlib inline
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[1,4,2,8,10]
y2=[2,3,7,5,9]
plt.plot(x,y1,
         label='Line 1',
         color='blue',
         linestyle='-',
         marker='o',
         linewidth=2)
plt.plot(x,y2,
         label='Line 2',
         color='red',
         linestyle='--',
         marker='s',
         linewidth=2)
plt.title('Sample Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.legend()
plt.show()