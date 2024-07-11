-- Interseccção (dados comuns) --

SELECT * FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario
INNER JOIN destinos ds ON rs.id_destino = ds.id;

-- Left Join --

INSERT INTO usuarios (nome, email, data_nascimento, rua, numero, cidade, estado)
VALUES ('sem reserva', 'dio@teste.com', '1992-05-05', 'rua', '12', 'cidade', 'estado');

SELECT * FROM usuarios us
LEFT JOIN reservas rs ON us.id = rs.id_usuario

-- Rigth Join --

INSERT INTO destinos (nome, descricao) VALUES ('Destino sem reservas', 'Descricao');

SELECT * FROM reservas rs
RIGHT JOIN destinos ds
ON rs.id_destino = ds.id

-- SubConsultas --
-- Consulta aninhada --

SELECT * FROM destinos
WHERE id NOT IN (SELECT id_destino FROM reservas);

SELECT * FROM usuarios
WHERE id NOT IN (SELECT id_usuario FROM reservas);

-- Criar nova coluna --

SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas FROM usuarios;