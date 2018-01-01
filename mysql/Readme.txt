pip3 install pymysql
pip3 install SQLAlchemy

pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

CREATE TABLE user (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(32),
    password VARCHAR(64),
    PRIMARY KEY (id)
)

