from turtle import pd
from mine import line1, line2, listProverit1, listProverit2, zatrat
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

# Func to draw line segment
def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0],p2[0]], [p1[1],p2[1]], color='skyblue')
    ax.add_line(l)
    return l

# Figure and Axes
fig, ax = plt.subplots(1,1,figsize=(35,5), facecolor='#f7f7f7', dpi= 80)

listColor1 = []
listColor2 = []

for i in listProverit1:
    if i == 0:
        listColor1.append('aqua')
    elif i == 1:
       listColor1.append('magenta')
    elif i == 2:
        listColor1.append('rebeccapurple')
    elif i == 3:
        listColor1.append('seagreen')
    elif i == 4:
        listColor1.append('coral')
    elif i == 5:
        listColor1.append('deeppink')
    elif i == 6:
        listColor1.append('teal')
    elif i == 7:
        listColor1.append('dodgerblue')
    elif i == 8:
        listColor1.append('lime')
    else:
        listColor1.append('crimson')

for i in listProverit2:
    if i == 0:
        listColor2.append('aqua')
    elif i == 1:
       listColor2.append('magenta')
    elif i == 2:
        listColor2.append('rebeccapurple')
    elif i == 3:
        listColor2.append('seagreen')
    elif i == 4:
        listColor2.append('coral')
    elif i == 5:
        listColor2.append('deeppink')
    elif i == 6:
        listColor2.append('teal')
    elif i == 7:
        listColor2.append('dodgerblue')
    elif i == 8:
        listColor2.append('lime')
    else:
        listColor2.append('crimson')


del line2[-1]
line2[-1] = 674
# Vertical Lines
for i, (colors, hours) in enumerate(zip(listColor1, line1)):
    if i == 0:
        ax.vlines(x=1, ymin=0, ymax=3, color='green', alpha=1, linewidth=1, linestyles='dotted')
        ax.hlines(y=1, xmin=1, xmax=line1[i] - 1, color=colors, alpha=1, linewidth=15)
        ax.vlines(x=line1[i] - 1, ymin=0, ymax=3, color='green', alpha=1, linewidth=1, linestyles='dotted')
    elif i < len(line1):
        ax.hlines(y=1, xmin=line1[i-1], xmax=line1[i] - 1, color=colors, alpha=1, linewidth=15)
        ax.vlines(x=line1[i] - 1, ymin=0, ymax=3, color='green', alpha=1, linewidth=1, linestyles='dotted')
    else:
        break


for i, (colors, hours) in enumerate(zip(listColor2, line2)):
    if i == 0:
        ax.vlines(x=2, ymin=0, ymax=3, color='grey', alpha=1, linewidth=1, linestyles='dotted')
        ax.hlines(y=2, xmin=1, xmax=line1[i] - 1, color=colors, alpha=1, linewidth=15)
        ax.vlines(x=line2[i] - 1, ymin=0, ymax=3, color='grey', alpha=1, linewidth=1, linestyles='dotted')
    elif i < len(line2):
        ax.hlines(y=2, xmin=line2[i-1], xmax=line2[i] - 1, color=colors, alpha=1, linewidth=15)
        ax.vlines(x=line2[i] - 1, ymin=0, ymax=3, color='grey', alpha=1, linewidth=1, linestyles='dotted')
    else:
        break


listLines = line1 + line2
listLines= sorted(listLines)
print(listLines)

# Decoration
ax.set_facecolor('#f7f7f7')
ax.set_title("Производственный график", fontdict={'size':22})
ax.set(xlim=(0, 720), ylim=(0, 3), ylabel='Производственные линии')
ax.set_xticks(listLines)

ax.legend(fontsize = 15,
          ncol = 2,    #  количество столбцов
          facecolor = 'mintcream',    #  цвет области
          edgecolor = 'r',    #  цвет крайней линии
          title = 'Общие затраты = 260780.835' ,    #  заголовок
          title_fontsize = '20'    #  размер шрифта заголовка
         )

plt.show()