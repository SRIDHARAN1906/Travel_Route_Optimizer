"""
Travel Route Optimizer — Flask Backend
Subject : 21CSC201T (Artificial Intelligence)
Live    : https://travel-route-optimizer-33na.onrender.com/
"""

from flask import Flask, request, jsonify, render_template
from tsp_algorithms import solve

app = Flask(__name__)

# ─────────────────────────────────────────────
#  PRESET CITY GROUPS
# ─────────────────────────────────────────────

PRESETS = {
    "india": [
        {"name": "Chennai",     "lat": 13.0827, "lon": 80.2707},
        {"name": "Mumbai",      "lat": 19.0760, "lon": 72.8777},
        {"name": "Delhi",       "lat": 28.6139, "lon": 77.2090},
        {"name": "Kolkata",     "lat": 22.5726, "lon": 88.3639},
        {"name": "Bangalore",   "lat": 12.9716, "lon": 77.5946},
        {"name": "Hyderabad",   "lat": 17.3850, "lon": 78.4867},
        {"name": "Ahmedabad",   "lat": 23.0225, "lon": 72.5714},
        {"name": "Jaipur",      "lat": 26.9124, "lon": 75.7873},
    ],
    "europe": [
        {"name": "London",      "lat": 51.5074, "lon": -0.1278},
        {"name": "Paris",       "lat": 48.8566, "lon":  2.3522},
        {"name": "Berlin",      "lat": 52.5200, "lon": 13.4050},
        {"name": "Rome",        "lat": 41.9028, "lon": 12.4964},
        {"name": "Madrid",      "lat": 40.4168, "lon": -3.7038},
        {"name": "Amsterdam",   "lat": 52.3676, "lon":  4.9041},
        {"name": "Vienna",      "lat": 48.2082, "lon": 16.3738},
        {"name": "Prague",      "lat": 50.0755, "lon": 14.4378},
    ],
    "usa": [
        {"name": "New York",    "lat": 40.7128, "lon": -74.0060},
        {"name": "Los Angeles", "lat": 34.0522, "lon":-118.2437},
        {"name": "Chicago",     "lat": 41.8781, "lon": -87.6298},
        {"name": "Houston",     "lat": 29.7604, "lon": -95.3698},
        {"name": "Phoenix",     "lat": 33.4484, "lon":-112.0740},
        {"name": "Philadelphia","lat": 39.9526, "lon": -75.1652},
        {"name": "San Antonio", "lat": 29.4241, "lon": -98.4936},
        {"name": "Dallas",      "lat": 32.7767, "lon": -96.7970},
    ],
}


# ─────────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main frontend page."""
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():
    """
    Accepts a JSON body:
    {
        "cities"    : [{"name": "...", "lat": ..., "lon": ...}, ...],
        "algorithm" : "nearest_neighbor" | "held_karp" | "genetic" | "brute_force"
    }
    Returns optimized route + total distance as JSON.
    """
    data = request.get_json(force=True)

    cities    = data.get("cities", [])
    algorithm = data.get("algorithm", "nearest_neighbor")

    if not cities:
        return jsonify({"error": "No cities provided."}), 400
    if len(cities) < 2:
        return jsonify({"error": "At least 2 cities are required."}), 400

    result = solve(cities, algorithm)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 200


@app.route("/presets", methods=["GET"])
def presets():
    """
    Returns all preset city groups.
    Optional query param: ?group=india | europe | usa
    """
    group = request.args.get("group", "").lower()

    if group:
        if group not in PRESETS:
            return jsonify({"error": f"Unknown preset '{group}'. Choose from: {list(PRESETS.keys())}"}), 404
        return jsonify({"group": group, "cities": PRESETS[group]}), 200

    return jsonify({"presets": PRESETS}), 200


@app.route("/algorithms", methods=["GET"])
def algorithms():
    """Returns metadata about the 4 supported algorithms."""
    return jsonify({
        "algorithms": [
            {
                "id":          "nearest_neighbor",
                "name":        "Nearest Neighbor",
                "type":        "Greedy / Heuristic",
                "complexity":  "O(n²)",
                "description": "Always visits the closest unvisited city next. Fast but not always optimal."
            },
            {
                "id":          "held_karp",
                "name":        "Held-Karp DP",
                "type":        "Exact / Dynamic Programming",
                "complexity":  "O(n² × 2ⁿ)",
                "description": "Guarantees the optimal route using bitmask memoization. Expensive for large n."
            },
            {
                "id":          "genetic",
                "name":        "Genetic Algorithm",
                "type":        "Metaheuristic / Evolutionary",
                "complexity":  "O(gen × pop × n)",
                "description": "Evolves a population of routes using selection, crossover, and mutation."
            },
            {
                "id":          "brute_force",
                "name":        "Brute Force",
                "type":        "Exact / Exhaustive Search",
                "complexity":  "O(n!)",
                "description": "Tries every permutation to find the absolute shortest route. Limited to ≤10 cities."
            },
        ]
    }), 200


# ─────────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # debug=False in production (Render sets its own host/port via gunicorn)
    app.run(debug=True, host="0.0.0.0", port=5000)
