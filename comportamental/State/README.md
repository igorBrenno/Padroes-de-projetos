# Padrão de Projeto: State (Estado)

## 📌 Objetivo
O **State** é um padrão de projeto comportamental que permite a um objeto alterar seu comportamento quando seu estado interno muda. É como se o objeto mudasse de classe em tempo de execução, pois as respostas aos mesmos métodos variam conforme o estado.



---

## 🧩 Como funciona?
O padrão State está intimamente relacionado com o conceito de **Máquina de Estados Finita**. A ideia principal é que, em vez de ter um objeto cheio de condicionais complexas (`if/else` ou `switch/case`), cada estado é transformado em uma classe própria.

### Componentes:
* **Contexto (Context)**: Mantém uma instância de um estado concreto que define o estado atual. Ele delega o trabalho para o objeto de estado em vez de tentar resolvê-lo sozinho.
* **Estado (Interface)**: Define uma interface comum para todos os estados concretos.
* **Estados Concretos**: Cada classe implementa comportamentos específicos associados a um estado do Contexto.

## ✅ Vantagens
* **Single Responsibility Principle**: Organiza o código relativo a estados específicos em classes separadas.
* **Open/Closed Principle**: Introduz novos estados sem mudar as classes de estado existentes ou o contexto.
* **Simplificação**: Elimina condicionais volumosas e repetitivas.

## ❌ Desvantagens
* **Overkill**: Pode ser um exagero se a máquina de estados for muito simples (apenas 2 estados, por exemplo).
* **Número de Classes**: Aumenta a quantidade de arquivos/classes no projeto.