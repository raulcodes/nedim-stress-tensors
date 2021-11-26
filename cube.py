import math
import matplotlib.pyplot as plt
import numpy as np

class UnitCube:
    def __init__(self, figure_size=(15, 15), title=""):
        fig = plt.figure(figsize=figure_size)
        self.points = np.array([[0., 0., 0.],
                          [ 1., 0., 0.],
                          [ 1.,  1., 0.],
                          [0.,  1., 0.],
                          [0., 0.,  1.],
                          [ 1., 0.,  1.],
                          [ 1.,  1.,  1.],
                          [0.,  1.,  1.]])
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(title)
        ax.set_ymargin(0.8)
        ax.set_xmargin(0.8)
        ax.set_zmargin(0.8)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_zticks([])
        ax.set_xlim3d(-2,2)
        ax.set_ylim3d(2,-2)
        ax.set_zlim3d(-2,2)
        ax.quiver(0, 0, 0, 1, 0, 0, length=4, arrow_length_ratio=.08, color="blue")
        ax.quiver(0, 0, 0, 0, 1, 0, length=4, arrow_length_ratio=.08, color="green")
        ax.quiver(0, 0, 0, 0, 0, 1, length=4, arrow_length_ratio=.08, color="red")
        self.ax = ax

    def drawInitialCube(self, color):
        self.drawCube(self.points, color)

    def drawTransformedCube(self, N_1, N_2, N_3, color):
        X = N_1
        Y = N_2
        Z = N_3
        A = np.add(N_1, N_2)
        B = np.add(N_1, N_3)
        C = np.add(np.add(N_1, N_2), N_3)
        D = np.add(N_2, N_3)

        self.drawCube(np.array([
                          [0., 0., 0.],
                          X,
                          B,
                          Z,
                          Y,
                          A,
                          C,
                          D]), color)

    def drawCube(self, points, color="blue"):
        self.ax.scatter3D(points[:, 0], points[:, 1], points[:, 2], color=color)
        for i in range(len(points[:4])):
            k = i + 1
            if (k == 4):
                k = 0
            p = points[i]
            n_p = points[k]
            self.ax.plot3D([p[0], n_p[0]], [p[1], n_p[1]], [p[2], n_p[2]], color=color)

        for i in range(len(points[4:])):
            i += 4
            k = i + 1
            if (k == 8):
                k = 4
            p = points[i]
            n_p = points[k]
            self.ax.plot3D([p[0], n_p[0]], [p[1], n_p[1]], [p[2], n_p[2]], color=color)

        for i in range(len(points[4:])):
            k = i + 4
            if (k == 4):
                k = 4
            p = points[i]
            n_p = points[k]
            self.ax.plot3D([p[0], n_p[0]], [p[1], n_p[1]], [p[2], n_p[2]], color=color)

    # # Rotate shape around the z-axis
    # def rotateZ3D(self, theta):
    #     sinTheta = math.sin(theta);
    #     cosTheta = math.cos(theta);

    #     c_points = np.copy(self.points)
    #     for n in range(len(c_points)):
    #         x = c_points[n][0];
    #         y = c_points[n][1];
    #         c_points[n][0] = x * cosTheta - y * sinTheta;
    #         c_points[n][1] = y * cosTheta + x * sinTheta;
    #     self.points = c_points

    # # Rotate shape around the x-axis
    # def rotateX3D(self, theta):
    #     sinTheta = math.sin(theta);
    #     cosTheta = math.cos(theta);

    #     c_points = np.copy(self.points)
    #     for n in range(len(c_points)):
    #         y = c_points[n][1];
    #         z = c_points[n][2];
    #         c_points[n][1] = y * cosTheta - z * sinTheta;
    #         c_points[n][2] = z * cosTheta + y * sinTheta;
    #     self.points = c_points

    # # Rotate shape around the y-axis
    # def rotateY3D(self, theta):
    #     sinTheta = math.sin(theta);
    #     cosTheta = math.cos(theta);

    #     c_points = np.copy(self.points)
    #     for n in range(len(c_points)):
    #         x = c_points[n][0];
    #         z = c_points[n][2];
    #         c_points[n][0] = x * cosTheta + z * sinTheta;
    #         c_points[n][2] = z * cosTheta - x * sinTheta;
    #     self.points = c_points