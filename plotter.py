import matplotlib.pyplot as plt
import numpy as np

#labels=np.array([2,5,10,20,30,40,50,60,70,80,90,100])
accuracy=np.array([0.7935,0.7955,0.804,0.8075,0.812,0.82,0.8195,0.807,0.8105,0.817,0.8215,0.836])
precision=np.array([0.784,0.788,0.81,0.816,0.820,0.8219,0.817,0.8057,0.8114,0.8208,0.8277,0.8394])
recall=np.array([0.811,0.808,0.794,0.793,0.799,0.817,0.823,0.809,0.809,0.811,0.812,0.831])
labels=np.array([2,5,10,20,30,40,50,60,70,80,90,100])
plt.subplot(121)
plt.plot(labels,accuracy,'r',label='accuracy')
plt.plot(labels,precision,'g:',label='precision')
plt.plot(labels,recall,'b:',label='recall')
plt.xlabel('Precentage of labeled data in %')
plt.title('TSVM binary ')
plt.legend(loc='top left')
#plt.margins(y=0.9)
accuracy=np.array([0.8926,0.8882,0.8844,0.8844,0.8874,0.8888,0.8928,0.8944,0.894,0.8968,0.8967,0.8987])
precision=np.array([0.305,0.286,0.340,0.356,0.3875,0.386,0.417,0.431,0.425,0.459,0.454,0.481])
recall=np.array([0.058,0.079,0.167,0.194,0.217,0.19,0.182,0.175,0.171,0.178,0.165,0.168])

plt.subplot(122)
plt.plot(labels,accuracy,'r',label='accuracy')
plt.plot(labels,precision,'g:',label='precision')
plt.plot(labels,recall,'b:',label='recall')
plt.xlabel('Precentage of labeled data in %')
plt.title('TSVM one-vs-rest')
plt.legend(loc='top left')
#plt.margins(y=0.75)

x0, x1, y0, y1 = plt.axis()
print(plt.axis())
fig_size=plt.rcParams["figure.figsize"]
fig_size[0] = 1
fig_size[1] = 4
plt.rcParams["figure.figsize"] = fig_size
plt.show()

print(plt.rcParams["figure.figsize"])