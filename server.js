const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());

// ✅ THIS LINE FIXES YOUR PROBLEM
app.use(express.static(__dirname));

// API
app.get('/geocode', async (req, res) => {
  const city = req.query.city;

  const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(city)}&limit=1`;

  const response = await fetch(url, {
    headers: {
      'User-Agent': 'MyApp/1.0',
      'Accept-Language': 'en'
    }
  });

  const data = await response.json();

  if (data.length === 0) return res.json(null);

  res.json({
    lat: parseFloat(data[0].lat),
    lng: parseFloat(data[0].lon)
  });
});

// serve main page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(3000, '0.0.0.0', () => {
  console.log('Server running...');
});