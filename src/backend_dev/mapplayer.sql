CREATE TABLE map_player (
  player_id INT NOT NULL,
  map_id INT NOT NULL,
  map_coordinate_x INT NOT NULL,
  map_coordinate_y INT NOT NULL,
  map_coordinate_z INT NOT NULL,
  map_square VARCHAR(20),
  playr_inJail,
  player_status VARCHAR(20),
  player_cycle VARCHAR(20),
  datetime_lastupdate,
  PRIMARY KEY (player_id, map_id, property_name),
  FOREIGN KEY (player_id) REFERENCES player(player_id),
  FOREIGN KEY (map_id) REFERENCES monopoly_map(map_id)
);
