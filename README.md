# 🚀 Bot Discord - Temps d'Attente des Parcs d'attractions

## 📌 Description
Ce bot Discord permet d'afficher les temps d'attente des attractions dans différents parcs d'attractions en utilisant des commandes slash (`/`).  

Il a été développé dans le cadre d'un projet pour [mon compte TikTok 🎢: clip2ep.fan](https://www.tiktok.com/@clip2ep.fan).  
Étant donné, que j'aime beaucoup les parcs d'attractions, j'ai voulu créer un outil simple et pratique pour obtenir rapidement les informations sur les files d'attente depuis Discord.  


## 📜 Fonctionnalités
- `/time <parc>` : Récupère les temps d'attente des attractions d'un parc.
- `/help` : Affiche la liste des commandes disponibles.
- `/liste` : Affiche la liste des parcs disponibles.

## 🔧 Installation et Configuration

### 1️⃣ Prérequis
- Python 3.x installé
- Un serveur Discord avec les permissions pour ajouter un bot
- Un token de bot Discord

### 2️⃣ Installation
1. Clone ce dépôt ou télécharge les fichiers.
2. Installe les dépendances nécessaires :
   ```bash
   pip install discord requests
   ```
3. Configure le fichier **`config.json`** avec le token de votre bot :
   ```json
   { 
   "TOKEN": "VOTRE_TOKEN_ICI" 
   }
   ```
### 3️⃣ Lancement du bot
Exécute la commande suivante :
``` bash
python main.py
```
## 📂 Structure du projet
```python
📁 projet-bot/ 
├── 📁 commands/ # Dossier contenant les commandes du bot 
│ ├── 📄 help.py # Commande `/help` 
│ ├── 📄 liste.py # Commande `/liste` 
│ ├── 📄 time.py # Commande `/time` 
├── 📁 utils/ # Dossier pour les fonctions utilitaires 
│ ├── 📄 helpers.py # Fonction pour normaliser les noms des parcs 
├── 📄 parks.py # Liste des parcs et leurs URLs API 
├── 📄 config.json # Fichier de configuration 
├── 📄 main.py # Script principal du bot 
└── 📄 README.md # Documentation du projet
```

## 🛠 Développement
Si vous souhaitez modifier ou améliorer le bot :
-   **Clonez** ce dépôt
-    Apportez vos **modifications**
- **Testez** avec :
```bash
python bot.py
```
-   Proposez une **pull request** 🎉

## 💡 Remarque
Le bot utilise les données de **`queue-times.com`**. Si un parc ne fonctionne pas, vérifiez l'URL correspondante dans **`parks.py`**.

## 📬 Contact
Si vous avez des questions ou suggestions, n'hésitez pas à me contacter sur baptiste.didier@proton.me !