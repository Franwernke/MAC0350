-- Type: tipo_acesso

-- DROP TYPE public.tipo_acesso;

CREATE TYPE public.tipo_acesso AS ENUM
    ('Leitura', 'Alteracao', 'Escrita', 'Delecao');

-- Type: tipo_exame

-- DROP TYPE public.tipo_exame;

CREATE TYPE public.tipo_exame AS ENUM
    ('sanguineo', 'arsenico', 'Benzeno', 'Cádmio', 'Cariótipo', 'Tirosina', 'Urina');

-- Type: tipo_perfil

-- DROP TYPE public.tipo_perfil;

CREATE TYPE public.tipo_perfil AS ENUM
    ('Aluno', 'Enfermaria', 'Limpeza', 'Medico', 'Professor', 'Administrativo');

-- Type: tipo_servico

-- DROP TYPE public.tipo_servico;

CREATE TYPE public.tipo_servico AS ENUM
    ('Ler todos os exames', 'Ler um exame', 'Adicionar um exame', 'Adicionar usuario', 'Ler todos os usuarios', 
    'Alterar exame', 'Deletar paciente', 'Adicionar paciente', 'Solicitar exame');