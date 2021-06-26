-- Table: public.acessa

-- DROP TABLE public.acessa;

CREATE TABLE public.acessa
(
    horario timestamp with time zone NOT NULL,
    tipo tipo_acesso NOT NULL,
    cpf integer NOT NULL,
    codigo_servico integer NOT NULL,
    CONSTRAINT acessa_pkey PRIMARY KEY (cpf, codigo_servico)
)

-- Table: public.amostra

-- DROP TABLE public.amostra;

CREATE TABLE public.amostra
(
    codigo integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
    cpf integer NOT NULL,
    data_da_coleta date NOT NULL,
    tipo_de_material character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT amostra_pk PRIMARY KEY (cpf, codigo)
)

