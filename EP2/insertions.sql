INSERT INTO ep2.paciente (data_de_nascimento, nome, cpf, endereco)
VALUES 
('1993-07-22', 'Lance Tucker', '26235437836', '809 Hooper Road Suite 759\nCarterchester, KS 21429'),
('1998-01-06', 'Kathleen Gardner', '90424667526', '835 Kristin Turnpike\nMatthewfort, MT 13893'),
('1997-02-16', 'Crystal Johnson', '47577707087', '8458 Tiffany Flat Apt. 137\nNorth Cindystad, KS 06498'),
('1990-04-06', 'April Casey', '66675800178', '96946 Brian Valleys Apt. 344\nEast Karenside, WI 26460'),
('2001-04-16', 'Ruth Coleman', '74437328370', '6225 Kevin Isle\nLake Marymouth, WV 69311'),
('1982-10-18', 'Katherine Reynolds', '64475669389', '3022 Melton Islands\nNew Kimberlyborough, NE 55731');

INSERT INTO ep2.outros_dados_paciente (dado, cpf)
VALUES
('Chegou atrasado 3 vezes semana passada', '90424667526'),
('Altura: 1.52m', '64475669389'),
('Peso: 150kg', '26235437836');


INSERT INTO ep2.exame (virus, tipo, data_solicitacao, data_realizacao) 
VALUES 
('COVID-19', 'PCR', '2021-06-04 09:11:40', '2021-06-12 07:24:37'),
('H1N1', 'PCR', '2021-06-16 03:24:49', '2021-06-25 00:30:58'),
('herpesvirus', 'PCR', '2021-06-05 03:46:04', '2021-06-14 19:30:10'),
('HIV', 'PCR', '2021-06-04 12:31:08', '2021-06-11 01:44:11'),
('DENV', 'anticorpos', '2021-06-11 02:27:21', '2021-06-26 15:42:30'),
('COVID-22', 'anticorpos', '2021-06-11 23:21:11', '2021-06-17 19:15:40'),
('ZAPVIRUS', 'anticorpos',  '2021-05-31 10:00:48', '2021-06-13 23:16:26');

INSERT INTO ep2.amostra (cpf, data_da_coleta, tipo_de_material)
VALUES 
('26235437836', '2021-06-05 09:11:40', 'a'),
('26235437836', '2021-06-17 03:24:49', 'b'),
('90424667526', '2021-06-06 03:46:04', 'c'),
('47577707087', '2021-06-05 12:31:08', 'd'),
('66675800178', '2021-06-12 02:27:21', 'e'),
('74437328370', '2021-06-12 23:21:11', 'f');

INSERT INTO ep2.outros_dados_amostra 
VALUES
('Coco com sangue', 2),
('Alta concentração de potássio', 4);

INSERT INTO ep2.possui (cpf, codigo_exame, codigo_amostra)
VALUES
('26235437836', 0, 0),
('26235437836', 1, 1),
('90424667526', 2, 2),
('47577707087', 3, 3),
('66675800178', 4, 4),
('74437328370', 5, 5),
('64475669389', 6, null);

INSERT INTO ep2.usuario (cpf, nome, endereco, instituicao, data_de_nascimento, login, senha)
VALUES 
('65745289213', 'Kimberly Williamson', 'USCGC Adams\nFPO AE 55753', 'UFMG', '1984-04-14', 'Kiwi', '6574'),
('57831064721', 'Thomas Barker', '1344 Acosta Place Suite 478\nNorth Holly, AL 43486', 'USP', '1988-03-10', 'Thom', 'MarleyEEu'),
('18152004253', 'Dawn Ray', '1071 Susan Harbors\nWest Lisamouth, AR 16933', 'USP', '1986-09-24', 'Dawn', 'DontLetmMeDawn25'),
('47448675230', 'Jessica Wells', '516 Baker Lane\nLawsonmouth, ID 32571', 'Hospital Albert Einstein', '1974-01-05', 'Jess', 'HenryCavillLindo'),
('71226266546', 'Jason Moss', '31825 Joseph Fort\nMccoystad, TN 26646', '', '1992-01-10', 'Jas', 'EJas239'),
('77823177937', 'Emma Hester', '2103 Molina Valley\nBenjaminbury, MD 03040', 'UFBA', '1981-12-02', 'Emminha', 'ViniciusBonitao'),
('89011513206', 'Stefanie Smith', '2619 Mcdonald Coves Apt. 417\nMarkstad, NE 20662', '', '1986-08-25', 'Steeeh2009', 'FranciscoLindo');

INSERT INTO ep2.area_de_pesquisa (area, cpf)
VALUES 
('Oncologia', '65745289213'),
('Dermatologia', '57831064721'),
('Pediatria', '18152004253'),
('Oftamologia', '77823177937'),
('Citologia', '89011513206');

INSERT INTO ep2.perfil (tipo)
VALUES 
('Aluno'), 
('Pesquisador'), 
('Funcionario'), 
('Usuario comum'), 
('Eventuais'), 
('Administrador'),
('Aluno tutelado'),
('Pesquisador tutelado'),
('Funcionario tutelado'), 
('Usuario comum tutelado'),
('Eventuais tutelado'), 
('Administrador tutelado');

INSERT INTO ep2.usuario_tutelado(nome, cpf_tutor, tipo_perfil)
VALUES 
('Bailey Mcdonald', '18152004253', 'Funcionario tutelado'),
('Nicole Hogan', '18152004253', 'Funcionario tutelado'),
('Lance Vasquez', '89011513206', 'Usuario comum tutelado'),
('Justin Rhodes', '65745289213', 'Pesquisador tutelado'),
('Shawn Johnson', '47448675230', 'Administrador tutelado');

INSERT INTO ep2.servico (tipo, descricao)
VALUES 
('Solicitar exames', 'Pedir a realização de um exame periódico.'),
('Inserir exames', 'Postar o resultado de um exame.'),
('Consultar exames','Visualizar um exame.');

INSERT INTO ep2.realiza (tipo_perfil, codigo_servico)
VALUES
('Aluno', 2),
('Pesquisador', 2),
('Pesquisador', 0),
('Funcionario', 0),
('Funcionario', 2),
('Funcionario', 1),
('Usuario comum', 0),
('Eventuais', 0),
('Administrador', 0),
('Administrador', 2),
('Administrador', 1),
('Aluno tutelado', 2),
('Pesquisador tutelado', 2),
('Funcionario tutelado', 2),
('Administrador tutelado', 0),
('Administrador tutelado', 2);

INSERT INTO ep2.possui_um (cpf, tipo_perfil)
VALUES 
('65745289213', 'Pesquisador'),
('57831064721', 'Aluno'),
('18152004253', 'Funcionario'),
('47448675230', 'Administrador'),
('71226266546', 'Eventuais'),
('77823177937', 'Pesquisador'),
('89011513206', 'Usuario comum');

INSERT INTO ep2.acessa (horario, cpf, codigo_servico, tipo_perfil)
VALUES 
('2021-06-04 09:11:40', '65745289213', 0, 'Pesquisador'), 
('2021-06-16 03:24:49', '57831064721', 0, 'Aluno'),
('2021-06-05 03:46:04', '18152004253', 0, 'Funcionario'),
('2021-06-04 12:31:08', '47448675230', 0, 'Administrador'),
('2021-06-11 02:27:21', '71226266546', 0, 'Eventuais'),
('2021-06-11 23:21:11', '77823177937', 0, 'Pesquisador'),
('2021-05-31 10:00:48', '89011513206', 0, 'Usuario comum'),

('2021-06-12 07:24:37', '47448675230', 1, 'Administrador'),
('2021-06-25 00:30:58', '47448675230', 1, 'Administrador'),
('2021-06-14 19:30:10', '47448675230', 1, 'Administrador'),
('2021-06-11 01:44:11', '77823177937', 1, 'Pesquisador'),
('2021-06-26 15:42:30', '77823177937', 1, 'Pesquisador'),
('2021-06-17 19:15:40', '77823177937', 1, 'Pesquisador'),
('2021-06-13 23:16:26', '77823177937', 1, 'Pesquisador'),

('2021-06-12 11:32:40', '57831064721', 2, 'Aluno'),
('2021-06-13 13:16:26', '57831064721', 2, 'Aluno');