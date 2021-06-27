-- Lista todos os exames realizados, com seus respectivos tipos, bem como os seus
-- usuários com suas respectivas datas de solicitação e execução.

SELECT paciente.cpf, exame.tipo, acessa.horario, amostra.data_da_coleta
FROM paciente
WHERE acessa.tipo='Solicitar exame';

-- Liste os 5 exames realizados com maior eficiência (diferença entre data de execução e
-- data de solicitação).

SELECT *
FROM exame
ORDER BY amostra.data_da_coleta - acessa.horario 
WHERE acessa.tipo='Solicitar exame', acessa.cpf=amostra.cpf
LIMIT 5;

-- Liste os serviços que podem ser utilizados por usuários tutelados para cada usuário
-- tutor.

SELECT usuario.nome, usuario.cpf, usuario_tutelado.nome, servico.tipo
FROM usuario, servico, usuario_tutelado
WHERE 

-- Liste em ordem crescente o total de serviços utilizados agrupados pelos tipos de
-- serviços disponíveis e pelo perfil dos usuários.