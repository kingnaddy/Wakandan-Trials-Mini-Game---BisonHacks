// data.js

// 1) General Game Configuration
const GAME_CONFIG = {
    // Canvas dimensions
    canvasWidth: 800,
    canvasHeight: 600,
  
    // Player movement speed
    baseSpeed: 4,
  
    // Starting health
    startingHP: 100,
  
    // Leveling thresholds (XP needed for each level)
    xpToLevel: [100, 200, 300, 450, 600, 800, 1000, 1250, 1500],
  
    // Enemy spawn settings
    spawnInterval: 2000,         // milliseconds between spawns initially
    spawnIntervalMin: 500,       // minimum possible spawn interval
    spawnIntervalDecrement: 10,  // how much to reduce spawn interval each wave
    maxEnemies: 300,             // maximum on screen (if you want a limit)
  
    // Quick Hack event timing
    quickHackInterval: 45000,    // every 45 seconds
  };
  
  // 2) Weapons
  // Each weapon could have unique properties like damage, cooldown (ms), projectile speed, area, etc.
  const WEAPONS = {
    energyGauntlet: {
      name: "Energy Gauntlet",
      damage: 15,
      cooldown: 800,          // in milliseconds
      projectileSpeed: 6,
      color: "#42f5a7",
      size: 5,
    },
    sonicDisruptor: {
      name: "Sonic Disruptor",
      damage: 10,
      cooldown: 500,
      projectileSpeed: 7,
      color: "#f542a7",
      size: 4,
    },
    vibraniumDrone: {
      name: "Vibranium Drone",
      damage: 20,
      cooldown: 1200,
      // This might behave differently (orbiting the player or auto-targeting)
      color: "#4287f5",
      size: 8,
    },
    // Feel free to add more weapons, synergy logic, etc.
  };
  
  // 3) Enemy Types
  // A few examples to represent variety in speed, HP, damage, etc.
  const ENEMY_TYPES = {
    drone: {
      name: "Surveillance Drone",
      hp: 30,
      speed: 2.5,
      damage: 5,
      size: 12,
      xp: 10,
      color: "#f55742",
    },
    mercenary: {
      name: "Mercenary",
      hp: 60,
      speed: 1.8,
      damage: 10,
      size: 14,
      xp: 15,
      color: "#f59e42",
    },
    cyborg: {
      name: "Cybernetic Operative",
      hp: 100,
      speed: 1.5,
      damage: 15,
      size: 16,
      xp: 25,
      color: "#a742f5",
    },
    tank: {
      name: "Armored Tank",
      hp: 200,
      speed: 1.0,
      damage: 20,
      size: 22,
      xp: 40,
      color: "#4287f5",
    },
  };
  
  // 4) Companion Abilities (Optional)
  const COMPANIONS = {
    decoy: {
      name: "Decoy Projection",
      cooldown: 15000, // ms
      // In your main code, you might spawn "decoy objects" to distract enemies
    },
    repair: {
      name: "Vibranium Repair Field",
      cooldown: 20000,
      healAmount: 10,
      radius: 100,
      // Heals the player (and maybe allies) within a certain radius
    },
    turret: {
      name: "Automated Turret",
      cooldown: 25000,
      damage: 8,
      fireRate: 500, // ms between turret shots
      duration: 10000, // turret stays active for 10s
    },
  };
  
  // 5) Arenas or Stages (Optional)
  const ARENAS = {
    palace: {
      name: "Royal Palace Grounds",
      backgroundColor: "#0f1a2b",
    },
    lab: {
      name: "Underground Tech Labs",
      backgroundColor: "#0a1f1a",
    },
    mines: {
      name: "Vibranium Mines",
      backgroundColor: "#1f1a25",
    },
    border: {
      name: "Borderlands Outposts",
      backgroundColor: "#2b1a0a",
    },
  };
  
  // 6) Quick Hack Options (Optional)
  const QUICK_HACK_OPTIONS = [
    { id: "drone", name: "Drone Overload", effect: "damageAll" },
    { id: "confuse", name: "Guard Confusion", effect: "stunEnemies" },
    { id: "blackout", name: "Surveillance Blackout", effect: "weakenEnemies" },
  ];
  
  // 7) Missions / Minigames (Optional)
  const MISSIONS = {
    nodeDefense: {
      name: "Vibranium Node Defense",
      description: "Match the correct RFID signatures to secure the nodes",
      duration: 30000, // 30s
    },
    intruderAlert: {
      name: "Intruder Alert Challenge",
      description: "Neutralize sensor hotspots before enemies become enhanced",
      duration: 25000,
    },
    hackingChallenge: {
      name: "Security System Bypass",
      description: "Complete the hacking sequence to gain system access",
      duration: 40000,
    },
  };
  
  // Everything here is now available globally in your other scripts (e.g., game.js) 
  // as long as this file is loaded first in index.html.
  