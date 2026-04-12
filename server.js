const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');

const app = express();
app.use(cors());

// API endpoint
app.get('/geocode', async (req, res) => {
  const city = req.query.city;

  if (!city) {
    return res.status(400).json({ error: 'City required' });
  }

  try {
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(city)}&limit=1`;

    const response = await fetch(url, {
      headers: {
        'User-Agent': 'MyApp/1.0 (student project)',
        'Accept-Language': 'en'
      }
    });

    const data = await response.json();

    if (data.length === 0) {
      return res.json(null);
    }

    res.json({
      lat: parseFloat(data[0].lat),
      lng: parseFloat(data[0].lon)
    });

  } catch (err) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});