
**Desafio RPA challenge**
 A automação realiza os seguintes passos:

    Informa um token de acesso;
    Clica no botão iniciar;
    Lê todos os pedidos;
    Lê o número do lote que será usado em outra aplicação;
    Abre outra aplicação desktop chamada STLOG.EXE;
    Digita o número do lote a ser pesquisado na aplicação;
    Busca as informações de cada um dos pedidos;
    Na página de controle de pedidos, preenche os códigos de rastreamento que estiverem ausentes;
    Na página de controle de pedidos, preenche a situação atual de cada pedido;
    Quando todas as informações estiverem corretamente preenchidas, clica no botão Atualizar pedidos.
    
Mais informações em:
https://marcelstein.com/elochallenge/



Possível problema: 
Como não consegui utilizar a função locateOnScreen da biblioteca pyautogui, tive que trabalhar com as posições dos elementos em tela. Ou seja: O perfeito funcionamento da automação está diretamente ligada ao tamanho da tela de quem fizer o uso desse RPA. Com isso, deve-se atualizar manualmente a posição de cada elemento (que estão salvos em variaveis) a fim de manter o funcionamento da automação.


**Instalação:**

Para a leitura de texto, foi utilizado o textify: 
https://www.techspot.com/downloads/6891-textify.html
Ele deve ser baixado e instalado. 


Selenium:
    pip install selenium

Pyautogui
    pip install pyautogui
