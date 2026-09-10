// ===================================================
// STUDENT TASK: Build a graphical dashboard for Seneye
// ===================================================

// Replace this with your teacher's Cloudflare Worker URL:
const PROXY_URL = "https://seneye-proxy.ezankov.workers.dev/";

// Toggle to true if you are working offline without network access
const USE_OFFLINE_MOCK = false;

let aquariumData = null;
let lastUpdated = "";

function preload() {
  // Load initial data before setup() runs
  let endpoint = USE_OFFLINE_MOCK ? "sample-data.json" : PROXY_URL;
  aquariumData = loadJSON(endpoint, onDataLoaded, onError);
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  
  // Refresh live data every 5 minutes (300,000 ms)
  if (!USE_OFFLINE_MOCK) {
    setInterval(() => {
      loadJSON(PROXY_URL, onDataLoaded, onError);
    }, 1000);
  }
}

function onDataLoaded(data) {
  aquariumData = data;
  lastUpdated = new Date().toLocaleTimeString();
  console.log("Data refreshed successfully:", data);
}

function onError(err) {
  console.error("Failed to load aquarium data. Check proxy URL or network.", err);
}

function draw() {
  background(17, 82, 190); // Dark blue aquarium background

  // 1. Draw Title Header
  fill(255);
  textSize(24);
  textAlign(LEFT, TOP);
  text("Fish Environment Dashboard", 30, 30);

  // Display connection status
  textSize(12);
  fill(150, 200, 255);
  text("Last updated: " + (lastUpdated || "Loading..."), 30, 65);

  // 2. Render Dashboard Graphics
  if (aquariumData) {
    // NOTE: Update these keys based on your actual Seneye JSON response structure!
    // Example fields commonly found in sensor data:
    let temp = aquariumData[0].exps.temperature.curr;
    let ph = aquariumData[0].exps.ph.curr;
    let nh3 = aquariumData[0].exps.nh3.curr; 
    let o2 = aquariumData[0].exps.o2.curr;

    // Call your custom graphic widgets
    drawGaugeWidget(width / 5 - 100, 120, "Water Temp", temp);
    drawGaugeWidget(2 * width / 5 - 100, 120, "pH Level", ph);
    drawGaugeWidget(3 * width / 5 - 100, 120, "Ammonia (NH3)", nh3);
    drawGaugeWidget(4 * width / 5 - 100, 120, "Oxygen (O2)", o2);
  } else {
    // Loading State
    fill(255, 100, 100);
    textSize(18);
    text("Connecting to sensor stream...", 30, 120);
  }
}
// Example Widget Function: Simple Bar Gauge
function drawGaugeWidget(x, y, label, val) {
  fill(35, 48, 68);
  strokeWeight(3);
  stroke("black");
  rect(x, y, 200, 150, 10);

  noStroke();
  fill(180, 200, 220);
  textSize(14);
  text(label, x + 15, y + 15);

  fill(192, 192, 192);
  textSize(28);
  text(val, x + 15, y + 50);

  if (label == "pH Level"){
    if (aquariumData[0].exps.ph.status == "1") {
      textSize(38);
      fill("red");
      text("WARNING!", x + 5, y + 100);
    }
  }
  else if (label == "Ammonia (NH3)"){
    if (aquariumData[0].exps.nh3.status == "1") {
      textSize(38);
      fill("red");
      text("WARNING!", x + 5, y + 100);
    }
  }
  else if (label == "Oxygen (O2)"){
    if (aquariumData[0].exps.o2.status == "1") {
      textSize(38);
      fill("red");
      text("WARNING!", x + 5, y + 100);
    }
  }
  else if (label == "Water Temp"){
    if (aquariumData[0].exps.temperature.status == "1") {
      textSize(38);
      fill("red");
      text("WARNING!", x + 5, y+ 100);
    }
  }
}