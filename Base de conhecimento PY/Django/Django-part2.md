# Django part 2

## Status HTTP

Os códigos de status HTTP são códigos numéricos que indicam o resultado de uma solicitação HTTP entre o cliente (geralmente um navegador da web) e o servidor. Eles são divididos em cinco classes:

1. **1xx (Informativo)**: A solicitação foi recebida, continuando o processo.

   - Exemplo: `100 Continue`

2. **2xx (Sucesso)**: A solicitação foi bem-sucedida.

   - Exemplos:
     - `200 OK`: Solicitação bem-sucedida.
     - `201 Created`: A solicitação foi bem-sucedida e um novo recurso foi criado como resultado.
     - `204 No Content`: A solicitação foi bem-sucedida, mas não há conteúdo para enviar no corpo da resposta.

3. **3xx (Redirecionamento)**: A solicitação precisa de ações adicionais para ser concluída.

   - Exemplos:
     - `301 Moved Permanently`: A página solicitada foi movida permanentemente para uma nova localização.
     - `302 Found`: A página solicitada foi movida temporariamente para uma nova localização.

4. **4xx (Erro do Cliente)**: O cliente parece ter feito algo errado.

   - Exemplos:
     - `400 Bad Request`: A solicitação não pode ser entendida ou foi malformada.
     - `401 Unauthorized`: O cliente deve se autenticar para obter a resposta solicitada.
     - `403 Forbidden`: O cliente não tem permissão para acessar o recurso.

5. **5xx (Erro do Servidor)**: O servidor falhou ao cumprir uma solicitação aparentemente válida.

   - Exemplos:
     - `500 Internal Server Error`: Um erro genérico de servidor.
     - `502 Bad Gateway`: O servidor, ao atuar como gateway ou proxy, recebeu uma resposta inválida do servidor upstream.
     - `503 Service Unavailable`: O servidor não está pronto para manipular a solicitação. Geralmente, isso é devido a sobrecarga temporária ou manutenção do servidor.

Esses são alguns exemplos comuns de códigos de status HTTP, mas existem muitos outros. Cada código tem um significado específico e é utilizado para informar sobre o estado da solicitação e da resposta entre o cliente e o servidor.

