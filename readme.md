# UTC-PR00-STREAMLIT
⚠️ Annexe du projet [UTC-PR00](https://https://github.com/tigrou23/UTC-PR00) ⚠️
___
- Lien vers le site : [https://pr00.hugopereira.fr](https://pr00.hugopereira.fr).
- Lien vers le site de statistiques : [https://pr00.stat.hugopereira.fr](https://pr00.stat.hugopereira.fr).
___

## Explication du projet

### 1. Objectif 

Le but de ce projet est de créer un site pour visualiser des informations concernant l'utilisation du site [UTC-PR00](https://pr00.hugopereira.fr).

Voici des captures d'écran du site :

<img width="1015" alt="Capture d’écran 2024-06-18 à 14 06 53" src="https://github.com/tigrou23/UTC-PR00-STREAMLIT/assets/54220880/41498687-687b-4d3a-b597-5b336962b3a2">
<img width="1015" alt="Capture d’écran 2024-06-18 à 14 06 53" src="https://github.com/tigrou23/UTC-PR00-STREAMLIT/assets/54220880/8bf428d1-45d1-4588-8632-a1d4d7cf03c7">

### 2. Technologies utilisées

- Python 3
- Streamlit
- Pandas

### 3. Base de données

Les requêtes des utilisateurs sont stockées dans une base de données MySQL (cf. [UTC-PR00-PROXY](https://https://github.com/tigrou23/UTC-PR00-PROXY)). L'application Streamlit va se connecter à cette base de données pour récupérer les informations et les afficher sur le site.

## Installation

### 1. Installation de Python 3

Pour installer Python 3, il suffit de suivre les instructions sur le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Installation de Streamlit

Pour installer Streamlit, il suffit de suivre les instructions sur le site officiel : [https://streamlit.io/](https://streamlit.io/).

### 3. Installation de Pandas

Pour installer Pandas, il suffit de suivre les instructions sur le site officiel : [https://pandas.pydata.org/](https://pandas.pydata.org/).

### 3. Environnement virtuel

Créer un environnement virtuel : 

```bash
python3 -m venv .venv && source .venv/bin/activate
```

### 4. Installation de l'application

Pour installer l'application, il suffit de cloner le dépôt Git et d'installer les dépendances :

```bash
cd UTC-PR00-STREAMLIT
pip install -r requirements.txt

```

### 5. Configuration

Nous devons faire un service qui va lancer l'application Streamlit au démarrage du serveur. Pour cela, nous allons créer un fichier de service pour systemd.

```bash
sudo nano /etc/systemd/system/streamlit.service
```

```bash
[Unit]
Description=Streamlit Application
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash -c 'source /root/UTC-PR00-STREAMLIT/.venv/bin/activate && exec streamlit run /root/UTC-PR00-STREAMLIT/main.py'
WorkingDirectory=/root/UTC-PR00-STREAMLIT
Restart=always
User=root
Group=root
Environment=PATH=/usr/bin:/usr/local/bin:/root/UTC-PR00-STREAMLIT/.venv/bin
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target

```

### 6. Démarrage du service

Mettre à jour avec le nouveau service

```bash
sudo systemctl daemon-reload
```

Démarrer le service

```bash
sudo systemctl start streamlit
```

Activer au démarrage

```bash
sudo systemctl enable streamlit
```
