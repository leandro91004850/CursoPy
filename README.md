# CursoPy

## Instalando o env
    ```
    pip install virtualenv

    ```
### Em caso de errors ao instalar o virtualenv
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py 
    
    OU
    
    sudo apt-get install python3-venv

    ```    

 ## criando um ambiente virtual
    ```
    virtualenv nome_ambiente

    ```   

 ## ativando ambiente virtual
    ```
    source bin/activate

    ```   

 ## Criando um ambiente virtual com uma determinada versão do python
    ```
    virtualenv -p python3.7.3 api

    ```   

## Instalando o FASTAPI OBS: Executar como root

### Documentação [FastAPI](https://fastapi.tiangolo.com/pt/)
    ```
    pip install fastapi

    ```    

### Você também precisará de um servidor ASGI para produção, tal como [Uvicorn](https://www.uvicorn.org/) ou [Hypercorn](https://www.hypercorn.org/).
    ```
    pip install "uvicorn[standard]"

    ```
### rodando o Uvicorn
    ```
    uvicorn main:app --reload

    ```
### Documentaçao http://localhost:8000/docs ou http://localhost:8000/redoc

## Implementação do easygoogletranslate 0.0.4 [easygoogletranslate](https://pypi.org/project/easygoogletranslate/)
    ```
    pip install easygoogletranslate

    ```