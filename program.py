from my_utils import *
from graph_plotter import *
def main():
    # get min,max x
    x1,x2=get_2x()
    # get function
    s=get_funcx()
    # prep points for ploting graph
    x_pts,y_pts=get_pts_new(x1,x2,s)

    # print(x_pts)
    # print(y_pts)

    plot_graph_new(x_pts,y_pts,s)
    # print(is_funcx("x**a"))
    
if __name__ == "__main__":
    # Code for your main section here
    main()