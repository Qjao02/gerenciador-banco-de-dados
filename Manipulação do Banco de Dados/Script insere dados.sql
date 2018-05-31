USE `DBBANCO`;
SET SQL_SAFE_UPDATES = 0;
SET foreign_key_checks = 0;
--
--
DELETE FROM agencia;
INSERT INTO agencia(endereco, nome)
	VALUES("Mensalão Tucano", "Agencia Petrobras");
INSERT INTO agencia(endereco, nome)
	VALUES("2000", "Caixa Federal");
INSERT INTO agencia(endereco, nome)
	VALUES("2001", "Caixa Federal Interior");
-- SELECT * FROM agencia;
--
DELETE FROM administrador;
INSERT INTO administrador(login, senha, agencia)
	VALUES("Test0", "test0", (SELECT id FROM agencia WHERE nome="Agencia Petrobras"));
-- SELECT * FROM administrador;
--
DELETE FROM cliente;
INSERT INTO cliente(cadastroDatetime, endereco, nome)
	VALUES(NOW(), "Avenida Paulista, 221, Belo Horizonte, Minas Gerais", "Jeremias de Alagoas");
-- SELECT * FROM cliente;
--
DELETE FROM fisico;
INSERT INTO fisico(cpf, cliente)
	VALUES("44255256261", (SELECT id FROM cliente WHERE nome="Jeremias de Alagoas"));
-- SELECT * FROM fisico;
--
DELETE FROM juridico;
INSERT INTO juridico(cnpj, cliente)
	VALUES("44255256261777", (SELECT id FROM cliente WHERE nome="Jeremias de Alagoas"));
-- SELECT * FROM juridico;
--
DELETE FROM operacao;
INSERT INTO operacao(operacao, fisico, fisicoCPF)
	VALUES(13, (SELECT id FROM fisico WHERE cpf="44255256261"), (SELECT cpf FROM fisico WHERE cpf="44255256261"));
--
INSERT INTO conta(conta, cadastroDatetime, senha, saldo, operacao)
	VALUES("123456789", NOW(), "password", 1500, (SELECT id FROM operacao WHERE operacao=13));
--
--
SET SQL_SAFE_UPDATES = 1;
SET foreign_key_checks = 1;