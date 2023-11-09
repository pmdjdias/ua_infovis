###############################################################################
#       						widget.py
###############################################################################



# Import all VTK modules
from vtkmodules.all import *

def main():

    # We Create an instance of vtkConeSource and set some of its
    # properties. The instance of vtkConeSource "cone" is part of a
    # visualization pipeline (it is a source process object); it produces data
    # (output type is vtkPolyData) which other filters may process.
    
    coneSource = vtkConeSource()
    # coneSource.SetResolution(10)

    sphereSource = vtkSphereSource()
    # sphereSource.SetThetaResolution(100)
    # sphereSource.SetPhiResolution(100)

    polydata = vtkPolyData()
    # polydata.SetPoints(points)
    polydata = sphereSource.GetOutput()

    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())
    # glyph.SetInputData(polydata)
    # glyph.Update()
    glyph.SetScaleFactor(0.2)
    glyph.SetVectorModeToUseNormal()

    glyphMapper = vtkPolyDataMapper()
    glyphMapper.SetInputConnection( glyph.GetOutputPort() )
    
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort() )

    
    glyphActor = vtkActor()
    glyphActor.SetMapper(glyphMapper)

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    

    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    ren.AddActor( glyphActor )
    ren.AddActor( sphereActor )
    ren.SetBackground(1.0, 0.55, 0.41)
    
    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetSize(640, 480)
    renWin.SetWindowName('Picking')

    sphereSource2 = vtkSphereSource()
    sphereSource2.SetRadius(0.05)
    sphereMapper2 = vtkPolyDataMapper()
    sphereMapper2.SetInputConnection( sphereSource2.GetOutputPort() )
    sphereActor2 = vtkActor()
    sphereActor2.SetMapper(sphereMapper2)
    sphereActor2.GetProperty().SetColor(1,0,0)

    ren.AddActor(sphereActor2)

    
    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)


    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()