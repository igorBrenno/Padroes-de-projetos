# Padrão de Projeto: Command (Comando)

## 📌 Objetivo
O **Command** é um padrão de projeto comportamental que encapsula uma solicitação como um objeto, permitindo que você parametrize clientes com diferentes solicitações, enfileire solicitações ou registre logs, além de oferecer suporte a operações que podem ser desfeitas.



---

## 🧩 Como funciona?
Imagine um **Garçom em um restaurante**:
1. Você (Cliente) faz um pedido ao **Garçom (Invoker)**.
2. O Garçom escreve o pedido em um **Papel (Command)**.
3. Esse papel é levado para o **Cozinheiro (Receiver)**, que sabe exatamente como preparar o prato.

O Garçom não precisa saber cozinhar, ele apenas "dispara" o comando representado pelo papel. Se você desistir do pedido antes de começar, o papel pode ser rasgado (Undo).

### Componentes:
* **Command**: Interface que define o método `execute`.
* **Concrete Command**: Implementa o `execute` invocando as operações correspondentes no Receiver.
* **Receiver**: A classe que contém a lógica de negócio real (quem sabe fazer o trabalho).
* **Invoker**: Quem solicita que o comando seja executado (ex: um botão ou um controle remoto).
* **Client**: Cria o objeto Command concreto e associa-o ao Receiver.

## ✅ Vantagens
* **Desacoplamento**: A classe que invoca a operação é separada da classe que sabe como realizá-la.
* **Extensibilidade**: É fácil adicionar novos comandos sem alterar o código existente (Princípio Aberto/Fechado).
* **Composição**: Você pode criar "Macro Comandos" (uma lista de comandos executados em sequência).

## ❌ Desvantagens
* **Aumento de classes**: O código pode se tornar mais complexo devido à quantidade de novas classes para cada comando específico.