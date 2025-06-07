-- schema.sql
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS trails;
DROP TABLE IF EXISTS modules;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'learner' -- 'learner' ou 'volunteer'
);

CREATE TABLE trails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    difficulty TEXT, -- 'Iniciante', 'Intermediário', 'Avançado'
    creator_id INTEGER,
    FOREIGN KEY (creator_id) REFERENCES users (id)
);

CREATE TABLE modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trail_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT, -- Pode ser Markdown ou HTML
    FOREIGN KEY (trail_id) REFERENCES trails (id)
);

-- Inserir um usuário voluntário para testes
INSERT INTO users (username, password, role) VALUES ('voluntario1', 'senha123', 'volunteer');
-- Inserir um usuário aprendiz para testes
INSERT INTO users (username, password, role) VALUES ('aprendiz1', 'senha456', 'learner');