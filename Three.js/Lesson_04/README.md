# Lesson 4 - Interaction and Selection

## Outline
* Mouse Interaction
* Raycast selection of objects 
* Camera interaction
* 3D Text

# Mouse Interaction
Use as a base an example with a cube and some lighting (Lighting and materials from lesson 2 for example). Disable animations and camera control (with orbitControl).
The objective is to control the object's orientation using the mouse replacing the orbitControl.
Analyze the following code and use it to allow the rotation of the cube according to mouse movement (consider phi the rotation angle in x and theta in y).
``` html
    var drag = false;
    var phi = 0, theta = 0;
    var old_x, old_y;

    var mouseDown = function (e) {
        drag = true;
        old_x = e.pageX, old_y = e.pageY;
        return false;
    }

    var mouseUp = function (e) {
        drag = false;
    }

    var mouseMove = function (e) {
        if (!drag) return false;
        var dX = e.pageX - old_x,
        dY = e.pageY - old_y;
        theta += dX * 2 * Math.PI / window.innerWidth;
	phi += dY * 2 * Math.PI / window.innerHeight;
        old_x = e.pageX, old_y = e.pageY;
    }

    renderer.domElement.addEventListener("mousedown", mouseDown);
    renderer.domElement.addEventListener("mouseup", mouseUp);
    renderer.domElement.addEventListener("mousemove", mouseMove);
``` 

# Object Selection
three.js provides two classes (Projector e Raycaster) that can be used to perform raycasting to intercept/Select objects on the scene.
The Projector class computes a 3D ray on the scene from all 3D coordinates that are projected on the pixel on the screen (it requires the 2D coordinate of the pixel and the camera information()(. To use the projector, you need to include the following code: 
``` html
<script src="https://threejs.org/examples/js/Projector.js"></script>
``` 
The Raycaster is used to determine the objects that intersect the 3D ray generated from a pixel using the camera position and orientation.
Analyze the following code and use it to select objects from the scene by clicking on pixels of the window.
``` html
//mouse event variables
var raycaster = new THREE.Raycaster(); // create once
var mouse = new THREE.Vector2(); // create once
intersects = [];
function onMouseDown(e) {
	//compute transform betweem mouse and three.jscoordinate systems
	mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
	mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
	//Calls raycaster function with camera position and orientation
	raycaster.setFromCamera( mouse, camera );
	//Check if the ray intercept an object on the scene
	intersects = raycaster.intersectObject(cube);
	if (intersects.length) {
		alert("hit");
	}
}
``` 
Place another model in the scene (another cube for example) and modify the code to distinguish which model was selected. You may also change the color of the selected object: when clicking on one of the 3D objects, it turns red, for example.

Add a OrbitControls or TrackballControls and see what happens when the cubes are aligned. Ensure that the code allows selecting the two cubes when 
they are aligned (you can use rayCaster's IntersectObjects method with scene.children variable and then acess all the selected objects trough the returning variable) as shown below:
``` html
intersects = raycaster.intersectObjects(scene.children);
for (var i=0; i<intersects.length; i++) {
  // Change the material of the selected objects
}
``` 

# Control of the Camera position
The method used previously in the first exercize only allows you to turn an object on itself (try using the same code with the two cubes with x=-2 and x=2 and see the result).
To allow changing the point of view, it is necessary to act on the position and orientation of the camera and not on the position and orientation of the object.
Modify the code from the first example to move the camera over a sphere centered on the origin with radius 5. It should allow updating the position of the camera on the sphere according to the variables phi and theta. Note that in addition to the position (camera.position.set(x,y,z)) you must also set the camera´s orientation (camera.lookAt()). To calculate Cartesian coordinates (x,y,z) from spherical coordinates (rho, phi, theta).
You can use the following code:
``` html
theta = …
phi = …
camera.position.x = raio * Math.sin(theta) * Math.cos(phi);
camera.position.y = raio * Math.sin(phi);
camera.position.z = raio * Math.cos(theta) * Math.cos(phi);
camera.updateMatrix();
``` 
Use the +/- keys on the keyboard (see the last lesson) to allow “zoom in” and “zoom out”.

# Texto 
Use Three.js' TextGeometry (https://threejs.org/docs/#examples/en/geometries/TextGeometry) to place a text on top of the cubes indicating “cube1” or “cube2”. Use the font "helvetiker" (you can use the file provided in the examples/fonts folder of three.js (helvetiker_regular.typeface.json) To define the text object you can use the following code to create the text geometry for cube 1. You need to add the follwoong js files:
``` html
<script src="https://threejs.org/examples/js/loaders/FontLoader.js"></script>
<script src="https://threejs.org/examples/js/geometries/TextGeometry.js"></script>
```
And use the following code to create the text
``` html
var textMesh1;
var loader = new THREE.FontLoader();
loader.load("https://threejs.org/examples/fonts/helvetiker_regular.typeface.json", function (font) {
    textGeometry1 = new THREE.TextGeometry("Cube 1", {
        font: font,
        size: 0.22,
        height: 0.05,
    });
    var materialText = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    textMesh1 = new THREE.Mesh(textGeometry1, materialText);
    textMesh1.position.x = -2.5;
    textMesh1.position.y = 1.5;
});
``` 
Modify the example so that the text only appears when a given cube is selected (see Object Selection) and use the mesh's visible property accordingly.
