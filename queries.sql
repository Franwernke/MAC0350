-- Lista todos os exames realizados, com seus respectivos tipos, bem como os seus
-- usuários com suas respectivas datas de solicitação e execução.

SELECT possui.cpf, exame.tipo, acessa.horario, amostra.data_da_coleta
FROM possui
WHERE acessa.tipo='Solicitar exame';

-- Liste os 5 exames realizados com maior eficiência (diferença entre data de execução e
-- data de solicitação).

-- Liste os serviços que podem ser utilizados por usuários tutelados para cada usuário
-- tutor.

-- Liste em ordem crescente o total de serviços utilizados agrupados pelos tipos de
-- serviços disponíveis e pelo perfil dos usuários.