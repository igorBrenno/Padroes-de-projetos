# Padrão de Projeto: Facade (Fachada)

## 📌 Objetivo
O **Facade** é um padrão de projeto estrutural que fornece uma interface unificada e simplificada para um conjunto de interfaces em um subsistema. Ele define uma interface de nível superior que torna o subsistema mais fácil de ser usado.

---

## 🧩 Como funciona?
Pense em um **Atendente de Restaurante**. Você (cliente) faz um pedido simples ("Quero um X-Burguer"). Você não precisa falar com o açougueiro, com o chapeiro, com o fornecedor de pães e com o estoquista. O atendente serve como sua **Fachada**, coordenando todos os processos internos para te entregar o resultado.

1. **Fachada (Facade)**: Conhece quais classes do subsistema são responsáveis por um pedido e delega o trabalho corretamente.
2. **Subsistemas Complexos**: O conjunto de classes que realiza o trabalho real. Elas não conhecem a Fachada e operam de forma independente.
3. **Cliente**: Acessa apenas a Fachada para realizar suas tarefas, ignorando a complexidade interna.

## ✅ Vantagens
* **Facilidade de uso**: Simplifica a vida do desenvolvedor que utiliza o seu código.
* **Desacoplamento**: O cliente não precisa conhecer os detalhes internos do sistema, facilitando manutenções futuras.
* **Isolamento**: Protege o cliente de mudanças nos componentes internos do subsistema.

## ❌ Desvantagens
* **Risco de "Classe Deus"**: Uma fachada pode se tornar um objeto muito complexo e centralizado se tentar fazer tudo sozinha.
* **Limitação**: Pode impedir que usuários avançados acessem funcionalidades específicas do subsistema que não foram expostas pela fachada.