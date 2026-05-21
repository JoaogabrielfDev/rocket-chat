# Rocket Chat 🚀
![Version](https://img.shields.io/badge/version-v1.0-blue)

## Chat de IA focado em resolver problemas em python

<!-- ### Projeto feito durante o curso de FastApi da Rocketseat -->
### O projeto ultiliza como principal as seguintes tecnologias:

* FastApi
* ollama
* phi3-mini
* Streamlit

## Como rodar o código?

### Passo 1
#### Primeiramente faça o dowload do Ollama (Mac, Linux e Windows) em seu dispositivo através do site oficial: https://ollama.com/download

<img width="1919" height="641" alt="Image" src="https://github.com/user-attachments/assets/4a07e8da-ee2a-4e1b-a5ff-5a3af188d4ae" />

#### Digite no seu terminal para conferir se o ollama está instalado (Obs: recomendado usar o terminal da sua maquina e não o do VScode)

```
ollama --version
```

#### Após isso em seu terminal digite o comando para fazer o dowload do modelo desejado (Phi3:mini):

```
ollama pull phi3:mini
```

#### Verifique que se o modelo está instalado digitando assim em seu terminal:

```
ollama list
```
---
### Passo 2
#### abra o seu terminal no ambiente Backend e instale as dependências necessárias:

#### Para entrar:
```
cd backend
```

#### Para instalar:

```
pip install requirements.txt
```


#### abra o seu terminal no ambiente Frontend e instale as dependências necessárias:


```
rocket-chat/frontend
```

#### Para instalar:

```
pip install requirements.txt
```
---

### Passo 3 (Opcional)
### Caso queira rodar o Frontend e o Backend de forma separada
### Frontend

#### Para rodar o frontend basta entrar em seu diretório e digitar em seu terminal
#### Para entrar:

```
 cd frontend 
```

#### Para Rodar:
```
python -m streamlit run main.py 
```

### Backend

#### Para rodar o Backend basta entrar em seu diretório e digitar em seu terminal
#### Para entrar:

```
 cd backend
```

#### Para Rodar:
```
python run.py
```
---

### Passo 4

#### Rodando o App 
#### Depois de ter seguido o passo a passo e ter instalado todas as dependências, para rodar o projeto completo de forma conjunta, em seu diretório raiz da aplicação basta digitar no seu terminal:

```
python run.py 
```
#### O app deve abrir normalmente em seu navegador padrão:
<img width="1919" height="621" alt="Image" src="https://github.com/user-attachments/assets/9af7d0b7-093e-4f61-bbc6-cdd0c6a3e39d" />