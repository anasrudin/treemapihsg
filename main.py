import matplotlib.pyplot as plt
import squarify 

size_list = [13,22,35,5]
label_list = ["group A", "group B", "group C", "group D"]
color_list = ["red","green","blue", "grey"]

def draw_plot(sizes, labels, colors):
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.5 )
    plt.axis('off')
    plt.show()


draw_plot(size_list, label_list, color_list)

# print("hello world")