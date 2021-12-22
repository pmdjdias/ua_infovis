# Lesson 2 - Projections, lighting and transformations

## Outline
* Camera models: perspective and orthogographic cameras
* Interaction with camera
* Lighting and shading
* Transformations


# Camera models
Modify the first example from the last lesson to visualize the cube in wireframe (you can get the code at https://threejs.org/docs/index.html#manual/introduction/Creating-a-scene). You must activate the appropriate material property. Also disable the cube rotation.

Instead of using a perspective camera, now use an Orthographic Camera (https://threejs.org/docs/#api/en/cameras/OrthographicCamera). Note that in this type of camera the upper limits are specified in x and y coordinates on the scene and not with the field of view angle as in the  perspective camera. Modify the parameters so that the world view is between -3 and 3 on the x-axis while respecting the window's aspect ratio.
Compare the result with the two type of cameras. Is this what you expected?

Optional/HomeWork: Add a function to ensure that the cube aspect ratio does not change when the window is resized (adapt from the Viewport Update in last lesson).

# Orbit control
three.js provides classes to allow an easy control of the camera pose, see for example the OrbitControls. Note that to use these controls you will have to include the file separately in your HTML (files in the /examples directory). You might also add the following script:

``` html
<script src="https://threejs.org/examples/js/controls/OrbitControls.js"></script>
``` 
In the previous example, replace the camera control with the following line and see what happens:

``` html
const controls = new THREE.OrbitControls(camera, renderer.domElement);
``` 
Do not forget to update the camera controls in the render function: 
``` html
controls.update();
```
Other camera controls are available. Try some of them, for example the TrackballControls, FirstPersonControls or FlyControls.

# Lighting and materials
Let's now add lights to the scene.
Get back to the perspective camera, disable the wireframe and turn the rotation of the cube back on.
Create a DirectionalLight (https://threejs.org/docs/#api/en/lights/DirectionalLight) at position 0.5.0 with color 0xffffff and intensity 1.0. Do not forget to add it to the scene. Do you see any changes in the scene? In order for the object to interact with light it is necessary to use a material of a different type from MeshBasicMaterial. Replace the MeshBasicMaterial with a MeshPhongMaterial material and observe what happens.

``` html
const material = new THREE.MeshPhongMaterial({
            	color: '#006063',
		specular: '#a9fcff',
		shininess: 100
            });
``` 
Add an ambient light, note (note that the ambient light component (color) of the material is only used if there is ambient light in the scene). You may use the following code:
``` html
const alight = new THREE.AmbientLight(0xffffff);
scene.add(alight);
``` 

# Shading
Modify the original rotating cube example to represent not a cube but a sphere (primitive sphereGeometry) of radius 1.
Modify parameters 2 and 3 with the wireframe option active. What do the widthSegments and heightSegments parameters correspond to? Disable wireframe and set the number of segments to 10.

Now create another sphere with the same characteristics and place one sphere at x=-2.5 and the other at x=2.5 (use the position.x method).

Add the ambient light and directional light from the previous exercize located between the two spheres with y=5. Apply the same MeshPhongMaterial to the two spheres (use the previous example). Modify the flatShading option of one of the materials by toggling between true and false and observe the result.

Optional/HomeWork: Apply to the first sphere a MeshLambertMaterial type material with the same characteristics as sphere 2. In the Lambertian-type material, remove the specular and shininess components. What do you observe? Lambertian materials scatter light evenly in all directions so the specular coefficient and brightness are ignored.

Modify the properties of the spheres by selecting some values from the following table (note that the brightness must be multiplied by 256) to see the effects of different materials. See the example:

``` html
const emerald = new THREE.MeshPhongMaterial({
shading: THREE.SmoothShading	});
emerald.color = new THREE.Color(0.07568, 0.61424, 0.07568);
emerald.specular= new THREE.Color(0.633, 0.7278, 0.633);
emerald.shininess = 0.6 * 256;
``` 
Name             |Ambient                             |Diffuse	                        |Specular	                        |Shininess
-----------------|------------------------------------|-----------------------------------|-----------------------------------|----------:
emerald          |0.0215	0.1745	0.0215      |0.07568	0.61424	0.07568     |0.633	0.727811	0.633       |0.6
Gold             |0.24725	0.1995	0.0745      |0.75164	0.60648	0.22648     |0.628281	0.555802	0.366065    |0.4
Silver           |0.19225	0.19225	0.19225     |0.50754	0.50754	0.50754     |0.508273	0.508273	0.508273    |0.4
Black plastic    |0.0	0.0	0.0                     |0.01	0.01	0.01                    |0.50	0.50	0.50                    |0.25
Red plastic      |0.0	0.0	0.0                     |0.5	0.0	0.0                     |0.7	0.6	0.6                     |0.25
White plastic    |0.0	0.0	0.0                     |0.55	0.55	0.55                    |0.70	0.70	0.70                    |0.25
Black rubber     |0.02	0.02	0.02                    |0.01	0.01	0.01                    |0.4	0.4	0.4                     |0.0781
Red rubber       |0.05	0.0	0.0                     |0.5	0.4	0.4                     |0.7	0.04	0.04                    |0.0781
White rubber     |0.05	0.05	0.05                    |0.5	0.5	0.5                     |0.7	0.7	0.7                     |0.0781

You may use the following sites to visualize other lighting effects or other materials using:

http://www.realtimerendering.com/teapot/

http://www.lighthouse3d.com/2014/01/webgl-basic-material-list-from-teapots-c/

Optional/HomeWork: Add the following lights, all pointing to the origin of the scene: 
Red directional light in position (-5,0,0)
Blue directional light in position (5,0,0)
Green spotlight light in position (0,0,-5) with angle Math.PI/20 and target object in (-2.5,0,0)

# Transparency
In the previous example (two spheres located at x=-2.5 and x=2.5) add spheres (or cubes) with a slightly larger size around original spheres.
Use the following material for these two models and observe the effect. Modify the opacity parameter to adjust the transparency.
``` html
const glassMaterial = new THREE.MeshPhongMaterial( { 
color: 0x222222, 
specular: 0xFFFFFF,
shininess: 100, 
opacity: 0.3, 
transparent: true 
} );
``` 

# Transformations (scale and rotation)
Create a new scene consisting of a box of size (2,1,4) (use the scale property) at position (0,0,0) and four spheres (radius 0.5) centered on its lower vertices (see figure below). Instead of adding multiple separate meshes, you can add multiple meshes into a single THREE.Object3D() via the add command.
View the transformation matrices of the parallelepiped and of one of the spheres on the console, accessing the matrix (matrix) with the transformations of the objects.

![paralelepípedo1](./paralelepípedo1.png)

# Transformations (rotations)
Create an object that represents a coordinate system using three red, green, and blue cylinders (CylinderGeometry) for each axis. The three cylinders must belong to a single object named axis. Add this object to the previous scene and replace the spheres with cylinders with radius 0.5 and height 0.2.
You may also see the axisHelper geometry as an alternative for visualization of the axes.

![paralelepípedo2](./paralelepípedo2.png)

Now add an animation to move the "car" along a predefined circuit (for example perform a rotation of radius 1 around the point (0,0,-1)).
