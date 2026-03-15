# Padaria - Sistema de Administração

Sistema de administração para padaria desenvolvido com Django e PostgreSQL.

---

## Tecnologias Utilizadas
- **Backend:** Python 3.14 + Django 6.0
- **Banco de Dados:** PostgreSQL 18
- **Frontend:** HTML + Bootstrap 5

---

## Como Instalar e Rodar o Projeto

### Pre-requisitos
- Python 3.14+
- PostgreSQL 18+
- Git

### Passo 1 - Clonar o repositorio
```bash
git clone https://github.com/Daiosleri/projeto-padaria.git
cd projeto-padaria
```

### Passo 2 - Instalar as dependencias
```bash
pip install django
pip install psycopg2-binary
```

### Passo 3 - Configurar o banco de dados
Crie um banco de dados no PostgreSQL chamado `padaria` e configure o arquivo `padaria/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'padaria',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Passo 4 - Rodar as migracoes
```bash
python manage.py migrate
```

### Passo 5 - Criar o superusuario
```bash
python manage.py createsuperuser
```

### Passo 6 - Iniciar o servidor
```bash
python manage.py runserver
```

### Passo 7 - Acessar o sistema
- **Sistema:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

---

## Estrutura do Projeto
```
projeto-padaria/
├── padaria/          - Configuracoes principais
├── produtos/         - Cadastro de Produtos
├── funcionarios/     - Cadastro de Funcionarios
├── pedidos/          - Registro de Pedidos
└── relatorios/       - Relatorios Financeiros
```