# Sistema de Agenda Automática
## Objetivo
<p> A aplicação visa gerenciar e otimizar o agendamento de serviços, integrando tecnologias como Python, Django, e JavaScript para uma experiência de usuário eficiente e automatizada. O sistema permite aos clientes agendarem compromissos e envia automaticamente um e-mail. As datas passadas são removidas automaticamente, mantendo uma agenda organizada. O proprietário também pode remover clientes manualmente conforme necessário, reduzindo notificações desnecessárias aos clientes e facilitando a administração. O projeto busca automatizar e otimizar o processo de agendamento, garantindo eficiência operacional, escalabilidade e uma experiência de usuário superior. </p>

## Vídeo Demonstrativo

https://github.com/user-attachments/assets/536fa507-37ec-411c-a880-8549259630f2

## Conteúdo dos E-mails Enviados
Os e-mails enviados pela aplicação incluem:

Confirmação de agendamentos com detalhes como horário, serviço selecionado e contatos do profissional.

Informações sobre pedidos, incluindo descrição dos itens, valores e forma de pagamento.

Regras e políticas importantes, como tempo de tolerância, taxas aplicáveis em caso de atraso, e orientações para cancelamento de pedidos ou horários agendados.

## Automatizações

### Formulário para Agendar um Horário com Procedimento

#### Fluxo

O cliente acessa a página de agendamento.
Preenche os campos obrigatórios:

Nome

E-mail

Telefone

Data e hora desejada

Procedimento desejado (selecionado de uma lista).

Uma confirmação de agendamento é enviada para o e-mail do cliente.

**Validação no Backend:**

Verificação de conflitos de horário no banco de dados.

Campos obrigatórios devem estar preenchidos.

Data e hora devem ser futuras.

### Remoção de Registros

#### Fluxo:

Após o cliente realiza o cadastro o registro é salvo no banco de dados e adicionado a uma lista de controle.

Após a data do agendamento passar:

Um processo automático verifica os registros antigos.

Registros com datas passadas são removidos do banco de dados.

### Formulário para Fazer Pedido de um Produto

#### Fluxo:

O cliente acessa a página de pedidos.

Preenche os campos obrigatórios:

Produto desejado.

Aroma.

Quantidade (ml).

Nome.

E-mail.

Telefone.

O pedido é registrado temporariamente no banco de dados.

E-mails de confirmação são enviados ao cliente e ao proprietário.

O registro do pedido é removido do banco de dados após o envio dos e-mails.

**Validação no Backend:**

Envio do e-mail para o usuário e para o proprietário

Exclusão do pedido do banco de dados

Campos obrigatórios devem estar preenchidos.

### Envio de E-mail de Confirmação de Agendamento para o Cliente

#### Fluxo:

Após o agendamento ser validado e salvo no banco de dados, o sistema dispara um e-mail para o cliente.

O e-mail inclui:

Nome do cliente.

Data e hora do agendamento.

Procedimento agendado.

Informativo de como reagendar ou cancelar, tolerância de atraso e formas de pagamento, além de email e número de contato do proprietário.

### Envio de E-mail de Confirmação do Pedido do Produto

#### Fluxo:

Quando o pedido é enviado, o sistema valida e registra o pedido temporariamente.

Dois e-mails são enviados:

**Para o Cliente:**

Inclui detalhes do produto, quantidade, aroma e informações de contato.

Informações sobre o cliente que fez o pedido, incluindo nome, número de contato e e-mail.

**Para o Proprietário:**

Inclui detalhes do pedido como produto, aroma e quantidade.

Após os e-mails serem enviados com sucesso, o registro é removido do banco de dados.

## Organização da arquitetura

### Branchs e suas funcionalidades

#### Main
Onde encontra-se a conclusão do projeto e suas funcionalidades, que foram desenvolvidas em branchs específicas, aprovadas e unidas ao main.

#### FronEnd-Agendamento
Focado na criação e estilização dos templates, incluindo:
- Criação das páginas HTML e organização do conteúdo.
- Estruturação e organização das pastas do projeto.
- Conexão e integração com CSS para estilização.
- Design extensível e inclusão de logotipos e outros elementos visuais.

#### BackEnd-Agendamento
Responsável por integrar o front-end às funcionalidades, assegurando que as respostas e os dados enviados sejam processados corretamente:
- Desenvolvimento da lógica do cadastro, autenticação e gerenciamento de horários.
- Verificação do envio dos formulários e recebimento pelo banco de dados.
- Controle das views, models, forms e configuração de URLs.
- Exclusão dos registros do BD.

#### Cloud-Integration
Visa a integração com o banco de dados
- Integração com o PostgreSQL para armazenamento seguro e escalável.
- Configuração de segurança e backups periódicos dos dados.

#### JavaScript
Concentra-se em deixar o layout do usuário dinâmico.
- Oculta e acrescenta informações de forma interativa.
- Confirmação se as informações dos formulários foram preenchidas corretamente.
- Utilizando flatpickr para configurar o horário e a data.
- Armazena a resposta do usuário verificando se o mesmo já realizou uma avaliação prévia para os procedimentos necessários.

#### Email
Responsável pelo desenvolvimento do sistema de notificação:
- Lógica de envio de e-mails automatizados, alertando os clientes.

## Frameworks e Bibliotecas
***Django***
Framework principal para a criação das funcionalidades do sistema, incluindo a gestão de templates, controle de autenticação, e processamento de agendamentos.

***Bootstrap*** 
Utilizado para o desenvolvimento responsivo dos formulários, organização dos agendamentos e elementos no menu, facilitando a navegação tanto no desktop quanto em dispositivos móveis.

***Flatpickr***
Biblioteca JavaScript utilizada para facilitar a seleção de datas e horários nos formulários de agendamento.

## Visualização
Aqui estão algumas imagens criadas no Figma, ilustrando o design esperado para as páginas principais do sistema:

Tela Inicial do Cliente: Primeira interface de contato, com opções de agendamento e visualização de compromissos.
Tela do Proprietário: Interface de administração, onde é possível gerenciar a agenda e realizar cadastros de novos clientes ou compromissos.

## Requisitos de Sistema
Python 3.8+
PostgreSQL (configurar base de dados com credenciais seguras)
Bootstrap (integrado via CDN no HTML)

## Suporte e Contribuição
### Reportar Problemas
Para reportar problemas, abrir uma issue no GitHub detalhando o erro, contexto e possíveis passos para replicar o problema.

### Contato para Suporte
Para baixar todas as dependências utilizadas a aplicação possui 'requirements.txt'.
Disponibilizamos um canal de comunicação por e-mail (gabriellesantisilva@gmail.com) para questões técnicas e suporte ao usuário.
