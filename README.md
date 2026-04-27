# 🌍 AI Travel Route Optimizer (TSP Solver)

An interactive web application that calculates the most efficient travel route between multiple cities using classic and AI-based algorithms.

---

## 🚀 Features

* 🗺️ Real-time map visualization using Leaflet
* 📍 Add cities dynamically via geocoding
* ⚡ Multiple route optimization algorithms:

  * Nearest Neighbor (Greedy)
  * Held-Karp Dynamic Programming (Exact)
  * Genetic Algorithm (AI-based)
  * Brute Force (Optimal for small inputs)
* 📊 Algorithm comparison with distance metrics
* 📱 Fully responsive UI (works on mobile & desktop)
* 📦 Installable as a Progressive Web App (PWA)

---

## 🧠 Technologies Used

* Frontend: HTML, CSS, JavaScript
* Backend: Node.js, Express
* Maps: Leaflet.js + OpenStreetMap
* API: Nominatim (Geocoding)
* Deployment: Render

---

## 🌐 Live Demo

👉 https://travel-route-optimizer-33na.onrender.com

## ⚙️ Installation (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/route-optimizer.git
cd route-optimizer
```

### 2. Install dependencies

```bash
npm install
```

### 3. Run the server

```bash
node server.js
```

### 4. Open in browser

```text
http://localhost:3000
```

---

## 📱 PWA Installation

* Open the app in Chrome
* Click **Install App** or **Add to Home Screen**
* Use it like a native application

---

## 📊 Algorithms Used

### 🔹 Nearest Neighbor

Fast greedy approach, but not always optimal.

### 🔹 Held-Karp (Dynamic Programming)

Exact solution with exponential complexity.

### 🔹 Genetic Algorithm

Uses evolutionary principles to approximate optimal routes.

### 🔹 Brute Force

Checks all permutations (best for small inputs only).

---

## 🧩 Project Structure

```text
route-optimizer/
│
├── index.html
├── server.js
├── manifest.json
├── service-worker.js
├── package.json
├── icons/
```

---

## 🚧 Future Improvements

* 🔹 Real-time traffic integration
* 🔹 Backend computation optimization
* 🔹 Offline support (full PWA caching)
* 🔹 AI-based route prediction

---


