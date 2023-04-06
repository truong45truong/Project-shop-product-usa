
import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.118/build/three.module.js"
var camera, scene, renderer;

var isUserInteracting = false,
  onMouseDownMouseX = 0, onMouseDownMouseY = 0,
  lon = 0, onPointerDownLon = 0,
  lat = 0, onPointerDownLat = 0,
  phi = 0, theta = 0 , onPointerDownPointerX = 0 , onPointerDownPointerY = 0;

var time_fov = 0;
var OptionViewer = 0  
init();
animate();

function onDocumentMouseClick(event) {
  console.log("click")
  event.preventDefault();
    if( time_fov <= 0 ){

      onPointerDownPointerX = event.clientX;
      onPointerDownPointerY = event.clientY;

      time_fov = 15;
      OptionViewer = 1; 
    }
  // isUserInteracting = false;
}

function init() {

  var container, mesh;

  container = document.getElementById('container');

  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1100);
  camera.target = new THREE.Vector3(0, 0, 0);

  // Tạo 1 không gian 3d
  scene = new THREE.Scene();

  var geometry = new THREE.SphereGeometry(500, 60, 40);
  geometry.scale(- 1, 1, 1);

  var material = new THREE.MeshBasicMaterial({
    map: new THREE.TextureLoader().load('./media/3D-img/pexels-sergio-souza-5048124.jpg')
  });

  mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  container.addEventListener("click", onDocumentMouseClick);

  renderer = new THREE.WebGLRenderer();
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  container.appendChild(renderer.domElement);
  // const controls = new OrbitControls( camera, renderer.domElement );
  // controls.target.set( 0, 0.5, 0 );
  // controls.update();
  // controls.enablePan = false;
  // controls.enableDamping = true; 
}

function onWindowResize() {

  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize(window.innerWidth, window.innerHeight);

}


function animate() {

  requestAnimationFrame(animate);
  update();

}

function update() {
  console.log(camera.target.x,camera.target.y,camera.target.y)
  console.log(500 * Math.sin(phi) * Math.cos(theta))
  lon += 0.1;
    lat = Math.max(- 85, Math.min(85, lat));
    phi = THREE.Math.degToRad(90 - lat);
    theta = THREE.Math.degToRad(lon);
  switch(OptionViewer) {
    case 0:
      // lon += 0.1;
      // lat = Math.max(- 85, Math.min(85, lat));
      // phi = THREE.Math.degToRad(90 - lat);
      // theta = THREE.Math.degToRad(lon);
    
      // camera.target.x = 500 * Math.sin(phi) * Math.cos(theta);
      // camera.target.y = 500 * Math.cos(phi);
      // camera.target.z = 500 * Math.sin(phi) * Math.sin(theta);
      break;
    case 1:
      camera.target.z = 500 * Math.sin(phi) * Math.sin(theta);
      // camera.target.y = camera.target.y +1*(onPointerDownPointerY/onPointerDownPointerX) 
      console.log(camera.target.x,camera.target.y)
      if(time_fov < 0 ){
        OptionViewer = 0
      }
      time_fov = time_fov - 1
      camera.fov -= 0.3;
      
	    camera.updateProjectionMatrix();
      break;
    default:
      // code block
  }

  camera.lookAt(camera.target);

  /*
  // distortion
  camera.position.copy( camera.target ).negate();
  */

  renderer.render(scene, camera);

}


