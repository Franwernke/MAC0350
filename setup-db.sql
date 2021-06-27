CREATE SCHEMA ep2;

-- Type: tipo_acesso

-- DROP TYPE ep2.tipo_acesso;

CREATE TYPE ep2.tipo_acesso AS ENUM
    ('Visualizacao', 'Alteracao', 'Insercao', 'Remocao');

-- Type: tipo_exame

-- DROP TYPE ep2.tipo_exame;

CREATE TYPE ep2.tipo_exame AS ENUM
    ('PCR', 'anticorpos');

-- Type: tipo_perfil

-- DROP TYPE ep2.tipo_perfil;

CREATE TYPE ep2.tipo_perfil AS ENUM
    ('Aluno', 'Pesquisador', 'Funcionario', 'Usuario comum', 'Eventuais', 'Administrador');

-- Type: tipo_servico

-- DROP TYPE ep2.tipo_servico;

CREATE TYPE ep2.tipo_servico AS ENUM
    ('Solicitar exames', 'Inserir exames', 'Consultar exames');

-- Table: ep2.paciente

-- DROP TABLE ep2.paciente;

CREATE TABLE ep2.paciente
(
    data_de_nascimento date,
    nome character varying COLLATE pg_catalog."default" NOT NULL,
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    endereco character varying COLLATE pg_catalog."default",
    CONSTRAINT paciente_pkey PRIMARY KEY (cpf),
    CONSTRAINT paciente_unique UNIQUE (cpf)
);

-- Table: ep2.usuario

-- DROP TABLE ep2.usuario

CREATE TABLE ep2.usuario
(
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    nome character varying COLLATE pg_catalog."default" NOT NULL,
    endereco character varying COLLATE pg_catalog."default",
    instituicao character varying COLLATE pg_catalog."default",
    data_de_nascimento date,
    login character varying COLLATE pg_catalog."default" NOT NULL,
    senha character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (cpf),
    CONSTRAINT usuario_unique UNIQUE (cpf)
);



-- Table: ep2.servico

-- DROP TABLE ep2.servico;

CREATE TABLE ep2.servico
(
    codigo integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
    tipo ep2.tipo_servico NOT NULL,
    descricao character varying COLLATE pg_catalog."default",
    CONSTRAINT servico_pkey PRIMARY KEY (codigo),
    CONSTRAINT servico_unique UNIQUE (codigo)
);


-- Table: ep2.acessa

-- DROP TABLE ep2.acessa;

CREATE TABLE ep2.acessa
(
    horario timestamp without time zone NOT NULL,
    tipo ep2.tipo_acesso NOT NULL,
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    codigo_servico integer NOT NULL,
    CONSTRAINT acessa_pkey PRIMARY KEY (cpf, codigo_servico, horario),
    CONSTRAINT acessa_unique UNIQUE (cpf, codigo_servico, horario),
    CONSTRAINT acessa_servico_fkey FOREIGN KEY (codigo_servico)
        REFERENCES ep2.servico (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT acessa_usuario_fkey FOREIGN KEY (cpf)
        REFERENCES ep2.usuario (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Table: ep2.amostra

-- DROP TABLE ep2.amostra;

CREATE TABLE ep2.amostra
(
    codigo integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    data_da_coleta timestamp without time zone NOT NULL,
    tipo_de_material character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT amostra_pk PRIMARY KEY (cpf, codigo),
    CONSTRAINT amostra_codigo_unique UNIQUE (codigo),
    CONSTRAINT amostra_unique UNIQUE (cpf, codigo),
    CONSTRAINT amostra_fk FOREIGN KEY (cpf)
        REFERENCES ep2.paciente (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Table: ep2.area_de_pesquisa

-- DROP TABLE ep2.area_de_pesquisa;

CREATE TABLE ep2.area_de_pesquisa
(
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    area character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT area_de_pesquisa_pkey PRIMARY KEY (cpf, area),
    CONSTRAINT area_de_pesquisa_unique UNIQUE (cpf, area),
    CONSTRAINT area_de_pesquisa_fkey FOREIGN KEY (cpf)
        REFERENCES ep2.usuario (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Table: ep2.exame

-- DROP TABLE ep2.exame;

CREATE TABLE ep2.exame
(
    codigo integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
    virus character varying COLLATE pg_catalog."default" NOT NULL,
    tipo ep2.tipo_exame NOT NULL,
    data_solicitacao timestamp without time zone NOT NULL,
    data_realizacao timestamp without time zone,
    CONSTRAINT exame_pkey PRIMARY KEY (codigo),
    CONSTRAINT exame_unique UNIQUE (codigo)
);

-- Table: ep2.outros_dados_amostra

-- DROP TABLE ep2.outros_dados_amostra;

CREATE TABLE ep2.outros_dados_amostra
(
    dado character varying COLLATE pg_catalog."default" NOT NULL,
    codigo_amostra integer NOT NULL,
    CONSTRAINT outros_dados_amostra_pkey PRIMARY KEY (dado, codigo_amostra),
    CONSTRAINT outros_dados_amostra_unique UNIQUE (codigo_amostra, dado),
    CONSTRAINT outros_dados_amostra_fkey FOREIGN KEY (codigo_amostra)
        REFERENCES ep2.amostra (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Table: ep2.outros_dados_paciente

-- DROP TABLE ep2.outros_dados_paciente;

CREATE TABLE ep2.outros_dados_paciente
(
    dado character varying COLLATE pg_catalog."default" NOT NULL,
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT outros_dados_paciente_pkey PRIMARY KEY (dado, cpf),
    CONSTRAINT outros_dados_paciente_unique UNIQUE (dado, cpf),
    CONSTRAINT outros_dados_paciente_fkey FOREIGN KEY (cpf)
        REFERENCES ep2.paciente (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);



-- Table: ep2.perfil

-- DROP TABLE ep2.perfil;

CREATE TABLE ep2.perfil
(
    tipo ep2.tipo_perfil NOT NULL,
    CONSTRAINT perfil_pkey PRIMARY KEY (tipo),
    CONSTRAINT perfil_unique UNIQUE (tipo)
);

-- Table: ep2.possui

-- DROP TABLE ep2.possui;

CREATE TABLE ep2.possui
(
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    codigo_exame integer NOT NULL,
    codigo_amostra integer,
    CONSTRAINT possui_pkey PRIMARY KEY (cpf, codigo_exame),
    CONSTRAINT possui_unique UNIQUE (cpf, codigo_exame, codigo_amostra),
    CONSTRAINT possui_amostra_fkey FOREIGN KEY (codigo_amostra)
        REFERENCES ep2.amostra (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT possui_exame_fkey FOREIGN KEY (codigo_exame)
        REFERENCES ep2.exame (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT possui_paciente_fkey FOREIGN KEY (cpf)
        REFERENCES ep2.paciente (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Table: ep2.possui_um

-- DROP TABLE ep2.possui_um;

CREATE TABLE ep2.possui_um
(
    cpf character varying COLLATE pg_catalog."default" NOT NULL,
    tipo_perfil ep2.tipo_perfil NOT NULL,
    CONSTRAINT possui_um_pkey PRIMARY KEY (cpf, tipo_perfil),
    CONSTRAINT possui_um_unique UNIQUE (cpf, tipo_perfil),
    CONSTRAINT possui_um_perfil_fkey FOREIGN KEY (tipo_perfil)
        REFERENCES ep2.perfil (tipo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT possui_um_usuario_fkey FOREIGN KEY (cpf)
        REFERENCES ep2.usuario (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Table: ep2.realiza

-- DROP TABLE ep2.realiza;

CREATE TABLE ep2.realiza
(
    tipo_perfil ep2.tipo_perfil NOT NULL,
    codigo_servico integer NOT NULL,
    CONSTRAINT realiza_pkey PRIMARY KEY (tipo_perfil, codigo_servico),
    CONSTRAINT realiza_unique UNIQUE (tipo_perfil, codigo_servico),
    CONSTRAINT realiza_perfil_fkey FOREIGN KEY (tipo_perfil)
        REFERENCES ep2.perfil (tipo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT realiza_servico_fkey FOREIGN KEY (codigo_servico)
        REFERENCES ep2.servico (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);


-- Table: ep2.usuario_tutelado

-- DROP TABLE ep2.usuario_tutelado;

CREATE TABLE ep2.usuario_tutelado
(
    nome character varying COLLATE pg_catalog."default" NOT NULL,
    cpf_tutor character varying COLLATE pg_catalog."default" NOT NULL,
    codigo_servico integer NOT NULL,
    CONSTRAINT usuario_tutelado_pkey PRIMARY KEY (nome, cpf_tutor, codigo_servico),
    CONSTRAINT usuario_tutelado_unique UNIQUE (nome, cpf_tutor, codigo_servico),
    CONSTRAINT codigo_servico_fkey FOREIGN KEY (codigo_servico)
        REFERENCES ep2.servico (codigo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT usuario_fkey FOREIGN KEY (cpf_tutor)
        REFERENCES ep2.usuario (cpf) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

INSERT INTO ep2.paciente (data_de_nascimento, nome, cpf, endereco)
VALUES 
('1993-07-22', 'Lance Tucker', '26235437836', '809 Hooper Road Suite 759\nCarterchester, KS 21429'),
('1998-01-06', 'Kathleen Gardner', '90424667526', '835 Kristin Turnpike\nMatthewfort, MT 13893'),
('1997-02-16', 'Crystal Johnson', '47577707087', '8458 Tiffany Flat Apt. 137\nNorth Cindystad, KS 06498'),
('1990-04-06', 'April Casey', '66675800178', '96946 Brian Valleys Apt. 344\nEast Karenside, WI 26460'),
('2001-04-16', 'Ruth Coleman', '74437328370', '6225 Kevin Isle\nLake Marymouth, WV 69311'),
('1982-10-18', 'Katherine Reynolds', '64475669389', '3022 Melton Islands\nNew Kimberlyborough, NE 55731');


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

INSERT INTO ep2.perfil (tipo)
VALUES 
('Aluno'), 
('Pesquisador'), 
('Funcionario'), 
('Usuario comum'), 
('Eventuais'), 
('Administrador');

INSERT INTO ep2.servico (tipo, descricao)
VALUES 
('Solicitar exames', 'Pedir a realização de um exame periódico.'),
('Inserir exames', 'Postar o resultado de um exame.' ),
('Consultar exames','Visualizar um exame.' );