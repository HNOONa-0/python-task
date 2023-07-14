import matplotlib.pyplot as plt
from my_utils import math_expr

def plot_graph_old(x_pts,y_pts,s):
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Plotting function: "+math_expr(s) )
    plt.plot(x_pts,y_pts)
    plt.show()
def plot_graph_new(x_pts,y_pts,s):
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Plotting function: "+math_expr(s) )
    # plote each subarray in x_pts to its corrosponding y_pts
    for i in range(len(x_pts) ):
        x_arr,y_arr=x_pts[i],y_pts[i]
        plt.plot(x_arr,y_arr,color='blue')
    plt.show()
