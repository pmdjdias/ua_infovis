# Lesson 1 - three.js Introduction

## Outline
* Configuration of environment 
* First example, Visualization pipeline
* Visualization of a poligonal mesh with color
* Viewport Update
* Other primitives in three.js
 

## three.js configuration 
Three.js is a library built on webGL to abstract some of the difficulties related to low-level graphics and to reduce the quantity of code to produce the visualizations. Its configuration is similar to the one used by webGL.
To use three.js, it is necessary to include the following lines in you javascript code:


``` html
<script src="https://threejs.org/build/three.js"></script>
```

It is also possible to downlaod  three.js from http://threejs.org/ and use a local copy with the following link:

``` html
<script src="js/three.js"></script>
```

You can explore some three.js examples at the following site : http://threejs.org/examples/

## First example 
Create your first three.js example based on the tutorial available at:
https://threejs.org/docs/index.html#manual/introduction/Creating-a-scene
See the all the necessary steps to create and visualize a scene:

1.	Definition of the scene, camera and renderer:
``` html
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
```
2.	Definition of an object/geometry and camera position:
``` html
const geometry = new THREE.BoxGeometry(1,1,1);
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } ); 
const cube = new THREE.Mesh( geometry, material ); 
scene.add( cube ); 
camera.position.z = 5;
```
3.	Scene rendering: 
``` html
function render() {
	requestAnimationFrame(render);
	renderer.render(scene, camera);
}
render();
```
4.	Scene animation: 
``` html
cube.rotation.x += 0.01;
cube.rotation.y += 0.01;
```

## 2D primitives
Modify the previous example to visualize a black 2D triangle.
Use the following coordinates for the vertices (-1,-1,0) (1,-1,0) and (1,1,0).
To create  the mesh, you can use the following code:

``` html
var geometry = new THREE.BufferGeometry();

const vertices = new Float32Array( [
	-1.0, -1.0,  0.0,
	1.0, -1.0,  0.0,
	1.0,  1.0,  0.0,
] );

geometry.setAttribute( 'position', new THREE.BufferAttribute( vertices, 3 ) );
```

Create another material so that the triangle is black over a red background (use the setClearColor function of the Renderer for backgroundColor).
Modify the code to obtain the same scene without modifying the camera position.

## Addition of color
To allow the mapping of different colors in a mesh face, it is necessary to associate a color to each vertice. This can be done as follow:

``` html
var colors = new Uint8Array( [
	 255,  0,  0,  
	 0,  255,  0,  
	 0,  0,  255,  
] );

geometry.setAttribute( 'color', new THREE.BufferAttribute( colors, 3, true) );
```
A material is also necessary (see following code):
``` html
const geometryMaterial = new THREE.MeshBasicMaterial( {vertexColors: true} );
```
Modify the example to create a scene similar to the figure below using the following 2D coordinates:
``` html
(0.0,  0.0,  0.0) ( 0.5,  0.75, 0.0) ( 1.0,  0.0,  0.0);
(0.0,  0.0,  0.0) (-0.35,-1.0,  0.0) (-0.7,  0.25, 0.0);
(-0.2, 0.15, 0.0) ( 0.35, 0.65, 0.0) (-0.85, 0.9,  0.0 );
(0.15,-0.95, 0.0) ( 0.90,-0.7,  0.0) ( 0.65, 0.10, 0.0); 
```

If you cannot see some triangle, use the "side" flag in the material with the argument THREE.DoubleSide.
What is this option used for? This issue is related to the fact that only triangles with normal facing towards the camera are rendered (see Back Face Culling). How can you solve the problem in another way (an more elegant way)?
For the last triangle, it is necessary to create another model with the wireframe property activated in its MeshBasicMaterial.

![4Triângulos](./figura1.png)

## Viewport Update
Go back to the first example (rotation cube). Visualize the example and  change the dimensions of the browser window. What happens? This is due to the fact that the visualization window (viewport) is not update when the browser window size changes.
To solve this problem, create a new function to be called when the browser window size is update. This function need to access the window size (window.innerWidth and window.innerHeight) and update the  renderer size accordingly (renderer.setSize()). It also needs to modify the aspect camera ratio as well (camera.aspect=…) and update this change  (camera.updateProjectionMatrix()).
Add the code necessary in the following function to ensure the correct resizing of the viewport when the window size is modified. Observe the results.

``` html
window.addEventListener('resize', function () {				       
	… code to update the viewport correctly
		});
```
## Other primitives
Modify the first example to show the cube in wireframe.
Investigate other available geometries (Extras / Geometries) and visualize at least 4 other geometries in the same scene changing some of their default parameters. 
Write a report following the template available at the course page (http://sweet.ua.pt/paulo.dias/vi/ReportVI_template.docx) about the experiences done in this class. It should contain examples of the visualizations produced in each exercise, as well your comments about them.


