#!/bin/bash

mysql -u root --password=""  << EOF
USE ${DB_NAME};
SHOW DATABASES;
GRANT ALL PRIVILEGES ON  test_${DB_NAME}.* TO '${DB_USER}';
EOF


