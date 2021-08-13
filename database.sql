-- Crear y cargar Tabla a mysql

-- DROP TABLE datos;
CREATE TABLE `datos` (
    `id` VARCHAR(50) NOT NULL,
    `company_name` VARCHAR(50) NULL,
    `company_id` VARCHAR(50) NOT NULL ,
    `amount` DECIMAL(16,2) NOT NULL,
    `status` VARCHAR(50) NOT NULL,
    `created_at` TIMESTAMP NOT NULL,
    `updated_at` TIMESTAMP NULL,
    PRIMARY KEY (`id`)
);

LOAD DATA LOCAL INFILE "/home/ojitos369/Documentos/Progra/Prueba_Tecnica/data_prueba_tecnica.csv" 
    INTO TABLE datos
    FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '\\'
    LINES TERMINATED BY '\n';

/* select * from datos limit 10;

select * from datos where (amount=66.16 and status='pending_payment'); */


-- Tablas para PosgreSQL

CREATE TABLE companies (
    id VARCHAR(50) NOT NULL,
    name VARCHAR(50) NULL,
    PRIMARY KEY (id)
);

CREATE TABLE status (
    id INT NOT NULL,
    state VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE charges (
    id VARCHAR(50) NOT NULL,
    company_id VARCHAR(50) NOT NULL,
    amount DECIMAL(16,2) NOT NULL,
    status_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES companies(id),
    FOREIGN KEY (status_id) REFERENCES status(id)
);
