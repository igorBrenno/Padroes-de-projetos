# Factory Method Pattern 🏭

Este repositório contém uma implementação didática do padrão de projeto **Factory Method** utilizando Python.

## 📌 Objetivo
O **Factory Method** é um padrão criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

O foco principal é o **desacoplamento** entre o código que utiliza o objeto e o código que decide qual classe concreta instanciar.

---

## 🛠 Estrutura do Exemplo

No exemplo implementado, simulamos um sistema de notificações:

1.  **Produto (`Notificacao`):** Interface abstrata que define o comportamento comum.
2.  **Produtos Concretos (`Email`, `SMS`):** As implementações reais de envio.
3.  **Criador (`NotificacaoFactory`):** Classe que contém a lógica de negócio e chama o método fábrica.
4.  **Criadores Concretos (`EmailFactory`, `SMSFactory`):** Decidem qual classe instanciar.

---