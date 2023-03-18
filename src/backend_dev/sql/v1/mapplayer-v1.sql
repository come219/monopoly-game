CREATE TABLE map_player (
  player_id INT NOT NULL,
  map_id INT NOT NULL,
  map_coordinate_x INT NOT NULL,
  map_coordinate_y INT NOT NULL,
  map_coordinate_z INT NOT NULL,
  map_square VARCHAR(20) NOT NULL,
  player_in_jail BOOLEAN,
  player_status VARCHAR(20),
  player_cycle VARCHAR(20),
  datetime_lastupdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (player_id, map_id),
  FOREIGN KEY (player_id) REFERENCES player_v1(player_id),
  FOREIGN KEY (map_id) REFERENCES monopoly_map_v1(map_id)
);
