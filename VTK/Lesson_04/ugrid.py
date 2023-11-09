###############################################################################
#       						Poligonal.py
###############################################################################

# Import all VTK modules
from vtkmodules.all import *

def main():

    # tetra
    coords = [[0,0,0], [1,0,0], [0.5,1,0], [0.5,0.5,1]]
    aTetra = [0,1,2,3]
    
    #################################
	# VTKUnstructuredGrid Definition
    Ugrid = vtkUnstructuredGrid()
    points = vtkPoints()
    
    # Vertex  
    for i in range(len(coords)):
        points.InsertPoint(i,coords[i])
    
    # Cell
    Ugrid.InsertNextCell(VTK_TETRA,4,aTetra)
    
    Ugrid.SetPoints(points)
    
    # Mapper and actor
    UGriMapper = vtkDataSetMapper()
    UGriMapper.SetInputData(Ugrid)

    UgridActor = vtkActor()
    UgridActor.SetMapper(UGriMapper)

    # Creation of renderer, render window, and interactor.
    ren1 = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    ren1.AddActor(UgridActor)
    ren1.SetBackground(1.0, 0.55, 0.41) 

	# render
    renWin.Render()

	# Start of interaction
    iren.Start()

if __name__ == '__main__':
    main()
