CREATE TABLE monopoly_map (
  map_id INT NOT NULL AUTO_INCREMENT,
  map_name VARCHAR(255) NOT NULL,
  players INT NOT NULL,
  datetime_lastupdate DATETIME NOT NULL,
  creator VARCHAR(255),
  image_url VARCHAR(255),
  description TEXT,
  PRIMARY KEY (map_id)
);
