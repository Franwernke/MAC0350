-- Lista todos os exames realizados, com seus respectivos tipos, bem como os seus
-- pacientes com suas respectivas datas de solicitação e execução.

SELECT paciente.nome, exame.tipo, exame.virus, exame.data_solicitacao, exame.data_realizacao 
FROM ep2.possui
	INNER JOIN ep2.paciente ON paciente.cpf=possui.cpf
	INNER JOIN ep2.exame ON exame.codigo=possui.codigo_exame;

-- Liste os 5 exames realizados com maior eficiência (diferença entre data de execução e
-- data de solicitação). ready

SELECT exame.virus, exame.tipo, exame.data_solicitacao, exame.data_realizacao, 
		(data_realizacao - data_solicitacao) as dif_tempo 
FROM ep2.exame 
ORDER BY dif_tempo 
LIMIT 5;

-- Liste os serviços que podem ser utilizados por usuários tutelados para cada usuário
-- tutor.

SELECT DISTINCT usuario.nome as tutor, usuario_tutelado.nome, servico.tipo as servico
FROM ep2.realiza
	INNER JOIN ep2.perfil ON perfil.tipo=realiza.tipo_perfil
	INNER JOIN ep2.servico ON servico.codigo=realiza.codigo_servico
	INNER JOIN ep2.usuario_tutelado ON perfil.tipo=usuario_tutelado.tipo_perfil
	INNER JOIN ep2.usuario ON usuario_tutelado.cpf_tutor=usuario.cpf
ORDER BY usuario.nome;

-- Liste em ordem crescente o total de serviços utilizados agrupados pelos tipos de
-- serviços disponíveis e pelo perfil dos usuários.

SELECT servico.tipo as tipo_servico, perfil.tipo as tipo_perfil, COUNT(servico.tipo) as total
FROM ep2.acessa
    INNER JOIN ep2.servico ON servico.codigo=acessa.codigo_servico
	INNER JOIN ep2.perfil ON perfil.tipo=acessa.tipo_perfil
GROUP BY servico.tipo, perfil.tipo
ORDER BY total DESC;