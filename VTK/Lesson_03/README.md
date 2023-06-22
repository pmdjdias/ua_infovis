# Lesson 3 - Callbacks, Glyphing and Picking

## Outline
* Observers and callbacks
* Glyphing 
* Picking

# Use of callbacks for interaction
An important feature of VTK is the possibility to define Callback functions making it possible to associate to an object a "callback" function to be executed whenever a given event occurs. The association between the function and the event is done using an observer.
Add the following function in the cone with interaction example (see lesson 02)

``` html
##############################
# Callback for the interaction
##############################
class vtkMyCallback(object):
    def __init__(self, renderer):
        self.ren = renderer

    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        print(caller.GetClassName(), 'Event Id:', ev)
        # Now print the camera position.
        print("Camera Position: %f, %f, %f" % (self.ren.GetActiveCamera().GetPosition()[0],self.ren.GetActiveCamera().GetPosition()[1],self.ren.GetActiveCamera().GetPosition()[2]))
# Callback for the interaction

....

In Code
################################################################
# Here is where we setup the observer, we do a new and ren1 
mo1 = vtkMyCallback(ren)
ren.AddObserver(vtkCommand.AnyEvent,mo1)
################################################################
```

What do you observe when running the program? Try modifying the type of interaction (EndEvent, StartEvent, ResetCameraEvent, etc...)

# Glyphing
Glyphing is a form of visualization that represents data using geometric representations (glyphs).
The vtkGlyph3D class allows using this type of representation. To do so, the object needs an input (typically data with the various points where the Glyphs should be placed) and a source (which corresponds to the symbol to be placed at the various points).
Study the vtkGlyph 3D class and visualize a sphere with cones placed at each point of the sphere's polygonal model. You may adapt the following code.

``` html
glyph = vtkGlyph3D()
glyph.SetSourceConnection(coneSource.GetOutputPort())
glyph.SetInputConnection(sphereSource.GetOutputPort())
```

Explore and try to understand what  the SetScaleFactor and SetVectorModeToUseNormal methods are used fro? Try to replicate the following model.

![Example using class vtkGlyph3D ](./vtkGlyph3D.png)

Changemodify the theta (SetThetaResolution) and Phi (SetPhiResolution) resolutions of the sphere. What do you observe?

# Object picking
Add a VtkPointPicker object to the interactor of the previous example to allow the selection of points of the model (use the setPicker method of the interactor). Associate a callback to this picker.
The Callback must show, in the command window, the coordinates of the selected point (use the GetPickPosition command of the vtkPointPicker object). 
Note that the picking action is predefined in VTK with the P key.
Finally add a sphere indicating the selected point. To do so, create an actor that represents the sphere, which will be passed to the callback and whose position will be updated according to the selected point (actor's SetPosition method).
Note: You may use the VisibilityOn/VisibilityOff methods so that the sphere is only visible after picking.

``` html
myPicker = vtkPointPicker()
mo1 = vtkMyCallback(myPicker)
myPicker.AddObserver(vtkCommand.EndPickEvent ,mo1)
...
iren.SetPicker(myPicker)
```

# Display of coordinates
Modify the CallBack to show the point coordinates in the renderer next to the selected point. Use a textMapper and a vtkActor2D to visualize the coordinates of the selected point in the renderer.
To do so, modify the program as follows:

``` html
textMapper = vtkTextMapper()

textActor = vtkActor2D()
textActor.SetMapper(textMapper);
textActor.VisibilityOff();

ren1.AddActor( textActor );

mo1 = vtkMyCallback()
mo1.tMapper = textMapper;
mo1.tActor = textActor;
  
myPicker = vtkPointPicker()
	
myPicker.AddObserver(vtkCommand::EndPickEvent ,mo1)

iren.SetPicker(myPicker);
```

The pseudo code of your program should be:
* Test if the selection is valid (one possibility is to test the return of GetPointId()) – If the value is negative, the Actor becomes invisible.
* Get the selected point coordinate [3D] (GetPickPosition method)
* Get the coordinate of the selected pixel [2D] (GetSelectionPoint method). This coordinate is relative to the Viewport and represents a value in pixels.
* Update the TextMapper with the pixel coordinates (setInput)
* Update the TextActor position  (SetPosition)
* Make the actor visible.

![Expected result after point picking ](./vtkPicking.png)

Use the textMapper options to modify the format of the text used to display the coordinates (centered, with font courrier and bold).
