const mysql = require('mysql');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Parse incoming request bodies as JSON
app.use(bodyParser.json());


// Index page/route
app.get('/', (req, res) => {
  res.send('Welcome to my app!');
});





// Create a MySQL connection pool
const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'root',
  password: '1337',
  database: 'lstand_monopoly_v1'
});


// Create account route
app.post('/accounts', (req, res) => {
  // Extract account information from request body
  const { player_name, player_email, player_password } = req.body;

  // Get a connection from the pool
  pool.getConnection((err, connection) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: 'Internal Server Error' });
    }

    // Check if username or email is already in use
    const checkQuery = 'SELECT * FROM player_v1 WHERE player_name = ? OR player_email = ?';
    connection.query(checkQuery, [player_name, player_email], (err, rows) => {
      if (err) {
        console.error(err);
        return res.status(500).json({ error: 'Internal Server Error' });
      }

      // If a row with the same username or email exists, return an error
      if (rows.length > 0) {
        return res.status(400).json({ error: 'Username (name) or email is already in use' });
      }

      // Insert new account into the database
      const insertQuery = 'INSERT INTO player_v1 (player_name, player_email, player_password) VALUES (?, ?, ?)';
      connection.query(insertQuery, [player_name, player_email, player_password], (err, result) => {
        // Release the connection back to the pool
        connection.release();

        if (err) {
          console.error(err);
          return res.status(500).json({ error: 'Internal Server Error' });
        }

        // Return success message and ID of new account
        res.json({ message: 'Account created successfully', accountId: result.insertId });
      });
    });
  });
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
    const sql = 'SELECT id, name FROM monopoly_map_v1 WHERE id = ?';
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
      res.json(map);
    });
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

