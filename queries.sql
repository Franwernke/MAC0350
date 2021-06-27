-- Lista todos os exames realizados, com seus respectivos tipos, bem como os seus
-- pacientes com suas respectivas datas de solicitação e execução.

SELECT paciente.cpf, exame.tipo, exame.data_solicitacao, exame.data_realizacao 
FROM ep2.possui
	INNER JOIN ep2.paciente ON paciente.cpf=possui.cpf
	INNER JOIN ep2.exame ON exame.codigo=possui.codigo_exame;

-- Liste os 5 exames realizados com maior eficiência (diferença entre data de execução e
-- data de solicitação). ready

SELECT *, (data_realizacao - data_solicitacao) as timeDiff 
FROM ep2.exame ORDER BY timeDiff LIMIT 5;

-- Liste os serviços que podem ser utilizados por usuários tutelados para cada usuário
-- tutor.

SELECT usuario.nome, usuario.cpf, usuario_tutelado.nome, servico.tipo
FROM usuario, servico, usuario_tutelado
WHERE 

-- Liste em ordem crescente o total de serviços utilizados agrupados pelos tipos de
-- serviços disponíveis e pelo perfil dos usuários.