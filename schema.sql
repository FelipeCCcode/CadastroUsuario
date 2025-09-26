-- Apaga a tabela se ela já existir, para podermos recriá-la do zero.
DROP TABLE IF EXISTS user;

-- Cria a tabela de usuários.
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE
);

