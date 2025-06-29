-- Таблица стран
CREATE TABLE countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL
);

-- Таблица услуг
CREATE TABLE services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    service_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Таблица клиентов
CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100),
    email VARCHAR(100)
);

-- Таблица туров
CREATE TABLE tours (
    tour_id INT PRIMARY KEY AUTO_INCREMENT,
    tour_name VARCHAR(100),
    country_id INT,
    service_id INT,
    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Таблица заказов (переменная информация)
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT,
    tour_id INT,
    order_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id)
);
