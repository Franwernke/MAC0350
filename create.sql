-- Table: ep2.paciente

-- DROP TABLE ep2.paciente;

CREATE TABLE ep2.paciente
(
    data_de_nascimento date,
    nome character varying COLLATE pg_catalog."default" NOT NULL,
    cpf integer NOT NULL,
    endereco character varying COLLATE pg_catalog."default",
    CONSTRAINT paciente_pkey PRIMARY KEY (cpf),
    CONSTRAINT paciente_unique UNIQUE (cpf)
);

-- Table: ep2.usuario

-- DROP TABLE ep2.usuario

CREATE TABLE ep2.usuario
(
    cpf integer NOT NULL,
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
    horario timestamp with time zone NOT NULL,
    tipo ep2.tipo_acesso NOT NULL,
    cpf integer NOT NULL,
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
    cpf integer NOT NULL,
    data_da_coleta timestamp with time zone NOT NULL,
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
    cpf integer NOT NULL,
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
    cpf integer NOT NULL,
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
    cpf integer NOT NULL,
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
    cpf integer NOT NULL,
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
    cpf_tutor integer NOT NULL,
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