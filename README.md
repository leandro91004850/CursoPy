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