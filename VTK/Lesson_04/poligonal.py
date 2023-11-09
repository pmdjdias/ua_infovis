###############################################################################
#       						Poligonal.py
###############################################################################

from vtkmodules.all import *

import vtk

def main():

    coords = [[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]]
    cells = [[0,1,2,3], [4,5,6,7], [0,1,5,4], [1,2,6,5], [2,3,7,6], [3,0,4,7]]
    print("ole1")
    cube = vtk.vtkPolyData()
    points = vtk.vtkPoints()
    polys = vtk.vtkCellArray()
    scalars= vtk.vtkFloatArray()
    print("ole2")

    print(len(coords))
    for i in range(len(coords)):
        points.InsertPoint(i,coords[i])
        print(coords[i])
    for i in range(len(cells)):
        polys.InsertNextCell(4,cells[i])
        print(cells[i])
    cube.SetPoints(points)
    cube.SetPolys(polys)
    

	# Creation of mapper, actor, etc...
    cubeMapper = vtkPolyDataMapper()
    cubeMapper.SetInputData(cube)

    cubeActor = vtkActor()
    cubeActor.SetMapper(cubeMapper)

	# Creation of renderer, render window, and interactor.
    ren1 = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    ren1.AddActor(cubeActor)
    # Change Background color
    ren1.SetBackground(1.0, 0.55, 0.41) 

	# render
    renWin.Render()

	# Start of interaction
    iren.Start()

if __name__ == '__main__':
    main()
