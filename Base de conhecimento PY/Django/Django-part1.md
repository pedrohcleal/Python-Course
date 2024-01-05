# Django

Django é um popular framework de desenvolvimento web de código aberto que é escrito em Python. Ele foi criado para simplificar o desenvolvimento de aplicações web complexas, seguindo o padrão arquitetural Model-View-Controller (MVC) ou Model-View-Template (MVT), que é uma variação do MVC.

Aqui estão alguns dos principais aspectos e recursos do Django:

1. Modelo de Desenvolvimento: O Django segue o princípio "baterias incluídas", o que significa que oferece uma ampla gama de componentes e funcionalidades prontos para uso, economizando tempo e esforço no desenvolvimento. Isso inclui sistemas de autenticação, administração, roteamento de URLs, manipulação de formulários e muito mais.

2. ORM (Object-Relational Mapping): O Django possui um ORM embutido que permite que os desenvolvedores interajam com o banco de dados usando Python em vez de SQL. Isso simplifica a manipulação de dados e torna o código mais legível e portável entre diferentes sistemas de gerenciamento de banco de dados.

3. Administração Automatizada: O Django inclui um painel de administração automatizado que pode ser facilmente personalizado para gerenciar os dados da aplicação sem a necessidade de escrever código adicional. Isso é extremamente útil para tarefas de back-end e facilita a gestão do sistema.

4. Sistema de Roteamento de URLs: O Django possui um sistema de roteamento de URLs que mapeia URLs para funções de visualização, tornando a criação de páginas da web e a navegação entre elas fácil de gerenciar.

5. Segurança: Django tem uma forte ênfase na segurança. Ele oferece proteção contra ameaças comuns, como injeção de SQL, CSRF (Cross-Site Request Forgery), XSS (Cross-Site Scripting) e muitas outras vulnerabilidades web.

6. Template System: Django fornece um sistema de templates que permite a separação limpa entre a lógica de apresentação e o código Python. Isso facilita a manutenção e a personalização da aparência da aplicação.

7. Escalabilidade: Django é altamente escalável e adequado para desenvolver desde pequenos sites até aplicativos web empresariais de grande escala. Ele oferece suporte para cache, balanceamento de carga e otimizações de desempenho.

8. Comunidade Ativa: Django tem uma comunidade de desenvolvedores ativa e uma grande base de usuários. Isso significa que há uma abundância de recursos, bibliotecas e pacotes disponíveis para estender e aprimorar o framework.

9. Documentação Abundante: Django possui uma excelente documentação que é frequentemente atualizada e é uma valiosa fonte de referência para desenvolvedores.

Django é uma escolha popular para desenvolvedores devido à sua facilidade de uso, robustez e eficiência no desenvolvimento de aplicações web. É amplamente utilizado em muitos tipos de projetos, desde sites simples a aplicativos empresariais complexos. Se você está interessado em desenvolver aplicativos web em Python, o Django é uma excelente opção a ser considerada.

## Django-admin & manage.py

O Django é um framework web de alto nível para a linguagem de programação Python, projetado para facilitar o desenvolvimento rápido e limpo de aplicações web. Duas ferramentas importantes fornecidas pelo Django para facilitar a administração e o gerenciamento de projetos são o `django-admin` e o `manage.py`.

1. **`django-admin`**:

   - O `django-admin` é uma linha de comando que permite interagir com projetos Django de várias maneiras, incluindo a criação de novos projetos, a criação de aplicativos dentro de projetos, a execução de tarefas administrativas e muito mais.

   - Para criar um novo projeto Django, você pode usar o seguinte comando no terminal:

     ```bash
     django-admin startproject nome_do_projeto
     ```

     Isso criará uma estrutura básica de diretórios e arquivos para o seu projeto.

   - Além disso, o `django-admin` pode ser usado para criar aplicativos dentro do projeto, executar migrações de banco de dados, entre outras tarefas administrativas.

2. **`manage.py`**:

   - O `manage.py` é um script Python que é criado automaticamente dentro do diretório principal de cada projeto Django quando você executa `startproject`.

   - Este script é usado para realizar várias tarefas administrativas, como iniciar um servidor de desenvolvimento, aplicar migrações de banco de dados, criar superusuários para a área de administração, entre outras coisas.

   - Por exemplo, para iniciar o servidor de desenvolvimento, você pode usar o seguinte comando:

     ```bash
     python manage.py runserver
     ```

   - Para aplicar migrações de banco de dados, você usaria:

     ```bash
     python manage.py migrate
     ```

   - O `manage.py` também permite criar um superusuário para acessar a interface de administração do Django:

     ```bash
     python manage.py createsuperuser
     ```

   - Através do `manage.py`, você tem acesso a várias funcionalidades administrativas que são cruciais durante o desenvolvimento e manutenção de um projeto Django.

O `django-admin` e o `manage.py` são partes essenciais do fluxo de trabalho do desenvolvedor Django, fornecendo ferramentas para criar, gerenciar e manter projetos web de forma eficiente e organizada.
