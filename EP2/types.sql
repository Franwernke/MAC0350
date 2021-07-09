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