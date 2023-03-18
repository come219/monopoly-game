CREATE TABLE monopoly_map_v1 (
  map_id INT NOT NULL AUTO_INCREMENT,
  map_name VARCHAR(255) NOT NULL,
  players INT NOT NULL,
  datetime_lastupdate DATETIME NOT NULL,
  PRIMARY KEY (map_id)
);
