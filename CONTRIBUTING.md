
## Bem-vindo(a)! 
Se você chegou até aqui, é provável que tenha interesse em contribuir com o **RateHUB**, um software de avaliações de filmes desenvolvido em Django. O RateHUB foi criado para permitir a troca entre conhecimentos sobre cinema entre diferentes pessoas ao redor do mundo. Antes de começar a colaborar, leia este guia para entender melhor como nosso sistema funciona e como você pode ajudar a melhorar ainda mais essa ferramenta.

<br>

## Como contribuir:
Você pode colocar uma nova funcionalidade em prática, solucionar alguma issue do projeto (botão abaixo) ou adicionar uma melhoria.
<br>
<p align="center">
  <a href="https://github.com/GUSTAVO-PEDROSA-MIRANDA/ProjetoFDS/issuess">
    <img src="https://img.shields.io/badge/Ver issues-7f1d1d?style=for-the-badge&logoColor=white"/>
  </a>
</p>

<br>

## Configurando o repositório

<strong>1º) Fork do Repositório:</strong> Faça um Fork para levar uma cópia do repositório para a sua conta.  Dessa forma, você pode realizar suas modificações sem impactar o repositório original. 
<br>
<p align="center">
  <img src="Aplicativo/static/imagens/contributing1.png">
</p>

<strong>2º) Clonar o repositório:</strong> 
```
git clone https://github.com/SuaConta/ProjetoFDS.git
```

<strong>3º) Criar sua própria Branch:</strong> 
```
git checkout -b minha-nova-funcionalidade
```

<br>

## Configurando o ambiente de desenvolvimento

<strong>1º) Entre no Diretório do Projeto:</strong>
```
cd ProjetoFDS
```

<strong>2º) Crie um Ambiente Virtual:</strong>
```
python -m venv venv
```

<strong>3º) Ative o Ambiente Virtual:</strong>
```
Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate
```

<strong>4º) Instale as Dependências:</strong>
```
pip install -r requirements.txt
```

<strong>5º) Aplique as Migrations (Criar o Banco de Dados):</strong>
```
python manage.py migrate
```

<strong>6º) Rode o Servidor:</strong>
```
python manage.py runserver
```

## Caso queira garantir que o código adicionado não quebre outras partes da aplicação:
rode os testes existentes e, caso necessário, crie novos testes. Para fazer isto:

<strong>1º) Baixe o <a href="https://nodejs.org/en" target="_blank">Node</a> na sua versão LTS:</strong>

<strong>2º) Instale as dependências:</strong>
```
npm ci
```

<strong>3º) Rode os testes com:</strong>
```
npx cypress run
```

<br>

## Confirmando suas Alterações
Abra um Pull Request com uma descrição das alterações realizadas.

<strong>1º) No repositório que você deu fork, clique em ```Contribute```:</strong>

<p align="center">
  <img src="">
</p>

<strong>2º) Depois clique em ```Open pull request```:</strong>

<p align="center">
  <img src="" width="300">
</p>

<strong>3º) Agora selecione o repositório que você deu fork e a branch que você fez suas alterações:</strong>

<p align="center">
  <img src="">
</p>

<strong>4º) Então, para criar seu PR, clique em ```Create pull request```:</strong>

<p align="center">
  <img src="" width="300">
</p>

<strong>5º) No final:</strong>

<p>A equipe do RateHUB irá revisar sua submissão e, caso algo não esteja em conformidade com o projeto, entraremos em contato para ajustar o seu código.</p>

<br>

## 🙏 Agradecimentos!

A equipe do **RateHUB** agradece imensamente pela sua contribuição! Cada sugestão, melhoria e ajuste faz uma grande diferença para que possamos oferecer um sistema de avaliação de filmes ainda mais eficiente e otimizado para os entusiastas do cinema.

Estamos animados para ver suas ideias em ação e trabalharmos juntos para transformar o atendimento e a organização de dados dos usuários.

<br>

Se precisar de qualquer coisa ou tiver dúvidas durante o processo, não hesite em entrar em contato. Muito obrigado por ajudar a tornar o **RateHUB** cada vez melhor!

<br>
<br>
Fale com a gente:
- [Luca Albuquerque](https://github.com/LucaAlbuquerque) - lra3@cesar.school
<br>
- [Gustavo Pedrosa](https://github.com/GUSTAVO-PEDROSA-MIRANDA) - hft@cesar.school
<br>
- [Ricardo Machado](https://github.com/ricardomvlins) - rmvl@cesar.school
<br>
- [Arthur von Sohsten](https://github.com/arthurvonsohsten) - alvs@cesar.school
<br>
- [Victor Vilela](https://github.com/) - vmv2@cesar.school
<br>

<br>
