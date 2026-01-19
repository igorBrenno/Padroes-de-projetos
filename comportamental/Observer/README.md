# Padrão de Projeto: Observer (Observador)

## 📌 Objetivo
O **Observer** é um padrão de projeto comportamental que permite definir um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.



---

## 🧩 Como funciona?
Imagine que você está esperando por um novo modelo de smartphone. Você pode ir à loja todo dia para checar se chegou (o que é ineficiente), ou pode se inscrever na **lista de e-mails** da loja. Assim que o celular estiver disponível, a loja envia um aviso para todos os inscritos.

### Componentes:
* **Subject (Sujeito/Publicador)**: Mantém uma lista de observadores e fornece métodos para adicionar ou remover inscritos. É ele quem envia as notificações.
* **Observer (Interface)**: Define o método que o Publicador usará para notificar as mudanças (geralmente um método `update`).
* **Concrete Observers (Inscritos)**: Implementam a interface e definem o que deve ser feito ao receber a notificação.

## ✅ Vantagens
* **Open/Closed Principle**: Você pode introduzir novos tipos de observadores sem precisar mudar o código do publicador.
* **Relacionamentos Dinâmicos**: As inscrições podem ser feitas ou canceladas em tempo de execução.
* **Desacoplamento**: O Publicador e o Observador não precisam saber detalhes internos um do outro.

## ❌ Desvantagens
* **Ordem Aleatória**: Geralmente, os observadores são notificados em uma ordem aleatória.
* **Vazamento de Memória**: Se você esquecer de desinscrever um observador que não é mais usado, ele pode continuar ocupando memória (conhecido como "Lapsed Listener Problem").