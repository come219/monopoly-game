const mysql = require('mysql');
const express = require('express');

const app = express();

// Create a MySQL connection pool
const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'your_database_host',
  user: 'your_database_user',
  password: 'your_database_password',
  database: 'your_database_name'
});

// Define a route to handle GET requests with a map ID parameter
app.get('/maps/:id', (req, res) => {
  // Get a connection from the pool
  pool.getConnection((err, connection) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Internal Server Error' });
    }

    // Perform a query to select map details based on the ID parameter
    const sql = 'SELECT * FROM maps WHERE id = ?';
    const id = req.params.id;
    connection.query(sql, [id], (err, rows) => {
      // Release the connection back to the pool
      connection.release();

      if (err) {
        console.error(err);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // Check if a map was found
      if (rows.length === 0) {
        return res.status(404).json({ error: 'Map not found' });
      }

      // Return the map details as JSON
      const map = rows[0];
      res.json({
        id: map.id,
        name: map.name,
        description: map.description,
        image_url: map.image_url,
        // Add any other details you want to return
      });
    });
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
