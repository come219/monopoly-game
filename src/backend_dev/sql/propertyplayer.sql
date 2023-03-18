CREATE TABLE player_property (
  player_id INT NOT NULL,
  map_id INT NOT NULL,
  stand_id INT NOT NULL,
  isRent BOOLEAN,
  isBuy BOOLEAN,
  property_name VARCHAR(255) NOT NULL,
  property_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (player_id, map_id, property_name),
  FOREIGN KEY (player_id) REFERENCES player(player_id),
  FOREIGN KEY (map_id) REFERENCES monopoly_map(map_id)
);
