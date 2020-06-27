import tornado
import matplotlib.pyplot as plt

a = [50, 40, 30]
b = [120, 130, 160]
c = 100

plt.figure()
tornado.plot(a, b, center=c)
tornado.set_labels(['Apples', 'Bananas', 'Oranges'])
plt.savefig('example.png')
plt.show()
