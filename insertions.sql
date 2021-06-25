INSERT INTO acessa (horario, tipo)
VALUES (horario, tipo);

INSERT INTO amostra (cpf, data_da_coleta, tipo_de_material)
VALUES (cpf, data_da_coleta, tipo_de_material);

INSERT INTO area_de_pesquisa (area, cpf)
VALUES (area, cpf);

INSERT INTO exame (virus, tipo) VALUES (virus, tipo);

INSERT INTO outros_dados_amostra VALUES (dado, codigo_amostra);

INSERT INTO perfil (tipo)
VALUES (tipo);

INSERT INTO usuario (cpf, nome, endereco, instituicao, data_de_nascimento, login, senha)
VALUES (cpf, nome, endereco, instituicao, data_de_nascimento, login, senha);

INSERT INTO usuario_tutelado(nome, cpf_tutor)
VALUES (nome, cpf_tutor);

INSERT INTO paciente (data_de_nascimento, nome, cpf, endereco)
VALUES (data_de_nascimento, nome, cpf, endereco);

INSERT INTO outros_dados_paciente (dado, cpf)
VALUES (dado, cpf);

INSERT INTO possui (cpf, codigo_exame, codigo_amostra)
VALUES (cpf, codigo_exame, codigo_amostra);