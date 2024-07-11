-- COUNT --

SELECT COUNT(*) AS total_usuarios FROM usuarios;

SELECT COUNT(*) AS total_usuarios FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario

-- MAX -- 

SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade
FROM usuarios;

-- Agrupamento de Resultados --

INSERT INTO reservas(id_usuario, id_destino) VALUES (1, 3);

SELECT COUNT(*) AS quantidade_reservas, id_destino FROM reservas
GROUP BY id_destino;

-- Ordenação de Resultados --

SELECT COUNT(*) AS quantidade_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY quantidade_reservas DESC, id_destino ASC