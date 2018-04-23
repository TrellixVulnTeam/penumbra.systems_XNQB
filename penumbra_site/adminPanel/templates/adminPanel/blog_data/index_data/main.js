//Condensed for easy inlining
(function() {
	var scene = new THREE.Scene();
	var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
	var renderer = new THREE.WebGLRenderer();
	renderer.setSize( window.innerWidth, window.innerHeight );
	document.body.appendChild( renderer.domElement );
	//------------------------------------SCENE LIGHTING SETUP-----------------------------------------------------
	var light, materials;
	scene.add( new THREE.AmbientLight( 0x666666 ) );
	light = new THREE.DirectionalLight( 0xdfebff, 1.75 );
	light.position.set( 50, 200, 100 );
	light.position.multiplyScalar( 1.3 );
	light.castShadow = true;
	//light.shadowCameraVisible = true;
	light.shadowMapWidth = 1024;
	light.shadowMapHeight = 1024;
	var d = 300;
	light.shadowCameraLeft = -d;
	light.shadowCameraRight = d;
	light.shadowCameraTop = d;
	light.shadowCameraBottom = -d;
	light.shadowCameraFar = 1000;
	//light.shadowDarkness = 0.5;
	light.shadowDarkness = 0;
	scene.add( light );
	//------------------------------------CUBE MATERIALS SETUP-----------------------------------------------------
	//var cubeTexture = THREE.ImageUtils.loadTexture( 'textures/patterns/circuit_pattern.png' );
	var cubeTexture = THREE.ImageUtils.loadTexture( 'textures/patterns/cry.png' );
	cubeTexture.wrapS = cubeTexture.wrapT = THREE.RepeatWrapping;
	cubeTexture.anisotropy = 16;
	var cubeMaterial = new THREE.MeshPhongMaterial( { alphaTest: 0.5, color: 0x336699, specular: 0x336699, emissive: 0x111111, shiness: 10, map: cubeTexture, side: THREE.DoubleSide } );
	var uniforms = { texture:  { type: "t", value: cubeTexture } };
	var vertexShader = document.getElementById( 'vertexShaderDepth' ).textContent;
	var fragmentShader = document.getElementById( 'fragmentShaderDepth' ).textContent;
	var cubes = [];
	//for (var i = 0, len = 66; i < len; i++) {
	for (var i = 0, len = 60; i < len; i++) {
		//Mesh Setup
		var cubeGeometry = new THREE.SphereGeometry( Math.random() * (i * 0.05), Math.random() * (i * 0.05), Math.random() * (i * 0.05));
		var cube = new THREE.Mesh( cubeGeometry, cubeMaterial);
		cube.position.set( -2 + (Math.random() * (i * 0.11)), -2 + (Math.random() * (i * 0.11)), -2 + (Math.random() * (i * 0.11)) );
		cube.castShadow = true;
		cube.receiveShadow = true;
		scene.add( cube );
		cube.customDepthMaterial = new THREE.ShaderMaterial( { uniforms: uniforms, vertexShader: vertexShader, fragmentShader: fragmentShader } );
		cubes.push(cube);
	}
	camera.position.z = 5;
	var maxX = 1;
	var minX = -1;
	var direction = 1;
	var left = -1;
	var right = 1;
	var speed = .005;
	function renderObject(time) {
		for (var i = 0, len = cubes.length; i < len; i++) {
			cubes[i].rotation.x += (i % 2 === 0) ? -1 * speed : speed;
	  		cubes[i].rotation.y += (i % 2 === 0) ? -1 * speed : speed;
			//position movements
			//if(i % 2 == 0){
			//cubes[i].position.set( -2 + (Math.random() * (i * 0.11)), -2 + (Math.random() * (i * 0.11)), -2 + (Math.random() * (i * 0.11)) );
			//}
		}
	}
	function render(time) {
		requestAnimationFrame( render );
		renderObject(time);
		renderer.render( scene, camera );
	}
	render();
})();
