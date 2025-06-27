const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let player = {x: 400, y: 550, w:30, h:30, speed: 5, color: "#00f7a6"};
let enemies = [];
let keys = {};

fetch('/api/generate_level')
    .then(response => response.json())
    .then(data => {
        enemies = data.enemies;
        requestAnimationFrame(gameLoop);
    });

// Key Handlers
window.addEventListener('keydown', e => keys[e.key.toLowerCase()] = true);
window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);

// Game Loop
function gameLoop(){
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// Update Logic
function update(){
    if(keys['arrowleft'] || keys['a']) player.x -= player.speed;
    if(keys['arrowright'] || keys['d']) player.x += player.speed;
    if(keys['arrowup'] || keys['w']) player.y -= player.speed;
    if(keys['arrowdown'] || keys['s']) player.y += player.speed;

    player.x = Math.max(0, Math.min(canvas.width - player.w, player.x));
    player.y = Math.max(0, Math.min(canvas.height - player.h, player.y));

    enemies.forEach(enemy => {
        enemy.y += enemy.speed;
        if(enemy.y > canvas.height + 20){
            enemy.y = -20;
            enemy.x = Math.random()*(canvas.width - 30);
        }
    });
}

// Draw Logic
function draw(){
    ctx.clearRect(0,0,canvas.width,canvas.height);

    // Draw Player
    ctx.fillStyle = player.color;
    ctx.fillRect(player.x, player.y, player.w, player.h);

    // Draw Enemies
    ctx.fillStyle = "#f54242";
    enemies.forEach(enemy => {
        ctx.fillRect(enemy.x, enemy.y, 25, 25);
    });
}
