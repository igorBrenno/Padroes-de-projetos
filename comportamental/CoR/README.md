# Padrão de Projeto: Chain of Responsibility (Corrente de Responsabilidade)

## 📌 Objetivo
O **Chain of Responsibility** é um padrão de projeto comportamental que permite evitar o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a oportunidade de tratar a solicitação. Ele encadeia os objetos receptores e passa a solicitação ao longo da corrente até que um objeto a trate.

---

## 🧩 Como funciona?
Imagine um **Sistema de Atendimento Automático** de um banco por telefone:
1. Primeiro, você fala com a **URA** (opções automáticas).
2. Se não resolve, você passa para um **Atendente Humano**.
3. Se for algo complexo, ele te passa para um **Gerente**.

Cada nível é um "elo" da corrente. Se um elo sabe resolver, ele para o processo. Se não sabe, ele delega para o próximo.

## ✅ Vantagens
* **Redução do acoplamento**: O cliente não precisa saber qual objeto resolve o problema.
* **Flexibilidade**: Você pode mudar a ordem da corrente ou adicionar novos elos sem alterar o código do cliente.
* **Princípio da Responsabilidade Única**: Cada classe foca em um tipo específico de solução.

## ❌ Desvantagens
* **Garantia de recebimento**: Não há garantia de que a solicitação será tratada (ela pode chegar ao fim da corrente e ser descartada).
* **Performance**: Pode haver um leve impacto se a corrente for muito longa e o tratamento estiver apenas no último elo.