# Padrão de Projeto: Template Method

## 📌 Objetivo
O **Template Method** é um padrão de projeto comportamental que define o esqueleto de um algoritmo na superclasse, mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura.



---

## 🧩 Como funciona?
Imagine uma **Receita de Bolo**. O modo de preparo geral é o mesmo: bater a massa, colocar na forma e levar ao forno. No entanto, o "bater a massa" muda se o bolo for de chocolate ou de cenoura. 

O Template Method centraliza o que é comum e delega o que é específico.

### Componentes:
* **Classe Abstrata**: Define o método do template e os passos abstratos que serão implementados pelas subclasses.
* **Classe Concreta**: Implementa os passos específicos do algoritmo, mas não pode alterar o fluxo definido no método do template.

## ✅ Vantagens
* **Reutilização de código**: Partes comuns do algoritmo não precisam ser reescritas.
* **Fácil manutenção**: Mudanças no fluxo principal são feitas em um único lugar (na superclasse).
* **Estrutura rígida**: Garante que os passos do algoritmo sejam sempre executados na ordem correta.

## ❌ Desvantagens
* **Limitação**: Algumas subclasses podem se sentir limitadas pelo esqueleto fixado pela superclasse.
* **Violação do Princípio de Substituição de Liskov**: Se não for bem planejado, mudar um passo pode quebrar a lógica esperada do fluxo principal.