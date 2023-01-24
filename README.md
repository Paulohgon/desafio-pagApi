# Desafio Transfeera

## Problema
Criar um gerenciador de pagamentos

##  Tecnologias ulitizadas
- Python3
- Sqlite
- FastAPI

## Aquitetura e características
Foi escolhido um princípio de clean arch, a própria clean arch seria demais para um projeto pequeno como esse, então fora utilizado parte da modularização de código proposta pelo clean arch. Ponto como, usecases, foram ignorados. Além disso, todas as deleções são realizadas com softdelete.


## Problemas conhecidos
Por conta do tempo, proposto por mim, e por conta da minha especialidade, back-end, não foi implementado um front-end no projeto. Além disso, não houve muita preocupação com a segurança do código, estando passível de um possivel sqlinjection. Porém resolver esses problemas para um projeto pequeno e que nao ficará exposto tomaria muito tempo. Também foi escolhido um banco simples, sqlite, que supre as necessidades e facilita o desenvolvimento de protótipos como este. Para um grande projeto deveria ser usado postgrees, que possibilitaria realizar validações no próprio banco. Não foi escolhido o postgrees pois houve um foco maior em velocidade nesse projeto, então qualquer obstáculo que pudesse ser facilitado, foi facilitado.

## Tempo de desenvolvimento
Foi utilizado em média 4 a 5 horas por dia durante 14 dias para o desenvolvimento. Houveram dias onde não houve evolução ou mudança no código por motivos externos. Por exemplo nos finais de semana que tiveram viagens. Com isso foi utilizado o equivalente a 1 semana de trabalho de 8 horas em média.

## Instalar projeto
Clonar o projeto em sua máquina

Com python3 instalado faça instalações das bibliotecas do projeto

- pip install requirements.txt

Após instalado, use o makefile para rodar o projeto com o comando:

- make dev

Depois de rodar o projeto, acesse localhost:10000 para acessar o root da api e localhost:10000/docs para acessar a documentação

O mesmo vale para a aplicação online https://transfeera.onrender.com/ e https://transfeera.onrender.com/docs, pode ser necessário fazer o dump do banco para fazer os testes por conta do ambiente localizado.

Para facilitar o dump do projeto, foi criado um endpoint que faz o dump ja com dados. Basta acessa-lo na documentação.
