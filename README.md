# osv
Cadastro de OSV.
Esse projeto foi feito para otimizar o cadastro de senhas telefônicas na common management platform, visto que o site não permite cadastro via script. Ele também permite remover as senhas antigas mesmo depois de incluir as novas senhas.
Foi ultilizado selenium para efetuar o cadastro das mil senhas telefonicas por controle do navegador Chrome. E também para remoção das mesmas.
As senhas e credenciais foram ocultadas.

Passos:
Para incluir as novas senhas, comente o trecho de código em que chama os métodos que excluem as mesmas. 
Para excluir as senhas, comente o trecho de código que chama o método que incluem as mesmas.

No arquivo credencial.py, coloque o seu login e senha do common management platform.
No arquivo interator.py, linha 11, coloque o site do common management platform.
No arquivo senhas, coloque todas as senhas que deseja cadastrar, separadas por virgula.
No arquivo oldsenha, coloque as senhas que deseja excluir após ter cadastrado as novas.

Enjoy :)
