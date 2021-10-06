let bugs = []; // array of Jitter objects
let numberOfBugs = 1000;

function setup() {
  createCanvas(710, 400);
  // Create objects
  
  for (let i = 0; i < numberOfBugs; i++) {
    bugs.push(new Jitter());
  }
}

function draw() {
  background(50, 89, 100);
  
  for (let i = 0; i < numberOfBugs; i++) {
    bugs[i].move();
    bugs[i].display();

    if (i % 10 == 0) {
      bugs[i].diameter = 100; 
    }
  }

}

// Jitter class
class Jitter {
  constructor() {
    this.x = random(width);
    this.y = random(height);
    this.diameter = random(10, 30);
    this.speed = 1;
    this.color = color(random(255),random(255), random(255));
  }

  move() {
    this.x += random(-this.speed, this.speed);
    this.y += random(-this.speed, this.speed);
  }

  display() {
    fill(this.color);
    ellipse(this.x, this.y, this.diameter, this.diameter);
  }
}