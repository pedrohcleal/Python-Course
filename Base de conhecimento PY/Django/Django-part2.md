# Django part 2

## Status HTTP

Os códigos de status de respostas HTTP são uma parte importante do protocolo HTTP. Eles são usados ​​para informar ao cliente o status da solicitação que ele fez ao servidor.

Os códigos de status HTTP são divididos em cinco classes:

* **1xx (Informativo)**: A solicitação foi recebida pelo servidor e está sendo processada.
* **2xx (Confirmação)**: A solicitação foi bem-sucedida.
* **3xx (Redirecionamento)**: O cliente precisa tomar alguma ação adicional para completar a solicitação.
* **4xx (Erro do cliente)**: A solicitação foi incorreta ou incompleta.
* **5xx (Erro do servidor)**: O servidor não foi capaz de processar a solicitação corretamente.

**Códigos de status informativos (1xx)**

Os códigos de status informativos são usados ​​para informar ao cliente que a solicitação foi recebida e está sendo processada. Eles não indicam se a solicitação foi bem-sucedida ou não.

Os códigos de status informativos são:

* **100 Continue:** O servidor recebeu a solicitação e está esperando por mais informações.
* **101 Switching Protocols:** O servidor está mudando para um protocolo diferente.
* **102 Processing:** O servidor está processando a solicitação e enviará a resposta assim que estiver pronta.
* **103 Early Hints:** O servidor está fornecendo informações antecipadas que podem ser usadas pelo cliente para melhorar o desempenho da solicitação.

**Códigos de status de confirmação (2xx)**

Os códigos de status de confirmação são usados ​​para informar ao cliente que a solicitação foi bem-sucedida.

Os códigos de status de confirmação são:

* **200 OK:** A solicitação foi bem-sucedida e a resposta contém o conteúdo solicitado.
* **201 Created:** A solicitação foi bem-sucedida e um novo recurso foi criado.
* **202 Accepted:** A solicitação foi bem-sucedida e o servidor está processando-a.
* **203 Non-Authoritative Information:** A solicitação foi bem-sucedida e a resposta contém informações de um servidor diferente.
* **204 No Content:** A solicitação foi bem-sucedida, mas não há conteúdo a ser retornado.
* **205 Reset Content:** A solicitação foi bem-sucedida e o cliente deve redefinir o conteúdo da área de exibição.
* **206 Partial Content:** A solicitação foi bem-sucedida e apenas uma parte do conteúdo foi retornada.

**Códigos de status de redirecionamento (3xx)**

Os códigos de status de redirecionamento são usados ​​para informar ao cliente que ele precisa tomar alguma ação adicional para completar a solicitação.

Os códigos de status de redirecionamento são:

* **300 Multiple Choices:** O recurso solicitado pode ser encontrado em vários locais.
* **301 Moved Permanently:** O recurso solicitado foi movido permanentemente para outro local.
* **302 Found:** O recurso solicitado foi movido temporariamente para outro local.
* **303 See Other:** O recurso solicitado pode ser encontrado usando um método diferente.
* **304 Not Modified:** O conteúdo do recurso solicitado não foi alterado desde a última solicitação.
* **305 Use Proxy:** O recurso solicitado deve ser solicitado usando um proxy.
* **307 Temporary Redirect:** O recurso solicitado foi movido temporariamente para outro local.

**Códigos de status de erro do cliente (4xx)**

Os códigos de status de erro do cliente são usados ​​para informar ao cliente que a solicitação foi incorreta ou incompleta.

Os códigos de status de erro do cliente são:

* **400 Bad Request:** A solicitação foi incorreta ou incompleta.
* **401 Unauthorized:** O cliente não está autorizado a fazer a solicitação.
* **402 Payment Required:** O cliente deve pagar para fazer a solicitação.
* **403 Forbidden:** O cliente não tem permissão para fazer a solicitação.
* **404 Not Found:** O recurso solicitado não foi encontrado.
* **405 Method Not Allowed:** O método HTTP usado na solicitação não é permitido para o recurso solicitado.
* **406 Not Acceptable:** O servidor não pode retornar o conteúdo solicitado no formato especificado.
* **407 Proxy Authentication Required:** O cliente deve autenticar-se com o proxy antes de fazer a solicitação.
* **408 Request Timeout:** O cliente levou muito tempo para enviar a solicitação.
* **409 Conflict:** O recurso solicitado está em conflito com outro recurso.
* **410 Gone:** O recurso solicitado foi removido permanentemente.
* **411 Length Required:** A solicitação deve especificar o comprimento do corpo da mensagem.

